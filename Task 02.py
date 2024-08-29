# Create a stock portfolio tracking tool that allows users to add, remove, and track the performance of their
# stock investments. Utilize financial APIs for real-time stock data

import tkinter as tk
import requests


class Application:
    def __init__(self, root):
        self.root = root
        self.stock = {}

        self.root.title("Stock Portfolio Tracker")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.title_label = tk.Label(self.root, text="Stock Portfolio Tracker", font=("Arial Black", 18))
        self.title_label.grid(column=0, row=0, columnspan=2, pady=10)

        self.stock_symbol_label = tk.Label(self.root, text="Stock Symbol:", font=("Calibri", 12))
        self.stock_symbol_label.grid(column=0, row=1, padx=10, pady=10, sticky='e')
        self.stock_symbol_entry = tk.Entry(self.root, width=40)
        self.stock_symbol_entry.grid(column=1, row=1, padx=10, pady=10, sticky='w')
        self.stock_symbol_entry.focus()

        self.listbox = tk.Listbox(self.root, width=60)
        self.listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Stock", font=("Calibri", 12), command=self.add_stock)
        self.add_button.grid(column=0, row=3, padx=10, pady=10, sticky='e')

        self.remove_button = tk.Button(self.root, text="Remove Stock", font=("Calibri", 12), command=self.remove_stock)
        self.remove_button.grid(column=1, row=3, padx=10, pady=10, sticky='w')

        self.message_label = tk.Label(self.root, text="")
        self.message_label.grid(row=4, columnspan=2)

    def add_stock(self):
        symbol = self.stock_symbol_entry.get().upper()
        if symbol in self.stock:
            self.message_label.config(text=f"Stock {symbol} already exists")
            return

        try:
            price = self.get_stock_price(symbol)
            self.stock[symbol] = price
            self.listbox.insert(tk.END, f"{symbol}: ${price:.2f}")
            self.message_label.config(text=f"Stock added successfully.")
        except Exception as e:
            self.message_label.config(text=f"Failed to add stock: {e}")

    def remove_stock(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            self.message_label.config(text="Please select a stock to remove")
            return
        symbol = self.listbox.get(selected_index[0]).split(":")[0].strip()
        del self.stock[symbol]
        self.listbox.delete(selected_index)
        self.message_label.config(text="Stock removed successfully")

    def get_stock_price(self, symbol):
        api_key = "ZJ1ICNJVIQQFS9Q0"  # Replace with your actual API key
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
        response = requests.get(url)
        data = response.json()

        # Print out the response for debugging
        print(data)

        if "Global Quote" in data and "05. price" in data["Global Quote"]:
            return float(data["Global Quote"]["05. price"])
        elif "Note" in data:
            raise Exception("API request limit reached. Please wait and try again later.")
        elif "Error Message" in data:
            raise Exception("Invalid stock symbol or API request failed.")
        else:
            raise Exception("Invalid response from API")


root = tk.Tk()
app = Application(root)
root.mainloop()