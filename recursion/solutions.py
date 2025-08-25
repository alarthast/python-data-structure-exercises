import pathlib


def walk_1(path: pathlib.Path):  # Recusion and no generators
    """Return a list of all paths to files nested in path."""
    if not path.is_dir():
        return [path]
    return [path_ for item in path.iterdir() for path_ in walk_1(item)]


def walk_2(path: pathlib.Path):  # Recusion and generators
    """Return a list of all paths to files nested in path."""
    return list(_walk_2(path))


def _walk_2(path: pathlib.Path):
    if not path.is_dir():
        yield path
    else:
        for item in path.iterdir():
            yield from _walk_2(item)


def walk_3(path: pathlib.Path):  # No recursion
    """Return a list of all paths to files nested in path."""
    files = []
    directories = [path]
    while len(directories) > 0:
        current_dir = directories.pop(0)
        for item in current_dir.iterdir():
            if item.is_dir():
                directories.append(item)
            else:
                files.append(item)

    return files
