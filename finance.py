import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data Loading
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print("Error: ", str(e))

# Data Cleaning
def clean_data(data):
    try:
        data.dropna(inplace=True)  # Remove rows with missing values
        data.drop_duplicates(inplace=True)  # Remove duplicate rows
        return data
    except Exception as e:
        print("Error: ", str(e))

# Exploratory Data Analysis
def perform_eda(data):
    try:
        # Calculate key metrics
        total_market_cap = data['Mar Cap - Crore'].sum()
        total_sales = data['Sales Qtr - Crore'].sum()
        average_market_cap = data['Mar Cap - Crore'].mean()
        average_sales = data['Sales Qtr - Crore'].mean()

        # Print key metrics
        print('Total Market Capitalization: ', total_market_cap)
        print('Total Sales: ', total_sales)
        print('Average Market Capitalization: ', average_market_cap)
        print('Average Sales: ', average_sales)

        # Plot market capitalization distribution
        plt.figure(figsize=(10,6))
        sns.distplot(data['Mar Cap - Crore'])
        plt.title('Market Capitalization Distribution')
        plt.xlabel('Market Capitalization (Crores)')
        plt.ylabel('Frequency')
        plt.show()

        # Plot sales distribution
        plt.figure(figsize=(10,6))
        sns.distplot(data['Sales Qtr - Crore'])
        plt.title('Sales Distribution')
        plt.xlabel('Sales (Crores)')
        plt.ylabel('Frequency')
        plt.show()

        # Plot market capitalization vs sales
        plt.figure(figsize=(10,6))
        sns.scatterplot(x='Mar Cap - Crore', y='Sales Qtr - Crore', data=data)
        plt.title('Market Capitalization vs Sales')
        plt.xlabel('Market Capitalization (Crores)')
        plt.ylabel('Sales (Crores)')
        plt.show()

        # Calculate correlation between market capitalization and sales
        correlation = data[['Mar Cap - Crore', 'Sales Qtr - Crore']].corr()
        print('Correlation between Market Capitalization and Sales: ', correlation)

    except Exception as e:
        print("Error: ", str(e))

# Main function
def main():
    file_path = 'Financial Analytics data.csv'
    data = load_data(file_path)

    if data is not None:
        data = clean_data(data)
        perform_eda(data)

if __name__ == "__main__":
    main()