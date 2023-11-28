class CodeBlockMarkers:
    """
    Defines markers for different code blocks in various programming languages.
    """

    B_PYTHON: str = "[PYTHON]"
    """
    Start marker for Python code blocks.
    """

    E_PYTHON: str = "[/PYTHON]"
    """
    End marker for Python code blocks.
    """

    B_CPP: str = "[CPP]"
    """
    Start marker for C++ code blocks.
    """

    E_CPP: str = "[/CPP]"
    """
    End marker for C++ code blocks.
    """

    B_INST: str = "[INST]"
    """
    Start marker for instantiation code blocks.
    """

    E_INST: str = "[/INST]"
    """
    End marker for instantiation code blocks.
    """
