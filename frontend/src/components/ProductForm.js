import React, { useState } from 'react';
import { Plus } from 'lucide-react';

const ProductForm = ({ onSubmit, loading }) => {
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    price: '',
    category: '',
    stock: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
    setFormData({ name: '', description: '', price: '', category: '', stock: '' });
    setShowForm(false);
  };

  return (
    <div className="form-container">
      <button
        className="btn-primary"
        onClick={() => setShowForm(!showForm)}
      >
        <Plus size={20} />
        {showForm ? 'Cancel' : 'Add New Product'}
      </button>

      {showForm && (
        <div className="form-card">
          <h2>Add New Product</h2>
          <div className="form-grid">
            <div className="form-group">
              <label>Product Name</label>
              <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
                placeholder="Enter product name"
                required
              />
            </div>

            <div className="form-group">
              <label>Category</label>
              <input
                type="text"
                name="category"
                value={formData.category}
                onChange={handleChange}
                placeholder="e.g., Electronics"
                required
              />
            </div>

            <div className="form-group">
              <label>Price ($)</label>
              <input
                type="number"
                name="price"
                value={formData.price}
                onChange={handleChange}
                placeholder="0.00"
                step="0.01"
                min="0"
                required
              />
            </div>

            <div className="form-group">
              <label>Stock Quantity</label>
              <input
                type="number"
                name="stock"
                value={formData.stock}
                onChange={handleChange}
                placeholder="0"
                min="0"
                required
              />
            </div>

            <div className="form-group form-group-full">
              <label>Description</label>
              <textarea
                name="description"
                value={formData.description}
                onChange={handleChange}
                placeholder="Enter product description"
                rows="3"
                required
              />
            </div>

            <div className="form-group form-group-full">
              <button
                className="btn-submit"
                onClick={handleSubmit}
                disabled={loading}
              >
                {loading ? 'Adding...' : 'Add Product'}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ProductForm;
