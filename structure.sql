BEGIN TRANSACTION;
CREATE TABLE "websites" (
    `id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    `domain_name`	INTEGER UNIQUE,
    `lastup`	INTEGER,
    `is_down`	INTEGER,
    `insert_time`	INTEGER
);
CREATE TABLE "users" (
    `telegram_id`    INTEGER PRIMARY KEY UNIQUE,
    `telegram_name`	TEXT,
    `insert_time`	INTEGER
);
CREATE TABLE "users_websites" (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    `websites_id`   INTEGER,
    `telegram_id`   INTEGER,
    `insert_time` INTEGER
);
CREATE TABLE "history" (
    `id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    `lastup`	INTEGER,
    `downtime`	INTEGER,
    `insert_time`	INTEGER
);
CREATE TABLE "commands" (
    `id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    `users_id`	INTEGER,
    `commands`	TEXT,
    `insert_time`	INTEGER
);
CREATE TABLE `admin` (
    `id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    `name`	TEXT,
    `users_id`	INTEGER
);
COMMIT;
