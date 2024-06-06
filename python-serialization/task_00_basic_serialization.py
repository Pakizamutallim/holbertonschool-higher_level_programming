import json
"""
module that adds the functionality to serialize
"""


def serialize_and_save_to_file(data, filename):
    """
    module that adds the functionality to serialize
    """

    with open(filename, 'r', encoding='utf-8') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    module that adds the functionality to serialize
    """

    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
