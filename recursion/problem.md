Come up with three implementations for the following function:
```
def walk(path: Path):
    """Return a list of all paths to files nested in path."""
    ...
```
The first implementation should use recursion and no generators; 
the second you use recursion and generators; 
the third should not use recursion.

The only methods on Path objects you should use are .is_dir() and .iterdir().
Using .walk() is cheating!