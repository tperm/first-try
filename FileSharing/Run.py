import presigned_url
import boto3
import constants

clients3 = 's3'
presigned_url.generate_presigned_url(s3_client=clients3,client_method='get_object',method_parameters=('aws-logs-589201481762-us-east-1','audio/2023-09-10_123718_000.wav'), expires_in= 1000)