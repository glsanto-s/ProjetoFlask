from config import app
from professor.controller import professores_blueprint

app.register_blueprint(professores_blueprint)

if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )