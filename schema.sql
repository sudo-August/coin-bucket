DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions(
	id SERIAL NOT NULL PRIMARY KEY,
	type TEXT NOT NULL, 
	sequence INT NOT NULL, 
	product_id TEXT NOT NULL, 
	price TEXT NOT NULL, 
	open_24h TEXT NOT NULL, 
	volume_24h TEXT NOT NULL, 
	low_24h TEXT NOT NULL, 
	high_24h TEXT NOT NULL, 
	volume_30d TEXT NOT NULL, 
	best_bid TEXT NOT NULL, 
	best_ask TEXT NOT NULL, 
	side TEXT NOT NULL, 
	time TEXT, 
	trade_id INT NOT NULL, 
	last_size TEXT NOT NULL
);