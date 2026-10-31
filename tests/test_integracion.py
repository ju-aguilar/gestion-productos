import unittest

from productos import (
    DuplicateProductError,
    ProductManager,
    ProductNotFoundError,
)


class TestProductosIntegracion(unittest.TestCase):
    def setUp(self):
        self.manager = ProductManager()

    def test_registrar_y_buscar_producto(self):
        self.manager.register_product("I001", "Laptop", 800.00, 2)

        producto = self.manager.find_product("I001")

        self.assertEqual(producto.name, "Laptop")
        self.assertEqual(producto.quantity, 2)

    def test_actualizar_y_verificar_cambio(self):
        self.manager.register_product("I002", "Tablet", 300.00, 4)

        self.manager.update_product("I002", price=350.00, quantity=6)
        producto = self.manager.find_product("I002")

        self.assertEqual(producto.price, 350.00)
        self.assertEqual(producto.quantity, 6)

    def test_eliminar_y_confirmar_que_no_existe(self):
        self.manager.register_product("I003", "Cargador", 20.00, 10)

        self.manager.delete_product("I003")

        with self.assertRaises(ProductNotFoundError):
            self.manager.find_product("I003")

    def test_operar_sobre_producto_inexistente(self):
        with self.assertRaises(ProductNotFoundError):
            self.manager.update_product("NOEXISTE", price=10.00)

    def test_registrar_codigo_duplicado(self):
        self.manager.register_product("I004", "Audífonos", 50.00, 5)

        with self.assertRaises(DuplicateProductError):
            self.manager.register_product("I004", "Audífonos 2", 60.00, 3)


if __name__ == "__main__":
    unittest.main()