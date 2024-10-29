# from apscheduler.schedulers.background import BackgroundScheduler
# from django_apscheduler.jobstores import DjangoJobStore, register_events
# from django.core.management import call_command
# import logging
# import calendar
# from datetime import datetime

# logger = logging.getLogger(__name__)

# def ejecutar_estrategia():
#     hoy = datetime.today()
#     ultimo_dia = calendar.monthrange(hoy.year, hoy.month)[1]
#     if hoy.day == ultimo_dia:
#         logger.info("Ejecutando estrategia...")
#         call_command('ejecutar_estrategia')
#     else:
#         logger.info("Hoy no es el último día del mes. No se ejecuta la estrategia.")

# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_jobstore(DjangoJobStore(), "default")

#     scheduler.add_job(
#         ejecutar_estrategia,
#         trigger='cron',
#         hour=0,
#         minute=0,
#         id='ejecutar_estrategia',
#         replace_existing=True,
#     )

#     register_events(scheduler)
#     scheduler.start()
#     logger.info("Scheduler iniciado...")


from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.core.management import call_command
import logging
import asyncio 

logger = logging.getLogger(__name__)

def ejecutar_estrategia():
    logger.info("Ejecutando estrategia...")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        call_command('ejecutar_estrategia')
    finally:
        loop.close()
        logger.info("Estrategia ejecutada y bucle de eventos cerrado.")

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
        ejecutar_estrategia,
        trigger='interval',
        minutes=2, 
        id='ejecutar_estrategia',
        replace_existing=True,
    )

    register_events(scheduler)
    scheduler.start()
    logger.info("Scheduler iniciado...")