import os
from dotenv import load_dotenv
from flask import Flask
from web.routes import web_bp

load_dotenv()

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

app.secret_key = os.getenv('SECRET_KEY')

app.register_blueprint(web_bp)

if __name__ == '__main__':

   app.run(port=5001, debug=True)