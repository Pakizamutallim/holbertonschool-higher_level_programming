import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The name of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load data from a JSON file and deserialize it into a Python dictionary.

    Args:
        filename (str): The name of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

