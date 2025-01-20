from fastapi import APIRouter, HTTPException
from app.storage import storage

router = APIRouter()

@router.post("/register")
async def register_user(username: str, password: str) -> dict[str, str]:
    """
    Register a new user.
    """
    if username in storage.users_db:
        raise HTTPException(status_code=409, detail="User already exists")
    storage.users_db[username] = password
    return {"status": "User registered successfully"}

@router.post("/login")
async def login_user(username: str, password: str) -> dict[str, str]:
    """
    Login user and create a session token.
    """
    if username not in storage.users_db or storage.users_db[username] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    session_token = f"token-{username}"  # Example token
    storage.sessions_db[session_token] = username
    return {"token": session_token}

@router.post("/logout")
async def logout_user(token: str) -> dict[str, str]:
    """
    Logout user and invalidate the session token.
    """
    if token not in storage.sessions_db:
        raise HTTPException(status_code=401, detail="Invalid session token")
    del storage.sessions_db[token]
    return {"status": "User logged out successfully"}

@router.get("/introspect")
async def introspect_token(token: str) -> dict[str, str]:
    """
    Validate the session token and return user information.
    """
    if token not in storage.sessions_db:
        raise HTTPException(status_code=401, detail="Invalid session token")
    username = storage.sessions_db[token]
    return {"username": username, "status": "Token is valid"}
