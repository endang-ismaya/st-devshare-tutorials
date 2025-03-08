"""
Application Settings
"""

from pathlib import Path

# base directory for application
BASE_DIR = Path(__file__).resolve().parent.parent

# dev/prod mode (if needed)
DEBUG = True

# database path
DATABASES = BASE_DIR / "db" / "youtube_tutorials.db"
