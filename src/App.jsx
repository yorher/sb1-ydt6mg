import { useState, useEffect } from 'react';
import axios from 'axios';
import { toast, Toaster } from 'react-hot-toast';
import ProductForm from './components/ProductForm';
import ProductList from './components/ProductList';

function App() {
  const [products, setProducts] = useState([]);
  const [editingProduct, setEditingProduct] = useState(null);

  // Use environment variable or fallback for API URL
  const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

  const fetchProducts = async () => {
    try {
      const response = await axios.get(`${API_URL}/productos`);
      setProducts(response.data);
    } catch (error) {
      toast.error('Error al cargar productos');
      console.error('Error fetching products:', error);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  const handleSubmit = async (product) => {
    try {
      if (editingProduct) {
        await axios.put(`${API_URL}/productos/${editingProduct.id}`, product);
        toast.success('Producto actualizado exitosamente');
      } else {
        await axios.post(`${API_URL}/productos`, product);
        toast.success('Producto agregado exitosamente');
      }
      fetchProducts();
      setEditingProduct(null);
    } catch (error) {
      toast.error('Error al procesar el producto');
      console.error('Error processing product:', error);
    }
  };

  const handleDelete = async (id) => {
    try {
      await axios.delete(`${API_URL}/productos/${id}`);
      toast.success('Producto eliminado exitosamente');
      fetchProducts();
    } catch (error) {
      toast.error('Error al eliminar el producto');
      console.error('Error deleting product:', error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <Toaster position="top-right" />
      <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="px-4 py-6 sm:px-0">
          <h1 className="text-3xl font-bold text-gray-900 mb-8">
            Sistema de Gestión de Productos
          </h1>
          <div className="grid grid-cols-1 gap-8 md:grid-cols-2">
            <ProductForm 
              onSubmit={handleSubmit} 
              initialProduct={editingProduct}
            />
            <ProductList 
              products={products} 
              onEdit={setEditingProduct}
              onDelete={handleDelete}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;