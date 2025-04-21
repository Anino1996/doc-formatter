from io import BufferedReader
import os

NEW_LINE: bytes = b"\n"

def format_to_file(lines_per_paragraph, source_file, dest_file = None, force_replace = False):

    if lines_per_paragraph <= 0:
        raise ValueError("lines_per_paragraph must be greater than 0")
    
    if not source_file:
        raise ValueError("source_file must be provided")        

    if dest_file:
        if os.path.exists(dest_file):
            if not force_replace:
                raise FileExistsError(f"Destination file {dest_file} already exists. Use force_replace=True to overwrite.")
            else:
                print(f"Warning: Destination file {dest_file} already exists and will be overwritten.")
    
    else:
        dest_file = __generate_destination_name(source_file)

    with open(source_file, "rb") as source:
        with open(dest_file, "wb") as dest:

            output_buffer = format_bytes(lines_per_paragraph, source)
            dest.write(output_buffer)
            
    print(f"New file written to {dest_file}!")


def format_bytes(lines_per_paragraph, source_buffer: BufferedReader) -> bytearray:
    if lines_per_paragraph <= 0:
        raise ValueError("lines_per_paragraph must be greater than 0")
    
    if not source_buffer:
        raise ValueError("source_file must be provided")
        
    new_paragraph = False
    lines_read = 0

    output_buffer = bytearray()

    while line := source_buffer.readline():            
        data = line.strip()

        if not data:
            continue

        if new_paragraph:
            output_buffer.extend(NEW_LINE)

        output_buffer.extend(data)
        output_buffer.extend(NEW_LINE)

        lines_read += 1

        new_paragraph = lines_read % lines_per_paragraph == 0
    
    return output_buffer


def __generate_destination_name(source_file: str) -> str:
    """
    Generates a destination name for the formatted file.
    """
    root, extension = os.path.splitext(source_file)
    generated_name = f"{root}_formatted{extension}"

    suffix = 0

    while os.path.exists(generated_name):
        suffix += 1
        generated_name = f"{root}_formatted_{suffix}{extension}"

    return generated_name
