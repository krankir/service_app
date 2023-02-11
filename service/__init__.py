from .celery_app import app as celery_app

# Чтобы celery_app стартанула вместе с приложением Django.
__all__ = ('celery_app',)
