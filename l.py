"""
L - Liskov Substitution Principle
Subtypes should be substitutable for their base types.
Example: Using a base class for different types of database operations.
"""


class DatabaseService:
    def save(self, data: dict):  # type: ignore
        raise NotImplementedError("Save method not implemented")


class PostgresService(DatabaseService):
    def save(self, data: dict):  # type: ignore
        print(f"Saving to PostgreSQL: {data}")


class MongoDBService(DatabaseService):
    def save(self, data: dict):  # type: ignore
        print(f"Saving to MongoDB: {data}")


@app.post("/save/")  # type: ignore
async def save_data(data: dict, use_mongo: bool = False):  # type: ignore
    db_service: DatabaseService = MongoDBService() if use_mongo else PostgresService()
    db_service.save(data)  # type: ignore
    return {"message": "Data saved"}
