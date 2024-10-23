# import pickle
# import boto3

# s3 = boto3.client('s3', endpoint_url='http://localhost:4566')


# def lambda_handler(event, context):
#     # Download the model from S3
#     s3 = boto3.client('s3', endpoint_url='http://localhost:4566')
#     s3.download_file('my-test-bucket', 'model.pkl', '/tmp/model.pkl')

#     # Load the model
#     with open('/tmp/model.pkl', 'rb') as model_file:
#         model = pickle.load(model_file)

#     # Dummy input for prediction
#     input_data = [5.1, 3.5, 1.4, 0.2]
#     prediction = model.predict([input_data])

#     return {'prediction': prediction.tolist()}

# --------------------------------------------------------------------------------------------------------------

# new suggestion from chatgtp to solve issue of....
import pickle
import json
import boto3
import subprocess

def lambda_handler(event, context):
    try:
        # Install dependencies
        subprocess.run(["pip", "install", "-r", "/tmp/requirements.txt"])

        # Load the model
        s3 = boto3.client('s3', endpoint_url='http://host.docker.internal:4566')
        response = s3.get_object(Bucket='my-test-bucket', Key='model.pkl')
        model_data = response['Body'].read()
        model = pickle.loads(model_data)

        # Make prediction
        X_new = [[5.1, 3.5, 1.4, 0.2]]  # Example input
        prediction = model.predict(X_new)[0]

        return {
            'statusCode': 200,
            'body': json.dumps({
                'prediction': prediction,
                'message': 'Prediction successful'
            })
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }


