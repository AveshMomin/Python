import tkinter as tk
from tkinter import messagebox
import pickle
import os

class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(root, text="Phone Number:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.contacts_text = tk.Text(root, width=50, height=10)
        self.contacts_text.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.load_contacts()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            contact = {'name': name, 'phone': phone, 'email': email}
            self.save_contact(contact)
            self.load_contacts()
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def save_contact(self, contact):
        if os.path.exists("contacts.txt"):
            with open("contacts.txt", "rb") as file:
                contacts = pickle.load(file)
        else:
            contacts = []

        contacts.append(contact)

        with open("contacts.pkl", "wb") as file:
            pickle.dump(contacts, file)

    def load_contacts(self):
        self.contacts_text.delete(1.0, tk.END)
        if os.path.exists("contacts.pkl"):
            with open("contacts.pkl", "rb") as file:
                contacts = pickle.load(file)
            for contact in contacts:
                self.contacts_text.insert(tk.END, f"Name: {contact['name']}\n")
                self.contacts_text.insert(tk.END, f"Phone: {contact['phone']}\n")
                self.contacts_text.insert(tk.END, f"Email: {contact['email']}\n")
                self.contacts_text.insert(tk.END, "-"*30 + "\n\n")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()
