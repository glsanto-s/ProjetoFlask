from config import app, db
from professor.controller import professores_blueprint

app.register_blueprint(professores_blueprint)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )