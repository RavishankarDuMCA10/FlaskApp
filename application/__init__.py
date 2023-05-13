import os

from flask import Flask

app = Flask(__name__)

from application import route

app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 3010)))
