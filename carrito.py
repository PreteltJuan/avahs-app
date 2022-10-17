

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        subTotal = self.session.get("subTotal")
        productoAgregado = self.session.get("productoAgregado")
        ultimoProductoAgregado = self.session.get("ultimoProductoAgregado")
        carritoLimpiado = self.session.get("carritoLimpiado")

        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
            self.session["productoAgregado"] = False
            self.productoAgregado = self.session["productoAgregado"]
            self.session["ultimoProductoAgregado"] = ""
            self.ultimoProductoAgregado = self.session["ultimoProductoAgregado"]
            self.session["carritoLimpiado"] = False
            self.carritoLimpiado = self.session["carritoLimpiado"]
            self.session["subTotal"] = 0
            self.subTotal = self.session["subTotal"]
        else:
            self.carrito = carrito
            self.productoAgregado = productoAgregado
            self.ultimoProductoAgregado = ultimoProductoAgregado
            self.carritoLimpiado = carritoLimpiado
            self.subTotal = subTotal


            
    
    def agregar(self, producto):
        id = str(producto.pk)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id" : producto.pk,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "precio": producto.precio,
                "cantidad": 1,

            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio

        self.productoAgregado = True;
        self.carritoLimpiado = False;
        self.ultimoProductoAgregado = producto.nombre
        self.guardar_carrito()


    def guardar_carrito(self):
        self.actualizarSubTotal()
        self.session["carrito"] = self.carrito
        self.session["productoAgregado"] = self.productoAgregado
        self.session["ultimoProductoAgregado"] = self.ultimoProductoAgregado
        self.session["carritoLimpiado"] = self.carritoLimpiado
        self.session["subTotal"] = self.subTotal
        self.session.modified = True

    def limpiar(self):
        self.productoAgregado = False
        self.carritoLimpiado = True
        self.carrito = {}
        self.guardar_carrito()

    def actualizarSubTotal(self):
        total = 0
        for key,value in self.carrito.items():
            total += int(value["acumulado"])
        self.subTotal = total

    
    def eliminar(self, producto):
        id = str(producto.pk)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
