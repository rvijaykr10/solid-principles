"""
I - Interface Segregation Principle
A class should not be forced to implement interfaces it does not use.
Example: Splitting user actions into smaller interfaces.
"""


class CanLogin:
    def login(self, username: str, password: str):  # type: ignore
        raise NotImplementedError()


class CanRegister:
    def register(self, username: str, password: str):  # type: ignore
        raise NotImplementedError()


class UserService(CanLogin, CanRegister):
    def login(self, username: str, password: str):
        return f"User {username} logged in"

    def register(self, username: str, password: str):
        return f"User {username} registered"


user_service = UserService()


@app.post("/user/login/")  # type: ignore
async def user_login(username: str, password: str):
    return {"message": user_service.login(username, password)}


@app.post("/user/register/")  # type: ignore
async def user_register(username: str, password: str):
    return {"message": user_service.register(username, password)}
