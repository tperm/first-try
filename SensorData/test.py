import json
from time import sleep
from json import dumps
from kafka import KafkaProducer

topic_name='sensor_data_consumer'
producer = KafkaProducer(bootstrap_servers=['34.226.216.135:9092']
,value_serializer=lambda x: dumps(x).encode('utf-8'))

def lambda_handler(event, context):
    # TODO implement
    # Extract the JSON file content from the event
    json_file_content = event["json_file_content"]
    
    try:
        # Parse the JSON content into a list of dictionaries
        data = json.loads(json_file_content)

        # Initialize a list to store the key-value pairs for each item
        key_value_pairs = []

        # Loop through the list of dictionaries and process each item
        for item in data:
            sensor = item.get("sensor", "")
            time = item.get("time", "")
            seconds_elapsed = item.get("seconds_elapsed", "")
            dBFS = item.get("dBFS", "")

            # Create a dictionary with key-value pairs for the current item
            item_key_values = {
                "Sensor": sensor,
                "Time": time,
                "Seconds Elapsed": seconds_elapsed,
                "dBFS": dBFS
            }

            # Append the key-value pairs for the current item to the list
            key_value_pairs.append(item_key_values)

    except Exception as e:
        # Handle any exceptions that may occur during parsing
        return str(e)
        print(data)
        producer.send(topic_name, value=data)
        producer.flush()
    return {
        'statusCode': 200,
        key_value_pairs
    }

