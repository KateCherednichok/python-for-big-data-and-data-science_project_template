def output_in_console(information_to_output):
    """
    Outputs information in console

    Args:
        information_to_output (str): information to output
    """
    print(information_to_output)


def output_in_file_build_in(information_to_output, file_name):
    """
    Outputs information in file

    Args:
        information_to_output (str): information to output
        file_name (str): path to the file for outputting information

    Raises:
        TypeError: if information_to_output is not str
    """
    with open(file_name, 'w') as file:
        file.write(information_to_output)