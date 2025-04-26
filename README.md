# DocFormatter

A Python utility for formatting text files into paragraphs with a specified number of lines.

## Features

- Format text files into paragraphs with customizable line counts
- Command line and GUI interfaces
- UTF-8 text support
- Automatic output filename generation
- Configurable overwrite protection

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/DocFormatter.git

# Install dependencies
pip install -r requirements.txt
```

## Usage

### GUI Interface

```bash
python ui.py
```

### Command Line Interface

```python
from doc_formatter import format_file

# Basic usage
format_file("input.txt", "output.txt", 2)

# Auto-generate output filename
format_file("input.txt", lines_per_paragraph=2)

# Force overwrite existing file
format_file("input.txt", "output.txt", 2, force_replace=True)
```

## Function Parameters

- `input_file`: Path to the source file to format
- `output_file`: (Optional) Path for the formatted output file
- `lines_per_paragraph`: Number of lines per paragraph (must be > 0)
- `force_replace`: (Optional) Set to True to overwrite existing files

## Output File Generation

When no output file is specified, files are generated as:

- `filename_formatted.txt`
- `filename_formatted_1.txt`
- `filename_formatted_2.txt` (if previous exists)

## Error Handling

The formatter will raise:

- `ValueError` if lines_per_paragraph is <= 0
- `FileNotFoundError` if input file doesn't exist
- `FileExistsError` if output file exists (without force_replace)

## Example

Input:

```text
Line 1
Line 2
Line 3

Line 4
Line 5
```

Output (lines_per_paragraph=2):

```text
Line 1
Line 2

Line 3
Line 4

Line 5
```

## Development

```bash
# Install development dependencies
pip install -r dev_requirements.txt

# Run tests
pytest tests/
```