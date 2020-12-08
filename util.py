import inspect
from pathlib import Path


def get_filename():
    path = inspect.stack()[1].filename
    filename = f'input/{Path(path).name.rsplit(".", 1)[0]}.txt'

    return filename
