import os


def end_overlap(a, b):
    """
    Find the index where the overlap between two strings ends.

    Args:
        a (str): First string.
        b (str): Second string.

    Returns:
        int: The index where the overlap between the two strings ends.
    """
    for i in range(0, len(a)):
        if b.startswith(a[i:]):
            return i
    return len(a)


def remove_prefix(s, prefix):
    """
    Remove a prefix from a string.

    Args:
        s (str): The string from which the prefix will be removed.
        prefix (str): The prefix to remove from the string.

    Returns:
        str: The string with the prefix removed.
    """
    prefix_end_idx = s.index(prefix) + len(prefix)
    return s[prefix_end_idx:]


def clean_code(code):
    """
    Clean code by removing duplicate function definitions.

    This function identifies and removes duplicate function definitions within the code,
    specifically addressing scenarios where function definitions appear consecutively,
    causing repetition when appending code context and response.

    Args:
        code (str): The code block as a string.

    Returns:
        str: The cleaned code with duplicate function definitions removed.

    Example:
        >>> code_block = '''
        ... def CalculateDifference(arr, n):def calculate_difference(arr, n):
        ...     # Function logic...
        ... '''
        >>> cleaned = clean_code(code_block)
        >>> print(cleaned)
        ... # Output will be the cleaned code with one instance of the function definition.
    """
    lines = code.split("\n")
    cleaned_code = []
    for line in lines:
        if line.count("def") == 2:
            code_context, response = line.split(":", 1)
            response = response.strip()
            cleaned_code.append(response)
        else:
            cleaned_code.append(line)

    return "\n".join(cleaned_code)


def save_file(path, code):
    with open(path, "w", encoding="utf-8") as file:
        file.write(code)


def save_to_code_file(directory, id, code, ext, pss=1):
    save_file(f"{directory}/question-{id}-pass-{pss}.{ext}", code)


def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
