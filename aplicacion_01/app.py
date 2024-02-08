import web

urls = (
    '/', 'hello',
    "/pagina2", "pagina2",
    "/pagina3", "pagina3"
)
app = web.application(urls, globals())

class hello:
    def GET(self):
        return "HOLA BIENVENIDO A PAGINA 1"
    
class pagina2:
    def GET(self):
        return "HOLA BIENVENIDO A PAGINA 2"    
    
class pagina3:
    def GET(self):
        return "HOLA BIENVENIDO A PAGINA 3"        

if __name__ == "__main__":
    app.run()
