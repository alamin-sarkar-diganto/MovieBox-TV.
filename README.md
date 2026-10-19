# MovieBox TV deployment pack

This pack contains the existing frontend and the small deployment files. It does NOT include the complete FastAPI backend source, because that source must be kept intact from your existing code.

## Put these files together in one GitHub repository
- `app.py` — your existing full FastAPI backend source (rename your current `api.py` to `app.py` if needed)
- `moviebox_tv.html` — included in this pack
- `requirements.txt` — included in this pack
- `vercel.json` — included in this pack

## Connect frontend to backend
1. In your existing backend, keep `app = FastAPI(...)` and all API routes.
2. Replace the current `GET /` dashboard route with the route shown in `ROOT_ROUTE_PATCH.py`.
3. If you rename `api.py` to `app.py`, update/remove the local-only `uvicorn.run("api:app", ...)` block. Vercel imports `app` from `app.py`.
4. The frontend uses `location.origin` by default, so it can call API routes on the same domain. Its settings panel also supports a separate FastAPI base URL if needed.
5. Push all files to GitHub and import that repository in Vercel.

## Important
The frontend expects routes such as `/search?keyword=...`, `/detail/{id}`, `/episodes/{id}`, and `/api/stream/{id}`. Keep these paths compatible with the existing backend. Successful deployment does not guarantee the third-party upstream stream will always work or that every TV browser supports its format.
