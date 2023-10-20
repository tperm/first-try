import json
from time import sleep
from json import dumps
from kafka import KafkaProducer



topic_name='sensor_data_consumer'
producer = KafkaProducer(bootstrap_servers=['54.159.58.15:9092']
,value_serializer=lambda x: dumps(x).encode('utf-8'))

def lambda_handler(event,context):

# Initialize a list to store the key-value pairs for each item
    # Extract the JSON strings from the "json_strings" key in the event dictionary
  
    data = json.dumps(event)
    producer.send(topic_name, value=data)
    producer.flush()
    return {
        'statusCode': 200,
        'body': json.dumps(event, indent=4)
    }

