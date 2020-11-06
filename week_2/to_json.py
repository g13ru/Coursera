import functools, json

def to_json(x):
    @functools.wraps(x)
    def inn_function(*args, **kwargs):
        return json.dumps(x(*args, **kwargs))
    return inn_function
