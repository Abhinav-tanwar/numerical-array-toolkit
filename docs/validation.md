# Execution and validation

Executed with Python 3.12 using the versions pinned in requirements.txt. Program run completed successfully. Generated notebook cells passed Python syntax compilation; the notebook wrapper calls the same validated module. Full notebook execution in a separate Jupyter kernel was not performed.

```text
test_inverse_and_singularity (test_analysis.ArrayTest.test_inverse_and_singularity) ... ok
test_slice_and_no_mutation (test_analysis.ArrayTest.test_slice_and_no_mutation) ... ok
test_temperature_ties (test_analysis.ArrayTest.test_temperature_ties) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.042s

OK
```

Input/output data were checked for required fields, finite values, and appropriate synthetic-versus-supplied provenance. Output files contain aggregate metrics or non-personal examples; row-level clinical predictions are not published.
