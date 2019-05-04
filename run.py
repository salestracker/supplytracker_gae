#!flask/bin/python
from app.entry import app
import os
port = int(os.environ['PORT'])
print('hello world!', port)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=port, debug=True)
