import decorator


@decorator.decorator
def change_functionality(func,  *args, **kwargs):
    """
    The function gets function(times2) and return the string "Surprise!".
    :param func:
    :param _: we will not use this variable.
    :return: The string "Surprise!".
    """
    return "Surprise!"


@change_functionality
def times2(number):
    """
    The function gets a number and first, calls to decorator function - type_check.
    :param number: The number that the function gets.
    :return: The number * 2
    """
    print(number)


if __name__ == "__main__":
    print(times2(2))
