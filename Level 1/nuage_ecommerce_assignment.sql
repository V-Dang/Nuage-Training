-- CREATING DATABASE
drop database if exists `nuage_ecommerce_assignment`;
create database `nuage_ecommerce_assignment`;
use `nuage_ecommerce_assignment`;

-- DROPPING EXISTING TABLES
drop table `categories`;
drop table `products`;
drop table `customers`;
drop table `orders`;
drop table `order_items`;

-- CREATING TABLES
create table `categories`
(
`category_id` int(1),
`category_name` char(1) not null unique,
	constraint category_id_pk primary key(category_id),
	constraint category_name_ck 
		check (category_name IN ('M', 'F', 'U'))
);

create table `products`
(
`product_id` int(5),
`product_name` varchar(20) not null unique,
`colour` varchar(10) not null,
`category_id` int(1) not null,
`price` double(5,2) not null,
	constraint product_id_pk primary key(product_id),
    constraint product_category_fk foreign key(category_id)
		references categories(category_id)
);

create table `customers`
(
`customer_id` int(5),
`fname` varchar(20) not null,
`lname` varchar(20) not null,
`address` varchar(30) not null,
`postal_code` char(6) not null,
`city` varchar(20) not null,
`province` char(2) not null,
	constraint customer_id_pk primary key(customer_id)
);

create table `orders`
(
`order_id` int(5),
`customer_id` int(5),
`order_date` date not null,
`order_time` datetime not null,
`order_status` varchar(10),
`delivery_date` date default null,
	constraint order_id_pk primary key(order_id),
    constraint customer_id_fk foreign key(customer_id)
		references customers(customer_id),
	constraint order_status_ck
		check (order_status IN ('processing', 'in transit', 'delivered')),
	constraint delivery_date_ck
		check (delivery_date IN(((order_date < delivery_date) and (order_status = 'delivered')), null))
);

create table `order_items`
(
`order_id` int(5),
`customer_id` int(5),
`product_id` int(5),
`price` double(5, 2),
`quantity` int(1) default 1,
`total_price` double(10,2),
	constraint order_id_fk foreign key(order_id)
		references orders(order_id),
	constraint product_id_fk foreign key(product_id)
		references products(product_id)
);
    
-- INSERTING ROWS
insert into categories values(1, 'M'), (2, 'F'), (3, 'U');

insert into customers values (1001, 'vivian', 'dang', '123 sesame street', 'a1b2c3', 'toronto', 'on');

insert into products values(2001, 'melina pant', 'mocha', 2, 159.75);

insert into orders values(3001, 1001, '2022-05-14', '2022-05-14 00:00:00', 'processing', null);

insert into order_items (order_id, product_id, quantity)  values(3001, 2001, 2);

-- MAKING SPECIAL CONDITIONS FOR ORDER_ITEMS TABLE
update order_items
	set customer_id = (select customer_id from orders where orders.order_id = order_items.order_id);
update order_items
	set price = (select price from products where order_items.product_id=products.product_id);
update order_items
	set total_price = price*quantity;
    



