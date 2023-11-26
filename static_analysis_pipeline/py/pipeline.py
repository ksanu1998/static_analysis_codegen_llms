from utils.preprocess import clean_code, end_overlap, remove_prefix
from utils.settings import CodeBlockMarkers as cm


def extract_code_python(prompt, response, code_context):
    trimmed_response = remove_prefix(response, prompt)
    if trimmed_response.startswith(cm.B_PYTHON):
        trimmed_response = remove_prefix(trimmed_response, cm.B_PYTHON)
    try:
        suffix_idx = trimmed_response.index(cm.E_PYTHON)
        trimmed_response = trimmed_response[:suffix_idx]
    except ValueError:
        pass

    trimmed_response = trimmed_response.strip()
    code_context = code_context.strip()
    overlap_idx = end_overlap(code_context, trimmed_response)
    cleaned_response = code_context[:overlap_idx] + trimmed_response
    return clean_code(cleaned_response)
