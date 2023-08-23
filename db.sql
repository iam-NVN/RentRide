CREATE DATABASE IF NOT EXISTS rentride;
USE rentride;

CREATE TABLE cars (
  CID varchar(12) NOT NULL PRIMARY KEY,
  Brand varchar(80) NOT NULL,
  Model varchar(80) NOT NULL,
  Type varchar(80) NOT NULL,
  Fuel varchar(15) NOT NULL,
  seating int(20) NOT NULL,
  Transmission varchar(10) NOT NULL,
  Rate float NOT NULL,
  PID varchar(12) NOT NULL,
  location_id varchar(10) NOT NULL,
  available int(11) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO cars (CID, Brand, Model, Type, Fuel, seating, Transmission, Rate, PID, location_id, available) VALUES
('155212173117', 'Volvo', 'S90', 'Sedan', 'Petrol', 5, 'Automatic', 472, '458217479907', 'Coimbatore', 1),
('172873560516', 'Lamborghini', 'Urus', 'SUV', 'Petrol', 5, 'Automatic', 929, '458217479907', 'Coimbatore', 1),
('181023893406', 'Porsche', '718 Boxster', 'Sports', 'Petrol', 2, 'Automatic', 916, '458217479908', 'Coimbatore', 1),
('202546019339', 'Toyota', 'Camry', 'Sedan', 'Petrol', 5, 'Automatic', 470, '458217479903', 'Coimbatore', 1),
('242434120792', 'Ford', 'Mustang GT', 'Sports', 'Petrol', 4, 'Manual', 650, '458217479907', 'Coimbatore', 1),
('291366307501', 'Mahindra', 'Scorpio Classic', 'SUV', 'Diesel', 7, 'Manual', 278, '458217479901', 'Coimbatore', 1),
('308447328150', 'Chevrolet', 'Camaro ZL1', 'Sports', 'Petrol', 4, 'Manual', 912, '458217479901', 'Coimbatore', 1),
('329104552730', 'Toyota', 'GR Supra', 'Coupe', 'Petrol', 2, 'Manual', 620, '458217479907', 'Coimbatore', 1),
('369078223827', 'Audi', 'A4', 'Sedan', 'Petrol', 5, 'Automatic', 800.5, '458217479901', 'Coimbatore', 1),
('369078223828', 'Audi', 'A6', 'Sedan', 'Petrol', 5, 'Automatic', 820, '458217479903', 'Coimbatore', 1),
('369078223829', 'Nissan', 'GTR R35', 'Sports', 'Petrol', 4, 'Automatic', 1385, '458217479901', 'Coimbatore', 1),
('384014423265', 'Toyota', 'Vellfire', 'MUV', 'Petrol', 7, 'Automatic', 462, '458217479907', 'Coimbatore', 1),
('413680853126', 'Mahindra', 'XUV300', 'SUV', 'Petrol', 5, 'Manual', 230, '458217479903', 'Coimbatore', 1),
('428322863911', 'Koenigsegg', 'CCXR', 'Sports', 'Petrol', 2, 'Automatic', 965, '458217479908', 'Coimbatore', 1),
('450327253074', 'Ferrari', 'Portofino', 'Coupe', 'Petrol', 2, 'Manual', 818, '458217479907', 'Coimbatore', 1),
('474016872907', 'Mahindra', 'XUV400', 'SUV', 'Electric', 5, 'Automatic', 219, '458217479903', 'Coimbatore', 1),
('487278706760', 'Mclaren', 'Artura', 'Sports', 'Petrol', 2, 'Manual', 902, '458217479901', 'Coimbatore', 1),
('519224091875', 'BMW', 'X7', 'SUV', 'Diesel', 5, 'Manual', 555, '458217479908', 'Coimbatore', 1),
('532816590190', 'Ford', 'Endeavour', 'SUV', 'Petrol', 7, 'Manual', 450, '458217479903', 'Coimbatore', 1),
('556781815828', 'Chevrolet', 'Corvette Z06', 'Sports', 'Petrol', 2, 'Manual', 912, '458217479907', 'Coimbatore', 1),
('574517811054', 'Toyota', 'Innova Crysta', 'MUV', 'Diesel', 8, 'Manual', 462, '458217479903', 'Coimbatore', 1),
('593811069203', 'Lamborghini', 'Revuelto', 'Sports', 'Petrol', 2, 'Automatic', 929, '458217479908', 'Coimbatore', 1),
('618021832415', 'BMW', 'M2', 'Coupe', 'Diesel', 4, 'Manual', 595, '458217479901', 'Coimbatore', 1),
('641052257623', 'BMW', 'Z4 M40i', 'Coupe', 'Diesel', 4, 'Automatic', 595, '458217479903', 'Coimbatore', 1),
('644615949756', 'Porsche', 'Cayenne', 'SUV', 'Petrol', 5, 'Automatic', 802, '458217479907', 'Coimbatore', 1),
('646485892394', 'Koenigsegg', 'Agera RS', 'Sports', 'Petrol', 2, 'Automatic', 989, '458217479901', 'Coimbatore', 0),
('682401082729', 'Ferrari', 'Purosangue', 'SUV', 'Petrol', 5, 'Automatic', 751, '458217479907', 'Coimbatore', 1),
('703394118777', 'Mazda', 'MX-5 Miata', 'Sports', 'Petrol', 2, 'Manual', 914, '458217479907', 'Coimbatore', 1),
('718948627625', 'Koenigsegg', 'Jesko', 'Sports', 'Petrol', 4, 'Automatic', 989, '458217479908', 'Coimbatore', 1),
('758898241797', 'Audi', 'Q7', 'SUV', 'Petrol', 6, 'Automatic', 472, '458217479905', 'Chennai', 1),
('784710910402', 'Mclaren', 'Artura', 'Sports', 'Petrol', 2, 'Manual', 806, '458217479907', 'Coimbatore', 1),
('796818903247', 'Toyota', 'GR86', 'Sports', 'Petrol', 4, 'Automatic', 799, '458217479907', 'Coimbatore', 1),
('883561303586', 'Porsche', '718 Cayman', 'Sports', 'Petrol', 2, 'Automatic', 916, '458217479908', 'Coimbatore', 1),
('885475116455', 'Nissan', 'GT-R', 'Coupe', 'Petrol', 4, 'Automatic', 750, '458217479907', 'Coimbatore', 1),
('896819065951', 'Nissan', 'GT-R', 'Coupe', 'Petrol', 5, 'Manual', 751, '458217479901', 'Coimbatore', 1),
('962831224758', 'Mahindra', 'XUV700', 'SUV', 'Diesel', 7, 'Automatic', 381, '458217479905', 'Chennai', 1),
('995060835728', 'Volvo', 'XC90', 'SUV', 'Petrol', 7, 'Automatic', 480, '458217479907', 'Coimbatore', 1),
('999507381291', 'Porsche', '911 GT3', 'Sports', 'Petrol', 2, 'Automatic', 916, '458217479908', 'Coimbatore', 1);

CREATE TABLE rentstats (
  UID varchar(12) NOT NULL,
  CID varchar(12) NOT NULL,
  OID varchar(12) NOT NULL PRIMARY KEY,
  Rent_Begin varchar(11) NOT NULL,
  Rent_End varchar(11) NOT NULL,
  Rent_Time varchar(30) NOT NULL,
  Price bigint(225) NOT NULL DEFAULT 0,
  Penalty bigint(225) NOT NULL DEFAULT 0,
  Total bigint(100) NOT NULL DEFAULT 0,
  Status varchar(10) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO rentstats (UID, CID, OID, Rent_Begin, Rent_End, Rent_Time, Price, Penalty, Total, Status) VALUES
('458217479902', '646485892394', '037924402212', '1691324069', '1691367268', '12', 11868, 0, 0, '0'),
('458217479902', '369078223827', '1T1MKHZAW4L5', '1688827296', '1688870494', '12', 850, 0, 17618, '1'),
('458217479902', '369078223827', '279964355338', '1688735849', '1688294000', '72', 850, 0, 50, '1'),
('458217479902', '369078223827', '7QO7KYFDS6QA', '1688827184', '1688837982', '3', 850, 22950, 596358, '1'),
('458217479901', '369078223827', '841079477222', '1691255669', '1691291668', '10', 8005, 0, 39, '1'),
('458217479902', '369078223828', '878290377854', '1691255637', '1691291637', '10', 8200, 0, 131, '1'),
('458217479902', '369078223828', '914094975437', '1691254919', '1691290918', '10', 8200, 0, 1775, '1'),
('458217479902', '369078223828', 'A5PT1DBUNTHH', '1688830234', '1688841029', '3', 900, 22950, 629323, '1'),
('458217479902', '369078223827', 'J1WX4766HMPK', '1688904247', '1688907843', '1', 801, 22950, 545976, '1'),
('458217479901', '369078223827', 'NUMSI8UVOYUJ', '1688827143', '1688837934', '3', 850, 22950, 596355, '1'),
('458217479902', '369078223828', 'RWQWCPH585QJ', '1688827193', '1689086390', '72', 850, 21250, 594655, '1'),
('458217479902', '369078223828', 'Z4V3CSRGOGNL', '1688827316', '1688870514', '12', 850, 22950, 596325, '1');

CREATE TABLE users (
  UID varchar(12) NOT NULL PRIMARY KEY,
  type varchar(15) NOT NULL,
  username varchar(18) NOT NULL UNIQUE,
  passwd varchar(18) NOT NULL,
  name varchar(80) NOT NULL,
  location_id varchar(10) NOT NULL,
  suspended int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO users (UID, type, username, passwd, name, location_id, suspended) VALUES
('458217479901', 'partner', 'fin', 'fin', 'Signature Cars', 'Coimbatore', 0),
('458217479902', 'user', 'muz', 'muz', 'Muz', 'Coimbatore', 0),
('458217479903', 'partner', 'srt', 'srt', 'SRT Automobiles', 'Coimbatore', 0),
('458217479905', 'partner', 'm4i', 'm4i', 'M4i Cars', 'Chennai', 0),
('458217479906', 'partner', 'zhr', 'zhr', 'ZHR Rentals', 'Trichy', 0),
('458217479907', 'partner', 'zhrc', 'zhrc', 'ZHR Coimbatore', 'Coimbatore', 0),
('458217479908', 'partner', 'm4ic', 'm4ic', 'M4i Cars', 'Coimbatore', 0),
('458217479969', 'admin', 'admin', 'admin', 'Admin', 'Coimbatore', 0);
