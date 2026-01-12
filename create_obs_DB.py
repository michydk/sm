import sqlite3
con = sqlite3.connect("stock.db")
cur = con.cursor()
cur.execute("CREATE TABLE ObsStocks(Name,Ticker,BuyTarget,CurrencyId,Lables,Comment)")
