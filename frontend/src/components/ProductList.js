import React from 'react';
import ProductCard from './ProductCard';

const ProductList = ({ products, loading, onDelete }) => {
  if (loading) {
    return (
      <div className="loading-container">
        <div className="spinner"></div>
        <p>Loading products from database...</p>
      </div>
    );
  }

  if (products.length === 0) {
    return (
      <div className="empty-state">
        <p>No products found. Add your first product!</p>
      </div>
    );
  }

  return (
    <div className="products-container">
      <h2>Product Catalog ({products.length} items)</h2>
      <div className="products-grid">
        {products.map((product) => (
          <ProductCard
            key={product.id}
            product={product}
            onDelete={onDelete}
          />
        ))}
      </div>
    </div>
  );
};

export default ProductList;
