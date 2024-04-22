import time
import unittest
from apscheduler.schedulers.blocking import BlockingScheduler
from HTMLTestRunner import HTMLTestRunner
from common.email_util import Email

def run_tests():
    suite = unittest.defaultTestLoader.discover('./testcase', 'test_*.py')
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = './report/' + now + 'result.html'

    with open(filename, 'wb') as report_file:
        runner = HTMLTestRunner(stream=report_file, title='Test Results')
        runner.run(suite)

    with open(filename, 'r') as fp:
        print(fp.read())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    #interval
    scheduler.add_job(run_tests, 'interval', seconds=10)

    #at one time in the future
    #scheduler.add_job(run_tests,'date',run_date=datetime(2024.6,1,13,30,31))

    #run in period everyday at 5:21 pm
    # scheduler.add_job(run_tests,'cron',day_of_week='0-6',hour=17,minute=21)
    scheduler.start()
