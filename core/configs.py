"""
project Project (Generated by Panther on 2023-09-17)
"""

from datetime import timedelta
from pathlib import Path

from panther.throttling import Throttling
from panther.utils import load_env

BASE_DIR = Path(__name__).resolve().parent
env = load_env(BASE_DIR / '.env')

SECRET_KEY = env['SECRET_KEY']

# # # More Info: Https://PantherPy.GitHub.io/middlewares/
MIDDLEWARES = [
    ('panther.middlewares.db.DatabaseMiddleware', {'url': f'pantherdb://{BASE_DIR}/database.pdb'}),
]

# More Info: https://PantherPy.GitHub.io/configs/#user_model
USER_MODEL = 'app.models.User'

# More Info: https://PantherPy.GitHub.io/authentications/
AUTHENTICATION = 'panther.authentications.JWTAuthentication'

# More Info: https://PantherPy.GitHub.io/monitoring/
MONITORING = True

# More Info: https://PantherPy.GitHub.io/log_queries/
LOG_QUERIES = True

# More Info: https://PantherPy.GitHub.io/throttling/
THROTTLING = Throttling(rate=60, duration=timedelta(minutes=1))

# More Info: https://PantherPy.GitHub.io/urls/
URLs = 'core.urls.url_routing'
