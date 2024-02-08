"""Fremework web.py"""
import web

#Rutas de los controladores
urls = (
    '/', 'mvc.controllers.hello.Hello',
    "/pagina2", "mvc.controllers.hello.Pagina2",
    "/pagina3", "mvc.controllers.hello.Pagina3"
)
app = web.application(urls, globals())

# Punto de entrada
if __name__ == "__main__":
    app.run()