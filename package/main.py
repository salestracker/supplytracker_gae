#!flask/bin/python
import os
import logging
from app.entry import app

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

port = int(os.environ.get('PORT', 8081))
logging.info('hello world runs at %s', port)

if __name__ == '__main__':
  logging.info('hello world! at port:%s', port)
  app.run(host='0.0.0.0', port=port, debug=True)
#
