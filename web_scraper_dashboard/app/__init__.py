from flask import Flask

def create_app():
    app = Flask(__name__)
     
    # Importação das views feita aqui para evitar importações circulares.
    from . import views
    app.register_blueprint(views.bp)
    
    return app