# PDF Tool

[![pipeline status](https://gitlab.com/laywill/advent-of-code-2020/badges/master/pipeline.svg)](https://gitlab.com/laywill/advent-of-code-2020/-/commits/master)

A Python based tool for managing and merging PDFs.

## Usage

### Setup

Use setuptools to install the requirements of the module.

On macOS and Linux:

```sh
python3 setup.py install
```

On Windows:

```powershell
python setup.py install
```

### Running

Help on how to run the tool can be found using:

```powershell
python pdf-tool.py --help
```

## Development

### Python Version

This has been developed using Python 3.9

### Create a virtual environment

It is reccommended to use the tool in a virtual environment to prevent package conflicts.

On macOS and Linux:

```sh
python3 -m venv venv
```

On Windows:

```powershell
python -m venv venv
```

### Activate virtual environment

On macOS and Linux:

```sh
source venv/bin/activate
```

On Windows:

```powershell
.\venv\Scripts\activate
```

### Install requirements from setup.py

Use setuptools to install the requirements of the class.

On macOS and Linux:

```sh
python3 setup.py install
```

On Windows:

```powershell
python setup.py install
```

### Install Development packages from requirements

Tell pip to install all of the packages in this file using the -r flag:

```sh
pip install -r requirements-dev.txt
```

### Install and configure git pre-commit

To install git hooks in your .git/ directory, execute:

```sh
pre-commit install
```

### Running checks on repsitory

If you want to run the checks on-demand (outside of git hooks), run:

```sh
pre-commit run --all-files --verbose
```

### Running the tool

Help on how to run the tool can be found using:

```sh
python pdf-tool.py --help
```

### Leaving the virtual environment

Simply type:

```sh
deactivate
```

#### Updating requirements

To update `requirements-dev.txt` or `setup.cfg` use the following command to see the currently installed modules:

```sh
pip freeze > currently_using_requirements.txt
```
