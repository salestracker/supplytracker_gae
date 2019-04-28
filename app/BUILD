load("@my_deps//:requirements.bzl", "requirement")

py_binary(
  name='entry',
  srcs=['entry.py'],
  python_version='PY3',
  stamp=0,
  deps=[
    ':views',
    ':models',
    ':jinja_custom_filter',
    ':__init__',
  ],
  visibility=['//visibility:public'],
)

py_library(
  name='__init__',
  srcs=['__init__.py'],
  deps=[
    # This takes the name as specified in requirements.txt
    requirement("flask"),
    requirement("sqlalchemy"),
    requirement("gunicorn"),
    requirement("werkzeug"),
  ],
  visibility=['//visibility:public']
)

py_library(
  name='jinja_custom_filter',
  srcs=['jinja_custom_filter.py'],
  deps=[
    ':__init__',
  ],
  visibility=['//visibility:public'],
)

py_library(
  name='utils',
  srcs=['utils.py'],
  deps=[
    '//:config',
  ],
  visibility=['//visibility:public'],
)

py_library(
  name='models',
  srcs=['models.py'],
  deps=[
    '//:config',
    ':__init__',
    ':utils',
  ],
  visibility=['//visibility:public']
)

py_library(
  name='forms',
  srcs=['forms.py'],
  deps=[
    ':utils',
    ':__init__',
    ':models',
    '//:config'
  ],
  visibility=['//visibility:public'],
)

py_library(
  name='views',
  srcs=['views.py'],
  deps=[
    ':utils',
    '//:config',
    ':models',
    ':forms',
  ],
  data=[
    "//app/templates:templates_html",
    "//app/templates:templates_js",
  ],
  visibility=['//visibility:public'],
)
