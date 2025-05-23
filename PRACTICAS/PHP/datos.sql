CREATE DATABASE IF NOT EXISTS juegos CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE juegos;
CREATE TABLE IF NOT EXISTS videojuego (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    fecha_salida DATE NOT NULL,
    portada VARCHAR(255) NOT NULL
);
INSERT INTO videojuego (titulo, fecha_salida, portada) VALUES
('The Legend of Zelda', '1986-02-21', 'zelda.jpg'),
('Super Mario Bros.', '1985-09-13', 'mario.jpg'),
('Minecraft', '2011-11-18', 'minecraft.jpg');