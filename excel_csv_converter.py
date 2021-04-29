import argparse
import os.path

import pandas as pd


def main():
    parser = argparse.ArgumentParser(
        description='Convert between excel formats and csv.',
        usage='<File>',
    )
    parser.add_argument('File', help='File to convert.')
    args = parser.parse_args()

    filename, file_extension = os.path.splitext(args.File)
    excel_formats = ['.xls', '.xlsx']
    try:
        if file_extension in excel_formats:
            df = pd.read_excel(args.File)
            df.to_csv(filename + '.csv', index=None, header=True)
        elif file_extension == '.csv':
            df = pd.read_csv(args.File)
            df.to_excel(filename + '.xlsx', index=None, header=True)
    except FileNotFoundError:
        raise


if __name__ == '__main__':
    exit(main())
