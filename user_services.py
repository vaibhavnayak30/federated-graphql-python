import uvicorn
import strawberry
from strawberry.federation import Schema
from strawberry.asgi import GraphQL
from typing import Optional

_USERS = {
    "1": {"id": "1", "username": "alice"},
    "2": {"id": "2", "username": "bob"},
}

@strawberry.federation.type(keys=["id"])
class User:
    id: strawberry.ID
    username: str

    @classmethod
    def resolve_reference(cls, id: strawberry.ID):
        data = _USERS.get(str(id))
        if not data:
            return None
        return User(id=data["id"], username=data["username"])
    

@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: strawberry.ID) -> Optional[User]:
        data = _USERS.get(str(id))
        if not data:
            return None
        return User(id=data['id'], username=data['username'])
    
schema = Schema(query=Query, types=[User])

    