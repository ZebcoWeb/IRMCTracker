from modules.database.basemodel import *
from .server import Server

class ServerMeta(BaseModel):
    key = CharField(max_length=255)
    value = LongTextField()
    server_id = ForeignKeyField(Server, 'id', backref='meta')

    class Meta:
        table_name = 'servers_meta'
        indexes = (
            (("key", "server_id"), True),
        )

def get(server, key: str) -> str:
    try:
        return ServerMeta.get((ServerMeta.key == key) & ServerMeta.server_id == server).value
    except DoesNotExist:
        return None

def delete(server, key) -> bool:
    if exists(server, key):
        meta = ServerMeta.get((ServerMeta.server_id == server) & (ServerMeta.key == key))
        meta.delete_instance()
        return True
    return False

def exists(server, key) -> bool:
    query = ServerMeta.select().where((ServerMeta.server_id == server) & (ServerMeta.key == key))
    if query.exists():
        return True
    return False

def add(server, key: str, value: str) -> bool:    
    ServerMeta.replace(
        server_id = server,
        key = key,
        value = value
    ).execute()

    return True

def update(server, key: str, value: str) -> bool:
    if not exists(server, key):
        return False

    ServerMeta.update(
        server_id = server,
        key = key,
        value = value
    ).where(
        (ServerMeta.server_id == server) & (ServerMeta.key == key)
    ).execute()
    
    return True
