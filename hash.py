import hashlib


def get_hash(file_path):
    with open(file_path) as f:
        for string in f:
            yield hashlib.md5(string.encode()).hexdigest()



