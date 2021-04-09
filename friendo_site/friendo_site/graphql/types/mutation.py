from ariadne import MutationType
from .users import resolve_login, get_user
from .servers import get_server, create_server, update_server

mutation = MutationType()
mutation.set_field("login", resolve_login)
mutation.set_field("user", get_user)
mutation.set_field("get_guild", get_server)
mutation.set_field("create_guild", create_server)
mutation.set_field("update_guild", update_server)
