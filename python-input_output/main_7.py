#!/usr/bin/python3

import json

data = {1, 2, 3}
data_list = list(data)
json_data = json.dumps(data_list)
print(json_data)

