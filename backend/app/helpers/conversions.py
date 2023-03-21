

def to_base_62(number):

    if not isinstance(number, int) or number < 0:
        raise TypeError("Only positive integers are allowed")
    
    base = 62
    possible_characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    reminders = []



    while number > 0:

        reminder = number % base
        reminders.append(possible_characters[reminder])

        number = number // base

    return ''.join(reminders[::-1])








        