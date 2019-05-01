FROM gcr.io/cloud-builders/bazel

CMD build --spawn_strategy=standalone //app:entry --copt --force_python=PY3 --color=yes --curses=yes --jobs=10 --loading_phase_threads=HOST_CPUS --aspects=@bazel_tools//tools/python:srcs_version.bzl%find_requirements --output_groups=pyversioninfo --verbose_failures

CMD build --spawn_strategy=standalone :run --copt  --aspects=@bazel_tools//tools/python:srcs_version.bzl%find_requirements --verbose_failures=true --show_timestamps=true --python_version=PY3 --build_python_zip --sandbox_debug --color=yes --curses=yes --jobs=10 --loading_phase_threads=HOST_CPUS

CMD run --spawn_strategy=standalone :run --copt  --aspects=@bazel_tools//tools/python:srcs_version.bzl%find_requirements --verbose_failures=true --show_timestamps=true --python_version=PY3 --build_python_zip --sandbox_debug --color=yes --curses=yes --jobs=10 --loading_phase_threads=HOST_CPUS
