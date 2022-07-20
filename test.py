from datetime_check import datetime_check


def test_module():
    assert datetime_check(0, '01.01.2005', '07:30') == 'The first date has been reached! ( 01.01.2005 - 07:30 )'
    assert datetime_check(1, '24.07.1995', '16:45') == 'The second date has been reached! ( 24.07.1995 - 16:45 )'
    assert datetime_check(2, '04.05.2012', '21:00') == 'The third date has been reached! ( 04.05.2012 - 21:00 )'
    assert datetime_check(3, '04.09.2024', '09:00') == 'The fourth date will reach! ( 04.09.2024 - 09:00 )'

    print('All test cases PASSED!')


if __name__ == '__main__':
    test_module()

