def user_schema(item) -> dict:
    """user schema"""
    return {
        "id": str(item.get("_id")),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"],
    }


def users_entities_schema(entity) -> list:
    """users schema"""
    return [user_schema(item) for item in entity]
