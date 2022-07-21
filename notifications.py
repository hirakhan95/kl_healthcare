import os
from datetime import datetime

DIR_LOCATION = os.path.dirname(os.path.abspath(__file__))
NOTIFY_PATH = DIR_LOCATION+'/notify.schedule'
NOTIFICATION_TITLE = 'KL Health Care Notification'


def os_notify(title: str, text: str):
    """
    OS Notification function
    :param title: title of the notification
    :param text: text for the notification
    """
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


with open(NOTIFY_PATH) as schedule_file:
    save_back_again = []
    for line in schedule_file:
        ordinal, dt = line.split('#')
        dt = dt.strip()

        dt_obj = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')

        if dt_obj <= datetime.now():
            ntfy_str = 'The {} date has been reached! ( {:%d.%m.%Y} - {:%H:%M} )'.format(ordinal, dt_obj.date(),
                                                                              dt_obj.time())
            os_notify(NOTIFICATION_TITLE, ntfy_str)
        else:
            save_back_again.append(f'{ordinal}#{dt}')

if os.path.exists(NOTIFY_PATH):
    os.remove(NOTIFY_PATH)

with open(NOTIFY_PATH, 'a+') as file:
    for text in save_back_again:
        file.write(f'{text}\n')
