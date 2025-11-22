# Python Docker Setup

This folder contains a minimal Docker-based Python development environment. It includes a small Flask web application that serves an HTML UI to demonstrate the containerized app.

Contents:
- `Dockerfile` - builds a Python 3.12 slim image and installs dependencies
- `docker-compose.yml` - runs the `app` service and an `nginx` reverse proxy
- `nginx/nginx.conf` - proxy configuration for forwarding requests to the app
- `src/app.py` - Flask app (serves `templates/index.html` and `static/style.css`)
- `src/requirements.txt` - Python dependencies
- `setup.sh` / `setup.bat` - helper scripts to start the environment

Quick Start (PowerShell on Windows):

```powershell
cd "1-docker-setup-Python"
.\setup.bat
```

Or on Linux/macOS:

```bash
cd "1-docker-setup-Python"
./setup.sh
```

The Flask app will be reachable at `http://localhost/` (nginx proxies to the app on port 8000).

Run with Docker (recommended)

These commands assume you are in the `1-docker-setup-Python` folder. Examples use PowerShell on Windows; the same `docker-compose` commands work in CMD or any POSIX shell.

1. Build and start the application (detached):

```powershell
docker-compose up -d --build
```

2. Check running containers:

```powershell
docker-compose ps
```

3. View live logs (press Ctrl+C to stop):

```powershell
docker-compose logs -f
```

4. Rebuild after making code changes (useful when you edit `src/` files):

```powershell
docker-compose up -d --build
```

5. Execute a shell inside the running app container for debugging:

```powershell
docker-compose exec app sh
```

6. Stop and remove the containers:

```powershell
docker-compose down
```

Notes:
- If port 80 is already used on your host, update the `ports` mapping in `docker-compose.yml` (for example, `- "8080:80"`) then open `http://localhost:8080`.
- If you only changed Python code and want immediate iteration without rebuilding the image, you can run the app locally (see "Developing locally without Docker") or mount the source into the container (the compose file already mounts `./src:/app` so changes should reflect immediately when the container runs gunicorn with reload disabled — rebuilding is only required when dependencies change.


Verify the web UI

1. Start the environment (see quick start above).
2. Check containers are running:

```powershell
docker-compose ps
```

3. Tail the logs if something goes wrong:

```powershell
docker-compose logs -f
```

4. Open the UI in a browser: `http://localhost/`

What the UI shows
- A simple landing page (`templates/index.html`) that displays a small status section and the content of `app.py` as a sample file. This demonstrates serving HTML/CSS from Flask and that the Python app is running in the container.
- A health endpoint at `/health` that returns JSON `{"status":"ok"}` for quick checks (e.g. `curl http://localhost/health`).

Developing locally without Docker

1. Create and activate a Python environment (Windows PowerShell example):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r src/requirements.txt
python src/app.py
```

2. Open `http://localhost:8000` in your browser.

Want more?

- Add routes and templates for additional examples.
- Add a database service (`mysql` or `postgres`) to `docker-compose.yml` if you need persistence.
- Add automated tests or CI to validate the app on push.
