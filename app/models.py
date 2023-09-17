from panther.db.models import Model


class User(Model):
    first_name: str | None = ''
    last_name: str | None = ''
    username: str
    password: str
