from celery import Celery

celery = Celery(
    "smartgrid",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)