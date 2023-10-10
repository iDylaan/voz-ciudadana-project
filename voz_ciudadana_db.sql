CREATE DATABASE IF NOT EXISTS VOZ_CIUDADANA_DB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE VOZ_CIUDADANA_DB;

CREATE TABLE USERS (
    id INT NOT NULL,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT FALSE,
    CONSTRAINT pk_users_id PRIMARY KEY (id)
);

CREATE TABLE REPORT_STATUS (
    id INT NOT NULL AUTO_INCREMENT,
    status_name VARCHAR(255) NOT NULL,
    CONSTRAINT pk_report_status_id PRIMARY KEY (id)
);

CREATE TABLE REPORT_CATEGORIES (
    id INT NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(255) NOT NULL,
    CONSTRAINT pk_report_categories_id PRIMARY KEY (id)
);

CREATE TABLE REPORTS (
    id INT NOT NULL AUTO_INCREMENT,
    report_title VARCHAR(255) NOT NULL,
    report_description TEXT NOT NULL,
    creation_dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated_dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    confirmation_request_count INT DEFAULT 0,
    solved_request_count INT DEFAULT 0,
    user_id INT,
    category_id INT,
    status_id INT,
    CONSTRAINT pk_reports_id PRIMARY KEY (id),
    CONSTRAINT fk_reports_user_id FOREIGN KEY (user_id) REFERENCES USERS(id),
    CONSTRAINT fk_reports_category_id FOREIGN KEY (category_id) REFERENCES REPORT_CATEGORIES(id),
    CONSTRAINT fk_reports_status_id FOREIGN KEY (status_id) REFERENCES REPORT_STATUS(id)
);

CREATE TABLE REPORT_IMAGES (
    id INT NOT NULL AUTO_INCREMENT,
    image_url VARCHAR(1024) NOT NULL,
    report_id INT,
    CONSTRAINT pk_report_images_id PRIMARY KEY (id),
    CONSTRAINT fk_report_images_report_id FOREIGN KEY (report_id) REFERENCES REPORTS(id)
);


INSERT INTO REPORT_STATUS (status_name) VALUES
('pendiente'),
('activo'),
('solicionado'),
('baja');


-- REPORTS API USER DB --
-- Crear el usuario (cambia 'password_secreto' por la contraseña que desees)
CREATE USER 'REPORTS_API_USER'@'%' IDENTIFIED BY 'password_secreto';

-- Otorgar permisos de SELECT, INSERT y UPDATE para las tablas especificadas
GRANT SELECT, INSERT, UPDATE ON VOZ_CIUDADANA_DB.REPORTS TO 'REPORTS_API_USER'@'%';
GRANT SELECT, INSERT, UPDATE ON VOZ_CIUDADANA_DB.REPORT_STATUS TO 'REPORTS_API_USER'@'%';
GRANT SELECT, INSERT, UPDATE ON VOZ_CIUDADANA_DB.REPORT_CATEGORIES TO 'REPORTS_API_USER'@'%';
GRANT SELECT, INSERT, UPDATE ON VOZ_CIUDADANA_DB.REPORT_IMAGES TO 'REPORTS_API_USER'@'%';

-- Otorgar permisos de SELECT para la tabla USERS
GRANT SELECT ON VOZ_CIUDADANA_DB.USERS TO 'REPORTS_API_USER'@'%';

-- Aplicar los cambios
FLUSH PRIVILEGES;


-- AUTH API USER DB --
-- Crear el usuario (cambia 'password_secreto' por la contraseña que desees)
CREATE USER 'AUTH_API_USER'@'%' IDENTIFIED BY 'password_secreto';

-- Otorgar permisos de SELECT, INSERT y UPDATE para la tabla USERS
GRANT SELECT, INSERT, UPDATE ON VOZ_CIUDADANA_DB.USERS TO 'AUTH_API_USER'@'%';

-- Aplicar los cambios
FLUSH PRIVILEGES;