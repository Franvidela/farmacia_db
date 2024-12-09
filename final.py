# Por medio de la consola interpretador de python (shell), realice las siguientes consultas:
#1. Obtenga todos los objetos tanto Laboratorio, DirectorGeneral y Productos.
#`python manage.py shell`

from laboratorio.models import Laboratorio, DirectorGeneral, Producto
laboratorio = Laboratorio.objects.all()
print('\n'.join(str(i.nombre) for i in laboratorio))

director_general = DirectorGeneral.objects.all()
print('\n'.join(str(i.nombre) for i in director_general))

producto = Producto.objects.all()
print('\n'.join(str(i.nombre) for i in producto))

# Obtenga el laboratorio del Producto cuyo nombre es ‘Producto 1’.
query = '''
        SELECT p.id, p.nombre AS nombre_producto, l.id, l.nombre AS nombre_laboratorio FROM laboratorio_producto p INNER JOIN laboratorio_laboratorio l ON p.laboratorio_id = l.id WHERE p.nombre = %s;
        '''
        
consulta1 = Producto.objects.raw(query, ['Producto 1'])
print('\n'.join(str(i.nombre_laboratorio) for i in consulta1))        























# Ordene todos los productos por nombre, y que muestre los valores de nombre y laboratorio.

# Realice una consulta que imprima por pantalla los laboratorios de todos los productos.