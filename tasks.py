from celery_worker import celery

@celery.task
def calculate_load_task(voltage, current):
    load = voltage * current

    if load > 1500:
        status = "Critical Load"
    elif load > 1000:
        status = "High Load"
    else:
        status = "Normal Load"

    return {
        "load": load,
        "status": status
    }