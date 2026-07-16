from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="Current Time API")

@app.get("/now")
def get_now():
    """Return current datetime in ISO 8601 format (UTC)."""
    now = datetime.now(timezone.utc).isoformat()
    return {"now": now}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)