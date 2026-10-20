# Numerical Array Toolkit

Reproducible matrix, sequence, and temperature analysis with NumPy.

## Data and scope

Examples use fabricated labels and non-personal numeric strings. Random arrays use seed 42; the temperature vector comes from the supplied notebook.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/analysis.py
python -m unittest discover -s tests -v
```

Outputs are written to `outputs/`. The clean notebook in `notebooks/analysis.ipynb` calls the same tested module. See `docs/provenance.md` for changes from the source notebook and `docs/validation.md` for actual execution results.

## Example output

The noninteractive demonstration ran successfully. Reproducible values are in `docs/example-results.json`; API behavior and edge cases are covered by the tests. These are small reusable utilities, not production services.
