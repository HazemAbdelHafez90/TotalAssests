from main import calculate_total_assets
import tkinter as tk
import threading

def submit():
    # Create loading message window
    loading_window = tk.Toplevel(window)
    loading_window.title("Loading...")
    loading_label = tk.Label(loading_window, text="Calculating...")
    loading_label.pack()

    # Get input values
    gold_values = gold.get()
    stocks_values = stocks.get()
    usd_values = usd.get()
    egp_values = egp.get()
    
    # Do something with the input values, e.g. print them
    total_assets = calculate_total_assets(gold_values,usd_values,egp_values , stocks_values)

    # Update output with calculated result
    output.delete('1.0', tk.END) # clear the previous content
    output.insert(tk.END, f"Total assets: {total_assets:,}")
    output.tag_configure("center", justify='center')
    output.tag_add("center", "1.0", "end")

    # Destroy loading message window
    loading_window.destroy()

window = tk.Tk()
window.title("Input Form")
window.geometry("600x450")

tk.Label(window, text="Gold:").grid(row=0, column=0, padx=10, pady=10, sticky="W")
gold = tk.Entry(window)
gold.grid(row=0, column=1, sticky="E")

tk.Label(window, text="Stocks:").grid(row=1, column=0, padx=10, pady=10, sticky="W")
stocks = tk.Entry(window)
stocks.grid(row=1, column=1, sticky="E")

tk.Label(window, text="USD:").grid(row=2, column=0, padx=10, pady=10, sticky="W")
usd = tk.Entry(window)
usd.grid(row=2, column=1, sticky="E")

tk.Label(window, text="EGP:").grid(row=3, column=0, padx=10, pady=10, sticky="W")
egp = tk.Entry(window)
egp.grid(row=3, column=1, sticky="E")

submit_button = tk.Button(window, text="Submit", command=submit)






submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

output = tk.Text(window, height=5, width=50)
output.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
