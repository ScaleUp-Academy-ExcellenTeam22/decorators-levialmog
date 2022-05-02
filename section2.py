from typing import Callable


def change_functionality(_: type) -> Callable:
    """
    The function gets function(times2) and call to inner function.
    :param _: The function, but we will not use this variable.
    :return: The answer of the inner function.
    """
    def inner(_: Callable) -> Callable:
        """
        The function prints Surprise!.
        :param _: The number, but we will not use this variable.
        """
        print("Surprise!")
    return inner


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
