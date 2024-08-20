-- SQLite
-- INSERT INTO people (Nama,Umur,Pekerjaan) VALUES ('Mike',25,'login'),('Nadzib',100,'Jual beli rudal');
INSERT INTO users (Username,Password) VALUES ('nadzib','admin#1234');
SELECT * FROM users;
DELETE FROM users WHERE ID IN (2);