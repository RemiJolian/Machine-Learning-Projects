import pickle
import json
import boto3


# Configure the S3 client to use the LocalStack endpoint
s3 = boto3.client('s3', endpoint_url='http://host.docker.internal:4566')
# s3 = boto3.client('s3', endpoint_url='http://localhost:4566')

def lambda_handler(event, context):
    try:
        print("Attempting to access S3")
        response = s3.get_object(Bucket='my-test-bucket', Key='model.pkl')
        print("File accessed successfully")
        model_data = response['Body'].read()

        model = pickle.loads(model_data)

        return {
            'statusCode': 200,
            'body': json.dumps('Model loaded successfully')
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }