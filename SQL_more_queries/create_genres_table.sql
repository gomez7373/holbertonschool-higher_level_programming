USE hbtn_0d_tvshows;

-- Create genres table
CREATE TABLE IF NOT EXISTS genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Populate genres table
INSERT INTO genres (name) VALUES
('Drama'),
('Comedy'),
('Mystery'),
('Crime'),
('Suspense'),
('Thriller'),
('Adventure'),
('Fantasy');

