"""Regression checks for stale or unsuccessful scientific replay receipts."""
import copy
import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from manuscript.scripts import validate
from analysis.revision.replay_independent import differing_fields


class ScientificManifestTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        hashes = {}
        for name in ('manuscript/scripts/reproduce.py', 'analysis/check.py',
                     'outputs/result.json', 'analysis/proof.md'):
            path = self.root/name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b'checked input\n')
            hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()
        self.manifest = {
            'all_checks_passed': True, 'historical_outputs_unchanged': True,
            'reproduction_script_sha256': hashes['manuscript/scripts/reproduce.py'],
            'replays': [{
                'script': 'analysis/check.py', 'script_sha256': hashes['analysis/check.py'],
                'historical_output': 'outputs/result.json',
                'historical_output_sha256': hashes['outputs/result.json'],
                'assertions_passed': True, 'historical_scientific_payload_identical': True,
                'changed_scientific_paths': [],
            }],
            'independent_cone_path_check': {
                'source': 'analysis/proof.md', 'source_sha256': hashes['analysis/proof.md'],
                'assertions_passed': True,
            },
            'independent_three_state_check': {'assertions_passed': True},
            'historical_output_hashes': {'outputs/result.json': hashes['outputs/result.json']},
        }
        self.root_patch = patch.object(validate, 'ROOT', self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)

    def test_matching_inputs_pass(self):
        self.assertEqual(validate.validate_computational_manifest(self.manifest), 4)

    def test_changed_inputs_are_rejected(self):
        for name in ('analysis/check.py', 'outputs/result.json', 'analysis/proof.md',
                     'manuscript/scripts/reproduce.py'):
            with self.subTest(path=name):
                path = self.root/name
                original = path.read_bytes()
                path.write_bytes(b'changed input\n')
                with self.assertRaisesRegex(AssertionError, name):
                    validate.validate_computational_manifest(self.manifest)
                path.write_bytes(original)

    def test_unsuccessful_receipt_is_rejected(self):
        for key in ('all_checks_passed', 'historical_outputs_unchanged'):
            with self.subTest(flag=key):
                manifest = copy.deepcopy(self.manifest)
                manifest[key] = False
                with self.assertRaises(AssertionError):
                    validate.validate_computational_manifest(manifest)
        manifest = copy.deepcopy(self.manifest)
        manifest['replays'][0]['historical_scientific_payload_identical'] = False
        with self.assertRaises(AssertionError):
            validate.validate_computational_manifest(manifest)

    def test_inconsistent_duplicate_hash_is_rejected(self):
        self.manifest['replays'][0]['historical_output_sha256'] = '0' * 64
        with self.assertRaisesRegex(AssertionError, 'outputs/result.json'):
            validate.validate_computational_manifest(self.manifest)


class ReplayComparisonTests(unittest.TestCase):
    def test_missing_and_added_fields_are_not_ignored(self):
        historical = {'check': True, 'missing': None, 'time_utc': 'old'}
        current = {'check': True, 'added': None, 'time_utc': 'new'}
        self.assertEqual(differing_fields(current, historical), ['added', 'missing'])

    def test_only_execution_time_is_ignored(self):
        self.assertEqual(differing_fields({'check': [1], 'time_utc': 'new'},
                                         {'check': [1], 'time_utc': 'old'}), [])
        self.assertEqual(differing_fields({'check': [2]}, {'check': [1]}), ['check'])


if __name__ == '__main__':
    unittest.main()
