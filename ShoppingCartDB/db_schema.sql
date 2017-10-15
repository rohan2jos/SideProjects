CREATE TABLE LoginCredentials(

id int primary key AUTO_INCREMENT, 

loginid varchar(50) not null unique, 

password varchar(50) not null); 

CREATE TABLE UserType( 

id int primary key AUTO_INCREMENT, 

userrole varchar(100) not null unique);

CREATE TABLE Users( 

id int primary key AUTO_INCREMENT, 

username varchar(50) not null, 

address varchar(200) not null, 

phone int, 

email varchar(100) not null unique, 

usertypeid int references UserType(id) on delete cascade on update cascade, 

logincredentialsid int references LoginCredentials(id) on delete cascade on 

update cascade); 

CREATE TABLE ProductType( 

id int primary key AUTO_INCREMENT, 

type varchar(200) not null unique); 

CREATE TABLE Product(

id int primary key AUTO_INCREMENT, 

name varchar(200) not null, 

modelno varchar(200) not null unique, 

description varchar(5000), 

stock int not null, 

price int not null, 

producttypeid int references ProductType(id) on delete cascade on update 

cascade); 

CREATE TABLE ProductRating(

    id int primary key AUTO_INCREMENT, 

rating int not null, 

userid int references User(id) on delete cascade on update cascade, 

productid int references Product(id) on delete cascade on update cascade);

CREATE TABLE PaymentInfo( 

id int primary key AUTO_INCREMENT, 

userid int references User(id) on delete cascade on update cascade, 

cardnumber bigint(16) not null unique, 

cvv int not null, 

expiredday varchar(200) not null, 

cardname varchar(200) not null);

CREATE TABLE OrderDetials( 

id int primary key AUTO_INCREMENT, 

userid int references user(id) on delete cascade on update cascade, 

productid int references Product(id) on delete cascade on update cascade, 

quantity int not null, 

orderdate date not null, 

totalamount int not null);

Table LoginCredentials

id loginid password 

1 Andy(admin) AAA 

2 Bob BBB 

3 Cindy CCC 

4 David DDD 

5 Eason EEE 

6 Fred FFF 

INSERT INTO `logincredentials` (`id`, `loginid`, `password`) VALUES ('1', 'Andy ', 

'AAA');

INSERT INTO `logincredentials` (`id`, `loginid`, `password`) VALUES ('2', 'Bob', 'BBB');

INSERT INTO `logincredentials` (`id`, `loginid`, `password`) VALUES ('3', 'Cindy', 'CCC');

INSERT INTO `logincredentials` (`id`, `loginid`, `password`) VALUES ('4', 'David', 

'DDD');

INSERT INTO `logincredentials` (`id`, `loginid`, `password`) VALUES ('5', 'Eason', 'EEE');

INSERT INTO `logincredentials` (`id`, `loginid`, `password`) VALUES ('6', 'Fred', 'FFF');

Table User

usernam

i

e 

d 

1 Andy City Center 

address phone email usertypei

2 Bob 12 Orchestra 

3 Cindy 87 Polk St. 

4 David 89 

5 Eason 2743 Bering 

6 Fred 2817 Milton 

Plaza 516 

Main St.,

Elgin,

97827,

USA 

Terrace ,

Walla,

99362,

USA 

Suite 5,

San 

Francisco,

94117,

USA 

Chiaroscuro 

Rd.,

Portland,

97219,

USA 

St.,

Anchorage,

99508,

USA 

Dr.,

Albuquerque

,

87110,

USA 

