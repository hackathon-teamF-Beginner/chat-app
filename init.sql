DROP DATABASE if exists chatapp;
DROP USER if exists 'testuser'@'localhost';

SET GLOBAL validate_password.policy=LOW;

CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testuser';
CREATE DATABASE chatapp DEFAULT CHARACTER SET utf8mb4;
USE chatapp;
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser'@'localhost';

CREATE TABLE M_USER (
    id varchar(255) PRIMARY KEY,
    user_name varchar(100) UNIQUE NOT NULL,
    email varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL
);

CREATE TABLE T_CHANNEL (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES M_USER(id),
    name varchar(255) UNIQUE NOT NULL,
    abstract varchar(255)
);

CREATE TABLE T_USER_CHANNEL (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES M_USER(id),
    cid integer REFERENCES T_CHANNEL(id) ON DELETE CASCADE,
    delete_privilege boolean
);

CREATE TABLE T_MESSAGE (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES M_USER(id),
    cid integer REFERENCES T_CHANNEL(id) ON DELETE CASCADE,
    message_contents text,
    send_at text
);

CREATE TABLE T_REACTION (
    id serial PRIMARY KEY,
    mid integer REFERENCES T_MESSAGE(id) ON DELETE CASCADE,
    uid varchar(255) REFERENCES M_USER(id),
    reaction_code varchar(255)
);

CREATE TABLE M_REACTION (
    id serial PRIMARY KEY,
    reaction_name text,
    file_path text
);

INSERT INTO M_USER(id, user_name, email, password)VALUES('970af84c-dd40-47ff-af23-282b72b7cca8','テスト','test@gmail.com','37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578');
INSERT INTO T_CHANNEL (id, uid, name, abstract)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8','秘密の部屋','最初からある部屋です。');
INSERT INTO T_MESSAGE(id, uid, cid, message_contents)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', 'どんどん送信してください');
INSERT INTO T_MESSAGE(id, uid, cid, message_contents)VALUES(2, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', 'テスト送信１');
INSERT INTO T_MESSAGE(id, uid, cid, message_contents)VALUES(3, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', 'テスト送信２');

INSERT INTO M_REACTION(id, reaction_name, file_path)VALUES(1, 'good', '../static/reaction_icons/good.png');
INSERT INTO M_REACTION(id, reaction_name, file_path)VALUES(2, 'look', '../static/reaction_icons/look.png');
INSERT INTO M_REACTION(id, reaction_name, file_path)VALUES(3, 'love', '../static/reaction_icons/love.png');
INSERT INTO M_REACTION(id, reaction_name, file_path)VALUES(4, 'pray', '../static/reaction_icons/pray.png');
INSERT INTO M_REACTION(id, reaction_name, file_path)VALUES(5, 'smile', '../static/reaction_icons/smile.png');


