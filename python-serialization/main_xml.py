#!/usr/bin/env python3
import task_03_xml

sample_dict = {
    'name': 'John',
    'age': '28',
    'city': 'New York'
}

xml_file = "data.xml"
task_03_xml.serialize_to_xml(sample_dict, xml_file)
print(f"Dictionary serialized to {xml_file}")

deserialized_data = task_03_xml.deserialize_from_xml(xml_file)
print("\nDeserialized Data:")
print(deserialized_data)
