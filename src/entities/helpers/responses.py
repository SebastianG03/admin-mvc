from fastapi.responses import JSONResponse
from fastapi import status


unauthorized_access_response: JSONResponse = JSONResponse(
    status_code=status.HTTP_401_UNAUTHORIZED, 
    content={"message": "Unauthorized Access"})

internal_server_error_response: JSONResponse = lambda message: JSONResponse(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
    content={"message": message}
)

no_content_response: JSONResponse = JSONResponse(
    status_code=status.HTTP_204_NO_CONTENT,
    content="Oh! This is to clean!"
)


#Auth responses
invalid_tokens_response: JSONResponse = JSONResponse(
    status_code=status.HTTP_400_BAD_REQUEST, 
    content={"message": "Invalid email or password"}
)
login_successful_response: JSONResponse = JSONResponse(
    status_code=status.HTTP_200_OK, 
    content={"message": "Login Successful"}
)

user_exists_response: JSONResponse = JSONResponse(
    status_code=status.HTTP_400_BAD_REQUEST, 
    content={"message": "User already exists"}
)

not_logged_response: JSONResponse = JSONResponse(
    status_code=status.HTTP_401_UNAUTHORIZED, 
    content={"message": "Not Logged In"})

already_logged_response: JSONResponse = JSONResponse(
    status_code=status.HTTP_400_BAD_REQUEST, 
    content={"message": "You are already logged. Log out before create an account"})

### Toma un bool como argumento, si esta loggeado es True, caso contrario False.
logout_response: JSONResponse = lambda logged: JSONResponse(
            status_code=status.HTTP_200_OK, 
            content={"message": "Logout Successfully"}) if logged else JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                content={"message": "You are not logged. Try logging in first"})