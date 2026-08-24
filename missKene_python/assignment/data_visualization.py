import tkinter as tk
import pandas as pd
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------- 1. Load and clean the data ----------
df = pd.read_csv("data_processing/Product_Sales.csv")

for col in ["Sale Price in ₦", "Marked Price in ₦", "Number of Ratings",
            "Number of Reviews", "Star Ratings"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["Star Ratings"] = df["Star Ratings"].fillna(0)
df["Number of Ratings"] = df["Number of Ratings"].fillna(0)

# The CSV has no Quantity/Stock/Date columns, so "Number of Ratings"
# is used as a stand-in (proxy) for quantity sold and stock.

# ---------- 2. Build the window ----------
root = tk.Tk()
root.title("Sales Analysis")
root.geometry("950x650")

tk.Label(root, text="Sales Analysis with Charts",
         font=("Segoe UI", 16, "bold")).pack(pady=(10, 2))
tk.Label(root, text="Choose a chart to analyze the Product Sales data",
         font=("Segoe UI", 10)).pack(pady=(0, 8))

# --- dropdown and button share this one frame, so they sit side by side ---
control_frame = tk.Frame(root)
control_frame.pack(pady=5)

tk.Label(control_frame, text="Chart Type:").pack(side="left", padx=(0, 6))

chart_var = tk.StringVar(value="Total sales by product")
options = [
    "Total sales by product",
    "Sales contribution by product",
    "Ratings distribution",
    "Price distribution",
    "Sales trend",
    "Price vs quantity sold",
    "Product vs stock",
    "Stock distribution",
]
ttk.Combobox(control_frame, textvariable=chart_var, values=options,
             state="readonly", width=28).pack(side="left", padx=(0, 8))

chart_frame = tk.Frame(root)


# ---------- 3. Draw whichever chart is selected ----------
def show_chart():
    for widget in chart_frame.winfo_children():   # remove the old chart
        widget.destroy()

    fig = Figure(figsize=(8.5, 5))
    ax = fig.add_subplot(111)
    choice = chart_var.get()

    if choice == "Total sales by product":                      # Bar chart
        sales = df.groupby("Product")["Sale Price in ₦"].sum()
        ax.bar(sales.index, sales.values, color="#4f46e5")
        ax.set_title("Total Sales by Product")
        ax.set_ylabel("Sales Amount (₦)")
        ax.tick_params(axis="x", rotation=30)

    elif choice == "Sales contribution by product":             # Pie chart
        sales = df.groupby("Product")["Sale Price in ₦"].sum()
        ax.pie(sales.values, labels=sales.index, autopct="%1.1f%%", startangle=90)
        ax.set_title("Contribution of Each Product to Total Sales")

    elif choice == "Ratings distribution":                      # Histogram
        ax.hist(df["Star Ratings"], bins=8, color="#059669", edgecolor="black")
        ax.set_title("Distribution of Product Ratings")
        ax.set_xlabel("Star Ratings")
        ax.set_ylabel("Frequency")

    elif choice == "Price distribution":                        # Histogram
        ax.hist(df["Sale Price in ₦"], bins=10, color="#dc2626", edgecolor="black")
        ax.set_title("Distribution of Sale Prices")
        ax.set_xlabel("Sale Price (₦)")
        ax.set_ylabel("Frequency")

    elif choice == "Sales trend":                               # Line chart
        trend = df["Sale Price in ₦"].cumsum()
        ax.plot(range(1, len(trend) + 1), trend, marker="o", color="#0284c7")
        ax.set_title("Sales Trend (cumulative)")
        ax.set_xlabel("Sale Number")
        ax.set_ylabel("Cumulative Sales (₦)")
        ax.grid(True, linestyle="--", alpha=0.5)

    elif choice == "Price vs quantity sold":                    # Scatter plot
        ax.scatter(df["Sale Price in ₦"], df["Number of Ratings"],
                   color="#7c3aed", alpha=0.7)
        ax.set_title("Price vs Quantity Sold")
        ax.set_xlabel("Sale Price (₦)")
        ax.set_ylabel("Quantity Sold (ratings as proxy)")
        ax.grid(True, linestyle="--", alpha=0.5)

    elif choice == "Product vs stock":                          # Bar chart
        stock = df.groupby("Product")["Number of Ratings"].sum()
        ax.barh(stock.index, stock.values, color="#f59e0b")
        ax.set_title("Product vs Stock")
        ax.set_ylabel("Stock (proxy)")
        ax.tick_params(axis="x", rotation=30)

    elif choice == "Stock distribution":                        # Pie chart
        stock = df.groupby("Product")["Number of Ratings"].sum()
        ax.pie(stock.values, labels=stock.index, autopct="%1.1f%%", startangle=90)
        ax.set_title("Stock Distribution by Product")

    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)   # glue figure into tkinter
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


# the button goes into the SAME control_frame, right after the combobox
ttk.Button(control_frame, text="Show Chart", command=show_chart).pack(side='left')

chart_frame.pack(fill="both", expand=True, padx=10, pady=10)

show_chart()          # draw the first chart on startup
root.mainloop()