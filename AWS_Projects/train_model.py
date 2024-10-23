import os
import pickle
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# File path for the output file in the same directory
output_file_path = os.path.join(script_dir, 'model.pkl')

# Load dataset
iris = load_iris()
X, y = iris["data"], iris["target"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the model
with open(output_file_path, 'wb') as model_file:
    pickle.dump(model, model_file)

print(f"Model trained and saved as {output_file_path}")
