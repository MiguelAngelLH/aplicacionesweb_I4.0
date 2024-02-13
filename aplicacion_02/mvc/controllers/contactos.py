import web
from mvc.models.modelo_contactos import ModeloContactos

render = web.template.render('mvc/views/', base="layout")
m_contactos = ModeloContactos()

class Contactos:
    def GET(self):
        try:
            Resultado = m_contactos.consultaProductos2()
            return render.contactos(Resultado)
        except Exception as e:
            print(f"Error 101- contactos {e.args}")
            return "Ups algo salio mal "
        