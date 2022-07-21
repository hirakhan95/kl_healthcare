import os
from _datetime import datetime
from crontab import CronTab
import inflect

p = inflect.engine()

DIR_LOCATION = os.path.dirname(os.path.abspath(__file__))
NOTIFY_PATH = DIR_LOCATION+'/notifications.py'
NOTIFY_LOGS = DIR_LOCATION+'/ntfy.logs'


def cron_function_every_minute(command):
    cron = CronTab(user=os.getlogin())
    exist = False
    for line in cron.lines:
        if line and command == line.command:
            exist = True

    if not exist:
        job = cron.new(command=command)
        job.minute.every(1)
        cron.write()


def datetime_check(index: int, date_str: str, time_str: str):
    """
    Datetime Check
    :param index: number to show
    :param date_str: date string
    :param time_str: time str
    :return: string that the date has been reached
    """
    index_ordinal = p.number_to_words(p.ordinal(index + 1))
    datetime_str = date_str + ':' + time_str
    datetime_obj = datetime.strptime(datetime_str, '%d.%m.%Y:%H:%M')

    with open('notify.schedule', 'a+') as file:
        file.write(f'{index_ordinal}#{datetime_obj}\n')


if __name__ == '__main__':
    question = int(input('How much data do you want to enter? '))
    for i in range(question):
        date_input = input('Please enter a date: ')
        time_input = input('Please enter a time: ')
        datetime_check(i, date_input, time_input)

    cron_function_every_minute(f'python3 {NOTIFY_PATH} > {NOTIFY_LOGS}')

    print("Thank you very much. I will notify them!\n...")
