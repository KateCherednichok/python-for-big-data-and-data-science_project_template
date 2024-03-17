import pandas


def input_from_console():
    """
    Get input from console

    Examples:
         >> input_from_console()
        'Hello'

    Returns:
        str: input from console
    """
    return input('Enter information to read:')


def input_from_file_build_in(file_name):
    """
    Read file by using method built in Python

    Examples:
         >> input_from_file_build_in('./data/test1.txt'):
        'First Test'

    Args:
        file_name (str): path of file to read

    Returns:
        str: information read from file

    Raises:
        FileNotFoundError: if the file at the specified path is not found
    """
    with open(file_name, 'r') as file:
        return file.read()


def input_from_file_by_pandas(file_name):
    """
    Read CSV file by using method from pandas library

    Examples:
         >> input_from_file_by_pandas('./data/test1.csv'):
        'Empty DataFrame
         Columns: [Test]
         Index: []'

    Args:
        file_name (str): path of file to read

    Returns:
        str: information read from file

    Raises:
        FileNotFoundError: if the file at the specified path is not found
        pandas.errors.EmptyDataError: if file is empty
    """
    info_from_file = pandas.read_csv(file_name)
    return info_from_file.to_string()