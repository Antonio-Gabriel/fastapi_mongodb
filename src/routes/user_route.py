from fastapi import APIRouter

from ..models.user import User
from ..configs.db import conn

from ..schemas.user_schema import users_entities_schema

user_route = APIRouter(prefix="/api/v1", tags=["Users"])


@user_route.get("/")
async def find_all_users():
    """find all users"""
    return users_entities_schema(conn.local.user.find())


@user_route.post("/create")
async def create_user(user: User):
    """create new user"""
    conn.local.user.insert_one(dict(user))
    return users_entities_schema(conn.local.user.find())
