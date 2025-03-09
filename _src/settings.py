"""
Application Settings
"""

from pathlib import Path

# base directory for application
BASE_DIR = Path(__file__).resolve().parent.parent

# dev/prod mode (if needed)
APP_VERSION = "1.0.0"
DEBUG = True

# database path
DATABASE_PATH = BASE_DIR / "youtube_tutorials.db"

# py template directory
PY_TEMPLATES_DIR = BASE_DIR / "py_templates"

# reserved name
CONTRIBUTOR_RESERVED_NAMES = ["admin", "superuser", "administrator", "root"]
