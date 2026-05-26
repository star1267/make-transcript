import json
import os

def write_json(path, content):
    """This creates a json file and write the dict to that file."""
    #
    with open(path, "w") as output:
        json.dump(content, output, indent=2)

    ...


def readjson(path):
    """This function checks to see if there is already a json file under the name. If so it reads the file and returns the content of the file."""

    # Checks if the json file exists. If not it returns nothing and the function is done
    if not os.path.exists(path):
        return None

    #  if the json file does exist it moves on to this
    else:
        # Opens the json file and reads the content
        with open(path, "r") as input:
            # Puts the content from the json in the dict filecontent
            filecontent = json.load(input)
            # returns the filecontent
            return filecontent
    ...