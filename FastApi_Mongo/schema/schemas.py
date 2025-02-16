def individual_serial(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "age": user["age"],
        "email": user["email"],
        "password": user["password"]
    }

def list_serial(users) -> list:
    return [individual_serial(user) for user in users]