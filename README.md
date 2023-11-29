# Leveraging static analysis for evaluating code-generation models

In recent times, the utilization of Large Language Models (LLMs) for code generation has gained substantial traction. Tools such as [ChatGPT](), [GitHub CoPilot](https://github.com/features/copilot), [Code Llama](), [Bard](https://blog.google/technology/ai/bard-google-ai-search-updates/), and the pioneering work of Rozière et al. with [Code Llama]() aim to streamline developer workflows and expedite development cycles. Despite their promising prospects, code produced by these tools often suffers from bugs, hampering their overall utility. While existing methodologies primarily focus on resource-intensive runtime analysis to address these issues, research exploring static analysis, especially across a limited range of programming languages, remains scarce.

Our study aims to enrich the baseline code generation model by incorporating insights from static error analysis, potentially refining code generation quality. To achieve this objective, we introduce a pipeline that assimilates feedback gleaned from static analysis into the baseline model. Furthermore, we enhance the baseline model by fine-tuning it using samples previously rejected due to static errors. Our empirical observations underscore the efficacy of both strategies in mitigating the occurrence of observed static errors.

# Getting Started
## Setup Guide for Project Dependencies
### Creating a Python Virtual Environment

1. **Navigate to the Project Directory:**
    ```bash
    cd /path/to/your/project
    ```

2. **Create a Virtual Environment:**
    ```bash
    python -m venv codegenllm
    ```

3. **Activate the Virtual Environment:**
    - On Windows:
        ```bash
        codegenllm/Scripts/activate
        ```
    - On macOS and Linux:
        ```bash
        source codegenllm/bin/activate
        ```

4. **Install Project Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    Executing this script will install the necessary libraries for code generation and linters for Python code evaluation.

### Install Linters for Static Evaluation
In case linters are not installed follow the below instructions.
1. `Flake 8` for Python
    ```bash
    cd linter_setup_scripts/flake8_utils
    chmod +x install_flake8.sh
    bash install_flake8.sh
    ```
2. `CPPCheck` for C++
    ```bash
    cd linter_setup_scripts/cppcheck_utils
    chmod +x install_cppcheck.sh
    bash install_cppcheck.sh
    ```

# About
This repository contains code base for project titled __`Leveraging static analysis for evaluating code-generation models`__ developed during the `CSCI 544 Applied Natural Language Processing` course, Fall 2023, at the `University of Southern California` (USC).

## Relevant links:
- [Paper presentation](https://github.com/ksanu1998/NLP_Group37/blob/main/reports/NLP_Group_37_Paper_Presentation.pdf)
- [Project proposal](https://github.com/ksanu1998/NLP_Group37/blob/main/reports/NLP_Group_37_Project_Proposal.pdf) 
- [Project status report](https://github.com/ksanu1998/NLP_Group37/blob/main/reports/NLP_Group_37_Project_Status_Report.pdf) 
- [Project presentation](https://github.com/ksanu1998/NLP_Group37/blob/main/reports/NLP_Group_37_Project_Presentation.pdf) 
- [Project final report]() 

## Authors
1. [Sai Anuroop Kesanapalli](https://github.com/ksanu1998) | `MS in Computer Science` | `USC`
2. [Abishek Anand](https://github.com/abhishekanand1710) | `MS in Computer Science` | `USC`
3. [Kayvan Shah](https://github.com/KayvanShah1) | `MS in Applied Data Science` | `USC`
4. [Indrani Panchangam](https://github.com/author4) | `MS in Computer Science` | `USC`
5. [Vishesh Mittal](https://github.com/author5) | `MS in Computer Science` | `USC`


#### Disclaimer

<small>
The content and code provided in this repository are for educational and demonstrative purposes only. The project may contain experimental features, and the code might not be optimized for production environments. The authors and contributors are not liable for any misuse, damages, or risks associated with the use of this code. Users are advised to review, test, and modify the code to suit their specific use cases and requirements. By using any part of this project, you agree to these terms.</small>



<!-- TODO:<br>
* Format the README nicely
* Explain setup guidlines for linters and LLMs (if needed)
* Explain all folders with link. Make sure to mention that the post_feedback is a proof of concept of automation. 
* Results in results/post_feedback are to demonstrate the automation and not the results of actual feedback analysis.
* Write something about LLMs that Abhishek is going to merge.
* Add author names and github handles
* Add link to final report -->
