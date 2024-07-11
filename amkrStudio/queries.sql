-- [TABLE]: auth_user

-- ALTER TABLE DROP COLUMNS
ALTER TABLE 
    auth_user 
DROP COLUMN username,
DROP COLUMN email,
DROP COLUMN password,
DROP COLUMN first_name,
DROP COLUMN last_name,
DROP COLUMN last_login,
DROP COLUMN is_superuser,
DROP COLUMN is_staff,
DROP COLUMN is_active,
DROP COLUMN date_joined;

-- ALTER TABLE ADD COLUMNS
ALTER TABLE 
    auth_user 
ADD COLUMN first_name VARCHAR(128) NOT NULL,
ADD COLUMN last_name VARCHAR(128) NOT NULL,
ADD COLUMN email VARCHAR(256) NOT NULL,
ADD COLUMN username VARCHAR(256) NOT NULL,
ADD COLUMN password VARCHAR(128) NOT NULL,
ADD COLUMN date_joined TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN created_by INTEGER NOT NULL,
ADD COLUMN updated_date TIMESTAMP WITH TIME ZONE,
ADD COLUMN updated_by INTEGER,
ADD COLUMN is_superuser BOOLEAN DEFAULT FALSE,
ADD COLUMN is_staff BOOLEAN DEFAULT TRUE,
ADD COLUMN is_active BOOLEAN DEFAULT TRUE,
ADD COLUMN last_login TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP;

-- ALTER TABLE ALTER COLUMNS
ALTER TABLE 
    auth_user
ALTER COLUMN first_name SET DATA TYPE VARCHAR(64),
ALTER COLUMN last_name SET DATA TYPE VARCHAR(64);


-- [TABLE]: investment_type

-- CREATE SEQUENCE
CREATE SEQUENCE investment_type_id_seq
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 2147483647
    START 1
    CACHE 1
    NO CYCLE;

-- CREATE TABLE
CREATE TABLE investment_type (
    id INTEGER DEFAULT nextval('investment_type_id_seq') PRIMARY KEY,
    type_name VARCHAR(64) NOT NULL,
    fund_name VARCHAR(128) NOT NULL,
    fund_category VARCHAR(64) NOT NULL,
    fund_type VARCHAR(64) NOT NULL,
    app_name VARCHAR(64) NOT NULL,
    created_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER NOT NULL,
    updated_date TIMESTAMPTZ,
    updated_by INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    is_trash BOOLEAN DEFAULT FALSE
);


-- [TABLE]: investment

-- CREATE SEQUENCE
CREATE SEQUENCE investment_id_seq
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 2147483647
    START 1
    CACHE 1
    NO CYCLE;

-- CREATE TABLE
CREATE TABLE investment (
    id INTEGER DEFAULT nextval('investment_id_seq') PRIMARY KEY,
    user_id INTEGER REFERENCES auth_user(id),
    investment_type_id INTEGER REFERENCES investment_type(id),
    day INTEGER NOT NULL,
    month INTEGER NOT NULL,
    year INTEGER NOT NULL,
    investment_amount INTEGER DEFAULT 0,
    total_invested INTEGER DEFAULT 0,
    total_percent_returns DECIMAL(7,2) DEFAULT 0,
    expense_ratio DECIMAL(7,2) DEFAULT 0,
    created_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER NOT NULL,
    updated_date TIMESTAMPTZ,
    updated_by INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    is_trash BOOLEAN DEFAULT FALSE
);


-- [TABLE]: credit_expense

-- CREATE SEQUENCE
CREATE SEQUENCE credit_expense_id_seq
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 2147483647
    START 1
    CACHE 1
    NO CYCLE;

-- CREATE TABLE
CREATE TABLE credit_expense (
    id INTEGER DEFAULT nextval('credit_expense_id_seq') PRIMARY KEY,
    user_id INTEGER REFERENCES auth_user(id),
    day INTEGER NOT NULL,
    month INTEGER NOT NULL,
    year INTEGER NOT NULL,
    amount INTEGER DEFAULT 0,
    category VARCHAR(64) NOT NULL,
    source VARCHAR(128) NOT NULL,
    is_credited BOOLEAN DEFAULT FALSE,
    created_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER NOT NULL,
    updated_date TIMESTAMPTZ,
    updated_by INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    is_trash BOOLEAN DEFAULT FALSE
);

