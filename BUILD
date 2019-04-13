py_library(
  name='manage',
  srcs=['manage.py'],
  deps=[
    '//app:__init__',
  ],
  visibility=['//visibility:public'],
)

py_library(
  name='config',
  srcs=['config.py'],
  visibility=['//visibility:public'],
)

py_binary(
  name='run',
  srcs=['run.py'],
  python_version='PY3',
  stamp=0,
  deps=[
    '//app:entry',
  ],
  visibility=['//visibility:public'],
)
