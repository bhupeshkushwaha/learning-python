# DSA Examples (Python)

This folder contains Data Structures & Algorithms examples implemented in Python. Each example includes:

- Problem description
- Clear explanation of the approach
- Time and space complexity
- Unit tests so you can validate implementations locally

Current example:

- `k_length_apart.py` — "Check If All 1's Are at Least K Places Apart"

How to run locally

1. Run the example script directly (requires Python 3.8+):

```powershell
cd "e:\Learning\learning-python\DSA"
python index.py
```

2. Run the unit tests (recommended). Install `pytest` if you don't have it:

```powershell
python -m pip install --user pytest
cd "e:\Learning\learning-python\DSA"
pytest -q
```

Notes:

- The tests live in `DSA/tests/` and assume you run `pytest` from the `DSA` directory so imports like `from k_length_apart import ...` resolve.
- If you prefer running tests from the repository root, set `PYTHONPATH=DSA` or run `python -m pytest DSA/tests`.

Want more examples?

I can add additional problems (with clear explanations and tests) and a small CI config to run tests automatically.
