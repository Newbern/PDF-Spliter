# PDF Splitter

A simple Python tool that splits a PDF document into individual PDF files, saving each page separately in an organized output folder.

## Features

- **File Selection:** Choose a PDF using a graphical file dialog.
- **Automatic Splitting:** Saves each page as an individual PDF.
- **Organized Output:** Creates a `split_output` folder with a separate timestamped subfolder for each run.
- **Error Handling:** Reports failed pages without stopping the entire process.
- **Progress Logging:** Displays saved files and the total number of pages processed.

## Requirements

- Python 3.8+
- [pypdf](https://pypi.org/project/pypdf/)
- Tkinter (usually included with Python)

## Installation

Install the required dependency:

```bash
pip install pypdf
```

## Usage

Run the script:

```bash
python pdf_splitter.py
```

1. Select the PDF file you want to split.
2. Wait for the script to process each page.
3. Find the individual PDF files in the generated output folder.

## Output Structure

```text
PDF-Splitter/
├── pdf_splitter.py
└── split_output/
    └── 2026-10-26_21-30-00/
        ├── page_1.pdf
        ├── page_2.pdf
        └── page_3.pdf
```

Each run creates a new timestamped folder to keep the output from previous runs organized.

## Technologies

- Python
- pypdf
- Tkinter
- os
- datetime

## License

This project is available for personal and educational use.
