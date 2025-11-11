import pandas as pd
from sqlalchemy import create_engine

def main():
	sales_df = pd.read_csv('../data/processed/sales.csv')
	customers_df = pd.read_csv('../data/processed/customers.csv')
	products_df = pd.read_csv('../data/processed/products.csv')
	countries_df = pd.read_csv('../data/processed/countries.csv')

	engine = create_engine('sqlite:///../data/warehouse/online_retail.db')

	sales_df.to_sql('sales', con=engine, if_exists='replace', index=False)
	customers_df.to_sql('customers', con=engine, if_exists='replace', index=False)
	products_df.to_sql('products', con=engine, if_exists='replace', index=False)
	countries_df.to_sql('countries', con=engine, if_exists='replace', index=False)

	print ("ETL process completed successfully.")

if __name__ == "__main__":
	main()