from database import db
from datetime import datetime

class Product(db.Model):
    """Product model for database"""
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Product {self.name}>'
    
    def to_dict(self):
        """Convert product to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': float(self.price),
            'category': self.category,
            'stock': self.stock,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    @staticmethod
    def seed_data():
        """Seed database with initial products (if using SQLite fallback)"""
        demo_products = [
            Product(
                name='Laptop Pro 15',
                description='High-performance laptop with 16GB RAM and 512GB SSD',
                price=1299.99,
                category='Electronics',
                stock=25
            ),
            Product(
                name='Wireless Mouse',
                description='Ergonomic wireless mouse with precision tracking',
                price=29.99,
                category='Accessories',
                stock=150
            ),
            # Add more products...
        ]
        
        db.session.bulk_save_objects(demo_products)
        db.session.commit()
