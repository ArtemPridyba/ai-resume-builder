from fastapi import FastAPI

app = FastAPI(title="AI Resume Builder API")


@app.get("/health")
def health() -> dict:
    """Перевірка працездатності сервісу."""
    return {"status": "ok"}