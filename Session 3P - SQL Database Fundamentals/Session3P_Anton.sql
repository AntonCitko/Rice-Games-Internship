CREATE SCHEMA IF NOT EXISTS ricegames;
USE ricegames;

CREATE TABLE IF NOT EXISTS members (
	member_id int NOT NULL AUTO_INCREMENT,
    name varchar(45),
    role varchar(45),
    PRIMARY KEY (member_id)
);

CREATE TABLE IF NOT EXISTS payment (
	payment_id int NOT NULL AUTO_INCREMENT,
    member_id int NOT NULL,
    payday date,
    recipient varchar(45),
    amount varchar(45),
    memo varchar(90),
    PRIMARY KEY (payment_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

INSERT INTO members (name, role)
VALUES
	('Julian Rice', 'Lead Developer'),
    ('Emily Keohane', 'Artist'),
    ('William Lajousky', 'Artist'),
    ('Rachel Riedel', 'Artist'),
    ('Jonas Müller', 'Artist'),
    ('Brian LaGuardia', 'Composer'),
    ('Mikkel Cloud', 'Composer'),
    ('Robert Mullis', 'Composer');

SELECT * FROM members;
SELECT name FROM members;
SELECT DISTINCT role FROM members;

INSERT INTO payment (member_id, payday, recipient, amount, memo)
VALUES
	(
		2,
		'2018-01-31',
		'Emily',
		130,
		'Shu Final Render + Expressions'
	),
    (
		3,
		'2018-02-07',
		'William',
		130,
		'Jin Final Render + Expressions'
    ),
    (
		4,
		'2018-01-30',
		'Rachel',
		130,
		'Kou Final Render + Expressions'
    ),
    (
		6,
		'2018-02-26',
		'Brian',
		60,
		'March Payment 2019'
    ),
    (
		7,
		'2018-02-26',
		'MikkelCloud',
		50,
		'March Payment 2019'
    ),
    (
		8,
		'2018-02-26',
		'Robert',
		50,
		'March Payment 2019'
    ),
    (
		5,
		'2018-03-24',
		'Jonas',
		72,
		'Decorations 1B'
    ),
    (
		5,
		'2018-04-07',
		'Jonas',
		120,
		'Backgrounds 1A'
    );

SELECT * FROM payment;

ALTER TABLE members
ADD COLUMN total int;

INSERT INTO members
SELECT member_id, SUM(amount) AS total FROM payment
GROUP BY member_id;

UPDATE members m
SET total = (SELECT SUM(amount) AS total FROM payment p
WHERE p.member_id = m.member_id);

INSERT INTO payment (member_id, payday, recipient, amount, memo)
VALUES
    (
		6,
		'2018-04-09',
		'Brian',
		60,
		'April Payment 2019'
    ),
    (
		7,
		'2018-04-09',
		'MikkelCloud',
		50,
		'April Payment 2019'
    ),
    (
		8,
		'2018-04-09',
		'Robert',
		50,
		'April Payment 2019'
    );
    
UPDATE members m
SET total = (SELECT SUM(amount) AS total FROM payment p
WHERE p.member_id = m.member_id);

SELECT * FROM payment;
SELECT * FROM members;

SELECT p.member_id, p.amount, m.name, p.payday, m.role, p.memo FROM payment p, members m
WHERE p.member_id = m.member_id;

SELECT role AS Role, SUM(total) AS `Total Paid` FROM members
WHERE Role = 'Artist';

SELECT role AS Role, SUM(total) AS `Total Paid` FROM members
WHERE Role = 'Composer';

SELECT name as Name,
	CASE
		WHEN total >= 150 THEN 'Paid Lots'
        WHEN total >= 120 AND total < 150 THEN 'Paid Well'
        WHEN total >= 100 AND total < 120  THEN 'Needs More'
        ELSE 'Neds Way More'
	END AS `Money Status`
FROM members;

CREATE TABLE IF NOT EXISTS sanrin_enemies (
	id int NOT NULL AUTO_INCREMENT,
    name varchar(15) UNIQUE,
    eng_name varchar(15) UNIQUE,
    hp int NOT NULL,
    attack int NOT NULL,
    weakness1 varchar(4) NOT NULL,
    weakness2 varchar(4) DEFAULT '',
    weakness3 varchar(4) DEFAULT '',
    weakness4 varchar(4) DEFAULT '',
    PRIMARY KEY (id)
);

INSERT INTO sanrin_enemies (id, name, eng_name, hp, attack, weakness1, weakness2, weakness3, weakness4)
VALUES
	(1, 'ari', 'ant', 3, 2, 'a', 'ri', DEFAULT, DEFAULT),
    (2, 'imori', 'salamander', 4, 2, 'i', 'mo', 'ri', DEFAULT),
    (3, 'uzura', 'quail', 6, 1, 'u', 'zu', 'ra', DEFAULT),
    (4, 'kaeru', 'frog', 4, 2, 'ka', 'e', 'ru', DEFAULT),
    (5, 'oni', 'demon', 8, 4, 'o', 'ni', DEFAULT, DEFAULT),
    (6, 'mokuoni', 'wood demon', 30, 6, 'mo', 'ku', 'o', 'ni');

SELECT * FROM sanrin_enemies;

SELECT name, eng_name,
	CASE
		WHEN hp > 10 THEN 'BOSS'
        ELSE 'ZAKO'
	END AS type
FROM sanrin_enemies
ORDER BY type DESC;

SELECT name, eng_name, hp, attack
FROM sanrin_enemies
ORDER BY attack;

SELECT name, eng_name, hp, attack
FROM sanrin_enemies
ORDER BY hp;








