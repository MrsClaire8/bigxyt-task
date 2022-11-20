import pandas as pd
import sqlite3

df = pd.DataFrame(
    columns=['Id', 'Order', 'Type', 'Price', 'Quantity']
    )

def create_table():
    conn=sqlite3.connect('data.db')
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS transactions (Id TEXT, 'Order' TEXT, Type TEXT, Price REAL, Quantity REAL)")
    conn.commit()
    conn.close()

def df_to_sql():
    database = "../transactions.sqlite"
    conn = sqlite3.connect('data.db')
    df.to_sql(name='transactions', con=conn, if_exists='replace')
    conn.close()

def sum ():
    create_table()
    global df

    id = []
    order = []
    type = []
    price = []
    quantity = []

    tran_type = input ("Do you want to add (type 'a') or remove (type 'r') transaction? ")

    if tran_type == "a":

        id_count = str(len(df.index)+1).zfill(3)
        id.append(id_count)

        type.append("Add")

        order_type = input ("Do you want to buy (type 'b') or sell (type 's') shares? ")

        if order_type == "b":
            order.append("Buy")
            buy_shares_price = int (input ("Please type the price: "))
            price.append(buy_shares_price)
            buy_shares_quantity = int (input ("Please type the quantity: "))
            quantity.append(buy_shares_quantity)
            print("You just bought " + str(buy_shares_quantity) + " shares at " + str(buy_shares_price) + " each. Worth is: " + str(buy_shares_price*buy_shares_quantity))

        elif order_type == "s":
            order.append("Sell")
            sell_shares_price = int (input ("Please type the price: "))
            price.append(sell_shares_price)
            sell_shares_quantity = int (input ("Please type the quantity: "))
            quantity.append(sell_shares_quantity)
            print("You just sold " + str(sell_shares_quantity) + " shares at " + str(sell_shares_price) + " each. Worth is: " + str(sell_shares_price*sell_shares_quantity))
        else: 
            print("Error occured. Try again.")
    
    elif tran_type == "r":
        type.append("Remove")
        print(df)
        remove = int(input("Please type index of transaction to remove: "))
        id_remove = str(remove+1).zfill(3)
        id.append(id_remove)
        order.append(df.iloc[remove,1])
        price.append(df.iloc[remove,3])
        quantity.append(df.iloc[remove,4])
        
    else: 
        print("Error occured. Try again.")

    transactions = zip(id, order, type, price, quantity)

    for transaction in transactions:
        temporary_df = pd.DataFrame([transaction], columns=['Id', 'Order', 'Type', 'Price', 'Quantity'])
        df = df.append(temporary_df, ignore_index=True)
    
    df_to_sql()
    print(df)

while(True):
    sum()
