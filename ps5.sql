DROP DATABASE IF EXISTS ncps5;

CREATE DATABASE ncps5;

USE ncps5;

CREATE TABLE Products(
    maker varchar(20),
    model real,
    type varchar(20),
    PRIMARY KEY(model)
);

CREATE TABLE PCs(
    model real,
    speed integer,
    ram integer,
    hd integer,
    price real,
    PRIMARY KEY(model)
);


CREATE TABLE Laptops(
    model real,
    speed integer,
    ram integer,
    hd integer,
    screen integer,
    price real,
    PRIMARY KEY(model)
);

CREATE TABLE Printers(
    model real,
    color boolean,
    type varchar(10),
    price real,
    PRIMARY KEY(model)
);





INSERT INTO Products VALUES("Microsoft", 333, "PC");
INSERT INTO Products VALUES("Google",343, "PC");
INSERT INTO Products VALUES("Apple",353,"PC");
INSERT INTO Products VALUES("Samasung",363, "PC");
INSERT INTO Products VALUES("Sony",373, "PC");
INSERT INTO Products VALUES("Toshiba", 383, "PC");
INSERT INTO Products VALUES("Lenovo",393, "PC");
INSERT INTO Products VALUES("Acer",433, "PC");
INSERT INTO Products VALUES("Apple",443, "PC");
INSERT INTO Products VALUES("Microsoft",453, "PC");
INSERT INTO Products VALUES("Samsung",463, "PC");
INSERT INTO PCs VALUES(333, 16, 8, 20, 150);
INSERT INTO PCs VALUES(343, 16, 8, 20, 150);
INSERT INTO PCs VALUES(353, 32, 10, 23, 250);
INSERT INTO PCs VALUES(363, 8, 14, 24, 130);
INSERT INTO PCs VALUES(373, 64, 12, 12, 155);
INSERT INTO PCs VALUES(383, 16, 8, 19, 200);
INSERT INTO PCs VALUES(393, 32, 5, 12, 300);
INSERT INTO PCs VALUES(433, 64, 12, 50, 400);
INSERT INTO PCs VALUES(443, 16, 5, 18, 255);
INSERT INTO PCs VALUES(453, 24, 19, 16, 1000);
INSERT INTO PCs VALUES(463, 18, 8, 32, 100);


INSERT INTO Products VALUES("Apple", 111, "Laptop");
INSERT INTO Products VALUES("Apple", 121, "Laptops");
INSERT INTO Products VALUES("Google", 131, "Laptops");
INSERT INTO Products VALUES("Microsoft", 141, "Laptops");
INSERT INTO Products VALUES("Toshiba",151, "Laptops");
INSERT INTO Products VALUES("Lenovo",161, "Laptops");
INSERT INTO Products VALUES("Samsung",171, "Laptops");
INSERT INTO Products VALUES("Apple",181, "Laptops");
INSERT INTO Products VALUES("Acer",191, "Laptops");
INSERT INTO Products VALUES("Microsoft",211, "Laptops");
INSERT INTO Products VALUES("Google",221, "Laptops");
INSERT INTO Products VALUES("Lenovo", 231, "Laptops");
INSERT INTO Products VALUES("Apple",241, "Laptops");
INSERT INTO Laptops VALUES(111, 20, 6, 23, 10, 100);
INSERT INTO Laptops VALUES(121, 22, 12, 44, 12, 200);
INSERT INTO Laptops VALUES(131, 24, 14, 55, 13, 223);
INSERT INTO Laptops VALUES(141, 45, 8, 23, 56, 444);
INSERT INTO Laptops VALUES(151, 44, 10, 13, 12, 222);
INSERT INTO Laptops VALUES(161, 66, 20, 56, 34, 1233);
INSERT INTO Laptops VALUES(171, 99, 60, 23, 12, 333);
INSERT INTO Laptops VALUES(181, 45, 43, 33, 13, 456);
INSERT INTO Laptops VALUES(191, 23, 46, 12, 56, 345);
INSERT INTO Laptops VALUES(211, 12, 12, 67, 77, 123);
INSERT INTO Laptops VALUES(221, 23, 11, 18, 44, 1234);
INSERT INTO Laptops VALUES(231, 34, 11, 18, 44, 1234);
INSERT INTO Laptops VALUES(241, 78, 11, 18, 44, 1234);


INSERT INTO Products VALUES("Sony", 222, "Printer");
INSERT INTO Printers VALUES(222, TRUE, "laser-jet", 200);