import os
from .common import *

# Override the DATABASES dictionary to add the required SSL mode.
# The other database settings (USER, PASSWORD, HOST, etc.) are already
# loaded from environment variables by the default `common.py` settings.
#
# Explicitly set all database credentials from environment variables to ensure
# they are correctly applied when using a custom config.
DATABASES["default"]["HOST"] = os.getenv("POSTGRES_HOST")
DATABASES["default"]["USER"] = os.getenv("POSTGRES_USER")
DATABASES["default"]["PASSWORD"] = os.getenv("POSTGRES_PASSWORD")
DATABASES["default"]["OPTIONS"] = { "sslmode": "require" }

#######################################################################

# Celery/RabbitMQ settings
#
BROKER_URL = "amqp://{user}:{password}@{hostname}:{port}/{vhost}".format(
    user=os.getenv("RABBITMQ_USER", "taiga"),
    password=os.getenv("RABBITMQ_PASS", "taiga"),
    hostname=os.getenv("RABBITMQ_HOST", "taiga-rabbitmq"),
    port=os.getenv("RABBITMQ_PORT", 5672),
    vhost=os.getenv("RABBITMQ_VHOST", "taiga"),
)
