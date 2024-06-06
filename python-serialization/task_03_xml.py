import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The name of the input XML file.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        result = {}
        for child in root:
            result[child.tag] = child.text
        
        return result
    except FileNotFoundError:
        return None
    except ET.ParseError:
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
