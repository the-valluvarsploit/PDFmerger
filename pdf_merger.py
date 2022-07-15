import argparse
import os
from PyPDF4 import PdfFileMerger
import sys

merger = PdfFileMerger()


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', dest='path', help="Path to PDF files directory")
    parser.add_argument('-o', '--output', dest='output', help='Output filename')
    args = parser.parse_args()
    if not (args.path and args.output):
        parser.print_help()
        sys.exit()
    return args


def merge_pdfs(path, source_files, output):
    for file in source_files:
        if file.endswith('pdf'):
            merger.append(path + '/' + file)

    merger.write(output)
    merger.close()


def main():
    args = get_arguments()
    source_files = os.listdir(args.path)
    source_files.sort()
    merge_pdfs(args.path, source_files, args.output)


if __name__ == '__main__':
    main()



