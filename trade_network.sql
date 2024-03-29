DROP DATABASE IF EXISTS trade_network;
CREATE SCHEMA trade_network;
USE trade_network;

DROP TABLE IF EXISTS SHOP ;
CREATE TABLE SHOP
(
	State_Code	INT	NOT NULL,
	Pan_Card_No VARCHAR(15)	NOT NULL,
	Random_No VARCHAR(4)	NOT NULL,
	Name	VARCHAR(100)	NOT NULL,
	Location VARCHAR(200)	NOT NULL,
	PRIMARY KEY(Location),
	UNIQUE(State_Code,Pan_Card_No,Random_No)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

LOCK TABLES SHOP WRITE;
/*insert data to table here that is write insert querries here*/;
INSERT INTO SHOP VALUES
('01','ABCDE1234F','1A5','RAM TRADERS','SHOP NO. 1 ANDHERI NAGRI DELHI'),
('01','GHIJK5678C','2A5','SHAM TRADERS','SHOP NO. 2 MODEL TOWN NAGPUR'),
('02','MNOPQ9101R','3A5','MUKESH TRADERS','SHOP NO. 3 NEAR IIIT-H'),
('19','AHODE1234F','4B6','SURESH TRADERS','SHOP NO. 3 NEAR FORTIS CHANDIGARH');
UNLOCK TABLES;

DROP TABLE IF EXISTS PERSON;
CREATE TABLE PERSON
(
	Aadhar_No	CHAR(12)	NOT NULL,
	Name 		VARCHAR(100) NOT NULL,
	Address		VARCHAR(200) NOT NULL,
	PRIMARY KEY (Aadhar_No)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

LOCK TABLES PERSON WRITE;
/*Insert data*/
INSERT INTO PERSON VALUES
	('123456789101','KALEEN BHAIYA','RKMKA NIWAS MIRZAPUR'),
	('123465112131','SHERLOCK HOLMES','221 B, BAKERS STREET'),
	('151617181920','TOKYO','MH-5, LONDON'),
	('212223242526','WATSON','221 B, BAKERS STREET'),
	('272829303132','MAQBOOL KHAN','MK NIWAS, MIRZAPUR'),
	('333435363738','RATI SHANKAR','RS NIWAS, JONPUR'),
	('394041424344','MUNNA BHAIYA','RNAID KAHAN MIRZAPUR'),
	('454647484950','JOHN WICK','JW ROOM NO. 5, CONTINENTAL GROUNDS');
UNLOCK TABLES;

DROP TABLE IF EXISTS S_EMPLOYEE;
CREATE TABLE S_EMPLOYEE
(
	Fk_Aad_No	CHAR(12)		NOT NULL,
	Fk_S		VARCHAR(200)	NOT NULL,
	Sup_Aad		CHAR(12),
	PRIMARY KEY (Fk_Aad_No),
	FOREIGN KEY (Fk_Aad_No) REFERENCES PERSON(Aadhar_No) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (Fk_S) REFERENCES SHOP(Location) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (Sup_Aad) REFERENCES S_EMPLOYEE(Fk_Aad_No) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

LOCK TABLES S_EMPLOYEE WRITE;
/*Insert data*/
INSERT INTO S_EMPLOYEE(Fk_Aad_No,Fk_S) VALUES
('123456789101','SHOP NO. 1 ANDHERI NAGRI DELHI'),
('454647484950','SHOP NO. 3 NEAR IIIT-H');
INSERT INTO S_EMPLOYEE VALUES('272829303132','SHOP NO. 1 ANDHERI NAGRI DELHI','123456789101');
UNLOCK TABLES;

DROP TABLE IF EXISTS INSURANCE_COMPANY;
CREATE TABLE INSURANCE_COMPANY
(
	Name 	VARCHAR(100)	NOT NULL,
	Cost	INT 	NOT NULL,
	PRIMARY KEY(Name)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

LOCK TABLES INSURANCE_COMPANY WRITE;
/*Insert Data*/
INSERT INTO INSURANCE_COMPANY VALUES
	('CLI','2'),
	('WEN','1');
UNLOCK TABLES;

DROP TABLE IF EXISTS CUSTOMERS;
CREATE TABLE CUSTOMERS
(
	Fk_Aad_No	CHAR(12)	NOT NULL,
	Fk_Insur	VARCHAR(100),
	PRIMARY KEY(Fk_Aad_No),
	FOREIGN KEY(Fk_Aad_No) REFERENCES PERSON(Aadhar_No) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(Fk_Insur) REFERENCES INSURANCE_COMPANY(Name) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

LOCK TABLES CUSTOMERS WRITE;
/*Insert data*/
INSERT INTO CUSTOMERS(Fk_Aad_No) VALUES('151617181920');
INSERT INTO CUSTOMERS VALUES('212223242526','CLI');
UNLOCK TABLES;

DROP TABLE IF EXISTS FACTORY;
CREATE TABLE FACTORY
(
	E_Mail		VARCHAR(200)	NOT NULL,
	Location 	VARCHAR(200)	NOT NULL,
	Fk_Own_Aad_No CHAR(12)		NOT NULL,
	PRIMARY KEY(E_Mail),
	UNIQUE(Location),
	FOREIGN KEY (Fk_Own_Aad_No) REFERENCES PERSON(Aadhar_No) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

LOCK TABLES FACTORY WRITE;
/*Insert Data*/
INSERT INTO FACTORY VALUES
	('kb@g.com','PLOT 1 MIRZAPUR','123456789101'),
	('mk@g.com','PLOT 2 MIRZAPUR','272829303132');
UNLOCK TABLES;

DROP TABLE IF EXISTS F_EMPLOYEE;
CREATE TABLE F_EMPLOYEE
(
	Fk_Aad_No	CHAR(12)		NOT NULL,
	Fk_F		VARCHAR(200)	NOT NULL,
	Sup_Aad		CHAR(12),
	PRIMARY KEY (Fk_Aad_No),
	FOREIGN KEY (Fk_Aad_No) REFERENCES PERSON(Aadhar_No) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (Fk_F) REFERENCES FACTORY(E_Mail) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (Sup_Aad) REFERENCES F_EMPLOYEE(Fk_Aad_No) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

LOCK TABLES F_EMPLOYEE WRITE;
/*Insert data*/
INSERT INTO F_EMPLOYEE(Fk_Aad_No,Fk_F) VALUES
	('123456789101','kb@g.com'),
	('272829303132','mk@g.com');
INSERT INTO F_EMPLOYEE VALUES('394041424344','kb@g.com','123456789101');
UNLOCK TABLES;

DROP TABLE IF EXISTS INSURED_VIA;
CREATE TABLE INSURED_VIA
(
	E_Aad	CHAR(12)	NOT NULL,
	F_Email 	VARCHAR(200)	NOT NULL,
	I_Name 		VARCHAR(100) 	NOT NULL,
	PRIMARY KEY(E_Aad,F_Email,I_Name),
	FOREIGN KEY(E_Aad) REFERENCES F_EMPLOYEE(Fk_Aad_No) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(F_Email) REFERENCES FACTORY(E_Mail) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(I_Name) REFERENCES INSURANCE_COMPANY(Name) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

LOCK TABLES INSURED_VIA WRITE;
/*Insert Data*/
INSERT INTO INSURED_VIA VALUES
	('394041424344','kb@g.com','WEN'),
	('123456789101','kb@g.com','CLI');
UNLOCK TABLES;

DROP TABLE IF EXISTS WORKS_ON;
CREATE TABLE WORKS_ON
(
Id 	VARCHAR(64)		NOT NULL,
Fk_Email	VARCHAR(200)	NOT NULL,
PRIMARY KEY(Id,Fk_Email),
FOREIGN KEY(Fk_Email) REFERENCES FACTORY(E_Mail) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

LOCK TABLES WORKS_ON WRITE;
/*Insert Data*/
INSERT INTO WORKS_ON VALUES
	('KTTON1','kb@g.com'),
	('AFEEM','mk@g.com'),
	('AFEEM1','mk@g.com');
UNLOCK TABLES;

DROP TABLE IF EXISTS COMMODITY;
CREATE TABLE COMMODITY
(
	Name 		VARCHAR(50)		NOT NULL,
	PRIMARY KEY(Name)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

LOCK TABLES COMMODITY WRITE;
/*insert data*/
INSERT INTO COMMODITY VALUES
	('GUN'),
	('INDIGO');
UNLOCK TABLES;

DROP TABLE IF EXISTS SUPPLY;
CREATE TABLE SUPPLY
(
	F_Email 	VARCHAR(200) 	NOT NULL,
	Name_Of_Com	VARCHAR(50)		NOT NULL,
	S_Location 	VARCHAR(200) 	NOT NULL,
	PRIMARY KEY(F_Email,Name_Of_Com,S_Location),
	FOREIGN KEY (F_Email) REFERENCES FACTORY(E_Mail) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (Name_Of_Com) REFERENCES COMMODITY(Name) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (S_Location) REFERENCES SHOP(Location) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

LOCK TABLES SUPPLY WRITE;
/*insert Data*/
INSERT INTO SUPPLY VALUES
	('kb@g.com','GUN','SHOP NO. 1 ANDHERI NAGRI DELHI'),
	('mk@g.com','INDIGO','SHOP NO. 3 NEAR IIIT-H');
UNLOCK TABLES;

DROP TABLE IF EXISTS TRACKS_INFO;
CREATE TABLE TRACKS_INFO
(
	CAAD	CHAR(12)		NOT NULL,
	Name_Of_Com VARCHAR(50)	NOT NULL,
	S_Location	VARCHAR(200)	NOT NULL,
	F_Email	VARCHAR(200)	NOT NULL,
	PRIMARY KEY(CAAD,Name_Of_Com,S_Location,F_Email),
	FOREIGN KEY (CAAD) REFERENCES CUSTOMERS(Fk_Aad_No) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (Name_Of_Com) REFERENCES COMMODITY(Name) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (S_Location) REFERENCES SHOP(Location) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (F_Email) REFERENCES FACTORY(E_Mail) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

LOCK TABLES TRACKS_INFO WRITE;
/*Insert data for TRACKS_INFO table*/
INSERT INTO TRACKS_INFO VALUES
	('151617181920','INDIGO','SHOP NO. 3 NEAR IIIT-H','mk@g.com'),
	('212223242526','GUN','SHOP NO. 1 ANDHERI NAGRI DELHI','kb@g.com');
UNLOCK TABLES;

DROP TABLE IF EXISTS CONSIGNMENT;
CREATE TABLE CONSIGNMENT
(
	Fk_Works_Id 	VARCHAR(64)		NOT NULL,
	Year			INT 			NOT NULL,
	Quantity		INT 			NOT NULL,
	PRIMARY KEY(Fk_Works_Id),
	FOREIGN KEY(Fk_Works_Id) REFERENCES WORKS_ON(Id) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

LOCK TABLES CONSIGNMENT WRITE;
/*Insert data*/
INSERT INTO CONSIGNMENT VALUES
	('KTTON1','2019','100'),
	('AFEEM','2020','200'),
	('AFEEM1','2020','300');
UNLOCK TABLES;
