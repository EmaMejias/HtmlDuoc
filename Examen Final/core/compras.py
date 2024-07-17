class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, producto):
        if self.puede_agregar(producto):
            if producto.idProducto not in self.carrito.keys():
                self.carrito[producto.idProducto] = {
                    "producto_id": producto.idProducto,
                    "nombre": producto.nombreProducto,
                    "descripcion": producto.descripcionProducto,
                    "precio": producto.precio,
                    "stock": producto.stock,
                    "cantidad": 1,
                    "total": producto.precio,
                }
            else:
                for key, value in self.carrito.items():
                    if key == producto.idProducto:
                        value["cantidad"] = value["cantidad"] + 1
                        value["precio"] = producto.precio
                        value["stock"] = value["stock"] - 1
                        value["total"] = value["total"] + producto.precio
                        break
            self.guardar_carrito()
        else:
            raise ValueError("No hay suficiente stock disponible para agregar más de este producto.")

    def puede_agregar(self, producto):
        cantidad_actual = self.carrito.get(producto.idProducto, {}).get("cantidad", 0)
        return (cantidad_actual + 1) <= producto.stock

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = producto.idProducto
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        for key, value in self.carrito.items():
            if key == producto.idProducto:
                value["cantidad"] = value["cantidad"]-1
                value["stock"]= value["stock"]+1
                value["total"] = int(value["total"])- producto.precio
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True


