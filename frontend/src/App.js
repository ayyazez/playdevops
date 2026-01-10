import React, { useState, useEffect } from 'react';
import './App.css';
import Header from './components/Header';
import ProductForm from './components/ProductForm';
import ProductList from './components/ProductList';
import ProductCard from './components/ProductCard';
import { productAPI } from './services/api';

function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Load products on component mount
  useEffect(() => {
    loadProducts();
  }, []);

  const loadProducts = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await productAPI.getAllProducts();
      setProducts(data);
    } catch (err) {
      setError('Failed to load products. Make sure the backend is running.');
      console.error('Error loading products:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleAddProduct = async (productData) => {
    setLoading(true);
    setError(null);
    try {
      await productAPI.addProduct(productData);
      await loadProducts(); // Reload products after adding
    } catch (err) {
      setError('Failed to add product. Please try again.');
      console.error('Error adding product:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteProduct = async (productId) => {
    if (!window.confirm('Are you sure you want to delete this product?')) {
      return;
    }

    setLoading(true);
    setError(null);
    try {
      await productAPI.deleteProduct(productId);
      await loadProducts(); // Reload products after deleting
    } catch (err) {
      setError('Failed to delete product. Please try again.');
      console.error('Error deleting product:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <Header />
      
      {error && (
        <div className="error-message">
          <p>{error}</p>
        </div>
      )}

      <ProductForm onSubmit={handleAddProduct} loading={loading} />
      
      <ProductList
        products={products}
        loading={loading && products.length === 0}
        onDelete={handleDeleteProduct}
      />

      <footer className="footer">
        <h3>Architecture Overview</h3>
        <ul>
          <li><strong>Presentation Layer:</strong> React frontend with forms and product display</li>
          <li><strong>Application Layer:</strong> Flask API handling business logic</li>
          <li><strong>Data Layer:</strong> SQLite database with 10 demo products</li>
          <li><strong>Features:</strong> Auto-fetch from DB, add/delete products, real-time updates</li>
        </ul>
      </footer>
    </div>
  );
}

export default App;
