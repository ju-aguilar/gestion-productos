from dataclasses import dataclass
from typing import Dict, Optional


class ProductError(Exception):
    """Error base del módulo de productos."""


class InvalidDataError(ProductError):
    """Datos inválidos."""


class DuplicateProductError(ProductError):
    """Código de producto duplicado."""


class ProductNotFoundError(ProductError):
    """Producto inexistente."""


@dataclass
class Product:
    code: str
    name: str
    price: float
    quantity: int


class ProductManager:
    def __init__(self):
        self._products: Dict[str, Product] = {}

    @staticmethod
    def _validate_code(code: str) -> str:
        if not isinstance(code, str) or not code.strip():
            raise InvalidDataError("El código no puede estar vacío.")
        return code.strip()

    @staticmethod
    def _validate_name(name: str) -> str:
        if not isinstance(name, str) or not name.strip():
            raise InvalidDataError("El nombre no puede estar vacío.")
        return name.strip()

    @staticmethod
    def _validate_price(price) -> float:
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise InvalidDataError("El precio debe ser numérico.")
        if price < 0:
            raise InvalidDataError("El precio no puede ser negativo.")
        return float(price)

    @staticmethod
    def _validate_quantity(quantity) -> int:
        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise InvalidDataError("La cantidad debe ser un número entero.")
        if quantity < 0:
            raise InvalidDataError("La cantidad no puede ser negativa.")
        return quantity

    def register_product(self, code: str, name: str, price, quantity: int) -> Product:
        code = self._validate_code(code)
        if code in self._products:
            raise DuplicateProductError(f"El código '{code}' ya existe.")
        name = self._validate_name(name)
        price = self._validate_price(price)
        quantity = self._validate_quantity(quantity)

        product = Product(code=code, name=name, price=price, quantity=quantity)
        self._products[code] = product
        return product

    def find_product(self, code: str) -> Product:
        code = self._validate_code(code)
        if code not in self._products:
            raise ProductNotFoundError(f"El producto '{code}' no existe.")
        return self._products[code]

    def update_product(
        self,
        code: str,
        name: Optional[str] = None,
        price: Optional[float] = None,
        quantity: Optional[int] = None,
    ) -> Product:
        product = self.find_product(code)
        new_name = product.name if name is None else self._validate_name(name)
        new_price = product.price if price is None else self._validate_price(price)
        new_quantity = (
            product.quantity if quantity is None else self._validate_quantity(quantity)
        )

        updated = Product(
            code=product.code,
            name=new_name,
            price=new_price,
            quantity=new_quantity,
        )
        self._products[product.code] = updated
        return updated

    def delete_product(self, code: str) -> bool:
        product = self.find_product(code)
        del self._products[product.code]
        return True

    def list_products(self):
        return list(self._products.values())