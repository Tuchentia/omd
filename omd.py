# Guido van Rossum <guido@python.org>

def step(message, step_yes, step_no):
    print(message)

    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    step_yes() if options[option] else step_no()


def step1():
    step(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️',
        step2_umbrella,
        step2_no_umbrella
    )


def step2_umbrella():
    step(
        'Зонтик не подходит к сумке утки-маляра. '
        'Взять ей зонтик?',
        step3_sad,
        step2_no_umbrella
    )


def step2_no_umbrella():
    step(
        'Утка-маляр любит свой зонтик. '
        'Взять ей зонтик?',
        step2_umbrella,
        step3_sad
    )


def step3_sad():
    step(
        'Утка-маляр расстроилась и не пошла в бар. '
        'Попробовать еще раз?',
        step1,
        end
    )


def end():
    pass


if __name__ == '__main__':
    step1()
