def change_functionality(_):
    """
    The function gets function(times2) and call to inner function.
    :param _: The func, but we will not use this variable.
    :return: The answer of inner function.
    """
    def inner(_):
        """
        The function prints Surprise!.
        :param _: The number, but we will not use this variable.
        """
        print("Surprise!")
    return inner


@change_functionality
def times2(number):
    """
    The function gets a number and first, calls to decorator function - type_check.
    :param number: The number that the function gets.
    :return: The number * 2
    """
    return number * 2


if __name__ == "__main__":
    print(times2(2))
