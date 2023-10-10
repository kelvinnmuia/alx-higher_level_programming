#!/user/bin/python3
"""defines function that write JSON
representain of an object to file"""


def save_to_json_file(my_obj, filename):
    """writes JSON representation of an object to a file"""
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj, ensure_ascii=False))
