import web
from mvc.models.modelo_index import ModeloIndex

render = web.template.render('mvc/views/')
m_index = ModeloIndex()

class Index:
    def GET(self):
        try:
            Resultado = m_index.consultaProductos()
            return render.index(Resultado)
        except Exception as e:
            print(f"Error 101- index {e.args}")
            return "Ups algo salio mal "
        
