import os
from .common import *

# Override the DATABASES dictionary to add the required SSL mode.
# The other database settings (USER, PASSWORD, HOST, etc.) are already
# loaded from environment variables by the default `common.py` settings.

# Explicitly set the HOST from the environment variable to ensure it's not missed.
DATABASES["default"]["HOST"] = os.getenv("POSTGRES_HOST")

# Add the required SSL mode for the connection.
DATABASES["default"]["OPTIONS"] = {
    "sslmode": "require"
}
