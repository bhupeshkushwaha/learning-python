# DSA Examples (Python)

This folder contains Data Structures & Algorithms examples implemented in Python. Each example includes:

- Problem description
- Clear explanation of the approach
- Time and space complexity
- Unit tests so you can validate implementations locally

Current example:

- `k_length_apart.py` — "Check If All 1's Are at Least K Places Apart"

How to run

You can run the examples and tests either locally (if you have Python installed) or using Docker (no local Python required). Below are copy-paste PowerShell commands.

Option A — Quick: run a script or tests using a temporary Python container (no changes to the repo)

- Run the example script (`index.py`):

```powershell
docker run --rm --mount type=bind,source="E:\Learning\learning-python\DSA",target=/app -w /app python:3.12-slim python index.py
```

- Run the unit tests (`pytest`):

```powershell
docker run --rm --mount type=bind,source="E:\Learning\learning-python\DSA",target=/app -w /app python:3.12-slim \
	sh -c "python -m pip install --upgrade pip && python -m pip install pytest && PYTHONPATH=/app python -m pytest -q"
```

Direct (single-line) commands

- Run the script directly (no shell wrapper):

```powershell
docker run --rm -v "E:\Learning\learning-python\DSA:/app" -w /app python:3.12-slim python index.py
```

- Run tests in one line (uses shell to install pytest then run):

```powershell
docker run --rm -v "E:\Learning\learning-python\DSA:/app" -w /app python:3.12-slim sh -c "python -m pip install --upgrade pip && python -m pip install pytest && PYTHONPATH=/app python -m pytest -q"
```

Notes for Option A:
- The command bind-mounts the `DSA` folder into the container at `/app` so no files are moved.
- The `PYTHONPATH=/app` ensures pytest can import modules from the mounted folder.

Option B — Use the existing Docker Compose app (recommended if you run the web app)

If you already started the Python web app in `1-docker-setup-Python`, the compose setup mounts `../DSA` into the app container at `/app/dsa`. To run tests from the app container:

```powershell
cd "E:\Learning\learning-python\1-docker-setup-Python"
docker-compose up -d --build
docker-compose exec app sh
# now inside the container shell:
cd /app/dsa
python -m pip install --upgrade pip
python -m pip install pytest
PYTHONPATH=/app pytest -q
```

Notes for Option B:
- This lets you use the already-running app container and interact with the mounted code.
- The compose setup mounts `DSA` read-only at `/app/dsa` by default; change `docker-compose.yml` if you need write access.

Option C — Run locally (install Python)

If you prefer running locally on Windows, install Python 3.8+ and then:

```powershell
cd "E:\Learning\learning-python\DSA"
python -m pip install --user pytest
python -m pytest -q
```

Notes:
- The tests live in `DSA/tests/` and expect imports like `from k_length_apart import ...` to work when running from the `DSA` directory. If you run tests from the repo root, set `PYTHONPATH=DSA` or run `python -m pytest DSA/tests`.

Want more examples or CI?

I can add more problems with tests, a small web UI to run examples from the browser, or a GitHub Actions workflow to run tests automatically on push.
