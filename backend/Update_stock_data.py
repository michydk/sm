import sqlite3
import datetime
import yfinance as yf
from scw_serverless import Serverless
import boto3

#https://stocks.s3.nl-ams.scw.cloud/stock.db

REGION = "fr-par"
S3_URL = "https://s3.nl-ams.scw.cloud"

def handle(event, context):

s3 = boto3.client(
        "s3",
        region_name=REGION,
        use_ssl=True,
        endpoint_url=S3_URL,
        aws_access_key_id=SCW_ACCESS_KEY,
        aws_secret_access_key=SCW_SECRET_KEY,
    )

logging.info(f"Uploading to {BUCKET_NAME}/{name}")
    s3.put_object(Bucket=BUCKET_NAME, Key=name, Body=target.value)

    return {"statusCode": 200, "body": f"Successfully uploaded {name} to bucket!"}




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
