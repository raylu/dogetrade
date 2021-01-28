import sqlite3

db = sqlite3.connect('dogetrade.db')
db.row_factory = sqlite3.Row

if __name__ == '__main__':
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
		else:
			print('found', count, 'stocks; doing nothing')
