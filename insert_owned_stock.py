import sqlite3
import sys

if len(sys.argv) != 7:
  count = str(len(sys.argv))
  sys.exit("Not 6 args (foundt " + count + "), syntax is: 'Name' 'BuyDate' 'Ticker' 'BuyIndex' 'CurrencyId' 'Amount'")
ca_name = str(sys.argv[1])
ca_buydate = str(sys.argv[2])
ca_ticker = str(sys.argv[3])
ca_buyindex = str(sys.argv[4])
ca_currencyid = str(sys.argv[5])
ca_amount = str(sys.argv[6])

insert = """INSERT INTO OwnedStocks (Name,BuyDate,Ticker,BuyIndex,CurrencyId,Amount) VALUES (?, ?, ?, ?, ?, ?); """
insert_values = (ca_name, ca_buydate, ca_ticker, ca_buyindex, ca_currencyid, ca_amount)

con = sqlite3.connect("stock.db")
cur = con.cursor()
cur.execute(insert, insert_values)
con.commit()
