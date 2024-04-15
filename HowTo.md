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

## Create a simple classifier with Scikit-Learn

Now that we have Scikit-Learn installed, let's create a simple classifier based on the Iris dataset. Change the content
of `main.py` to the following:

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def main():
    """
    This function is a hello-world function for scikit-learn.
    It loads the Iris dataset, splits it into training and testing sets, and trains a random forest classifier.
    :return: The model
    """
    # Load the Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train a random forest classifier
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Print the model's accuracy
    print(f'Model accuracy: {model.score(X_test, y_test)}')

    return model


if __name__ == '__main__':
    main()
```

Some explanations about the code:

- We load the Iris dataset using `load_iris()` from Scikit-Learn. Iris is a simple dataset with 150 samples and 4 features.
- We split the dataset into training and testing sets using `train_test_split()`. We use 80% of the data for training and 20% for testing.
- We train a random forest classifier using `RandomForestClassifier()`. This is a simple classifier that works well on the Iris dataset.
- We print the model's accuracy on the test set using `model.score(X_test, y_test)`.
- Finally, we return the trained model.

Try running the script with:

```bash
python main.py
```

You should see the model's accuracy printed to the console. In my case, the output was:

```
Model accuracy: 0.9
```
