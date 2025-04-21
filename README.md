# DocFormatter

A Python utility for formatting text files into paragraphs with a specified number of lines.

## Installation

Clone the repository and ensure you have Python 3.x installed.

## Usage

```python
from main import format_file

# Format a file with 30 lines per paragraph
format_file(30, "input.txt", "output.txt")

# Format a file and let it auto-generate the output filename
format_file(20, "input.txt")  # Creates input_formatted.txt

# Force overwrite an existing output file
format_file(25, "input.txt", "output.txt", force_replace=True)
```

## Function Parameters

- `lines_per_paragraph`: Number of lines to include in each paragraph (must be > 0)
- `source_file`: Path to the input file to format
- `dest_file`: (Optional) Path for the output file. If not provided, generates an automatic name
- `force_replace`: (Optional) Set to True to overwrite existing output file

## Auto-generated Filenames

If no destination file is specified, the formatter will generate a filename using the pattern:
- `filename_formatted.ext`
- `filename_formatted_1.ext`
- `filename_formatted_2.ext` (and so on)

## Error Handling

The formatter will raise:
- `ValueError` if lines_per_paragraph is <= 0
- `ValueError` if source_file is not provided
- `FileExistsError` if the destination file exists and force_replace is False

## Example

Input file:
```text
Line 1
Line 2
Line 3

Line 4
Line 5
```

Output file (with lines_per_paragraph=2):
```text
Line 1
Line 2

Line 3
Line 4

Line 5
```