import uvicorn as server
from fastapi import FastAPI

from src.routes.user_route import user_route

app = FastAPI(
    title="Users Application",
    description="An application to register user data",
)


@app.get("/")
def main() -> dict:
    return {"msg": "Welcome to user api"}


app.include_router(user_route)

if __name__ == "__main__":
    server.run(app, host="0.0.0.0", port=3333)
