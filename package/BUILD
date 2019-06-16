load("@bazel_for_gcloud_python//infra/serverless:gae_rules.bzl", "py_app_engine")
load("@my_deps//:requirements.bzl", "requirement")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
("@io_bazel_rules_docker//container:image.bzl",
 "container",
 "image",
 "container_image")
load("@io_bazel_rules_docker//python:image.bzl", "py_layer")

py3_image(
  name='manage',
  srcs=['manage.py'],
  python_version='PY3',
  stamp=0,
  layers=[
    # This takes the name as specified in requirements.txt
    requirement("flask-script"),
    requirement("flask-migrate"),
    requirement("gunicorn"),
    requirement("babel"),
    requirement('wtforms'),
    requirement('alembic'),
    requirement('mako'),
  ],
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
py_library(
  name="__init__",
  srcs=["__init__.py"],
  srcs_version="PY3",
  visibility=["//visibility:public"],
)

py3_image(
  name='main',
  srcs=['main.py'],
  python_version='PY3',
  stamp=0,
  default_python_version="PY3",
  layers=[
    # This takes the name as specified in requirements.txt
    requirement("gunicorn"),
    requirement("babel"),
    requirement('wtforms'),
    ":__init__",
    '//app:entry',
  ],
  visibility=['//visibility:public'],
)

# 'bazel main' this rule to trigger deployment.
py_app_engine(
  # Required parameters:
  name="main_deploy",
  src=":main",
  descriptor="app.yaml",
  entry="main",
  # Specify your pip requirements here
  requirements=[
    # flask is required.
    "flask",
    "gunicorn",
  ],
  # Specify a GCP project name instead of using the default:
  gcloud_project="supplytracker",
  #
  # Print the arguments for debugging when running the rule:
  debug=True,
)
