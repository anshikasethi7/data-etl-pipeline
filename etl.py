import pandas as pd
import sqlalchemy


df = pd.read_csv("data/sales_data.csv")

df['Date'] = pd.to_datetime(df['Date'])
df['Total'] = df['Quantity'] * df['Price']
df['Customer'] = df['Customer'].str.title()
df.fillna({"Quantity": 0, "Price": 0}, inplace=True)

print("Preview of Cleaned Data:")
print(df.head())

engine = sqlalchemy.create_engine("sqlite:///sales.db")
df.to_sql("sales_table", con=engine, if_exists="replace", index=False)

print("Data loaded into sales.db successfully!")
