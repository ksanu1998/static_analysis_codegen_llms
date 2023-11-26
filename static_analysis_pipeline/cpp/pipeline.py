import re

from utils.preprocess import clean_code, end_overlap, remove_prefix
from utils.settings import CodeBlockMarkers as cm


class CPPCodeAnalyzer:
    cpp_func_match_reg_exp = r"\\b[A-Za-z_][A-Za-z0-9_]*\s+[A-Za-z_][A-Za-z0-9_]*\s*\([^;{]*\)\s*{"


def clean_duplicate_func_signature(code):
    """Clean duplicate function signatures in C++ code.

    This function identifies and removes duplicate function declarations or definitions
    that appear sequentially in the code. For instance, it handles cases where the same
    function signature appears consecutively, discarding the duplicate ones.

    For CPP code files, it clean lines like the following which have duplicate function signatures:

        1. int countSol ( int coeff [ ] , int start , int end , int rhs ) {
        2. int countSol(int coeff[], int start, int end, int rhs) {

    Args:
        code (str): The C++ code as a string.

    Returns:
        str: The cleaned C++ code with duplicate function signatures removed.
    """
    lines = code.split("\n")
    cleaned_code = []
    for i, line in enumerate(lines):
        match = re.search(CPPCodeAnalyzer.cpp_func_match_reg_exp, line)
        if match and i < len(lines) - 1:
            second_match = re.search(CPPCodeAnalyzer.cpp_func_match_reg_exp, lines[i + 1])
            if not second_match:
                cleaned_code.append(line)
        else:
            cleaned_code.append(line)
    return "\n".join(cleaned_code)


def extract_code_cpp(prompt, response, code_context):
    """
    Extracts clean C++ code from the response within the provided context.

    This function is designed to extract and clean C++ code from a given response,
    removing unnecessary prefixes and suffixes, as well as duplicate function signatures
    within the provided code context.

    Args:
        prompt (str): The prompt indicating the start of the response.
        response (str): The response containing C++ code.
        code_context (str): The existing code context to which the response will be appended.

    Returns:
        str: Cleaned and extracted C++ code ready to be integrated into the code context.
    """
    trimmed_response = remove_prefix(response, prompt)
    if trimmed_response.startswith(cm.B_CPP):
        trimmed_response = remove_prefix(trimmed_response, cm.B_CPP)

    try:
        suffix_idx = trimmed_response.index(cm.E_CPP)
        trimmed_response = trimmed_response[:suffix_idx]
    except ValueError:
        pass

    try:
        suffix_idx = trimmed_response.index(cm.E_INST)
        trimmed_response = trimmed_response[:suffix_idx]
    except ValueError:
        pass

    trimmed_response = trimmed_response.strip()
    code_context = code_context.strip()
    overlap_idx = end_overlap(code_context, trimmed_response)
    cleaned_response = code_context[:overlap_idx] + "\n" + trimmed_response
    return clean_duplicate_func_signature(clean_code(cleaned_response))
