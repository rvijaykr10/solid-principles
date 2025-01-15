"""
D - Dependency Inversion Principle
High-level modules should not depend on low-level modules. Both should depend on abstractions.
Example: Using dependency injection in FastAPI.
"""

from fastapi import Depends


class UserRepository:
    def get_user_by_id(self, user_id: int):  # type: ignore
        return {"id": user_id, "name": "John Doe"}  # type: ignore


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_user_details(self, user_id: int):  # type: ignore
        return self.user_repo.get_user_by_id(user_id)  # type: ignore


def get_user_service(repo: UserRepository = Depends(UserRepository)):
    return UserService(repo)


@app.get("/users/{user_id}/")  # type: ignore
async def get_user(user_id: int, user_service: UserService = Depends(get_user_service)):  # type: ignore
    return user_service.get_user_details(user_id)  # type: ignore
