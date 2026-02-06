from flask import Flask
from flask_cors import CORS
from config import Config
from database import db, init_db
from routes import api
from models import Product

def create_app():
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Initialize database
    init_db(app)
    
    # Register blueprints
    app.register_blueprint(api, url_prefix='/api')
    
    # Seed database with demo data
    with app.app_context():
        Product.seed_data()
    
    return app

if __name__ == '__main__':
    app = create_app()
    print("=" * 50)
    print("🚀 Backend Server Starting...")
    print("📊 Database: SQLite")
    print("🌐 API Endpoint: http://localhost:5000/api")
    print("💚 Health Check: http://localhost:5000/api/health")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
