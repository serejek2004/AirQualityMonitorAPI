CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(80) UNIQUE NOT NULL,
    password_hash VARCHAR(500) NOT NULL,
    co2_max INTEGER NOT NULL DEFAULT 0,
    co2_min INTEGER NOT NULL DEFAULT 0,
    temperature_max INTEGER NOT NULL DEFAULT 0,
    temperature_min INTEGER NOT NULL DEFAULT 0,
    humidity_max INTEGER NOT NULL DEFAULT 0,
    humidity_min INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS monitors (
    id SERIAL PRIMARY KEY,
    co2 INTEGER NOT NULL DEFAULT 0,
    temperature INTEGER NOT NULL DEFAULT 0,
    humidity INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE monitor_users (
    users_id INTEGER,
    monitors_id INTEGER,
    PRIMARY KEY (users_id, monitors_id),
    FOREIGN KEY (users_id) REFERENCES users(id),
    FOREIGN KEY (monitors_id) REFERENCES monitors(id)
);