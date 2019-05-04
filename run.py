#!flask/bin/python
from app.entry import app
import os

print('hello world!')
app.run(host='0.0.0.0', port=os.environ['PORT'], debug=True)
