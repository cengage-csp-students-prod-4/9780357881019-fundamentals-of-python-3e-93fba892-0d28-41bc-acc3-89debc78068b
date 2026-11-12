"""A simple GUI text editor built with tkinter.

The program lets the user open, edit, and save plain text files. It has:
  * a labeled entry field for the filename
  * a multiline text widget with a vertical scrollbar
  * Open, Save, and New command buttons

Run with:  python texteditor.py
"""

import tkinter as tk
from tkinter import messagebox


class TextEditor(tk.Tk):
    """Main application window for the text editor."""

    def __init__(self):
        """Create the window and build all of its widgets."""
        super().__init__()
        self.title("Text Editor")
        self.geometry("600x450")

        # ----- Top row: labeled filename entry -----
        top = tk.Frame(self)
        top.pack(fill=tk.X, padx=8, pady=8)

        tk.Label(top, text="Filename:").pack(side=tk.LEFT)

        # StringVar keeps the entry's contents easy to read and update
        self.filename = tk.StringVar()
        self.entry = tk.Entry(top, textvariable=self.filename)
        # expand=True lets the entry stretch when the window is resized
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(6, 0))

        # ----- Middle: multiline text widget with vertical scrollbar -----
        middle = tk.Frame(self)
        middle.pack(fill=tk.BOTH, expand=True, padx=8)

        # Pack the scrollbar first so it stays on the right edge
        self.scrollbar = tk.Scrollbar(middle, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # yscrollcommand tells the text widget to update the scrollbar
        # whenever the visible portion of the text changes
        self.text = tk.Text(middle, wrap=tk.WORD,
                            yscrollcommand=self.scrollbar.set)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Connect the scrollbar back to the text widget so that dragging
        # the scrollbar scrolls the text (two-way link)
        self.scrollbar.config(command=self.text.yview)

        # ----- Bottom row: command buttons -----
        bottom = tk.Frame(self)
        bottom.pack(fill=tk.X, padx=8, pady=8)

        tk.Button(bottom, text="Open", width=10,
                  command=self.open_file).pack(side=tk.LEFT, padx=(0, 6))
        tk.Button(bottom, text="Save", width=10,
                  command=self.save_file).pack(side=tk.LEFT, padx=(0, 6))
        tk.Button(bottom, text="New", width=10,
                  command=self.new_file).pack(side=tk.LEFT)

    def open_file(self):
        """Load the file named in the entry field into the text widget."""
        name = self.filename.get().strip()

        # Require a filename before trying to open anything
        if not name:
            messagebox.showwarning("Open", "Please enter a filename.")
            return

        # Read the file; report any problem (missing file, bad permissions)
        try:
            with open(name, "r", encoding="utf-8") as f:
                contents = f.read()
        except OSError as e:
            messagebox.showerror("Open Error", f"Could not open file:\n{e}")
            return

        # Replace whatever is in the text widget with the file's contents
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", contents)

    def save_file(self):
        """Write the text widget's contents to the file named in the entry."""
        name = self.filename.get().strip()

        # Require a filename before trying to save anything
        if not name:
            messagebox.showwarning("Save", "Please enter a filename.")
            return

        try:
            with open(name, "w", encoding="utf-8") as f:
                # "end-1c" skips the extra newline tkinter adds at the end,
                # so saving doesn't grow the file each time
                f.write(self.text.get("1.0", "end-1c"))
        except OSError as e:
            messagebox.showerror("Save Error", f"Could not save file:\n{e}")

    def new_file(self):
        """Clear both the text widget and the filename entry."""
        self.text.delete("1.0", tk.END)
        self.entry.delete(0, tk.END)


# Only start the app when this file is run directly (not when imported)
if __name__ == "__main__":
    TextEditor().mainloop()