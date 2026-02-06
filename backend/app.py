from flask import Flask
from flask_cors import CORS
from config import Config
from database import db, init_db
from routes import api
import time
import sys

def create_app():
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Wait for database to be ready
    max_retries = 30
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            # Initialize database
            init_db(app)
            print("✅ Successfully connected to database!")
            break
        except Exception as e:
            retry_count += 1
            print(f"⚠️  Database connection attempt {retry_count}/{max_retries} failed: {e}")
            if retry_count >= max_retries:
                print("❌ Failed to connect to database after maximum retries")
                sys.exit(1)
            time.sleep(2)
    
    # Register blueprints
    app.register_blueprint(api, url_prefix='/api')
    
    # Seed database with demo data (only if empty)
    with app.app_context():
        from models import Product
        try:
            if Product.query.count() == 0:
                Product.seed_data()
                print("✅ Database seeded with demo data")
        except Exception as e:
            print(f"⚠️  Seeding skipped or failed: {e}")
    
    return app

if __name__ == '__main__':
    app = create_app()
    print("=" * 50)
    print("🚀 Backend Server Starting...")
    print(f"📊 Database: {app.config['SQLALCHEMY_DATABASE_URI'].split('@')[1] if '@' in app.config['SQLALCHEMY_DATABASE_URI'] else 'SQLite'}")
    print("🌐 API Endpoint: http://localhost:5000/api")
    print("💚 Health Check: http://localhost:5000/api/health")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
