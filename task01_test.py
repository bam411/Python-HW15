from task01_parsing import TextToDate
import argparse

if __name__ == '__main__':
    arg_pars = argparse.ArgumentParser(
        description='Определение даты из строки')
    arg_pars.add_argument('texts', metavar='S', type=str,
                          nargs='*', help='дата в виде: "1-й четверг ноября"')
    args = arg_pars.parse_args()

    ttd = TextToDate()
    if len(args.texts) > 0:
        print('Run set of user\'s tests')
        for text in args.texts:
            print(ttd(text))
    else:
        print('Run set of tests default')
        print(ttd('1-й четверг ноября'))
        print(ttd('3-я среда мая'))
        print(ttd.date)
        print(ttd('5-я среда мая'))
        print(ttd('2-я середина мая'))
        print(ttd('2-я среда месяца'))
        print(ttd())
        print(ttd(''))
