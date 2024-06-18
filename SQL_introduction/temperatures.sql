-- This script of  temperature table and populate it with sample data.

CREATE TABLE IF NOT EXISTS temperatures (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    value FLOAT NOT NULL
);

-- Insert sample data
INSERT INTO temperatures (city, value) VALUES ('Chandler', 72.8627);
INSERT INTO temperatures (city, value) VALUES ('Gilbert', 71.8088);
INSERT INTO temperatures (city, value) VALUES ('Pismo beach', 71.5147);
INSERT INTO temperatures (city, value) VALUES ('San Francisco', 71.4804);
INSERT INTO temperatures (city, value) VALUES ('Sedona', 70.7696);
INSERT INTO temperatures (city, value) VALUES ('Phoenix', 70.5882);
INSERT INTO temperatures (city, value) VALUES ('Oakland', 70.5637);
INSERT INTO temperatures (city, value) VALUES ('Sunnyvale', 70.5245);
INSERT INTO temperatures (city, value) VALUES ('Chicago', 70.4461);
INSERT INTO temperatures (city, value) VALUES ('San Diego', 70.1373);
INSERT INTO temperatures (city, value) VALUES ('Glendale', 70.1225);
INSERT INTO temperatures (city, value) VALUES ('Sonoma', 70.0392);
INSERT INTO temperatures (city, value) VALUES ('Yuma', 69.3873);
INSERT INTO temperatures (city, value) VALUES ('San Jose', 69.2990);
INSERT INTO temperatures (city, value) VALUES ('Tucson', 69.0245);
INSERT INTO temperatures (city, value) VALUES ('Joliet', 68.6716);
INSERT INTO temperatures (city, value) VALUES ('Naperville', 68.1029);
INSERT INTO temperatures (city, value) VALUES ('Tempe', 67.0441);
INSERT INTO temperatures (city, value) VALUES ('Peoria', 66.5392);

