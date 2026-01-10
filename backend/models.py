from database import db
from datetime import datetime

class Product(db.Model):
    """Product model for database"""
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
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
            'price': round(self.price, 2),
            'category': self.category,
            'stock': self.stock,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    @staticmethod
    def seed_data():
        """Seed database with initial products"""
        if Product.query.count() == 0:
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
                Product(
                    name='USB-C Hub',
                    description='7-in-1 USB-C adapter with HDMI and card reader',
                    price=49.99,
                    category='Accessories',
                    stock=80
                ),
                Product(
                    name='Monitor 27"',
                    description='4K UHD display with HDR support',
                    price=399.99,
                    category='Electronics',
                    stock=45
                ),
                Product(
                    name='Mechanical Keyboard',
                    description='RGB backlit mechanical keyboard with blue switches',
                    price=89.99,
                    category='Accessories',
                    stock=60
                ),
                Product(
                    name='Webcam HD',
                    description='1080p streaming webcam with autofocus',
                    price=79.99,
                    category='Electronics',
                    stock=35
                ),
                Product(
                    name='Desk Lamp',
                    description='LED adjustable desk lamp with touch control',
                    price=34.99,
                    category='Office',
                    stock=100
                ),
                Product(
                    name='Phone Stand',
                    description='Aluminum adjustable phone holder',
                    price=19.99,
                    category='Accessories',
                    stock=200
                ),
                Product(
                    name='Cable Organizer',
                    description='Desktop cable management system',
                    price=12.99,
                    category='Office',
                    stock=175
                ),
                Product(
                    name='Headphones Pro',
                    description='Noise-cancelling wireless headphones',
                    price=249.99,
                    category='Electronics',
                    stock=50
                )
            ]
            
            db.session.bulk_save_objects(demo_products)
            db.session.commit()
            print("✅ Database seeded with 10 demo products!")
