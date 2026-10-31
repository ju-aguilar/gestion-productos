import unittest

from productos import (
    InvalidDataError,
    ProductManager,
    ProductNotFoundError,
)


class TestProductosUnitarias(unittest.TestCase):
    def setUp(self):
        self.manager = ProductManager()

    def test_registro_producto(self):
        producto = self.manager.register_product("P001", "Teclado", 25.50, 10)

        self.assertEqual(producto.code, "P001")
        self.assertEqual(producto.name, "Teclado")
        self.assertEqual(producto.price, 25.50)
        self.assertEqual(producto.quantity, 10)

    def test_busqueda_producto(self):
        self.manager.register_product("P002", "Mouse", 15.00, 8)

        producto = self.manager.find_product("P002")

        self.assertEqual(producto.name, "Mouse")
        self.assertEqual(producto.price, 15.00)

    def test_actualizacion_producto(self):
        self.manager.register_product("P003", "Monitor", 100.00, 5)

        actualizado = self.manager.update_product(
            "P003", name="Monitor 24", price=120.00, quantity=7
        )

        self.assertEqual(actualizado.name, "Monitor 24")
        self.assertEqual(actualizado.price, 120.00)
        self.assertEqual(actualizado.quantity, 7)

    def test_eliminacion_producto(self):
        self.manager.register_product("P004", "Impresora", 80.00, 3)

        resultado = self.manager.delete_product("P004")

        self.assertTrue(resultado)
        with self.assertRaises(ProductNotFoundError):
            self.manager.find_product("P004")

    def test_validacion_precio_negativo(self):
        with self.assertRaises(InvalidDataError):
            self.manager.register_product("P005", "Producto inválido", -10.00, 1)


if __name__ == "__main__":
    unittest.main()