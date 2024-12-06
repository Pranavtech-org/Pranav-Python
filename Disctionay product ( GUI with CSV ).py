import tkinter as tk
from tkinter import messagebox
import csv

# Initialize products dictionary
products = {}

# File path for CSV
csv_file = "product.csv"

# Load products from CSV
def load_products():
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Avoid empty rows
                    pno, pnm, cost, company = int(row[0]), row[1], int(row[2]), row[3]
                    products[pno] = [pnm, cost, company]
    except FileNotFoundError:
        # If file doesn't exist, start with an empty dictionary
        pass

# Save products to CSV
def save_products():
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for pno, details in products.items():
            writer.writerow([pno] + details)

# Add Product Function
def add_product():
    try:
        pno = int(entry_pno.get())
        pnm = entry_pnm.get()
        cost = int(entry_cost.get())
        company = entry_company.get()
        
        if pno in products:
            messagebox.showerror("Error", "Product number already exists!")
        else:
            products[pno] = [pnm, cost, company]
            save_products()
            messagebox.showinfo("Success", "Product added successfully!")
        clear_entries()
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Ensure correct data format.")

# Search Product Function
def search_product():
    try:
        pno = int(entry_pno.get())
        if pno in products:
            details = products[pno]
            messagebox.showinfo("Product Found", f"Details: {details}")
        else:
            messagebox.showwarning("Not Found", "Product not in our list.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid product number.")

# Delete Product Function
def delete_product():
    try:
        pno = int(entry_pno.get())
        if pno in products:
            products.pop(pno)
            save_products()
            messagebox.showinfo("Success", f"Product {pno} deleted successfully!")
        else:
            messagebox.showwarning("Not Found", "Product not found.")
        clear_entries()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid product number.")

# Modify Product Function
def modify_product():
    try:
        pno = int(entry_pno.get())
        if pno in products:
            pnm = entry_pnm.get()
            cost = int(entry_cost.get())
            company = entry_company.get()
            products[pno] = [pnm, cost, company]
            save_products()
            messagebox.showinfo("Success", f"Product {pno} modified successfully!")
        else:
            messagebox.showwarning("Not Found", "Product not found.")
        clear_entries()
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Ensure correct data format.")

# Display All Products
def display_all():
    if products:
        all_products = "\n".join([f"{k}: {v}" for k, v in products.items()])
        messagebox.showinfo("All Products", all_products)
    else:
        messagebox.showinfo("No Products", "No products available.")

# Search by Company
def search_by_company():
    company = entry_company.get()
    result = [f"{k}: {v}" for k, v in products.items() if v[2] == company]
    if result:
        messagebox.showinfo("Search Results", "\n".join(result))
    else:
        messagebox.showwarning("Not Found", "No products found for this company.")

# Clear Entry Fields
def clear_entries():
    entry_pno.delete(0, tk.END)
    entry_pnm.delete(0, tk.END)
    entry_cost.delete(0, tk.END)
    entry_company.delete(0, tk.END)

# Exit Application
def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Product Sales Management System")
root.configure(bg="powder blue")

# Common font settings
font_settings = ("Candara", 30)

# Labels
tk.Label(root, text="Product Number:", bg="powder blue", font=font_settings).grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Product Name:", bg="powder blue", font=font_settings).grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Cost:", bg="powder blue", font=font_settings).grid(row=2, column=0, padx=10, pady=5)
tk.Label(root, text="Company:", bg="powder blue", font=font_settings).grid(row=3, column=0, padx=10, pady=5)

# Entry Fields
entry_pno = tk.Entry(root, font=font_settings)
entry_pnm = tk.Entry(root, font=font_settings)
entry_cost = tk.Entry(root, font=font_settings)
entry_company = tk.Entry(root, font=font_settings)

entry_pno.grid(row=0, column=1, padx=10, pady=5)
entry_pnm.grid(row=1, column=1, padx=10, pady=5)
entry_cost.grid(row=2, column=1, padx=10, pady=5)
entry_company.grid(row=3, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Product", bg="blue", fg="white", font=font_settings, command=add_product).grid(row=4, column=0, padx=10, pady=5)
tk.Button(root, text="Search Product", bg="blue", fg="white", font=font_settings, command=search_product).grid(row=4, column=1, padx=10, pady=5)
tk.Button(root, text="Delete Product", bg="blue", fg="white", font=font_settings, command=delete_product).grid(row=5, column=0, padx=10, pady=5)
tk.Button(root, text="Modify Product", bg="blue", fg="white", font=font_settings, command=modify_product).grid(row=5, column=1, padx=10, pady=5)
tk.Button(root, text="Display All", bg="blue", fg="white", font=font_settings, command=display_all).grid(row=6, column=0, padx=10, pady=5)
tk.Button(root, text="Search by Company", bg="blue", fg="white", font=font_settings, command=search_by_company).grid(row=6, column=1, padx=10, pady=5)
tk.Button(root, text="Exit", bg="red", fg="white", font=font_settings, command=exit_app).grid(row=7, column=0, columnspan=2, pady=10)

# Load products from CSV on startup
load_products()

root.mainloop()
