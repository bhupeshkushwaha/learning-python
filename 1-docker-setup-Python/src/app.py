from flask import Flask, render_template, abort
from pathlib import Path

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():
    # Read a small sample file to show in the UI (safe demo: app.py)
    sample_path = Path(__file__).resolve()
    try:
        content = sample_path.read_text(encoding='utf-8')
    except Exception:
        content = 'Unable to read sample file.'

    return render_template('index.html', sample_name=sample_path.name, sample_content=content)


@app.route('/health')
def health():
    return {'status': 'ok'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
