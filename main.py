import os
import platform
from datetime import datetime, timezone

import fasthtml
from fasthtml.common import Button, Div, FastHTML, H1, Main, P, Style, serve

# The app is created with FastHTML(), not fast_app(): fast_app() adds a route that
# serves files from the app folder by extension (.txt, .yaml, .csv and others), and the demo does not need it.
# FastHTML() does not add Pico CSS, and surreal.js is turned off: FastHTML loads them without a pinned version
app = FastHTML(
    surreal=False,
    htmlkw={"lang": "en"},
    title="FastHTML",
    secret_key=os.getenv("SESSKEY"),
)
rt = app.route


@rt("/")
def index():
    # Home page: rendered on the server
    return (
        Style("""
            body {
                font-family: system-ui, -apple-system, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 48px 24px;
                color: #111;
            }
            main {
                max-width: 640px;
                margin: 0 auto;
            }
            button {
                cursor: pointer;
                padding: 8px 16px;
                font-size: 16px;
                border-radius: 6px;
                border: 1px solid #ccc;
                background: #f8f9fa;
            }
            button:hover {
                background: #e9ecef;
            }
        """),
        Main(
            H1("Hello world"),
            P(f"FastHTML: {fasthtml.__version__}"),
            P(f"Python: {platform.python_version()}"),
            Div(
                Button(
                    "Get server time",
                    hx_get="/time",
                    hx_target="#server-time",
                    hx_swap="outerHTML",
                ),
                P("Server time: —", id="server-time"),
            ),
        ),
    )


@rt("/time")
def time():
    # Current server time in UTC (ISO 8601, to the second)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return P(f"Server time: {now}", id="server-time")


# Local run with python3 main.py
serve()
