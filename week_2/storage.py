import os, tempfile, argparse, json

storage_data = os.path.join(tempfile.gettempdir(), 'storage.data')

def data_add():
    if not os.path.exists(storage_data):
        return {}
    with open(storage_data, 'r') as f:
        data_temp = f.read()
        if data_temp:
            return json.loads(data_temp)
        return {}

def print_key(key):
    data = data_add()
    return data.get(key)

def add_key_value(key, value):
    data = data_add()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]
    with open(storage_data, 'w') as f:
        f.write(json.dumps(data))

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')

args = parser.parse_args()

if args.key and args.val:
    add_key_value(args.key, args.val)
elif args.key and not os.path.exists(storage_data):
    print(' ')
elif args.key and print_key(args.key):
    print(*print_key(args.key), sep=', ')