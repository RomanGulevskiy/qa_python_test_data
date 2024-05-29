import os


def get_path(filename: str):
    return os.path.join(os.path.dirname(__file__), filename)


CSV_FILE_PATH = get_path("books.csv")
JSON_FILE_PATH = get_path("users.json")
