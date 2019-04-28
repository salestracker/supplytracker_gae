#!flask/bin/python
from app.entry import app

print('hello world!')
app.run(host='0.0.0.0', port=8080, debug=True)
