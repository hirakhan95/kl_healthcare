from _datetime import datetime
import inflect
p = inflect.engine()


def datetime_check(index: int, date_str: str, time_str: str):
    """
    Datetime Check
    :param index: number to show
    :param date_str: date string
    :param time_str: time str
    :return: string that the date has been reached
    """
    checked_date = datetime.strptime(date_str, '%d.%m.%Y').date()
    checked_time = datetime.strptime(time_str, '%H:%M').time()
    s = p.number_to_words(p.ordinal(index+1))

    return 'The {} date has been reached! ( {:%d.%m.%Y} - {:%H:%M})'.format(s, checked_date, checked_time)


if __name__ == '__main__':
    question = int(input('How much data do you want to enter? '))
    res = []
    for i in range(question):
        date_input = input('Please enter a date: ')
        time_input = input('Please enter a time: ')
        res.append(datetime_check(i, date_input, time_input))

    print("Thank you very much. I will notify them!\n...")
    for r in res:
        print(r)
