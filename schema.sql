DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions(
	ID INT NOT NULL PRIMARY KEY,
	type TEXT NOT NULL, 
	sequence INT NOT NULL, 
	product_id TEXT NOT NULL, 
	price FLOAT NOT NULL, 
	open_24h FLOAT NOT NULL, 
	volume_24h FLOAT NOT NULL, 
	low_24h FLOAT NOT NULL, 
	high_24h FLOAT NOT NULL, 
	volume_30d FLOAT NOT NULL, 
	best_bid FLOAT NOT NULL, 
	best_ask FLOAT NOT NULL, 
	side TEXT NOT NULL, 
	time TEXT, 
	trade_id INT NOT NULL, 
	last_size FLOAT NOT NULL
);