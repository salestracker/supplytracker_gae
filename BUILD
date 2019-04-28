load("@bazel_for_gcloud_python//infra/serverless:gae_rules.bzl", "py_app_engine")
load("@my_deps//:requirements.bzl", "requirement")

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
    # This takes the name as specified in requirements.txt
    requirement("gunicorn"),
  ],
  visibility=['//visibility:public'],
)

# 'bazel run' this rule to trigger deployment.
py_app_engine(
  # Required parameters:
  name="run_deploy",
  src=":run",
  descriptor="app.yaml",
  entry="run",
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
