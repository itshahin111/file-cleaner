import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import send2trash
import logging

# Logging setup
log_file = "file_cleaner_log.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")

def get_extensions_in_folder(folder_path):
    extensions = set()
    for root, _, files in os.walk(folder_path):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext:
                extensions.add(ext)
    return sorted(extensions)

class FileCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Cleaner Tool")
        self.root.geometry("650x650")

        self.folder_path = tk.StringVar()
        self.max_size_bytes = tk.IntVar(value=0)
        self.extension_vars = {}
        self.extensions = []
        self.file_list_to_delete = []

        self.create_widgets()

    def create_widgets(self):
        # Folder selection
        tk.Label(self.root, text="Select Folder:").pack(pady=5)
        folder_frame = tk.Frame(self.root)
        folder_frame.pack(pady=5)
        tk.Entry(folder_frame, textvariable=self.folder_path, width=50).pack(side=tk.LEFT)
        tk.Button(folder_frame, text="Browse", command=self.browse_folder).pack(side=tk.LEFT, padx=5)

        # Max size input
        size_frame = tk.Frame(self.root)
        size_frame.pack(pady=5)
        tk.Label(size_frame, text="Maximum Size (Bytes):").pack(side=tk.LEFT)
        tk.Entry(size_frame, textvariable=self.max_size_bytes, width=15).pack(side=tk.LEFT)
        tk.Label(size_frame, text="(Leave blank or 0 to ignore size)").pack(side=tk.LEFT, padx=5)

        # Extension checkboxes
        self.extension_frame = tk.LabelFrame(self.root, text="File Types to Delete (if size ≤ max)")
        self.extension_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Select/Deselect All buttons
        action_frame = tk.Frame(self.root)
        action_frame.pack()
        tk.Button(action_frame, text="Select All", command=self.select_all_extensions).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="Deselect All", command=self.deselect_all_extensions).pack(side=tk.LEFT, padx=5)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Preview Files to Delete", command=self.preview_deletion).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Delete Files", command=self.delete_files).pack(side=tk.LEFT, padx=10)

        # Progress bar
        self.progress = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=500, mode='determinate')
        self.progress.pack(pady=10)

        # Log output
        self.log_output = tk.Text(self.root, height=10)
        self.log_output.pack(fill=tk.BOTH, padx=10, pady=10)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)
            self.load_extensions(folder)

    def load_extensions(self, folder):
        for widget in self.extension_frame.winfo_children():
            widget.destroy()

        self.extensions = get_extensions_in_folder(folder)
        self.extension_vars = {}

        for ext in self.extensions:
            var = tk.BooleanVar(value=True)
            cb = tk.Checkbutton(self.extension_frame, text=ext, variable=var)
            cb.pack(anchor='w')
            self.extension_vars[ext] = var

    def select_all_extensions(self):
        for var in self.extension_vars.values():
            var.set(True)

    def deselect_all_extensions(self):
        for var in self.extension_vars.values():
            var.set(False)

    def preview_deletion(self):
        folder = self.folder_path.get()
        if not folder:
            messagebox.showwarning("No Folder", "Please select a folder first.")
            return

        try:
            max_size = int(self.max_size_bytes.get())
        except:
            max_size = 0  # Treat invalid input as 0

        selected_exts = {ext for ext, var in self.extension_vars.items() if var.get()}
        self.file_list_to_delete = []

        for root, _, files in os.walk(folder):
            for file in files:
                full_path = os.path.normpath(os.path.join(root, file))
                ext = os.path.splitext(file)[1].lower()
                try:
                    size = os.path.getsize(full_path)
                except Exception as e:
                    logging.warning(f"Cannot access {full_path}: {e}")
                    continue

                if ext in selected_exts and (max_size == 0 or size <= max_size):
                    self.file_list_to_delete.append(full_path)

        self.log_output.delete(1.0, tk.END)
        self.log_output.insert(tk.END, "Files that would be deleted:\n\n")
        for f in self.file_list_to_delete:
            self.log_output.insert(tk.END, f + "\n")
        self.progress['value'] = 0

    def delete_files(self):
        if not self.file_list_to_delete:
            messagebox.showinfo("Nothing to Delete", "No files to delete. Run preview first.")
            return

        confirm = messagebox.askyesno(
            "Confirm Deletion",
            f"Are you sure you want to delete {len(self.file_list_to_delete)} files to Recycle Bin?"
        )
        if not confirm:
            return

        self.progress['maximum'] = len(self.file_list_to_delete)
        deleted_count = 0

        for file_path in self.file_list_to_delete:
            try:
                if os.path.exists(file_path):
                    send2trash.send2trash(file_path)
                    logging.info(f"Deleted: {file_path}")
                    deleted_count += 1
            except Exception as e:
                logging.error(f"Failed to delete {file_path}: {e}")

            self.progress['value'] = deleted_count
            self.root.update_idletasks()

        self.log_output.insert(tk.END, f"\n\n✅ Deleted {deleted_count} files. See {log_file} for details.")
        messagebox.showinfo("Done", f"Deleted {deleted_count} files. See log for details.")

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = FileCleanerApp(root)
    root.mainloop()
