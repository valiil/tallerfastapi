from fastapi import APIRouter
from models.loginRequest_model import LoginRequest
from controllers.loginRequest_controller import LoginRequestController

router = APIRouter()
login_controller = LoginRequestController()

@router.post("/login")
async def login(login_request: LoginRequest):
    return login_controller.login(login_request)