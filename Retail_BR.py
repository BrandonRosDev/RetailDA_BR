import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

PATH = 'retail_store_sales.csv'
df = pd.read_csv(PATH)
print("Path to dataset csv:", PATH)

df = pd.read_csv("/kaggle/input/retail-store-sales-dirty-for-data-cleaning/retail_store_sales.csv")


#Overview
df.head()

print("Shape:", df.shape)
print("Columns:", df.columns)
df.info()


#Removing duplicates
df.drop_duplicates(inplace=True)



#Adjusting data types for columns

#Quantity is decimal when it should be numeric. Any errors in this conversion will be set to NAN since you can buy a portion of an item.
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')


#Checking empty counts by col
df.isnull().sum()


#Item has a high empty count
missing_items_df = df[df['Item'].isnull()]
missing_items_df.head()


#Discount Applied checks
missing_discount_df = df[df["Discount Applied"].isnull()]
missing_discount_df.head()


discount_unique_values = df["Discount Applied"].unique()
print(discount_unique_values)


#Checking a missing dicount to see if true or false is nan
discount_df_check = df[df["Item"] == "Item_16_BEV"]
discount_df_check.head()


#Removing Null rows from 'Item'
df.dropna(subset=['Item'], inplace=True)

df.head()


#Checking again empty counts by col
df.isnull().sum()


#Category check:
df["Category"].unique()


#Payment Method check:
df["Payment Method"].unique()


#Location check:
df["Location"].unique()


# Summary statistics
df.info()
df.describe()




#Online vs In store Viz
sales_by_location_type = df.groupby('Location')['Total Spent'].sum()
sales_by_location_type.plot(kind='bar', title='In-Store vs Online Revenue', color='lightseagreen')
plt.xlabel('Location Type')
plt.ylabel('Revenue')
plt.show()


#Looking into payment method by usage Viz
payment_counts = df['Payment Method'].value_counts()

payment_counts.plot(kind='pie',autopct='%1.1f%%', title='Payment Method Breakdown By Usage')
plt.ylabel('')#gets rid of "count" over the Credit Card label
plt.show()




#Daily Total Sales Viz line
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
daily_sales = df.groupby(df['Transaction Date'].dt.month)['Total Spent'].sum()

daily_sales.plot(kind='line', title='Daily Total Sales')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.show()


#Checking revenue per the top ten retail categories for store Viz bar horiz
top_categories = df.groupby('Category')['Total Spent'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(8,6))
top_categories.plot(kind='barh', color='lightseagreen')
plt.title('Top 10 Categories by Revenue')
plt.xlabel('Total Revenue')
plt.tight_layout()
plt.show()





