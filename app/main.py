from fastapi import FastAPI
from app.authentication.router import router as auth_router
from app.files.router import router as files_router

app = FastAPI(
    title="File Storage API",
    description="API for user authentication and file management",
    version="1.0.0"
)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(files_router, prefix="/files", tags=["Files"])

@app.get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    """
    Endpoint to check if the API is running.
    """
    return {"status": "ok"}
