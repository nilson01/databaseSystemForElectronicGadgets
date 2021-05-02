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


INSERT INTO Products VALUES("Apple", 111, "Laptop");
INSERT INTO Products VALUES("Sony", 222, "Printer");
INSERT INTO Products VALUES("Microsoft", 333, "PC");

INSERT INTO PCs VALUES(333, 16, 8, 20, 150);
INSERT INTO Laptops VALUES(111, 20, 6, 23, 10, 100);
INSERT INTO Printers VALUES(222, TRUE, "laser-jet", 200);
