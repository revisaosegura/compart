from django_cron import CronJobBase, Schedule
from .scraper import scrape_site

class AtualizarCopartCron(CronJobBase):
    RUN_EVERY_MINS = 60  # 1 hora

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'copart.atualizar_copart_cron'

    def do(self):
        scrape_site()
