from flask import Flask
from web.routes import web_bp

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

app.register_blueprint(web_bp)

if __name__ == '__main__':

   app.run(port=5001, debug=True)