-- Create products table
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(500) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create index on category for better performance
CREATE INDEX idx_products_category ON products(category);

-- Insert demo data
INSERT INTO products (name, description, price, category, stock) VALUES
    ('Laptop Pro 15', 'High-performance laptop with 16GB RAM and 512GB SSD', 1299.99, 'Electronics', 25),
    ('Wireless Mouse', 'Ergonomic wireless mouse with precision tracking', 29.99, 'Accessories', 150),
    ('USB-C Hub', '7-in-1 USB-C adapter with HDMI and card reader', 49.99, 'Accessories', 80),
    ('Monitor 27"', '4K UHD display with HDR support', 399.99, 'Electronics', 45),
    ('Mechanical Keyboard', 'RGB backlit mechanical keyboard with blue switches', 89.99, 'Accessories', 60),
    ('Webcam HD', '1080p streaming webcam with autofocus', 79.99, 'Electronics', 35),
    ('Desk Lamp', 'LED adjustable desk lamp with touch control', 34.99, 'Office', 100),
    ('Phone Stand', 'Aluminum adjustable phone holder', 19.99, 'Accessories', 200),
    ('Cable Organizer', 'Desktop cable management system', 12.99, 'Office', 175),
    ('Headphones Pro', 'Noise-cancelling wireless headphones', 249.99, 'Electronics', 50);

-- Create function to update timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create trigger to automatically update updated_at
CREATE TRIGGER update_products_updated_at 
    BEFORE UPDATE ON products 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();
