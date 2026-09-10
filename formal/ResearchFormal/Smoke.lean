import Mathlib.Data.Real.Basic

namespace ResearchFormal

/-- A generic capability check, unrelated to the project's scientific claims. -/
theorem square_nonnegative (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

end ResearchFormal

#print axioms ResearchFormal.square_nonnegative
