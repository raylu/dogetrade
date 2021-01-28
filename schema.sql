CREATE TABLE IF NOT EXISTS stocks (
	stock_id INTEGER PRIMARY KEY,
	ticker TEXT,
	name TEXT
);

CREATE TABLE IF NOT EXISTS users (
	user_id INTEGER PRIMARY KEY,
	username TEXT
);

CREATE TABLE IF NOT EXISTS orders (
	order_id INTEGER PRIMARY KEY,
	stock_id INTEGER,
	user_id INTEGER,
	type INTEGER,
	price INTEGER,
	num_shares INTEGER,
	FOREIGN KEY(stock_id) REFERENCES stocks(stock_id),
	FOREIGN KEY(user_id) REFERENCES users(user_id)
);

CREATE INDEX IF NOT EXISTS idx_orders_stock_type ON orders (stock_id, type);
CREATE INDEX IF NOT EXISTS idx_orders_users ON orders (user_id);
