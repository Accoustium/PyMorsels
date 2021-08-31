from typing import *
import csv


def condense_csv(text: str, id_name: Optional[str] = None):
    output_dict = {}
    key_set = list()
    reader = csv.reader(text.split("\n"))

    while True:
        try:
            obj, key, value = next(reader)
            if id_name is None:
                id_name = obj
                continue

            if obj not in output_dict.keys():
                output_dict[obj] = {}

            output_dict[obj].update({key: value})
            if key not in key_set:
                key_set.append(key)

        except StopIteration:
            break

    output_text = ','.join([id_name, *key_set])
    for obj, __dict in output_dict.items():
        output_text += f"\n{obj}"
        for key in key_set:
            value = __dict.get(key, '')
            value = value if ',' not in value else f'"{value}"'
            output_text += f",{value}"

    return output_text
