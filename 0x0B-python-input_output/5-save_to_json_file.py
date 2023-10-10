#!/user/bin/python3
"""defines function that write JSON
representain of an object to file"""


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
