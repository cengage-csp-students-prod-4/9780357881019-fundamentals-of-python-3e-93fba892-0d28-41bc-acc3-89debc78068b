"""
viewfiles.py
Recursively displays a file's name and contents, or applies itself
to every name in a directory.
"""

import os


def view_files(pathname):
    if os.path.isfile(pathname):
        print("File name:", pathname)
        with open(pathname, "r") as f:
            print(f.read())
    elif os.path.isdir(pathname):
        print("Directory name:", pathname)
        names = os.listdir(pathname)
        # Files first, then subdirectories (each group alphabetical)
        names.sort(key=lambda n: (os.path.isdir(os.path.join(pathname, n)), n))
        for name in names:
            view_files(os.path.join(pathname, name))
    else:
        print("Not a valid file or directory:", pathname)


def main():
    # Build the test structure
    base = os.path.join("chapter7", "ex04", "student")
    assets = os.path.join(base, "assets")
    os.makedirs(assets, exist_ok=True)

    with open(os.path.join(base, "text.txt"), "w") as f:
        f.write("The girl caught the falling leaf.")
    with open(os.path.join(assets, "text.txt"), "w") as f:
        f.write("The boy kicked the red ball.")

    view_files(base)


if __name__ == "__main__":
    main()