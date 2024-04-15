# Scikit-Learn Hello World

This article is a simple example of how to use Scikit-Learn to create a simple classifier based on the Iris dataset.

## Installation

In this example, we use Python version 3.12.0 together with virtualenv. Ubuntu 24.04 comes with Python 3.12 pre-installed.
To install Python 3.12 on MacOS, you can use Homebrew:

```bash
brew install python@3.12
```

On Windows, you can use the official Python installer from the Python website.

Later we also use Docker to run the Python code in a container. The easiest way to install Docker is to install
Docker Desktop. For Linux, you can alternatively install Docker Engine natively.

## Create the Project with a Hello World Python script

First, create a new directory for the project and navigate into it. Then create a new file called `main.py` with
the following content:

```python
def main():
    print("Hello, world!")


if __name__ == '__main__':
    main()
```

This is a simple Python script that prints "Hello, world!" to the console. Try running it with the following command:

```bash
python main.py
```

If your Python binary requires you to specify the version, you can use `python3.12` instead of `python`.

## Initiate a virtual environment and install Scikit-Learn

Make sure you have virtualenv installed:

```bash
virtualenv --version
```

Then create a new virtual environment for the project:

```bash
virtualenv -p python3.12 venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install Scikit-Learn:

```bash
pip install scikit-learn
```

To have a list of all the installed packages with their versions, you can run:

```bash
pip freeze > requirements.txt
```

This will dump all the installed packages into a file called `requirements.txt`. This way, the next person who works on
the project can install the exact same versions of the packages.
