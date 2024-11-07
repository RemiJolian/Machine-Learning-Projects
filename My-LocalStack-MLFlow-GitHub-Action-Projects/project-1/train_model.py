import os
import pickle
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import mlflow
import boto3
# from sklearn.model_selection import train_test_split

mlflow.set_experiment("Basic-DecisionTree")

#mlflow.set_tracking_uri("My-Machine-Learning-Projects\My-Proj1-LocalStack-MLFlow-GitHub-Action\mlruns")
mlflow.set_tracking_uri("http://localhost:5000")

# Get the directory of the current script
#script_dir = os.path.dirname(os.path.abspath(__file__))

# File path for the output file in the same directory
#output_file_path = os.path.join(script_dir, 'model.pkl')

# Specify S3 bucket and path for saving the model artifacts
#artifact_path = "s3:/my-test-bucket/decision_tree_model"

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# if not os.path.exists("tmp"):
#     os.makedirs("tmp")

# Load dataset
iris = load_iris()
X, y = iris["data"], iris["target"]


# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

prediction_train = model.predict(X)
accuracy_train = accuracy_score(prediction_train, y)

with open("model.pkl", 'wb') as model_file:
    pickle.dump(model, model_file)

# # Save the accuracy value to a text file
# with open("accuracy.txt", "w") as accuracy_file:
#     accuracy_file.write(f"Accuracy of training: {accuracy_train}")

with mlflow.start_run():
    # Log accuracy metric
    mlflow.log_metric("accuracy", accuracy_train)
    # Log param- the model has no param, here
    mlflow.log_param("only-test", 0.00)

    # Save the model as an artifact
    #mlflow.sklearn.log_model(model, "decision_tree_model")
    mlflow.sklearn.log_model(model, artifact_path="model")

    print(f"Accuracy of training: {accuracy_train}")

# Initialize S3 resource to upload the .pkl file to LocalStack's S3
s3_resource = boto3.resource('s3', endpoint_url='http://localhost:4566')

bucket_name = "my-iris-bucket"

if not s3_resource.Bucket(bucket_name) in s3_resource.buckets.all():
    s3_resource.create_bucket(Bucket=bucket_name)

# Upload model file to S3 bucket
s3_resource.Bucket(bucket_name).upload_file('model.pkl', 'models/model.pkl')

# Upload accuracy.txt to S3 bucket
# s3_resource.Bucket(bucket_name).upload_file('accuracy.txt', 'models/accuracy.txt')