import sqlite3
con = sqlite3.connect("stock.db")
cur = con.cursor()
cur.execute("CREATE TABLE OwnedStocks(Name, BuyDate,Ticker,BuyIndex, CurrencyId, Amount)")
