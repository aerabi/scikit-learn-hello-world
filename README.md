# Scikit-Learn Hello World

This is a simple example of how to use Scikit-Learn to create a simple classifier based on the Iris dataset.

## Requirements

There are two options for running this project: in a Docker container or locally.

To run it in a Docker container, you need to have Docker installed. You can download Docker Desktop from the [official website](https://www.docker.com/products/docker-desktop).

To run it locally, you need to have Python 3.12.0 installed. You can download Python from the [official website](https://www.python.org/downloads/).
Ubuntu 24.04 comes with Python 3.12 pre-installed. You can also install it using Homebrew on MacOS or other Linux distributions:

```bash
brew install python@3.12
```

## Installation

To install the project, first clone the repository:

```bash
git clone https://github.com/aerabi/scikit-learn-hello-world.git
cd scikit-learn-hello-world
```

## Run the project in a Docker container

To run the project in a Docker container, you just need to use Docker Compose:

```bash
docker compose up --build
```

That's it!

## Run the project locally

To run the project locally, you need to create a virtual environment and install the dependencies:

```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then you can run the project:

```bash
python main.py
```
