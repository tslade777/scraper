from fastapi.responses import JSONResponse


class ClientErrorException(Exception):
    def __init__(self):
        self.status_code = 400
        self.error = "client_error"
        self.message = "An unknown error occurred"

    def response(self) -> JSONResponse:
        return JSONResponse(
            status_code=self.status_code, 
            content={
                "error": self.error,
                "message": self.message,
                },
            )


class EntityNotFound(ClientErrorException):
    def __init__(self, entity_name: str, entity_id: int):
        self.status_code = 404
        self.error = "entity_not_found"
        self.message = f"Unable to find {entity_name} with id={entity_id}"


class DuplicateChatNameDetected(ClientErrorException):
    def __init__(self, chat_name: str):
        self.status_code = 422
        self.error = "duplicate_entity_value"
        self.message = f"Duplicate value: chat with name={chat_name} already exists"

class NoChatMembershipDetected(ClientErrorException):
    def __init__(self, chat_id: int, owner_id: int):
        self.status_code = 422
        self.error = "chat_membership_required"
        self.message = f"Account with id={owner_id} must be a member of chat with id={chat_id}"

class CantRemoveChatOwner(ClientErrorException):
    def __init__(self):
        self.status_code = 422
        self.error = "chat_owner_removal"
        self.message = "Unable to remove the owner of a chat"

class UnprocessableEntity(ClientErrorException):
    def __init__(self, entity: str, value: int):
        self.status_code = 422
        self.error = "duplicate_entity_value"
        self.message = f"Duplicate value: account with {entity}={value} already exists"

class InvalidCredentials(ClientErrorException):
    def __init__(self):
        self.status_code = 401
        self.error = "invalid_credentials"
        self.message = f"Authentication failed: invalid username or password"

class NotAuthenticated(ClientErrorException):
    def __init__(self):
        self.status_code = 403
        self.error = "authentication_required"
        self.message = f"Not authenticated"

class ExpiredAccessToken(ClientErrorException):
    def __init__(self):
        self.status_code = 403
        self.error = "expired_access_token"
        self.message = f"Authentication failed: expired access token"

class InvalidAccessToken(ClientErrorException):
    def __init__(self):
        self.status_code = 403
        self.error = "invalid_access_token"
        self.message = f"Authentication failed: invalid access token"

class Unauthorized(ClientErrorException):
    def __init__(self):
        self.status_code = 401
        self.error = "invalid_credentials"
        self.message = f"Authentication failed: invalid username or password"

class AccessDenied(ClientErrorException):
    def __init__(self, item: str):
        self.status_code = 403
        self.error = "access_denied"
        self.message = f"Cannot create {item} on behalf of different account"