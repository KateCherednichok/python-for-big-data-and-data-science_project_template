from app.io.input import input_from_console, input_from_file_build_in, input_from_file_by_pandas
from app.io.output import output_in_console, output_in_file_build_in


def main():
    info_from_console = input_from_console()
    info_from_file_build_in = input_from_file_build_in('./data/test1.txt')
    info_from_file_by_pandas = input_from_file_by_pandas('./data/test1.csv')
    all_information = info_from_console+'\n'+info_from_file_build_in+'\n'+info_from_file_by_pandas
    output_in_console(all_information)
    output_in_file_build_in(all_information, 'output.txt')


if __name__ == '__main__':
    main()
