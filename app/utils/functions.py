from typing import Generator


def open_file(path: str) -> Generator | Exception:
    """
    Open file as generator
    :param path: file path
    :return: Generator object
    """
    try:
        with open(path, encoding='utf-8') as f:
            while True:
                try:
                    line = next(f)
                except StopIteration:
                    break
                yield line.strip('\n')
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path} is not found")
