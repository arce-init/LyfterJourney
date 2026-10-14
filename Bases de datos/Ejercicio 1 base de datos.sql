CREATE TABLE `Products`(
    `Code` BIGINT NOT NULL,
    `Name` VARCHAR(255) NOT NULL,
    `Price` DECIMAL(8, 2) NOT NULL,
    `Entry date` DATE NOT NULL,
    `Brand` VARCHAR(255) NOT NULL,
    `Stock available` INT NOT NULL,
    PRIMARY KEY(`Code`)
);
CREATE TABLE `Invoices`(
    `Invoice number` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Purchase date` DATE NOT NULL,
    `Buyer email` VARCHAR(255) NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `Products per Invoice`(
    `id` BIGINT NOT NULL,
    `Invoice number` BIGINT NOT NULL,
    `Product code` BIGINT NOT NULL,
    `Quantity` INT NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL,
    PRIMARY KEY(`id`)
);
CREATE TABLE `Shopping cart`(
    `Buyer email` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`Buyer email`)
);
CREATE TABLE `Shopping cart items`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Buyer email` VARCHAR(255) NOT NULL,
    `Product Code` BIGINT NOT NULL,
    `Quantity` INT NOT NULL
);
ALTER TABLE
    `Shopping cart items` ADD CONSTRAINT `shopping cart items_buyer email_foreign` FOREIGN KEY(`Buyer email`) REFERENCES `Shopping cart`(`Buyer email`);
ALTER TABLE
    `Products per Invoice` ADD CONSTRAINT `products per invoice_invoice number_foreign` FOREIGN KEY(`Invoice number`) REFERENCES `Invoices`(`Invoice number`);
ALTER TABLE
    `Products per Invoice` ADD CONSTRAINT `products per invoice_product code_foreign` FOREIGN KEY(`Product code`) REFERENCES `Products`(`Code`);
ALTER TABLE
    `Shopping cart items` ADD CONSTRAINT `shopping cart items_product code_foreign` FOREIGN KEY(`Product Code`) REFERENCES `Products`(`Code`);