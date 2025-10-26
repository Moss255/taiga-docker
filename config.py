import os
from .common import *

# Override the DATABASES dictionary to add the required SSL mode.
# The other database settings (USER, PASSWORD, HOST, etc.) are already
# loaded from environment variables by the default `common.py` settings.
DATABASES["default"]["OPTIONS"] = {
    "sslmode": "require"
}
