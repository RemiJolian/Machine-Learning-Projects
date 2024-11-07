import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
import mlflow
import mlflow.sklearn
import boto3
import joblib

mlflow.set_experiment("KNighborsClassifier-Basic")

# Set AWS credentials for LocalStack S3 bucket
os.environ['AWS_ACCESS_KEY_ID'] = 'test'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'test'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris_data = pd.read_csv(url, names=column_names)

# Split dataset into features and target variable
X = iris_data.iloc[:, :-1]  # Features
y = iris_data.iloc[:, -1]    # Target variable

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize KNN classifier
model = KNeighborsClassifier(n_neighbors=3)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# Set the tracking URI to your local MLflow server if applicable
mlflow.set_tracking_uri('http://localhost:5000')

with mlflow.start_run():
    # Log parameters
    mlflow.log_param("n_neighbors", 3)
    
    # Log metrics
    accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric("accuracy", accuracy)

    # Save the model locally as a .pkl file using joblib
    joblib.dump(model, 'iris_model.pkl')

    # Log the model to S3 bucket (make sure to specify your bucket name)
    mlflow.sklearn.log_model(model, artifact_path="iris_model")

# Initialize S3 resource to upload the .pkl file to LocalStack's S3
s3_resource = boto3.resource('s3', endpoint_url='http://localhost:4566')

# Ensure the bucket exists; if not, create it
bucket_name = 'my-iris-bucket'
if not s3_resource.Bucket(bucket_name) in s3_resource.buckets.all():
    s3_resource.create_bucket(Bucket=bucket_name)

# Upload model file to S3 bucket
s3_resource.Bucket(bucket_name).upload_file('iris_model.pkl', 'models/iris_model.pkl')