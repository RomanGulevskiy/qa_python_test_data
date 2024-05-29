from csv import DictReader
import json

from files import CSV_FILE_PATH
from files import JSON_FILE_PATH

result = []

with open(JSON_FILE_PATH, "r") as json_file, open(CSV_FILE_PATH, "r") as csv_file:
    for user in json.loads(json_file.read()):
        result.append(
            {
                'name': user['name'],
                'gender': user['gender'],
                'address': user['address'],
                'age': user['age'],
                'books': []
            }
        )

    iter_users = iter(result)
    for book in list(DictReader(csv_file)):
        try:
            user = next(iter_users)
            user['books'].append(
                {
                    "title": book['Title'],
                    "author": book['Author'],
                    "pages": book['Pages'],
                    "genre": book['Genre']
                }
            )
        except StopIteration:
            iter_users = iter(result)

with open('result.json', 'w') as f:
    f.write(json.dumps(result, indent=4))
