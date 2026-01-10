import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const productAPI = {
  getAllProducts: async () => {
    const response = await axios.get(`${API_URL}/products`);
    return response.data;
  },

  addProduct: async (product) => {
    const response = await axios.post(`${API_URL}/products`, product);
    return response.data;
  },

  deleteProduct: async (id) => {
    const response = await axios.delete(`${API_URL}/products/${id}`);
    return response.data;
  }
};
