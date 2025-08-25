import pathlib
import pytest

import solutions


@pytest.mark.parametrize("walk", [solutions.walk_3])
def test_walk(walk, tmpdir):
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

    assert set(walk(root_dir)) == set(files)
