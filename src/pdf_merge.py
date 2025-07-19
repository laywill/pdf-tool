import argparse
import os.path
from typing import Optional
from typing import Sequence

from PyPDF2 import PdfFileMerger


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    """
    Returns the parsed arguments from argv.

        Parameters:
            input_args (Optional[Sequence[str]]): argv contents

        Returns:
            arguments (argparse.Namespace): key (arg) value pairs
    """
    parser = argparse.ArgumentParser(
        prog="pdf_tool",
        description="Manage or merge PDFs.",
    )
    parser.add_argument(
        "-m",
        "--merge",
        action="store_true",
        help=("Merge input files, in order supplied, to form output file."),
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help=("Overwrite existing files."),
    )
    parser.add_argument(
        "-o",
        "--outfile",
        nargs=1,
        type=str,
        default=["pdf-tool-outfile.pdf"],
        action="store",
        help=("Filename that will be the outfile from the tool."),
    )
    parser.add_argument(
        "-i",
        "--infile",
        nargs="+",
        type=str,
        action="extend",
        default=[],
        help=("Filenames that will be input to the tool."),
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)

    return_code = 0

    output_file = args.outfile
    output_file = output_file[0]
    if os.path.isfile(output_file) and (not args.force):
        raise FileExistsError(
            (
                "Specified output file %s already exists."
                "Use a different filename, or force."
            )
            % output_file,
        )

    if args.merge:
        merger = PdfFileMerger()
        for filename in args.infile:
            assert os.path.isfile(filename)
            try:
                merger.append(filename)
            except (FileNotFoundError):
                print(
                    "Could not append file",
                    filename,
                    "as it could not be found",
                )
            except (IsADirectoryError):
                print(
                    "Could not append file",
                    filename,
                    "as it is a directory",
                )
        merger.write(output_file)
        merger.close()

    return return_code


if __name__ == "__main__":
    exit(main())
