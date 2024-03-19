from fastapi import APIRouter, HTTPException
from user.User import User
from user.UserController import UserController

router = APIRouter()

@router.post('/login')
async def login(form_data: User):
    user = UserController.login(form_data)
    if not user:
        raise HTTPException(
            status_code=400,
            detail='Incorrect username or password'
        )
    access_token = UserController.create_access_token(data={'sub': user})
    return {'access_token': access_token, 'token_type': 'bearer'}
