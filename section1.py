def type_check(correct_type):
    """
    The function gets a type that need to check if it's correct type and call to decorator_type_check function.
    :param correct_type: The wanted type.
    :return: The answer of decorator_type_check function.
    """
    def decorator_type_check(func):
        """
        The function gets function(times2) and call to inner function.
        :param func: The function that get.
        :return: The answer of inner function.
        """
        def inner(variable):
            """
            The function gets a variable and checks if its type is the same as the wanted type(correct_type),
            Yes - calls to func(in this case - times2), No - throw Exception.
            :param variable: The checked variable.
            :return: The answer of func function.
            """
            try:
                if not isinstance(variable, correct_type):
                    raise Exception("Incorrect type!")
                return func(variable)
            except Exception as error:
                print(error)

        return inner
    return decorator_type_check


@type_check(int)
def times2(number):
    """
    The function gets a number and first, calls to decorator function - type_check.
    :param number: The number that the function gets.
    :return: The number * 2
    """
    return number * 2


if __name__ == "__main__":
    print(times2(4))
