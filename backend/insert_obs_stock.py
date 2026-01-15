import sqlite3
import sys
from datetime import datetime

if len(sys.argv) != 7:
  count = str(len(sys.argv))
  sys.exit("Not 6 args (foundt " + count + "), syntax is: 'Name' 'Ticker' 'BuyTarget' 'CurrencyId' 'Lables' 'Comment'")
ca_name = str(sys.argv[1])
ca_ticker = str(sys.argv[2])
ca_buytaget = str(sys.argv[3])
ca_currencyid = str(sys.argv[4])
ca_lables = str(sys.argv[5])
ca_comment = str(sys.argv[6])
ca_today = datetime.today().strftime('%Y-%m-%d')

insert = """INSERT INTO ObsStocks (Name,Ticker,BuyTarget,CurrencyId,Lables,Comment,Evaluated) VALUES (?, ?, ?, ?, ?, ?, ?); """
insert_values = (ca_name, ca_ticker, ca_buytaget, ca_currencyid, ca_lables, ca_comment, ca_today)

con = sqlite3.connect("stock.db")
cur = con.cursor()
cur.execute(insert, insert_values)
con.commit()
