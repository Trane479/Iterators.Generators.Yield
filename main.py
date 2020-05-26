import hash
import json
from Iterator import CountryIterator


if __name__ == '__main__':
    with open('countries.json', encoding="utf-8") as f:
        data = json.load(f)
    for item in CountryIterator(0, 249, data):
        pass
    for hash_string in hash.get_hash('countries.txt'):
        print(hash_string)

