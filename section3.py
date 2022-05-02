from typing import Callable, Any

import decorator


@decorator.decorator
def change_functionality(func: Callable,  *args: Any, **kwargs: Any) -> int:
    """
    The function gets function(times2) and return the result of times2 function.
    :param func: The wrapper function for the function that was got (times2).
    :param args: The parameter that function gets.
    :param kwargs: The parameter that function gets.
    :return: The value that the function times2 returned.
    """
    return func(*args, **kwargs)


@change_functionality
def times2(number: int) -> int:
    """
    The function gets a number and first, calls to decorator function - type_check.
    :param number: The number that the function gets.
    :return: The number * 2
    """
    return number * 2


if __name__ == "__main__":
    print(times2(2))
