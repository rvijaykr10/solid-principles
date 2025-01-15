"""
O - Open/Closed Principle
Classes should be open for extension but closed for modification.
Example: Adding a new type of logging without modifying the existing code.
"""


class Logger:
    def log(self, message: str):  # type: ignore
        raise NotImplementedError("Log method not implemented")


class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"Log to console: {message}")


class FileLogger(Logger):
    def log(self, message: str):
        with open("logfile.txt", "a") as file:
            file.write(f"Log to file: {message}\n")


def log_event(logger: Logger, message: str):
    logger.log(message)


@app.get("/log/")  # type: ignore
async def log_event_api():
    logger = (
        ConsoleLogger()
    )  # Can be replaced with FileLogger without modifying log_event function
    log_event(logger, "User accessed the endpoint")
    return {"message": "Event logged"}
