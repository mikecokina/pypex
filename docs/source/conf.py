"""Sphinx configuration for builds directly from the source checkout."""
from __future__ import annotations

import sys
from pathlib import Path

# Resolve paths relative to this file, independently of the working directory.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from pypex import __version__  # noqa: E402

project = "pypex"
copyright = "2019–2026, Michal Cokina"
author = "mikecokina"
version = release = __version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
]

templates_path = []
source_suffix = {".rst": "restructuredtext"}
master_doc = "index"
language = "en"
locale_dirs = []
exclude_patterns = []
pygments_style = "sphinx"
todo_include_todos = True

html_theme = "nature"
html_static_path = ["_static"]
htmlhelp_basename = "pypex_doc"
