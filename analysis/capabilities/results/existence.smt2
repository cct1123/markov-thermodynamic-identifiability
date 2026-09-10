; benchmark generated from python API
(set-info :status unknown)
(declare-fun x () Real)
(declare-fun y () Real)
(assert
 (> x 0.0))
(assert
 (> y 0.0))
(assert
 (= (+ x y) 1.0))
(assert
 (let ((?x13 (* x y)))
(< (/ 1.0 8.0) ?x13)))
(check-sat)
