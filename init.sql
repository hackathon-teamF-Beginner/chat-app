DROP DATABASE if exists chatapp;
DROP USER if exists 'testuser'@'localhost';

SET GLOBAL validate_password.policy=LOW; 

CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp;
USE chatapp;
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser'@'localhost';



CREATE TABLE users (
    uid varchar(255) PRIMARY KEY,
    user_name varchar(255) UNIQUE NOT NULL,
    email varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL
);

CREATE TABLE channels (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES users(uid),
    name varchar(255) UNIQUE NOT NULL,
    abstract varchar(255)
);

CREATE TABLE messages (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES users(uid),
    cid integer REFERENCES channels(id) ON DELETE CASCADE,
    message text,
    contri_time text,
    created_at timestamp not null default current_timestamp
);

INSERT INTO users(uid, user_name, email, password)VALUES('970af84c-dd40-47ff-af23-282b72b7cca8','テスト','test@gmail.com','37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578');
INSERT INTO channels(id, uid, name, abstract)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8','秘密の部屋','最初からある部屋です。');
INSERT INTO messages(id, uid, cid, message)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', 'どんどん送信してください');
INSERT INTO messages(id, uid, cid, message)VALUES(2, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', 'テスト送信１');
INSERT INTO messages(id, uid, cid, message)VALUES(3, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', 'テスト送信２');