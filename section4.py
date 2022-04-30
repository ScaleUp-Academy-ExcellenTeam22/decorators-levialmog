import functools


class CsvFile:
    """
    A Csv File class. I chose:
    @functools.cached_property -Transform a method of a class into a property whose value is
    computed once and then cached as a normal attribute for the life of the instance.
    @functools.lru_cache Decorator to wrap a function with a memorizing callable that saves up to the maxsize most
    recent calls. It can save time when an expensive or I/O bound function is periodically called
    with the same arguments.
    @functools.total_ordering Given a class defining one or more rich comparison ordering methods, this class decorator
    supplies the rest.
    """
    def __init__(self, csv_file):
        """
        The function gets a csv file and and initialize the class member csv_file.
        :param csv_file: The csv file.
        """
        self.csv_file = csv_file

    @functools.cached_property
    def delete_empty_rows(self) -> None:
        """
        The function clears the table of blank rows.
        :return: The new table without clear blank rows.
        """
        return self.csv_file.dropna(inplace=True).toString()

    @functools.lru_cache(maxsize=None)
    def print_information(self) -> None:
        """
        The function provides additional information about the data set.
        :return: The information.
        """
        print(self.csv_file.info())

    @functools.total_ordering
    def appears_most(self, col_value) -> str:
        """
        The function gets the name of a requested column and returns the value that appears most often.
        :param col_value: The name of a column.
        :return: The value that appears most.
        """
        return self.csv_file[col_value].mode()[0]
