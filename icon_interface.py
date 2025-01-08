import os
import shutil
from tkinter import Tk, filedialog, messagebox, Button, Label, Listbox

class IconInterface:
    def __init__(self):
        self.root = Tk()
        self.root.title("IconInterface - Customize Your Windows Icons")

        self.selected_icons = {}

        self.label = Label(self.root, text="Select icons for your applications:")
        self.label.pack(pady=10)

        self.icon_listbox = Listbox(self.root, selectmode='multiple', width=50, height=15)
        self.icon_listbox.pack(pady=10)

        self.load_icons_button = Button(self.root, text="Load Icons", command=self.load_icons)
        self.load_icons_button.pack(pady=5)

        self.apply_icons_button = Button(self.root, text="Apply Icons", command=self.apply_icons)
        self.apply_icons_button.pack(pady=5)

        self.root.mainloop()

    def load_icons(self):
        icon_directory = filedialog.askdirectory(title="Select Icon Directory")
        if not icon_directory:
            return

        self.icon_listbox.delete(0, 'end')
        self.selected_icons.clear()

        for icon_file in os.listdir(icon_directory):
            if icon_file.endswith('.ico'):
                self.icon_listbox.insert('end', icon_file)
                self.selected_icons[icon_file] = os.path.join(icon_directory, icon_file)

    def apply_icons(self):
        selected_indices = self.icon_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("No Selection", "Please select at least one icon to apply.")
            return

        application_directory = filedialog.askdirectory(title="Select Application Directory")
        if not application_directory:
            return

        for index in selected_indices:
            icon_name = self.icon_listbox.get(index)
            icon_path = self.selected_icons[icon_name]

            try:
                shutil.copy(icon_path, application_directory)
                messagebox.showinfo("Success", f"{icon_name} applied successfully to {application_directory}.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to apply {icon_name}. Error: {str(e)}")

if __name__ == "__main__":
    IconInterface()