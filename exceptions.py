class RangeError(Exception):
    pass

class InvalidUserError(Exception):
    def __init__(self, name):
        super().__init__(f'{name} is not a valid username')


def get_int():
    val = int(input('Enter an integer: '))
    if not val in range(1, 11):
        raise RangeError(f'{val} is out of range - must be between 1 and 10')
        # for limited, range 1-10
    return val


# can do for my assignment, character
def get_username():
    valid_users = ['alice', 'toby']
    name = input('Username: ')
    if not name in valid_users:
        raise InvalidUserError(name)
    return name


while True:
    try:
        x = get_int()
        print(1 / x)
        break
    except RangeError as err:
        print(err)
    except ValueError as err:
        print('Input must be an integer')
    

    except ZeroDivisionError:
        print('Input cannot be zero')

    # else:
    #     print('else reached')
    #     break

    # finally:
    #     print('finally reached')
        # finally means it shows up everytime after input sth.

print(f'You entered {x}')