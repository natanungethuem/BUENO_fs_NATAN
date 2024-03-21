from fastapi import APIRouter, HTTPException
from .UserService import UserService
from .UserResponseModel import UserLogin

router = APIRouter()

@router.post('/login')
async def login(form_data: UserLogin):
    user = UserService.login(form_data)
    if not user:
        raise HTTPException(
            status_code=400,
            detail='Incorrect username or password'
        )
    access_token = UserService.create_access_token(data={'sub': user})
    return {'access_token': access_token, 'token_type': 'bearer'}
