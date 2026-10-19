# Copy this route into your existing FastAPI backend AFTER app = FastAPI(...)
# Replace your current GET / route with this route.
# Keep your existing API routes (/search, /detail/{subject_id}, /api/stream/{subject_id}, etc.).

from pathlib import Path
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def moviebox_frontend():
    html_path = Path(__file__).with_name("moviebox_tv.html")
    return HTMLResponse(html_path.read_text(encoding="utf-8"))
