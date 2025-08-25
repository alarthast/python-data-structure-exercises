import pathlib
import pytest

import solutions


@pytest.mark.parametrize("walk", [solutions.walk_1, solutions.walk_2])
def test_walk_with_recursion(walk, tmpdir):
    root_dir = pathlib.Path(tmpdir)
    dirs = [
        root_dir,
        root_dir / "child_1",
        root_dir / "child_1" / "grandchild_1",
        root_dir / "child_2",
    ]
    for dir in dirs:
        dir.mkdir(exist_ok=True)
    files = [
        root_dir / "root.md",
        root_dir / "child_1" / "child_1_file_1.md",
        root_dir / "child_1" / "grandchild_1" / "grandchild_1_file_1.md",
        root_dir / "child_1" / "grandchild_1" / "grandchild_1_file_2.md",
        root_dir / "child_2" / "child_2_file_1.md",
        root_dir / "child_2" / "child_2_file_2.md",
    ]
    for file in files:
        file.touch()

    retrieved = walk(root_dir)

    assert retrieved == files


def test_walk_with_while_loop(tmpdir):
    root_dir = pathlib.Path(tmpdir)
    dirs = [
        root_dir,
        root_dir / "child_1",
        root_dir / "child_1" / "grandchild_1",
        root_dir / "child_2",
    ]
    for dir in dirs:
        dir.mkdir(exist_ok=True)
    files = [
        root_dir / "root.md",
        root_dir / "child_1" / "child_1_file_1.md",
        root_dir / "child_2" / "child_2_file_1.md",
        root_dir / "child_2" / "child_2_file_2.md",
        root_dir / "child_1" / "grandchild_1" / "grandchild_1_file_1.md",
        root_dir / "child_1" / "grandchild_1" / "grandchild_1_file_2.md",
    ]
    for file in files:
        file.touch()

    assert solutions.walk_3(root_dir) == files
