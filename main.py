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
