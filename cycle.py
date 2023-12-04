import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as pdr
from datetime import datetime

# Set the style of matplotlib to 'dark_background', Set the font to 'Product Sans'
plt.style.use('dark_background')
plt.rcParams['font.family'] = 'Product Sans'

# Define the start and end date for the data
start_date = datetime(2000, 1, 1)
end_date = datetime.today()

# Fetching the data from FRED
gdp = pdr.get_data_fred('GDP', start_date, end_date)
unemployment = pdr.get_data_fred('UNRATE', start_date, end_date)
inflation = pdr.get_data_fred('CPIAUCSL', start_date, end_date)
consumer_confidence = pdr.get_data_fred('UMCSENT', start_date, end_date)
federal_funds_rate = pdr.get_data_fred('FEDFUNDS', start_date, end_date)
yield_curve = pdr.get_data_fred('T10Y2Y', start_date, end_date)
housing_starts = pdr.get_data_fred('HOUST', start_date, end_date)
existing_home_sales = pdr.get_data_fred('EXHOSLUSM495S', start_date, end_date)
retail_sales = pdr.get_data_fred('RSXFS', start_date, end_date)
industrial_production = pdr.get_data_fred('INDPRO', start_date, end_date)
durable_goods_orders = pdr.get_data_fred('DGORDER', start_date, end_date)
trade_balance = pdr.get_data_fred('BOPGSTB', start_date, end_date)

# Color coding by category
economic_activity_colors = {'GDP': 'blue', 'Unemployment': 'red', 'Inflation': 'green', 'Consumer Confidence': 'cyan', 
                            'Yield Curve': 'magenta', 'Federal Funds Rate': 'yellow', 'Housing Starts': 'orange', 
                            'Existing Home Sales': 'pink', 'Retail Sales': 'lightgreen', 'Industrial Production': 'lightblue', 
                            'Durable Goods Orders': 'violet', 'Trade Balance': 'lightyellow'}

# Plotting the data with the new indicators
plt.figure(figsize=(20, 20))

# Economic Activity
plt.subplot(4, 3, 1)
plt.plot(gdp, label='GDP', color=economic_activity_colors['GDP'])
plt.title('Gross Domestic Product')
plt.xlabel('Year')
plt.ylabel('Billions of Dollars')
plt.grid(True, alpha=0.5)
plt.legend()

plt.subplot(4, 3, 2)
plt.plot(unemployment, label='Unemployment Rate', color=economic_activity_colors['Unemployment'])
plt.title('Unemployment Rate')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.grid(True, alpha=0.5)
plt.legend()

plt.subplot(4, 3, 3)
plt.plot(inflation, label='CPI Inflation', color=economic_activity_colors['Inflation'])
plt.title('Consumer Price Index (Inflation)')
plt.xlabel('Year')
plt.ylabel('Index')
plt.grid(True, alpha=0.5)
plt.legend()

plt.subplot(4, 3, 4)
plt.plot(consumer_confidence, label='Consumer Confidence', color=economic_activity_colors['Consumer Confidence'])
plt.title('Consumer Confidence Index')
plt.xlabel('Year')
plt.ylabel('Index')
plt.grid(True, alpha=0.5)
plt.legend()

plt.subplot(4, 3, 5)
plt.plot(federal_funds_rate, label='Federal Funds Rate', color=economic_activity_colors['Federal Funds Rate'])
plt.title('Federal Funds Rate')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.grid(True, alpha=0.5)
plt.legend()

plt.subplot(4, 3, 6)
plt.plot(yield_curve, label='10Y-2Y Yield Curve', color=economic_activity_colors['Yield Curve'])
plt.title('10Y-2Y Yield Curve')
plt.xlabel('Year')
plt.ylabel('Percentage Points')
plt.grid(True, alpha=0.5)
plt.legend()

# Housing Market Indicators
plt.subplot(4, 3, 7)
plt.plot(housing_starts, label='Housing Starts', color=economic_activity_colors['Housing Starts'])
plt.title('Housing Starts')
plt.xlabel('Year')
plt.ylabel('Units')
plt.grid(True, alpha=0.5)
plt.legend()

plt.subplot(4, 3, 8)
plt.plot(existing_home_sales, label='Existing Home Sales', color=economic_activity_colors['Existing Home Sales'])
plt.title('Existing Home Sales')
plt.xlabel('Year')
plt.ylabel('Millions of Units')
plt.grid(True, alpha=0.5)
plt.legend()

# Consumer Spending
plt.subplot(4, 3, 9)
plt.plot(retail_sales, label='Retail Sales', color=economic_activity_colors['Retail Sales'])
plt.title('Retail Sales')
plt.xlabel('Year')
plt.ylabel('Millions of Dollars')
plt.grid(True, alpha=0.5)
plt.legend()

# Manufacturing and Industry
plt.subplot(4, 3, 10)
plt.plot(industrial_production, label='Industrial Production', color=economic_activity_colors['Industrial Production'])
plt.title('Industrial Production Index')
plt.xlabel('Year')
plt.ylabel('Index')
plt.grid(True, alpha=0.5)
plt.legend()

plt.subplot(4, 3, 11)
plt.plot(durable_goods_orders, label='Durable Goods Orders', color=economic_activity_colors['Durable Goods Orders'])
plt.title('Durable Goods Orders')
plt.xlabel('Year')
plt.ylabel('Millions of Dollars')
plt.grid(True, alpha=0.5)
plt.legend()

plt.subplot(4, 3, 12)
plt.plot(trade_balance, label='Trade Balance', color=economic_activity_colors['Trade Balance'])
plt.title('Trade Balance')
plt.xlabel('Year')
plt.ylabel('Millions of Dollars')
plt.grid(True, alpha=0.5)
plt.legend()

plt.tight_layout(pad=3.0)
plt.show()