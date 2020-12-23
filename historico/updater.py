from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from historico import api


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(api.check_status, 'interval', minutes=1)
    scheduler.start()