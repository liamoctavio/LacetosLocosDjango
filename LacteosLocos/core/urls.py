from django.urls import path
from .views import home, quienessomos,formulario,quesoslacteos,lacteos,quesos,listado_productos,nuevo_producto,modificar_producto,eliminar_producto,registro_usuario,galeria

urlpatterns = [
    path('', home, name = "home"),
    path('quienes-somos/', quienessomos, name="quienessomos" ),
    path('formulario/', formulario, name="formulario"),
    path('quesos-lacteos/', quesoslacteos, name="quesoslacteos"),
    path('lacteos/', lacteos, name ="lacteos"),
    path('quesos/',quesos , name = "quesos"),
    path('listado-productos/',listado_productos , name = "listado_productos"),
    path('nuevo-producto/',nuevo_producto , name = "nuevo_producto"),
    path('modificar-producto/<id>',modificar_producto , name = "modificar_producto"),
    path('eliminar-producto/<id>',eliminar_producto , name = "eliminar_producto"),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('galeria/' ,galeria, name='galeria'),


]
