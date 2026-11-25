# FastHTML

Example [FastHTML](https://fastht.ml/) app. FastHTML is a Python framework for building web apps entirely in Python, with htmx for interactivity instead of hand-written JavaScript.

## Deploy settings

| Field | Value |
| --- | --- |
| Build | Railpack |
| Project directory | `/` |
| Install command | leave empty |
| Build command | leave empty |
| Start command | leave empty |
| Application port | `8000` |
| Health check path | `/` |

## <a name="dev"></a>Run locally

```bash
# create virtual environment and install dependencies
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# start the app
python3 main.py
```

The server reloads on code changes and opens at http://localhost:5001.

Requires Python 3.11 or later (the platform uses Python 3.15 from `.python-version`).
