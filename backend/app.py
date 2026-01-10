from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db = SQLAlchemy(app)

# Database Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'stock': self.stock,
            'created_at': self.created_at.isoformat()
        }

# Initialize database and seed data
with app.app_context():
    db.create_all()
    
    # Seed initial data if database is empty
    if Product.query.count() == 0:
        demo_products = [
            Product(name='Laptop Pro 15', description='High-performance laptop', price=1299.99, category='Electronics', stock=25),
            Product(name='Wireless Mouse', description='Ergonomic wireless mouse', price=29.99, category='Accessories', stock=150),
            Product(name='USB-C Hub', description='7-in-1 USB-C adapter', price=49.99, category='Accessories', stock=80),
            Product(name='Monitor 27"', description='4K UHD display', price=399.99, category='Electronics', stock=45),
            Product(name='Mechanical Keyboard', description='RGB backlit keyboard', price=89.99, category='Accessories', stock=60),
            Product(name='Webcam HD', description='1080p streaming webcam', price=79.99, category='Electronics', stock=35),
            Product(name='Desk Lamp', description='LED adjustable lamp', price=34.99, category='Office', stock=100),
            Product(name='Phone Stand', description='Aluminum phone holder', price=19.99, category='Accessories', stock=200),
            Product(name='Cable Organizer', description='Desktop cable management', price=12.99, category='Office', stock=175),
            Product(name='Headphones Pro', description='Noise-cancelling headphones', price=249.99, category='Electronics', stock=50)
        ]
        db.session.bulk_save_objects(demo_products)
        db.session.commit()

# API Routes
@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    
    new_product = Product(
        name=data['name'],
        description=data['description'],
        price=float(data['price']),
        category=data['category'],
        stock=int(data['stock'])
    )
    
    db.session.add(new_product)
    db.session.commit()
    
    return jsonify(new_product.to_dict()), 201

@app.route('/api/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
