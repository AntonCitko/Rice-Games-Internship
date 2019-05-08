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

SELECT * FROM payment;
SELECT * FROM members;

SELECT p.member_id, p.amount, m.name, p.payday, m.role, p.memo FROM payment p, members m
WHERE p.member_id = m.member_id;















