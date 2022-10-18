from unicodedata import name
from django.core.management.base import BaseCommand
from tienda.models import Producto, Usuario, Factura, ProductoComprado
from faker import Faker
import random
from tienda.listas import lista_barrios, lista_sexos

class Command(BaseCommand):
    help = "Add entries in the database for Users, Products and Bills"

    def handle(self, *args, **options):
        faker = Faker()

        self.generar_productos(faker)
        self.generar_usuarios(faker)
        self.generar_facturas(faker)
        self.generar_datos_comprados(faker)

    def generar_productos(self, faker):
        if (len(Producto.objects.all()) == 0):
            for i in range(150):
                producto = Producto.objects.create(
                    nombre = faker.text(max_nb_chars=20),
                    descripcion = ' '.join(faker.paragraphs(nb=3)),
                    precio = random.randint(25000, 300000),
                    unidades = random.randint(1, 15),
                    nuevo = True,
                    #imagen
                )
                producto.save()

    def generar_usuarios(self, faker):
        if (len(Usuario.objects.all()) < 5):
            for i in range(80):
                profile = faker.profile()
                name_parts = profile["name"].split(" ")
                usuario = Usuario.objects.create(
                    username=profile['username'],
                    first_name=name_parts[0] if not name_parts[0].startswith("Mr") else name_parts[1],
                    last_name=name_parts[1] if not name_parts[0].startswith("Mr") else name_parts[2],
                    email=profile['mail'],
                    direccion=profile["address"],
                    barrio=lista_barrios[random.randint(0, len(lista_barrios) - 1)],
                    fecha_nacimiento = profile["birthdate"],
                    sexo=lista_sexos[random.randint(0, len(lista_sexos) - 1)],
                )

                usuario.set_password('qwe123')
                usuario.save()

    def generar_facturas(self, faker):
        if (len(Factura.objects.all()) < 10):
            usuarios = list(Usuario.objects.all())
            for i in range(120):
                usuario = usuarios[random.randint(0, len(usuarios) - 1)]
                factura = Factura.objects.create(
                    idUsuario=usuario,
                    precio=random.randint(250000, 750000)
                    )
                factura.save()

    def generar_datos_comprados(self, faker):
        if (len(ProductoComprado.objects.all()) < 10):
            productos = list(Producto.objects.all())
            facturas = list(Factura.objects.all())

            for factura in facturas:
                cantidad_productos = random.randint(1, 5)
                productos_usados = []

                for i in range(cantidad_productos):
                    while True:
                        producto = productos[random.randint(0, len(productos) - 1)]
                        if producto not in productos_usados:
                            break

                    productos_usados.append(producto)
                    producto_comprado = ProductoComprado.objects.create(
                        idFactura=factura,
                        idProducto=producto,
                        cantidad=random.randint(1, 3) 
                    )
                    producto_comprado.save()