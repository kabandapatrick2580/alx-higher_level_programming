def text_indentation(text):
    """
    Prints a text with two new lines after each of these characters: '.', '?', and ':'

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If the input text is not a string.

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text.strip() == "":
        return

    result_lines = []
    current_line = ""
    for char in text:
        current_line += char
        if char in (".", "?", ":"):
            result_lines.append(current_line.strip())
            result_lines.append("")
            current_line = ""

    if current_line:
        result_lines.append(current_line.strip())

    print("\n".join(result_lines))
