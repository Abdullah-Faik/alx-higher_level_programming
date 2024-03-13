--create user
CREATE USER IF NOT EXIST 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';