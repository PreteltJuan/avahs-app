

class Favorito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        favoritos = self.session.get("favoritos")

        if not favoritos:
            self.session["favoritos"] = {}
            self.favoritos = self.session["favoritos"]
        else:
            self.favoritos = favoritos


            
    
    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.favoritos.keys():
            self.favoritos[id] = {
                "nombre": producto.nombre,
                "precio": producto.precio,
        }

        self.guardar_favoritos()


    def guardar_favoritos(self):
        self.session["favoritos"] = self.favoritos
        self.session.modified = True

    def limpiar(self):
        self.favoritos = {}
        self.guardar_favoritos()

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.favoritos:
            del self.favoritos[id]
            self.guardar_favoritos()

    def inicializarFavorito(self, producto):
        self.limpiar()
        id = str(producto.id)
        self.favoritos[id] = {
                "nombre": producto.nombre,
                "precio": producto.precio,
        }
        self.guardar_carrito()