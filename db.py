import enum
import random
import sqlite3

db = sqlite3.connect('dogetrade.db')
db.row_factory = sqlite3.Row

class OrderType(enum.IntEnum):
	BUY = 1
	SELL = 2

def main():
	with db:
		cur = db.execute('SELECT COUNT(*) FROM stocks')
		[[count]] = cur.fetchall()
		if count == 0:
			print('found 0 stocks; seeding stocks')
			db.executemany('INSERT INTO stocks (ticker, name) VALUES(?, ?)', [
				('LABR', 'Retriever Technologies'),
				('GESH', 'Shepherd Enterprises'),
				('GOLD', 'Retriever Logistics'),
				('FREN', 'Bulldog Entertainment'),
				('POOD', 'Poodle Enterprises'),
				('BGLE', 'Beagle Enterprises'),
				('ROWE', 'Rottweiler and Rottweiler'),
				('WLSH', 'Corgi Entertainment'),
				('DACH', 'Dachshund Enterprises'),
				('YORK', 'Terrier Enterprises'),
			])
			for stock in db.execute('SELECT * FROM stocks'):
				price = random.randint(100000, 1000000)
				print('picking %.2f🍖 for %s (%s)' % (price / 10000, stock['ticker'], stock['name']))
				db.executemany('INSERT INTO orders (stock_id, type, price, num_shares) VALUES (?, ?, ?, ?)', [
					(stock['stock_id'], OrderType.BUY, price - 100, 1),
					(stock['stock_id'], OrderType.BUY, price - 200, 5),
					(stock['stock_id'], OrderType.BUY, price - 300, 10),
					(stock['stock_id'], OrderType.SELL, price + 100, 1),
					(stock['stock_id'], OrderType.SELL, price + 200, 5),
					(stock['stock_id'], OrderType.SELL, price + 300, 10),
				])
		else:
			print('found', count, 'stocks; doing nothing')

if __name__ == '__main__':
	main()
