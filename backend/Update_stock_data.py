import sqlite3
import datetime
import yfinance as yf

tickercon = sqlite3.connect("stock.db")
tickercur = tickercon.cursor()
for row in tickercur.execute('select distinct Ticker From OwnedStocks;'):
        print(row[0])
        dat = yf.Ticker(row[0])
        price2 = dat.info['currentPrice']
        right_now = datetime.datetime.now()
        print(price2)
        print ("---")


        update = """UPDATE Stockdata SET timestamp = ?, price = ? WHERE Ticker = ?; """
        update_values = (right_now, price2, row[0])

        con = sqlite3.connect("data.db")
        cur = con.cursor()
        cur.execute(update, update_values)
        con.commit()
        print ("-----------------------------------------")
