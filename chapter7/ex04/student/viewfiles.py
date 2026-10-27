"""
viewfiles.py
Recursively displays files: a file's name followed by its contents,
or applies itself to every name in a directory.
"""

import os


def view_files(pathname):
    """Display a file's name and contents, or recurse through a directory."""
    if os.path.isfile(pathname):
        print(pathname)
        with open(pathname, "r") as f:
            print(f.read())
            print()
    elif os.path.isdir(pathname):
        for name in os.listdir(pathname):
            view_files(os.path.join(pathname, name))
    else:
        print("Not a valid file or directory:", pathname)


def main():
    # Create a test directory containing the two text files
    os.makedirs("testdir", exist_ok=True)

    with open(os.path.join("testdir", "file1.txt"), "w") as f:
        f.write("The girl caught the falling leaf.")

    with open(os.path.join("testdir", "file2.txt"), "w") as f:
        f.write("The boy kicked the red ball.")

    # Test with the directory (recurses into each file)
    view_files("testdir")

    # Test with a single file
    view_files(os.path.join("testdir", "file1.txt"))


if __name__ == "__main__":
    main()