#1
import math

def safe_sqrt(number: int):
    if number >= 0:
        return math.sqrt(number)
    else:
        raise Exception('il numero è negativo')

#2
class InvalidPasswordError(Exception):
    'invalid password'

def validate_password(password):
    maiusc: int = 0
    spec_char: int = 0
    show_spec_char: str = '#@\'[]()+*!$£&?^'

    for char in password:

        if (char.isupper() == True):
            maiusc += 1

        if (char in show_spec_char):
            spec_char += 1

    if (len(password) >= 20) and (maiusc >= 3) and (spec_char >= 4):
        print('password is valid')
    else:
        raise InvalidPasswordError

#3










