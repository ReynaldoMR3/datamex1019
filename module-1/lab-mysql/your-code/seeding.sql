INSERT INTO Cars(VIN, Manufacturer, Model, Year, Color)values('3K096I98581DHSNUP', 'Volkswagen', 'Tiguan', 2019, 'Blue');
INSERT INTO Cars(VIN, Manufacturer, Model, Year, Color)values('ZM8G7BEUQZ97IH46V', 'Peugeot', 'Rifter', 2019, 'Red');
INSERT INTO Cars(VIN, Manufacturer, Model, Year, Color)values('RKXVNNIHLVVZOUB4M', 'Ford', 'Fusion', 2018, 'White');
INSERT INTO Cars(VIN, Manufacturer, Model, Year, Color)values('HKNDGS7CU31E9Z7JW', 'Toyota', 'RAV4', 2018, 'Silver');
INSERT INTO Cars(VIN, Manufacturer, Model, Year, Color)values('DAM41UDN3CHU2WVF6', 'Volvo', 'V60', 2019, 'Gray');
INSERT INTO Cars(VIN, Manufacturer, Model, Year, Color)values('DAM41UDN3CHU2WVF6', 'Volvo', 'V60 Cross Country', 2019, 'Gray');

INSERT INTO Customers values('10001', 'Pablo Picasso', '+34 636 17 63 82', '-', 'Paseo de la Chopera, 14', 'Madrid', 'Madrid', 'Spain', 28045);
INSERT INTO Customers values('20001', 'Abraham Lincoln', '+1 305 907 7086', '-', '120 SW 8th St', 'Miami', 'Florida', 'United States', 33130);
INSERT INTO Customers values('30001', 'Napoléon Bonaparte', '+33179754000', '-', '40 Rue du Colisée', 'Paris', 'Île-de-France', 'France', 75008);

INSERT INTO Salespersons values(00001, 'Petey Cruiser', 'Madrid');
INSERT INTO Salespersons values(00002, 'Anna Sthesia', 'Barcelona');
INSERT INTO Salespersons values(00003, 'Paul Molive', 'Berlin');
INSERT INTO Salespersons values(00004, 'Gail Forcewind', 'Paris');
INSERT INTO Salespersons values(00005, 'Paige Turner', 'Mimia');
INSERT INTO Salespersons values(00006, 'Bob Frapples', 'Mexico City');
INSERT INTO Salespersons values(00007, 'Walter Melon', 'Amsterdam');
INSERT INTO Salespersons values(00008, 'Shonda Leer', 'São Paulo');

INSERT INTO Invoices values(852399038, str_to_date("22-08-2018","%d-%m-%Y"), 0, 1, 3);
INSERT INTO Invoices values(731166526, str_to_date("31-12-2018","%d-%m-%Y"), 3, 0, 5);
INSERT INTO Invoices values(271135104, str_to_date("22-01-2019","%d-%m-%Y"), 2, 2, 7);