"""
S - Single Responsibility Principle
Each class or function should have one, and only one, responsibility.
Example: Separating logic for handling user registration from the database operations.
"""

from fastapi import FastAPI, HTTPException

app = FastAPI()


# Handles only user registration
class UserRegistrationService:
    def register_user(self, username: str, password: str):
        # Example validation logic
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long")
        return {"username": username, "status": "registered"}


# Handles database-related operations
class UserDatabaseService:
    def save_user_to_db(self, user: dict):  # type: ignore
        # Simulating database save operation
        print(f"Saving user: {user}")
        return True


@app.post("/register/")
async def register_user(username: str, password: str):
    user_service = UserRegistrationService()
    db_service = UserDatabaseService()

    try:
        user = user_service.register_user(username, password)
        db_service.save_user_to_db(user)  # type: ignore
        return {"message": "User registered successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
