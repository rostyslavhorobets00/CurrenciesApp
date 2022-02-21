import ccxt
import datetime
import asyncio

from sqlalchemy import  String, MetaData, Table, Integer, Column, create_engine


#Creation DataBase table using SQLAlchemy
engine = create_engine('sqlite:///currencies.db', echo=True)
meta = MetaData()
currencies = Table(
        'currencies', meta,
        Column('id',Integer, primary_key=True, autoincrement=True),
        Column('currency', String),
        Column('price', Integer),
        Column('date_', Integer)
    )


#meta.create_all(engine)   
connection = engine.connect()

#Adding Data to DataBase:
"""
connection.execute(currencies.insert(), [
   {'currency':'BTC', 'price' : '38388,58', 'date_' : 1645384382005 },
   {'currency':'ETH','price' : '2663,1', 'date_' : 1645384382005 },
   {'currency':'ADA','price' : '0,96', 'date_' : 1645384382005 },
   {'currency':'BNB','price' : '387,55127252', 'date_' : 1645384382005 },
   {'currency':'XRP','price' : '0,80602643', 'date_' : 1645384382005 }
   
])
"""
#Displaying Data from DataBase
async def oldDataBase():
    data = currencies.select()
    result = connection.execute(data)
    for row in result:
        print (row)

asyncio.run(oldDataBase())

#Updating Data in DataBase using ccxt library and datetime library
async def updateDataBase():
    lst = ['BTC', 'ETH', 'ADA', 'BNB', 'XRP']
    for i in lst:
        exchange = ccxt.kucoin()
        ticker = exchange.fetch_ticker(f'{i}/USDT')
        connection.execute(currencies.update().where(currencies.c.currency == i).values(price = exchange.last_json_response.get('data').get('averagePrice'),
        date_ = datetime.datetime.fromtimestamp(exchange.last_json_response.get('data').get('time')/1000)))
asyncio.run(updateDataBase())

#Displaying updeted Data from DataBase
async def updatedDataBase():
    data = currencies.select()
    result = connection.execute(data)
    for row in result:
        print (row)

asyncio.run(updatedDataBase())


