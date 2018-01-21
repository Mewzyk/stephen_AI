"""
Author: Stephen Thomas
Date Created: 1 December 2018
Pipeline between D3.js and Graph framework
Github Link: https://github.com/Mewzyk/stephen_AI.git
"""

import json

#with open("../visualization_code/miserbales_dataset.json", "r") as f:
#    content = f.read()

my_dict = json.loads(content)

for key in my_dict.keys():
    print(key)