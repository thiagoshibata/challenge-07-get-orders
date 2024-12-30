from flask import Flask, request
from src.drivers.jwt_handler import JwtHandler

def auth_jwt_verify():
    jwt_handler = JwtHandler()
    raw_token = request.headers.get("Authorization")
    user_id = request.headers.get("uid")

    if not raw_token or not user_id:
        raise Exception("Invalid Auth Informations")

    token = raw_token.split()[1]
    token_information = jwt_handler.decode_jwt_token(token)
    token_uid = token_information["user_id"]
    token_username = token_information["username"]

    if user_id and token_uid and (int(token_uid)==int(user_id)):
        return token_information
    
    raise Exception("User Unauthorized")