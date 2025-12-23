# Complete Python Developer in 2026: Zero to Mastery

This repository contains code, exercises, and projects from the **Complete Python Developer in 2026: Zero to Mastery** course.

## Overview

A comprehensive collection of Python programming concepts, from basics to advanced topics, including practical projects and real-world applications.

## Repository Structure

```
.
├── PythonBasics/           # Fundamental Python concepts
├── AdvancedPython/         # Advanced Python topics
│   ├── OOP/               # Object-Oriented Programming
│   ├── Functional/        # Functional Programming
│   ├── Decorator/         # Decorators
│   ├── Generator/         # Generators
│   └── ErrorHandling/     # Exception Handling
├── Modules/               # Python modules and packages
├── RegEx/                 # Regular Expressions
├── Scripting/             # Automation scripts
│   ├── ImageProcessing/   # Image manipulation with PIL/OpenCV
│   ├── pdf/              # PDF processing
│   ├── email_sender/     # Email automation
│   └── PasswordChecker/  # Password validation
├── UnitTesting/           # Testing with unittest/pytest
├── WebScraping/           # Web scraping with BeautifulSoup
├── WebDevelopment/        # Flask web development
├── debugger/              # Debugging techniques
└── ztm-python-course-exercises/  # Course exercises
```

## Topics Covered

- **Python Fundamentals**: Variables, data types, control flow, functions
- **Object-Oriented Programming**: Classes, inheritance, polymorphism, encapsulation
- **Functional Programming**: Lambda functions, map, filter, reduce, comprehensions
- **Advanced Concepts**: Decorators, generators, error handling
- **Regular Expressions**: Pattern matching and text processing
- **File I/O**: Reading/writing files, working with PDFs
- **Web Scraping**: BeautifulSoup, requests, data extraction
- **Web Development**: Flask framework, routing, templates
- **Scripting**: Automation, image processing, email sending
- **Testing**: Unit testing, test-driven development
- **Debugging**: Debugging tools and techniques

## Setup

### Prerequisites

- Python 3.13 or higher

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Python
```

2. Install dependencies using uv (recommended) or pip:
```bash
# Using uv
uv sync

# Or using pip
pip install -r pyproject.toml
```

### Dependencies

The project uses the following main packages:
- `beautifulsoup4` - Web scraping
- `requests` - HTTP requests
- `flask` - Web development
- `pillow` - Image processing
- `opencv-python` - Computer vision
- `pypdf` - PDF manipulation
- `python-dotenv` - Environment variables
- `argostranslate` - Translation

## Usage

Each directory contains standalone examples and exercises. Navigate to any folder and run the Python files:

```bash
python filename.py
```

For Jupyter notebooks in [PythonBasics/](PythonBasics/):
```bash
jupyter notebook Basics.ipynb
```

## Projects

### Scripting Projects
- **Image Processing**: Batch image manipulation and conversion
- **PDF Processing**: PDF merging, splitting, and manipulation
- **Email Sender**: Automated email sending
- **Password Checker**: Secure password validation

### Web Projects
- **Web Scraping**: Data extraction from websites
- **Flask Applications**: Web development with Flask framework

## Contributing

This is a personal learning repository. Feel free to fork and use for your own learning purposes.

## License

This repository is for educational purposes.

## Course Reference

**Complete Python Developer in 2026: Zero to Mastery**