INSERT INTO `users` (`id`, `username`, `address`, `phone`, `email`, `usertypeid`, 

`logincredentialsid`) VALUES ('1', 'Andy', 'City Center Plaza 516 Main 

St.,Elgin,97827,USA', '1715552222', 'Andy1@gmail.com', '1', '1');

INSERT INTO `users` (`id`, `username`, `address`, `phone`, `email`, `usertypeid`, 

`logincredentialsid`) VALUES ('2', 'Bob', '12 Orchestra Terrace,Walla,99362,USA', 

'1005554822', 'Bob2@gmail.com', '2', '2');

INSERT INTO `users` (`id`, `username`, `address`, `phone`, `email`, `usertypeid`, 

`logincredentialsid`) VALUES ('3', 'Cindy', '87 Polk St. Suite 5,San Francisco,94117,USA

', '2135555735', 'Cindy3@gmail.com', '2', '3'); 

INSERT INTO `users` (`id`, `username`, `address`, `phone`, `email`, `usertypeid`, 

`logincredentialsid`) VALUES ('4', 'David', '89 Chiaroscuro Rd.,Portland,97219,USA

', '1615554448', 'David4@gmail.com', '2', '4');

INSERT INTO `users` (`id`, `username`, `address`, `phone`, `email`, `usertypeid`, 

`logincredentialsid`) VALUES ('5', 'Eason', '2743 Bering St.,Anchorage,99508,USA

', '1145559022', 'Eason5@gmail.com', '2', '5');

INSERT INTO `users` (`id`, `username`, `address`, `phone`, `email`, `usertypeid`, 

`logincredentialsid`) VALUES ('6', 'Fred', '2817 Milton Dr.,Albuquerque,87110,USA

', '2145552955', 'Fred6@gmail.com', '2', '6');

Table UserType

id userrole 

1 administrator 

2 customer 

INSERT INTO `usertype` (`id`, `userrole`) VALUES ('1', 'administrator');

INSERT INTO `usertype` (`id`, `userrole`) VALUES ('2', 'customer');

Table Paymentinfo

id userid cardnumber cvv expiredday cardname 

1 2 1256473854129748 532 07/2018 Bob 

2 3 4827695812753485 567 05/2020 Cindy 

3 4 5146273849127453 565 05/2017 David 

4 5 5745137842153746 345 04/2019 Eason 

5 6 1756219516848665 546 06/2017 Fred 

INSERT INTO `paymentinfo` (`id`, `userid`, `cardnumber`, `cvv`, `expiredday`, 

`cardname`) VALUES ('1', '2', '1256473854129748', '532', '07/2018', 'Bob');

INSERT INTO `paymentinfo` (`id`, `userid`, `cardnumber`, `cvv`, `expiredday`, 

`cardname`) VALUES ('2', '3', '4827695812753485', '567', '05/2020', 'Cindy');

INSERT INTO `paymentinfo` (`id`, `userid`, `cardnumber`, `cvv`, `expiredday`, 

`cardname`) VALUES ('3', '4', '5146273849127453', '565', '05/2017', 'David');

INSERT INTO `paymentinfo` (`id`, `userid`, `cardnumber`, `cvv`, `expiredday`, 

`cardname`) VALUES ('4', '5', '5745137842153746', '345', '04/2019', 'Eason');

INSERT INTO `paymentinfo` (`id`, `userid`, `cardnumber`, `cvv`, `expiredday`, 

`cardname`) VALUES ('5', '6', '1756219516848665', '546', '06/2017', 'Fred');

Table ProductType

id type 

1 TV 

2 mobile 

3 laptop 

INSERT INTO `producttype` (`id`, `type`) VALUES ('1', 'TV');

INSERT INTO `producttype` (`id`, `type`) VALUES ('2', 'mobile');

INSERT INTO `producttype` (`id`, `type`) VALUES ('3', 'laptop');

Table Product

id name modelno description stock price producttypei 

1 Sony 48-Inch 

1080p Smart 

LED TV 

KDL48R510C Enjoy 

2 Vizio 24-

Inches 

1080p Smart 

LED TV 

E24-C1 Experience a 

3 LG 

Electronics 

49-Inch 

1080p LED 

TV 

49LF5400 The LF5400 

4 Apple 

iPhone 6S 

98UB9810 Comes with 

5 Samsung SM-G920F Internal 12 497 2 

Galaxy S6 Memory: 

6 HTC One M9 FE-1541-QQ 20 MP camera 

7 Toshiba 

Satellite 

15.6 Inch 

Laptop 

C55-C5241 Get connected, 

8 Acer 

Chromeboo

k 

CB3-111-C670 Intel Celeron 

9 Dell Inspiron 

15.6" Full-

HD Gaming 

Laptop  

i7559-763BLK Intel i5-

INSERT INTO `product` (`id`, `name`, `modelno`, `description`, `stock`, `price`, 

`producttypeid`) VALUES ('1', 'Sony 48-Inch 1080p Smart LED TV', 'KDL48R510C', 

'Enjoy incredible picture quality and top notch entertainment. This elegantly slim LED 

TV boasts Full HD 1080p for incredible detail and Edge LED backlighting for boosted 

contrast. ', '10', '448', '1');

INSERT INTO `product` (`id`, `name`, `modelno`, `description`, `stock`, `price`, 

`producttypeid`) VALUES ('2', 'Vizio 24-Inches 1080p Smart LED TV', 'E24-C1', 

'Experience a simplified and intuitive Smart TV with high-quality picture and 

enhanced performance all powered by a faster processor.', '8', '168', '1');

INSERT INTO `product` (`id`, `name`, `modelno`, `description`, `stock`, `price`, 

`producttypeid`) VALUES ('3', 'LG Electronics 49-Inch 1080p LED TV

', '49LF5400', 'The LF5400 provides top-notch 1080p resolution for Full HD movies, 

videogames and more. ', '12', '482', '1');

INSERT INTO `product` (`id`, `name`, `modelno`, `description`, `stock`, `price`, 

`producttypeid`) VALUES ('4', 'Apple iPhone 6S', '98UB9810', 'Comes with Easy to use 

iOS 9 with refinements at every level from the apps you see on your Home screen 

down to the foundation of the system', '15', '719', '2');

INSERT INTO `product` (`id`, `name`, `modelno`, `description`, `stock`, `price`, 

`producttypeid`) VALUES ('5', 'Samsung Galaxy S6', 'SM-G920F', 'Internal Memory: 

32GB, 3 GB RAM', '12', '497', '2');

INSERT INTO `product` (`id`, `name`, `modelno`, `description`, `stock`, `price`, 

`producttypeid`) VALUES ('6', 'HTC One M9', 'FE-1541-QQ', '20 MP camera with 

sapphire camera cover lens to deliver crisp', '6', '470', '2');

INSERT INTO `product` (`id`, `name`, `modelno`, `description`, `stock`, `price`, 

`producttypeid`) VALUES ('7', 'Toshiba Satellite 15.6 Inch Laptop', 'C55-C5241', 'Get 

connected, and get stuff done, with the exceptionally value-packed Satellite C55 

laptop. ', '20', '425', '3');

INSERT INTO `product` (`id`, `name`, `modelno`, `description`, `stock`, `price`, 

`producttypeid`) VALUES ('8', 'Acer Chromebook', 'CB3-111-C670', 'Intel Celeron 

N2830 Dual-Core Processor 2.16GHz with Intel Burst Technology up to 2.41GHz, 

Google Chrome Operating System', '8', '177', '3');

INSERT INTO `product` (`id`, `name`, `modelno`, `description`, `stock`, `price`, 

`producttypeid`) VALUES ('9', 'Dell Inspiron 15.6" Full-HD Gaming Laptop ', 'i7559-

763BLK', 'Intel i5-6300HQ 2.3 GHz Quad-Core (6M Cache, Turbo up to 3.2 GHz)', '13', 

'759', '3');

Table ProductRating

id rating userid productid 

1 4 2 9 

2 4 2 4 

3 5 3 5 

4 3 5 2 

5 5 4 4 

6 4 5 1 

INSERT INTO `productrating` (`id`, `rating`, `userid`, `productid`) VALUES ('1', '4', '2', 

'9');

INSERT INTO `productrating` (`id`, `rating`, `userid`, `productid`) VALUES ('2', '4', '2', 

'4');

INSERT INTO `productrating` (`id`, `rating`, `userid`, `productid`) VALUES ('3', '5', '3', 

'5');

INSERT INTO `productrating` (`id`, `rating`, `userid`, `productid`) VALUES ('4', '3', '5', 

'2');

INSERT INTO `productrating` (`id`, `rating`, `userid`, `productid`) VALUES ('5', '5', '4', 

'4');

INSERT INTO `productrating` (`id`, `rating`, `userid`, `productid`) VALUES ('6', '4', '5', 

'1');

Table OrderDetails

id userid productid quantitiy orderdate totalamoun

1 2 1 2 2015-11-27 896 

2 2 3 1 2015-11-26 482 

3 3 5 3 2015-10-30 1491 

4 4 5 2 2015-11-12 994 

5 5 4 3 2015-10-28 2157 

6 5 6 2 2015-10-25 940 

7 5 9 4 2015-10-8 2277 

INSERT INTO `orderdetials` (`id`, `userid`, `productid`, `quantity`, `orderdate`, 

`totalamount`) VALUES ('1', '2', '1', '2', '2015-11-27', '896');

INSERT INTO `orderdetials` (`id`, `userid`, `productid`, `quantity`, `orderdate`, 

`totalamount`) VALUES ('2', '2', '3', '1', '2015-11-26', '482');

INSERT INTO `orderdetials` (`id`, `userid`, `productid`, `quantity`, `orderdate`, 

`totalamount`) VALUES ('3', '3', '5', '3', '2015-10-30', '1491');

INSERT INTO `orderdetials` (`id`, `userid`, `productid`, `quantity`, `orderdate`, 

`totalamount`) VALUES ('4', '4', '5', '2', '2015-11-12', '994');

INSERT INTO `orderdetials` (`id`, `userid`, `productid`, `quantity`, `orderdate`, 

`totalamount`) VALUES ('5', '5', '4', '3', '2015-10-28', '2157');

INSERT INTO `orderdetials` (`id`, `userid`, `productid`, `quantity`, `orderdate`, 

`totalamount`) VALUES ('6', '5', '6', '2', '2015-10-25', '940');

INSERT INTO `orderdetials` (`id`, `userid`, `productid`, `quantity`, `orderdate`, 

`totalamount`) VALUES ('7', '5', '9', '4', '2015-10-08', '2277');