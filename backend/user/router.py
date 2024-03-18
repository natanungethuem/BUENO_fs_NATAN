from fastapi import APIRouter, HTTPException
# from fastapi.security import OAuth2PasswordRequestForm
from user.login import login as user_login, create_access_token
from user.User import User

router = APIRouter()

@router.post('/login')
async def login(form_data: User):
    user = user_login(form_data)
    if not user:
        raise HTTPException(
            status_code=400,
            detail='Incorrect username or password'
        )
    access_token = create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}
