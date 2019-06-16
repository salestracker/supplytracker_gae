# supplytracker_gae
gae ported version of supply tracker.
Supply tracker is a Sales CRM for MSME.

It is in early phase development for developers preview only. Not stable yet.
We have just ported it to appengine.

## Development/CI-CD Stack:

Build Tool: Bazel
Current Stack: Jinja2, Python3, Flask, SqlAlchemy, Sqlite.
Stack to Port to for the time being: 
  - Frontend: React
  - Backend: Python3, Flask, SqlAlchemy, Firestore(NoSQL), PostgreSQL(SQL).

We are keeping the mvc part micro so it does not dictate the design and development. Instead it should be a helper library.

### Project Structure
The current directory structure is like:
```
└── package
    ├── app
    │   ├── static
    │   │   ├── css
    │   │   ├── fonts
    │   │   └── js
    │   └── templates
    │       ├── add
    │       ├── edit
    │       ├── form_templates
    │       ├── javascript
    │       └── view
    └── deploy

```
All static files are under app/static. Templates are under app/tempalates.
This needs to be split into app_server/ and app/ dirs.

## How to download and build using Bazel
WIP

## How to download gcloud SDK
WIP

## How to Deploy locally:
1. Git clone it.
2. checkout to develop branch. Preferred to `git checkout -b <new_branch>` from `develop` branch.
3. `cd package`
4. ```
$HOME/bin/bazel run --spawn_strategy=standalone :main --copt  --aspects=@bazel_tools//tools/python:srcs_version.bzl%find_requirements --verbose_failures=true --show_timestamps=true --python_version=PY3 --build_python_zip --sandbox_debug --color=yes --curses=yes --jobs=10 --loading_phase_threads=HOST_CPUS
```
5. `curl locahost:8081` or `curl locahost:5000`

## How to Deploy to appengine
1. `cloud-build-local --config=cloudbuild.yaml --dryrun=false --push .`
