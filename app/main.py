import logging

from app.core.settings import get_settings
from app.core.database import setup_database
from app.core.fastapi import get_application

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("databases").setLevel(logging.DEBUG)

app = get_application(get_settings())

setup_database(app, get_settings())


