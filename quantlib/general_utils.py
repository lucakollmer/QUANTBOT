# This is a utility file for performing simple tasks.

import pickle

def save_file(path, obj):
    try:
        with open(path, "wb") as fp:
            pickle.dump(obj, fp)
    except Exception as err:
        # Do some error handling.
        print(err)

def load_file(path):
    try:
        with open(path, "rb") as fp:
            return pickle.load(fp)

    except Exception as err:
        # Do some error handling.
        print(err)
    