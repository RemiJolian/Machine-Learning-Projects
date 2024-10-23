# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree # try export_graphviz
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the decision tree classifier
clf = DecisionTreeClassifier(max_depth=3, random_state=42) # try max_depth = 4 or... 8
clf.fit(X_train, y_train)

# Evaluate the model
accuracy = clf.score(X_test, y_test)
#accuracy = clf.score(X_train, y_train) ???

print(f"Accuracy: {accuracy:.2f}")

# Visualize the decision tree
plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True, rounded=True)
# plt.show()

# This command is added to run in Docker only
plt.savefig('/app/iris_model_plot.png') 

# Make a prediction
sample = X_test[27].reshape(1, -1) # try X_test[0 or ...]
prediction = clf.predict(sample)
print(prediction)
print(f"Prediction for sample: {iris.target_names[prediction[0]]}")