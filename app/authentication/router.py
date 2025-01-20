from fastapi import APIRouter, HTTPException

router = APIRouter()

users_db = {}  # Temporary in-memory storage for users
sessions_db = {}  # Temporary in-memory storage for sessions

@router.post("/register")
async def register_user(username: str, password: str) -> dict[str, str]:
    """
    Register a new user.
    """
    if username in users_db:
        raise HTTPException(status_code=409, detail="User already exists")
    users_db[username] = password
    return {"status": "User registered successfully"}

@router.post("/login")
async def login_user(username: str, password: str) -> dict[str, str]:
    """
    Login user and create a session token.
    """
    if username not in users_db or users_db[username] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    session_token = f"token-{username}"  # Example token
    sessions_db[session_token] = username
    return {"token": session_token}

@router.post("/logout")
async def logout_user(token: str) -> dict[str, str]:
    """
    Logout user and invalidate the session token.
    """
    if token not in sessions_db:
        raise HTTPException(status_code=401, detail="Invalid session token")
    del sessions_db[token]
    return {"status": "User logged out successfully"}

@router.get("/introspect")
async def introspect_token(token: str) -> dict[str, str]:
    """
    Validate the session token and return user information.
    """
    if token not in sessions_db:
        raise HTTPException(status_code=401, detail="Invalid session token")
    username = sessions_db[token]
    return {"username": username, "status": "Token is valid"}
