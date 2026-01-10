import React from 'react';
import { Trash2 } from 'lucide-react';

const ProductCard = ({ product, onDelete }) => {
  const getStockColor = (stock) => {
    if (stock > 50) return 'stock-high';
    if (stock > 20) return 'stock-medium';
    return 'stock-low';
  };

  return (
    <div className="product-card">
      <div className="product-header">
        <h3>{product.name}</h3>
        <span className="product-id">ID: {product.id}</span>
      </div>

      <p className="product-description">{product.description}</p>

      <div className="product-details">
        <div className="detail-row">
          <span className="detail-label">Category:</span>
          <span className="detail-value">{product.category}</span>
        </div>

        <div className="detail-row">
          <span className="detail-label">Price:</span>
          <span className="product-price">${product.price.toFixed(2)}</span>
        </div>

        <div className="detail-row">
          <span className="detail-label">Stock:</span>
          <span className={`product-stock ${getStockColor(product.stock)}`}>
            {product.stock} units
          </span>
        </div>
      </div>

      <button
        className="btn-delete"
        onClick={() => onDelete(product.id)}
        title="Delete product"
      >
        <Trash2 size={16} />
        Delete
      </button>
    </div>
  );
};

export default ProductCard;
