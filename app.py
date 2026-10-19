from pathlib import Path
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def moviebox_frontend():
    html_path = Path(__file__).with_name("moviebox_tv.html")

    if not html_path.exists():
        return HTMLResponse(
            "<h1>MovieBox frontend file missing</h1>",
            status_code=500
        )

    return HTMLResponse(
        html_path.read_text(encoding="utf-8")
    )
