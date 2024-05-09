import tkinter as tk
from tkinter import messagebox
import os

def add_note():
    note = entry.get()
    if note:
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        messagebox.showinfo("Note Added", "Note added successfully!")
        entry.delete(0, tk.END)
        display_notes()
    else:
        messagebox.showwarning("Empty Note", "Please enter a note.")

def display_notes():
    if os.path.exists("notes.txt"):
        notes_text.delete(0, tk.END)
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            for note in notes:
                notes_text.insert(tk.END, note)
    else:
        messagebox.showwarning("No Notes Found", "No notes found.")

def clear_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt", "w") as file:
            file.truncate(0)
        display_notes()
    else:
        messagebox.showwarning("No Notes Found", "No notes found.")
        
def update_note():
    selected_index = notes_text.curselection()
    new_note = entry.get()
    if selected_index and new_note:
        selected_index = selected_index[0]
        print("Selected Index:", selected_index)
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            print("Before Update:", notes)
        with open("notes.txt", "w") as file:
            for i, note in enumerate(notes):
                if i == selected_index:
                    file.write(new_note + "\n")
                    print("Updated Note:", new_note)
                else:
                    file.write(note)
        messagebox.showinfo("Note Updated", "Note updated successfully!")
        entry.delete(0, tk.END)
        display_notes()
    else:
        messagebox.showwarning("Selection Error", "Please select a note and enter a new note to update.")

def search_notes():
    keyword = search_entry.get().lower()
    if keyword:
        if os.path.exists("notes.txt"):
            notes_text.delete(0, tk.END)
            with open("notes.txt", "r") as file:
                notes = file.readlines()
                print("All Notes:", notes)
                for note in notes:
                    if keyword in note.lower():
                        notes_text.insert(tk.END, note)
                        print("Matched Note:", note)
        else:
            messagebox.showwarning("No Notes Found", "No notes found.")
    else:
        messagebox.showwarning("Empty Search", "Please enter a keyword to search.")


root = tk.Tk()
root.title("Simple Notes App")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Add Note", command=add_note)
add_button.pack(side=tk.LEFT, padx=5)

update_button = tk.Button(root, text="Update Note", command=update_note)
update_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Notes", command=clear_notes)
clear_button.pack(pady=5)

search_entry = tk.Entry(root, width=50)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_notes)
search_button.pack(pady=5)

notes_text = tk.Listbox(root, width=50, height=10)
notes_text.pack()

display_notes()

root.mainloop()
