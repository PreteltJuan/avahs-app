
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        productoAgregado = self.session.get("productoAgregado")
        ultimoProductoAgregado = self.session.get("ultimoProductoAgregado")

        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
            self.session["productoAgregado"] = False
            self.productoAgregado = self.session["productoAgregado"]
            self.session["ultimoProductoAgregado"] = ""
            self.ultimoProductoAgregado = self.session["ultimoProductoAgregado"]
        else:
            self.carrito = carrito
            self.productoAgregado = productoAgregado
            self.ultimoProductoAgregado = ultimoProductoAgregado


            
    
    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id" : producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "precio": producto.precio,
                "cantidad": 1,

            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio
        self.productoAgregado = True;
        self.ultimoProductoAgregado = producto.nombre
        self.guardar_carrito()


    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session["productoAgregado"] = self.productoAgregado
        self.session["ultimoProductoAgregado"] = self.ultimoProductoAgregado
        self.session.modified = True

    def limpiar(self):
        self.productoAgregado = False
        self.carrito = {}
        self.guardar_carrito()