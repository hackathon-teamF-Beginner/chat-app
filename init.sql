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

CREATE TABLE M_USER (
    id varchar(255) PRIMARY KEY,
    user_name varchar(100) UNIQUE NOT NULL,
    email varchar(255) UNIQUE NOT NULL,
    password varchar(30) NOT NULL
);

CREATE TABLE T_CHANNEL (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES M_USER(id),
    name varchar(255) UNIQUE NOT NULL,
    abstract varchar(255),
    passport text
);

CREATE TABLE T_USER_MESSAGE (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES M_USER(id),
    cid integer REFERENCES T_CHANNEL(id) ON DELETE CASCADE,
    mid varchar(255) REFERENCES T_MESSAGE(id)
);

CREATE TABLE T_MESSAGE (
    id serial PRIMARY KEY,
    message_contents text,
    send_at text,
    rid varchar(255) REFERENCES T_REACTION(id)
);

CREATE TABLE T_REACTION (
    id serial PRIMARY KEY,
    reaction_code varchar(255)
);

CREATE TABLE M_REACTION (
    reaction_code serial PRIMARY KEY,
    reaction_name text,
    thumbnail_path text
);

INSERT INTO users(uid, user_name, email, password)VALUES('970af84c-dd40-47ff-af23-282b72b7cca8','テスト','test@gmail.com','37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578');
INSERT INTO channels(id, uid, name, abstract)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8','秘密の部屋','最初からある部屋です。');
INSERT INTO messages(id, uid, cid, message)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', 'どんどん送信してください');
INSERT INTO messages(id, uid, cid, message)VALUES(2, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', 'テスト送信１');
INSERT INTO messages(id, uid, cid, message)VALUES(3, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', 'テスト送信２');