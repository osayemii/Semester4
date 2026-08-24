import sys

import pandas as pd
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox, QPushButton,
    QVBoxLayout, QHBoxLayout, QSizePolicy,
)
from PySide6.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

# ---------- 1. Load and clean the data ----------
df = pd.read_csv("data_processing/Product_Sales.csv")

for col in ["Sale Price in ₦", "Marked Price in ₦", "Number of Ratings",
            "Number of Reviews", "Star Ratings"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["Star Ratings"] = df["Star Ratings"].fillna(0)
df["Number of Ratings"] = df["Number of Ratings"].fillna(0)

# The CSV has no Quantity/Stock/Date columns, so "Number of Ratings"
# is used as a stand-in (proxy) for quantity sold and stock.

CHART_OPTIONS = [
    "Total sales by product",
    "Sales contribution by product",
    "Ratings distribution",
    "Price distribution",
    "Sales trend",
    "Price vs quantity sold",
    "Product vs stock",
    "Stock distribution",
]


class SalesAnalysisWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sales Analysis")
        self.resize(950, 650)

        # ---------- 2. Build the window ----------
        heading = QLabel("Sales Analysis with Charts")
        heading.setAlignment(Qt.AlignCenter)

        subheading = QLabel("Choose a chart to analyze the Product Sales data")
        subheading.setAlignment(Qt.AlignCenter)

        # --- dropdown and button share this one row, so they sit side by side ---
        control_row = QHBoxLayout()
        control_row.addStretch()
        control_row.addWidget(QLabel("Chart Type:"))

        self.chart_combo = QComboBox()
        self.chart_combo.addItems(CHART_OPTIONS)
        self.chart_combo.setFixedWidth(230)
        control_row.addWidget(self.chart_combo)

        show_button = QPushButton("Show Chart")
        show_button.clicked.connect(self.show_chart)
        control_row.addWidget(show_button)
        control_row.addStretch()

        self.canvas = None
        self.chart_layout = QVBoxLayout()

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(heading)
        main_layout.addWidget(subheading)
        main_layout.addLayout(control_row)
        main_layout.addLayout(self.chart_layout)

        self.show_chart()  # draw the first chart on startup

    # ---------- 3. Draw whichever chart is selected ----------
    def show_chart(self):
        if self.canvas is not None:                 # remove the old chart
            self.chart_layout.removeWidget(self.canvas)
            self.canvas.deleteLater()
            self.canvas = None

        fig = Figure(figsize=(8.5, 5))
        ax = fig.add_subplot(111)
        choice = self.chart_combo.currentText()

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
        self.canvas = FigureCanvasQTAgg(fig)          # glue figure into Qt
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.chart_layout.addWidget(self.canvas)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SalesAnalysisWindow()
    window.show()
    sys.exit(app.exec())
