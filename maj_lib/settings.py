import os

if os.environ.get("RAILWAY_ENVIRONMENT_NAME") == "production":
    from .settings_prod import *
else:
    from .settings_local import *