import functools
from typing import Callable, Any


def type_check(correct_type: type) -> Callable:
    """
    The function is a decorator factory. The function returns decorators that decorate functions.
    :param correct_type: The wanted type.
    :return: The answer of decorator_type_check function.
    """
    def decorator_type_check(func: Callable) -> Callable:
        """
        The function gets function(times2) and call to inner function.
        :param func: The function that get.
        :return: The answer of inner function.
        """
        @functools.wraps(func)
        def inner(variable: Any) -> Any:
            """
            The function gets a variable and checks if its type is the same as the wanted type(correct_type),
            Yes - calls to func(in this case - times2), No - throw Exception.
            :param variable: The checked variable.
            :return: The answer of func function.
            """
            if isinstance(variable, correct_type):
                return func(variable)
            else:
                raise ValueError("Incorrect type!")

        return inner
    return decorator_type_check


@type_check(int)
def times2(number: int) -> int:
    """
    The function gets a number and first, calls to decorator function - type_check.
    :param number: The number that the function gets.
    :return: The number * 2
    """
    return number * 2


if __name__ == "__main__":
    try:
        print(times2(4))
        print(times2("4"))
    except ValueError as error:
        print(error)
