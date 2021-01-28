CREATE TABLE IF NOT EXISTS stocks (
	stock_id INTEGER PRIMARY KEY,
	ticker TEXT NOT NULL,
	name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
	user_id INTEGER PRIMARY KEY,
	username TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
	order_id INTEGER PRIMARY KEY,
	stock_id INTEGER NOT NULL,
	user_id INTEGER,
	type INTEGER NOT NULL,
	price INTEGER NOT NULL,
	num_shares INTEGER NOT NULL,
	FOREIGN KEY(stock_id) REFERENCES stocks(stock_id),
	FOREIGN KEY(user_id) REFERENCES users(user_id)
);

CREATE INDEX IF NOT EXISTS idx_orders_stock_type ON orders (stock_id, type);
CREATE INDEX IF NOT EXISTS idx_orders_users ON orders (user_id);
