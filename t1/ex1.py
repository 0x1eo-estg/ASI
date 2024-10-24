import re
import hashlib

def read_file(file):
    data = {}
    with open(file, 'r'):
        for i, line in enumerate(file):
            def hash_match(match):
                return hashlib.sha256(match.group(0).encode()).hexdigest()

            line = re.sub(r'8\d{6}', hash_match, line)
            data[i] = line

def write_file(data, file):
    with open(file, 'w') as file:
        for line in data:
            file.write(line)

def __main__():
    data = read_file('list.txt')
    write_file(data, 'list_hash.txt')