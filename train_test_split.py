import numpy as np
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

class Commodity:

    def __init__(self, csv_name):
        self.name = csv_name
        dataset = pd.read_csv(csv_name)
        self.X = dataset.iloc[:, :-1].values
        self.Y = dataset.iloc[:, 3].values
        
        # Split the dataset into training and testing subsets
        self.train_X, self.test_X, self.train_Y, self.test_Y = train_test_split(self.X, self.Y, test_size=0.2, random_state=42)

        # Train the decision tree regressor
        depth = random.randrange(7, 18)
        self.regressor = DecisionTreeRegressor(max_depth=depth)
        self.regressor.fit(self.train_X, self.train_Y)

    def evaluate(self):
        # Evaluate the model on the test set
        predicted_Y = self.regressor.predict(self.test_X)
        r_squared = r2_score(self.test_Y, predicted_Y)
        return r_squared

    def plot_regression(self):
        # Plotting actual vs. predicted values
        predicted_Y = self.regressor.predict(self.test_X)
        plt.scatter(self.test_Y, predicted_Y, color='blue')
        plt.title('Actual vs Predicted')
        plt.xlabel('Actual')
        plt.ylabel('Predicted')

        # Plotting the regression line
        sorted_indices = np.argsort(self.test_Y)
        plt.plot(self.test_Y[sorted_indices], predicted_Y[sorted_indices], color='red')
        plt.show()

# Usage example
commodity_dict = {
    "Cotton": "C:\\Users\\Hima\\Desktop\\New folder\\static\\Cotton.csv",
    "Paddy": "C:\\Users\\Hima\\Desktop\\New folder\\static\\Paddy.csv"
}

for name, csv_file in commodity_dict.items():
    commodity = Commodity(csv_file)
    r_squared = commodity.evaluate()
    accuracy_percentage = r_squared * 100
    print(f"Accuracy percentage for {name}: {accuracy_percentage}%")
    commodity.plot_regression()
