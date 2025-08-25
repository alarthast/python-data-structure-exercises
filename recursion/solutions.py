import pathlib


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
