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

'''
Как нужно было...
import argparse
import json
import os
import tempfile


def read_data(storage_path):
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as file:
        raw_data = file.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


def write_data(storage_path, data):
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    return parser.parse_args()


def put(storage_path, key, value):
    data = read_data(storage_path)
    data[key] = data.get(key, list())
    data[key].append(value)
    write_data(storage_path, data)


def get(storage_path, key):
    data = read_data(storage_path)
    return data.get(key, [])


def main(storage_path):
    args = parse()

    if args.key and args.val:
        put(storage_path, args.key, args.val)
    elif args.key:
        print(*get(storage_path, args.key), sep=', ')
    else:
        print('The program is called with invalid parameters.')


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)
'''