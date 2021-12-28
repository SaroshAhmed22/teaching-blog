from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
scheduler = BackgroundScheduler()
scheduler.configure(timezone=utc)

# jobs
import casting.views as cv

# scheduler.add_job(cv.FirstCronTest, 'interval', seconds=7)
# scheduler.add_job(cv.secondCronTest, 'interval', seconds=7)
scheduler.start()