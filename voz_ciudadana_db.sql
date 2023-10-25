CREATE DATABASE IF NOT EXISTS VOZ_CIUDADANA_DB
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE VOZ_CIUDADANA_DB;


DROP TABLE IF EXISTS USERS;
CREATE TABLE USERS (
    id BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    remember_token varchar(100) DEFAULT NULL,
    created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    is_admin BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT FALSE,
    CONSTRAINT pk_users_id PRIMARY KEY (id),
    CONSTRAINT uc_users_email UNIQUE (email)
) AUTO_INCREMENT = 7;

DROP TABLE IF EXISTS PERSONAL_ACCESS_TOKENS;
CREATE TABLE PERSONAL_ACCESS_TOKENS (
    id BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    tokenable_type VARCHAR(191) NOT NULL,
    tokenable_id BIGINT(20) UNSIGNED NOT NULL,
    name VARCHAR(191) NOT NULL,
    token VARCHAR(64) NOT NULL,
    abilities TEXT DEFAULT NULL,
    last_used_at TIMESTAMP NULL DEFAULT NULL,
    expires_at TIMESTAMP NULL DEFAULT NULL,
    created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_personal_access_tokens_id PRIMARY KEY (id),
    CONSTRAINT uc_personal_access_tokens_token UNIQUE (token),
    CONSTRAINT fk_personal_access_tokens_users FOREIGN KEY (tokenable_id) REFERENCES USERS(id) ON DELETE CASCADE
) AUTO_INCREMENT = 10;

DROP TABLE IF EXISTS REPORT_STATUS;
CREATE TABLE REPORT_STATUS (
    id INT NOT NULL AUTO_INCREMENT,
    status_name VARCHAR(255) NOT NULL,
    CONSTRAINT pk_report_status_id PRIMARY KEY (id)
);

DROP TABLE IF EXISTS REPORT_CATEGORIES;
CREATE TABLE REPORT_CATEGORIES (
    id INT NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(255) NOT NULL,
    CONSTRAINT pk_report_categories_id PRIMARY KEY (id)
);

DROP TABLE IF EXISTS REPORTS;
CREATE TABLE REPORTS (
    id INT NOT NULL AUTO_INCREMENT,
    report_title VARCHAR(255) NOT NULL,
    report_description TEXT NOT NULL,
    creation_dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated_dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    coords VARCHAR(255) NOT NULL,
    user_id BIGINT(20) UNSIGNED,
    category_id INT,
    status_id INT,
    CONSTRAINT pk_reports_id PRIMARY KEY (id),
    CONSTRAINT fk_reports_user_id FOREIGN KEY (user_id) REFERENCES USERS(id),
    CONSTRAINT fk_reports_category_id FOREIGN KEY (category_id) REFERENCES REPORT_CATEGORIES(id),
    CONSTRAINT fk_reports_status_id FOREIGN KEY (status_id) REFERENCES REPORT_STATUS(id)
);

DROP TABLE IF EXISTS REPORT_CONFIRMATIONS;
CREATE TABLE REPORT_CONFIRMATIONS (
    id INT NOT NULL AUTO_INCREMENT,
    report_id INT NOT NULL,
    user_id BIGINT(20) UNSIGNED NOT NULL,
    unconfirmed BOOLEAN NOT NULL DEFAULT FALSE,
    confirmed_dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_report_confirmations_id PRIMARY KEY (id),
    CONSTRAINT fk_report_confirmations_report_id FOREIGN KEY (report_id) REFERENCES REPORTS(id),
    CONSTRAINT fk_report_confirmations_user_id FOREIGN KEY (user_id) REFERENCES USERS(id)
)

DROP TABLE IF EXISTS REPORT_FIXED_CONFIRMATIONS;
CREATE TABLE REPORT_FIXED_CONFIRMATIONS (
    id INT NOT NULL AUTO_INCREMENT,
    report_id INT NOT NULL,
    user_id BIGINT(20) UNSIGNED NOT NULL,
    unconfirmed BOOLEAN NOT NULL DEFAULT FALSE,
    confirmed_dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_report_fixed_confirmations_id PRIMARY KEY (id),
    CONSTRAINT fk_report_fixed_confirmations_report_id FOREIGN KEY (report_id) REFERENCES REPORTS(id),
    CONSTRAINT fk_report_fixed_confirmations_user_id FOREIGN KEY (user_id) REFERENCES USERS(id)
)

DROP TABLE IF EXISTS REPORT_IMAGES;
CREATE TABLE REPORT_IMAGES (
    id INT NOT NULL AUTO_INCREMENT,
    image_url VARCHAR(1024) NOT NULL,
    report_id INT,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT pk_report_images_id PRIMARY KEY (id),
    CONSTRAINT fk_report_images_report_id FOREIGN KEY (report_id) REFERENCES REPORTS(id)
);


INSERT INTO REPORT_STATUS (status_name) VALUES
('PENDIENTE'),
('ACTIVO'),
('SOLICITADO'),
('DESHABILITADO');


-- REPORTS API USER DB --
-- Creacion el usuario
DROP USER 'REPORTS_API_USER'@'%';
CREATE USER 'REPORTS_API_USER'@'%' IDENTIFIED BY 'reports_api_user_pass2023*';

-- Otorgar permisos de SELECT, INSERT y UPDATE para las tablas especificadas
GRANT SELECT, INSERT, UPDATE ON VOZ_CIUDADANA_DB.REPORTS TO 'REPORTS_API_USER'@'%';
GRANT SELECT, INSERT, UPDATE ON VOZ_CIUDADANA_DB.REPORT_STATUS TO 'REPORTS_API_USER'@'%';
GRANT SELECT, INSERT, UPDATE ON VOZ_CIUDADANA_DB.REPORT_CATEGORIES TO 'REPORTS_API_USER'@'%';
GRANT SELECT, INSERT, UPDATE ON VOZ_CIUDADANA_DB.REPORT_IMAGES TO 'REPORTS_API_USER'@'%';
GRANT SELECT, INSERT, UPDATE ON VOZ_CIUDADANA_DB.REPORT_CONFIRMATIONS TO 'REPORTS_API_USER'@'%';
GRANT SELECT, INSERT, UPDATE ON VOZ_CIUDADANA_DB.REPORT_FIXED_CONFIRMATIONS TO 'REPORTS_API_USER'@'%';

-- Otorgar permisos de SELECT para la tabla USERS
GRANT SELECT ON VOZ_CIUDADANA_DB.USERS TO 'REPORTS_API_USER'@'%';

-- Aplicar los cambios
FLUSH PRIVILEGES;


-- AUTH API USER DB --
-- Creacion el usuario
DROP USER 'AUTH_API_USER'@'%';
CREATE USER 'AUTH_API_USER'@'%' IDENTIFIED BY 'auth_api_user_pass2023*';

-- Otorgar permisos de SELECT, INSERT y UPDATE para la tabla USERS y PERSONAL_ACCESS_TOKENS
GRANT SELECT, INSERT, UPDATE ON VOZ_CIUDADANA_DB.PERSONAL_ACCESS_TOKENS TO 'AUTH_API_USER'@'%';
GRANT SELECT, INSERT, UPDATE ON VOZ_CIUDADANA_DB.USERS TO 'AUTH_API_USER'@'%';

-- Aplicar los cambios
FLUSH PRIVILEGES;



--- CREDENCIALES ---
--user: admin--
--pass: V0z_C1ud4dan4_701*--
--host: voz-ciudadana-rds-1.cuhuub668g0y.us-east-2.rds.amazonaws.com--
--port: 3306--