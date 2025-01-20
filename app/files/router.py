from fastapi import APIRouter, HTTPException, Header
from app.storage import storage

router = APIRouter()

files_db = {}  # In-memory storage for files

@router.get("/")
async def list_files(auth: str = Header(...)) -> dict:
    """
    List all files belonging to the authenticated user.
    """
    user = validate_auth(auth)
    user_files = {file_id: file for file_id, file in files_db.items() if file["owner"] == user}
    return user_files

@router.post("/")
async def create_file(auth: str = Header(...), file_info: dict = None) -> dict:
    """
    Create a new file with metadata.
    """
    user = validate_auth(auth)
    file_id = f"file-{len(files_db) + 1}"
    files_db[file_id] = {"id": file_id, "owner": user, "info": file_info, "content": None}
    return {"file_id": file_id}

@router.get("/{file_id}")
async def get_file(file_id: str, auth: str = Header(...)) -> dict:
    """
    Get file metadata and content by ID.
    """
    validate_auth(auth)
    if file_id not in files_db:
        raise HTTPException(status_code=404, detail="File not found")
    return files_db[file_id]

@router.delete("/{file_id}")
async def delete_file(file_id: str, auth: str = Header(...)) -> dict:
    """
    Delete a file by ID.
    """
    validate_auth(auth)
    if file_id not in files_db:
        raise HTTPException(status_code=404, detail="File not found")
    del files_db[file_id]
    return {"status": "File deleted successfully"}

@router.post("/{file_id}")
async def upload_file_content(file_id: str, auth: str = Header(...), content: str = None) -> dict:
    """
    Upload content to an existing file.
    """
    validate_auth(auth)
    if file_id not in files_db:
        raise HTTPException(status_code=404, detail="File not found")
    files_db[file_id]["content"] = content
    return {"status": "File content updated successfully"}

def validate_auth(token: str) -> str:
    """
    Validate the session token and return the associated username.
    """
    if token not in storage.sessions_db:
        raise HTTPException(status_code=401, detail="Invalid session token")
    return storage.sessions_db[token]
