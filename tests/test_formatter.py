import os
import pytest
from doc_formatter import format_to_file
from contextlib import nullcontext as does_not_raise

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

EXPECTED_OUTPUT_2_LINES = (
        b"Whispers dance through the trees,\n"
        b"Moonlight spills on quiet seas.\n\n"
        b"Shadows stretch, the night unfolds,\n"
        b"Dreams are spun in threads of gold.\n\n"
        b"Stars hum songs of ancient lore.\n"
        b"Winds weave tales of distant lands,\n\n"
        b"Mountains rise with steady hands.\n"
        b"Rivers carve their endless path,\n\n"
        b"Time moves on, escapes our grasp.\n"
        b"Echoes linger, soft and sure.\n\n"
        b"Morning breaks with gentle hues,\n"
        b"Skies awake in vibrant blues.\n\n"
        b"Fields of green embrace the dawn,\n"
        b"Life begins, the night withdrawn.\n\n"
        b"Hope renews with every breath.\n"
    )

EXPECTED_OUTPUT_NO_PARAGRAPH = (
        b"Whispers dance through the trees,\n"
        b"Moonlight spills on quiet seas.\n"
        b"Shadows stretch, the night unfolds,\n"
        b"Dreams are spun in threads of gold.\n"
        b"Stars hum songs of ancient lore.\n"
        b"Winds weave tales of distant lands,\n"
        b"Mountains rise with steady hands.\n"
        b"Rivers carve their endless path,\n"
        b"Time moves on, escapes our grasp.\n"
        b"Echoes linger, soft and sure.\n"
        b"Morning breaks with gentle hues,\n"
        b"Skies awake in vibrant blues.\n"
        b"Fields of green embrace the dawn,\n"
        b"Life begins, the night withdrawn.\n"
        b"Hope renews with every breath.\n"
    )

@pytest.mark.parametrize(
    "lines_per_paragraph, input_file, expected_output, expected_exception",
    [
        (2, None, None, pytest.raises(ValueError)),  # Invalid case
        (2, os.path.join(CURRENT_DIRECTORY, "test_file.txt"), EXPECTED_OUTPUT_2_LINES, does_not_raise()),  # Valid case
        (2, os.path.join(CURRENT_DIRECTORY, "test_file_empty_lines.txt"), EXPECTED_OUTPUT_2_LINES, does_not_raise()),  # Valid case
        (-1, os.path.join(CURRENT_DIRECTORY, "test_file.txt"), None, pytest.raises(ValueError)),  # Invalid case
        (0, os.path.join(CURRENT_DIRECTORY, "test_file.txt"), None, pytest.raises(ValueError)),  # Invalid case
        (50, os.path.join(CURRENT_DIRECTORY, "test_file.txt"), EXPECTED_OUTPUT_NO_PARAGRAPH, does_not_raise()),  # Valid case
        (50, os.path.join(CURRENT_DIRECTORY, "test_file_empty_lines.txt"), EXPECTED_OUTPUT_NO_PARAGRAPH, does_not_raise())
    ]
)
def test_format_file_creates_output_file(lines_per_paragraph, input_file, expected_output, expected_exception, tmp_path):
    output_file = tmp_path / "formatted_file.txt"
    
    with expected_exception:
        format_to_file(lines_per_paragraph, input_file, output_file)
        assert output_file.exists()

        with open(output_file, "rb") as f:
            actual_output = f.read()

        assert actual_output == expected_output