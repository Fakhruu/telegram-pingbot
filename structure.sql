BEGIN TRANSACTION;
CREATE TABLE "websites" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`domain_name`	INTEGER UNIQUE,
	`lastup`	INTEGER,
	`is_down`	INTEGER,
	`insert_time`	INTEGER
);
CREATE TABLE "users" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`telegram_id`	INTEGER UNIQUE,
	`telegram_name`	BLOB,
	`web_id`	INTEGER,
	`insert_time`	INTEGER
);
CREATE TABLE "history" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`lastup`	INTEGER,
	`downtime`	INTEGER,
	`insert_time`	INTEGER
);
CREATE TABLE "commands" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`user_id`	INTEGER,
	`commands`	TEXT,
	`insert_time`	INTEGER
);
CREATE TABLE `admin` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT,
	`telegram_id`	INTEGER
);
COMMIT;
