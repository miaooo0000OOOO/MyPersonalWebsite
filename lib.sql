CREATE TABLE `library`(
   `book_id` INT UNSIGNED AUTO_INCREMENT,
   `book_name` VARCHAR(100) NOT NULL,
   `book_author` VARCHAR(40),
   `publish_time` DATE,
   PRIMARY KEY ( `book_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;