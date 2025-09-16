import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# create a sample csv file for anaylsis operations
csv_data = """Date, Product, Quantity Sold, Revenue($)
2025-03-01,Laptop,5,5000
2025-03-01,Mouse,15,300
2025-03-02,Laptop,3,3000
2025-03-02,Keyboard,8,800
2025-03-03,Mouse,12,240
2025-03-03,Monitor,4,1200
2025-03-04,Laptop,7,7000
2025-03-04,Keyboard,10,1000
2025-03-05,Monitor,6,1800
2025-03-05,Mouse,20,400
"""

with open("sales_data.csv", "w") as f:
    f.write(csv_data)

# --Create a SalesAnalyzer class
class SalesAnalyzer:
    """A class to load, analyze and report on sales from a csv file.
    It encapsulates the data and all related analysis methods
    """

    def __init__(self, file_path):
        """Initialize the SalesAnalyzer with a csv file path."""
        self.file_path = file_path
        try:
            self.data = pd.read_csv(self.file_path)
            self._prepare_data()
        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}.")
            self.data = None

    def _prepare_data(self):
        """Prepare data by converting date column to datetime."""
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.rename(columns={'Revenue($)': 'Revenue'}, inplace=True)

    def calculate_total_revenue(self):
        """Calculate total revenue."""
        if self.data is not None:
            return self.data['Revenue'].sum()
        
        return 0

    def find_best_selling_product(self):
        if self.data is not None:
            product_sales = self.data.groupby('Product')['Quantity Sold'].sum()
            best_seller = product_sales.idmax()
            units_sold = product_sales.max()
            return best_seller, units_sold
        
        return None, 0

    def find_highest_sales_day(self):
        """Find the day with highest sales."""
        if self.data is not None:
            daily_sales = self.data.groupby('Date')['Revenue'].sum()
            best_day = daily_sales.idmax()
            return best_day.strftime('%Y-%m-%d')
        
        return None
    
    def generate_summary_report(self, output_filepath='sales_summary.txt'):
        if self.data is not None:
            print("Cannot generate summary because data was not loaded")
            return

        total_revenue = self.calculate_total_revenue()
        best_product, units_sold = self.find_best_selling_product()
        highest_day = self.find_highest_sales_day()

        summary = (
            f"Sales Summary Report\n"
            f"====================\n"
            f"Total Revenue: ${total_revenue:,.2f}\n"
            f"Best Selling Product: {best_product} ({units_sold} units sold)\n"
            f"Highest Sales Day: {highest_day}\n"
        )

        with open(output_filepath, 'w') as f:
            f.write(summary)

        print("---Sales Insights---")
        print(summary)
        print(f"Summary report saved to {output_filepath}")



    # visualizing our data trends

    def plot_sales_trends(self):
        """Visualizes total daily revenue over time"""
        if self.data is None:
            print("Cannot plot trends because no data was loaded")
            return

        
        # prepare the data; group by date and sum the revenue
        # .reset_index() converts the grouped object back to a DataFrame
        # that seaborn can work on easily

        daily_revenue_df = self.data.groupby('Date')['Revenue'].sum().reset_index()

        # set the aesthetic style of the plot
        sns.set_theme(style='darkgrid',palette='viridis')

        # create the plot figure
        plt.figure(figsize=(10,6))

        # create the line plot using seaborn declarative syntax
        ax = sns.lineplot(
            data=daily_revenue_df,
            x='Date',
            y='Revenue',
            marker='o',
            color='yellow',
            linestyle='--'
        )

        # customize the plot using matplotlib's functions
        ax.set_title('Daily Sales Revenue Trend', fontsize=16)
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Revenue ($)', fontsize=12)

        # improve date formatting on the x-axis
        plt.xticks(rotation=45)
        plt.tight_layout()  # adjust the plot to fit into the figure area

        # display the plot
        plt.show()


if __name__ == "__main__":
    analyzer = SalesAnalyzer('sales_data.csv')

    if analyzer.data is not None:
        analyzer.generate_summary()
        analyzer.plot_sales_trends()

              