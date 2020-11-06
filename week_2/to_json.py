import functools, json

def to_json(x):
    @functools.wraps(x)
    def inn_function(*args, **kwargs):
        return json.dumps(x(*args, **kwargs))
    return inn_function


'''
import functools
import json


def to_json(func):

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapped
'''