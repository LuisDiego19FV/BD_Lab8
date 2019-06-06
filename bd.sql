DROP TABLE producto;
DROP TABLE pc;

CREATE TABLE pc(
    modelo varchar(255),
    velocidad float,
    ram int,
    disco int,
    precio float,
    PRIMARY KEY (modelo)
);

CREATE TABLE producto(
    fabricante varchar(255),
    modelo varchar(255),
    tipo varchar(255),
    FOREIGN KEY (modelo) REFERENCES pc(modelo)
);

INSERT INTO pc
VALUES  ('PC101', 4.0, 16, 256, 1200),
        ('PC102', 4.0, 32, 1024, 1500),
        ('PC201', 3.2, 8, 512, 800),
        ('PC202', 3.5, 16, 512, 1000),
        ('PC301', 4.2, 32, 1024, 2000);

INSERT INTO producto
VALUES  ('fabricanteA', 'PC101','PC'),
        ('fabricanteA', 'PC102','PC'),
        ('fabricanteB', 'PC201','PC'),
        ('fabricanteB', 'PC202','PC'),
        ('fabricanteC', 'PC301','PC');
