from typing import Iterator


# ----------------------------------------------------------------------------------------------------------------------
# Create class
class QueryHandler:
    def __init__(self, **data):
        """
        Initialize a query handler with the given data \n
        :param data: Dictionary data with command, value and iterable data
        """
        self._cmd = data.get("cmd")
        self._value = data.get("value")
        self._data = data.get("data")

    def filter_(self) -> Iterator:
        """
        Filter a data using the given query \n
        :return: Iterator object with the results
        """
        return filter(lambda line: self._value in line, self._data)

    def map_(self) -> Iterator | Exception:
        """
        Get the column in the data \n
        :return: Iterator object with the results
        """
        if not self._value.isdigit():
            raise TypeError("Invalid query, column must be a number")

        return map(lambda line: line.split()[int(self._value)], self._data)

    def unique_(self) -> set:
        """
        Get unique objects in data \n
        :return: Set with objects
        """
        return set(self._data)

    def sort_(self) -> list | Exception:
        """
        Sort data in ascending or descending order \n
        :return: Sorted data
        """
        if self._value not in ['asc', 'desc']:
            raise ValueError("Only 'asc' and 'desc' allowed")

        if self._value == 'desc':
            return sorted(self._data, reverse=True)
        return sorted(self._data, reverse=False)

    def limit_(self) -> list | Exception:
        """
        Limit data \n
        :return: Limited data
        """
        if not self._value.isdigit():
            raise TypeError("Invalid query, must be a number")

        return self._data[:int(self._value)]

    def build_query(self) -> Iterator | set | list | Exception:
        """
        Get result depending on input data \n
        :return: Filtered information depending on input query
        """
        if self._cmd == 'filter':
            return self.filter_()
        elif self._cmd == 'map':
            return self.map_()
        elif self._cmd == 'unique':
            return self.unique_()
        elif self._cmd == 'sort':
            return self.sort_()
        elif self._cmd == 'limit':
            return self.limit_()
        else:
            raise ValueError("Command name is not valid")

    def __repr__(self):
        return f"Instance with command '{self._cmd}', value '{self._value}' and data '{self._data}'"
