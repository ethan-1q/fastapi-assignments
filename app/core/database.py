from tortoise.contrib.fastapi import register_tortoise

from app.app.models import krew, member


def setup_database(app, settings):
    register_tortoise(
        app,
        config={
            "connections": {
                "icp_db": settings.ICP_DATABASE_URL,
                "my_db": settings.MY_DATABASE_URL,
            },
            "apps": {
                "member": {"models": [member], "default_connection": "icp_db"},
                "krew": {"models": [krew], "default_connection": "my_db"},
            },
        },
        generate_schemas=settings.GENERATE_SCHEMAS,
        add_exception_handlers=False
    )
