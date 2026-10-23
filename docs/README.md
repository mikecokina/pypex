# Build API documentation

The documentation uses **Python 3.12 or newer** and **Sphinx 9.1.0**.
Pypex itself supports Python 3.11–3.14. Run the commands below from a Bash
terminal on Linux, replacing `/path/to/pypex` with your checkout path.

## Create the documentation environment

```sh
cd /path/to/pypex
python3.12 -m venv /tmp/pypex-docs-venv
source /tmp/pypex-docs-venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r docs/requirements.txt
```

If creating the venv fails because `ensurepip` is unavailable, install the
matching `python3.12-venv` package on Debian/Ubuntu, or use an interpreter
with venv support.

The requirements include Pypex's runtime dependencies for autodoc imports.
`source/conf.py` resolves the checkout's `src` directory relative to its own
location and reads the version from Pypex. No editable install, `PYTHONPATH`
setting or application `.ini` file is needed. The built-in `nature` theme
does not require a separate theme package.

## Build and open HTML

From the repository root, with the environment activated:

```sh
python -m sphinx -W --keep-going -b html docs/source docs/build/html
xdg-open docs/build/html/index.html
```

`-W` treats warnings as errors; `--keep-going` reports all problems in one run.
For a full rebuild without cached documents:

```sh
python -m sphinx -W --keep-going -E -a -b html docs/source docs/build/html
```

The configuration also works from the documentation directory:

```sh
cd /path/to/pypex/docs
make html
```

`make html` uses the same output directory and treats warnings as errors by
default. On Windows, activate your venv and use `make.bat html` from `docs`,
or use the `python -m sphinx` command above. Open the HTML file in your browser.

For subsequent builds, activate the existing environment and repeat the build
command. Generated output under `docs/build/` is ignored by Git.

## Regenerate the API reference

From the repository root, with the environment activated:

```sh
python -m sphinx.ext.apidoc src/pypex -o docs/source/api_docs -f
python -m sphinx -W --keep-going -E -a -b html docs/source docs/build/html
```

The `-f` option overwrites the generated API pages. No manual `:noindex:` edits
are needed after generation. The index links only to `api_docs/modules`, which
owns the API navigation tree. If modules are removed or renamed, remove their
obsolete generated pages before regenerating.
