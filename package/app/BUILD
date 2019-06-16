load("@my_deps//:requirements.bzl", "requirement")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")

py_binary(
  name="entry",
  srcs=["entry.py"],
  python_version="PY3",
  default_python_version="PY3",
  stamp=0,
  visibility=["//visibility:public"],
  deps=[
    ":__init__",
    ":jinja_custom_filter",
    ":models",
    ":views",
  ],
)

# py3_image(
#   name="entry_image",
#   binary=":entry",
#   visibility=['//visibility:public'],
# )

py_library(
  name="__init__",
  srcs=["__init__.py"],
  srcs_version="PY3",
  visibility=["//visibility:public"],
  deps=[
    # This takes the name as specified in requirements.txt
    requirement("flask"),
    requirement("sqlalchemy"),
    requirement("gunicorn"),
    requirement("werkzeug"),
    requirement("flask_babel"),
    requirement("flask_login"),
    requirement("flask_mail"),
    requirement("flask_paginate"),
    requirement("flask_sqlalchemy"),
    requirement("jinja2"),
    requirement("markupsafe"),
    requirement("itsdangerous"),
    requirement("click"),
    "//:config",
  ],
)

py_library(
  name="jinja_custom_filter",
  srcs=["jinja_custom_filter.py"],
  srcs_version="PY3",
  visibility=["//visibility:public"],
  deps=[
    ":__init__",
  ],
)

py_library(
  name="utils",
  srcs=["utils.py"],
  srcs_version="PY3",
  visibility=["//visibility:public"],
  deps=[
    "//:config",
  ],
)

py_library(
  name="models",
  srcs=["models.py"],
  srcs_version="PY3",
  visibility=["//visibility:public"],
  deps=[
    ":__init__",
    ":utils",
    "//:config",
  ],
)

py_library(
  name="forms",
  srcs=["forms.py"],
  srcs_version="PY3",
  visibility=["//visibility:public"],
  deps=[
    ":__init__",
    ":models",
    ":utils",
    "//:config",
    requirement("flask_wtf"),
  ],
)

py_library(
  name="views",
  srcs=["views.py"],
  data=[
    "//app/templates:templates_html",
    "//app/templates:templates_js",
  ],
  srcs_version="PY3",
  visibility=["//visibility:public"],
  deps=[
    ":forms",
    ":models",
    ":utils",
    "//:config",
  ],
)
