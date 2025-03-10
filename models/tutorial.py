import sqlite3
import pandas as pd
from enum import Enum, auto

from _src.settings import DATABASE_PATH


class TutorialKeys(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return f"TUTORIAL__{str(name).upper()}"

    PAGE_NUM = auto()


class TutorialModel:
    """Represents a tutorial in the database."""

    def __init__(self):
        self.db_path = DATABASE_PATH
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self) -> None:
        """Creates the 'tutorials' table in the database if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tutorials (
                tutorial_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE NOT NULL,
                channel_name TEXT,
                video_url TEXT,
                brief_description TEXT,
                contributor_id INTEGER,
                FOREIGN KEY (contributor_id) REFERENCES contributors (id)
            )
        """)
        self.conn.commit()

    def add(
        self,
        title: str,
        channel_name: str,
        video_url: str,
        brief_description: str,
        contributor_id: int,
    ) -> bool:
        """Adds a new tutorial to the database."""

        try:
            self.cursor.execute(
                """
                INSERT INTO tutorials (title, channel_name, video_url, brief_description, contributor_id)
                VALUES (?, ?, ?, ?, ?)
            """,
                (title, channel_name, video_url, brief_description, contributor_id),
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error adding tutorial: {e} - {title}")
            return False

    def title_channel_exists(self, title: str, channel_name: str) -> bool:
        """Checks if a tutorial with the given title and channel_name exists (case-insensitive)."""
        self.cursor.execute(
            """
            SELECT 1
            FROM tutorials
            WHERE LOWER(title) = LOWER(?) AND LOWER(channel_name) = LOWER(?)
        """,
            (title.lower(), channel_name.lower()),
        )
        result = self.cursor.fetchone()
        return result is not None

    def get_all(self) -> pd.DataFrame:
        """Retrieves all tutorials from the database as a pandas DataFrame."""
        return pd.read_sql_query("SELECT * FROM tutorials", self.conn)

    def __del__(self) -> None:
        """Closes the database connection when the object is destroyed."""
        self.conn.close()


class Tutorial:
    """Represents a tutorial object."""

    def __init__(
        self,
        tutorial_id: int,
        title: str,
        channel_name: str,
        video_url: str,
        brief_description: str,
        contributor_id: int,
    ):
        self.tutorial_id = tutorial_id
        self.title = title
        self.channel_name = channel_name
        self.video_url = video_url
        self.brief_description = brief_description
        self.contributor_id = contributor_id

    # Getters
    @property
    def tutorial_id(self):
        return self._tutorial_id

    @property
    def title(self):
        return self._title

    @property
    def channel_name(self):
        return self._channel_name

    @property
    def video_url(self):
        return self._video_url

    @property
    def brief_description(self):
        return self._brief_description

    @property
    def contributor_id(self):
        return self._contributor_id

    # Setters
    @tutorial_id.setter
    def tutorial_id(self, tutorial_id):
        self._tutorial_id = tutorial_id

    @title.setter
    def title(self, title):
        self._title = title

    @channel_name.setter
    def channel_name(self, channel_name):
        self._channel_name = channel_name

    @video_url.setter
    def video_url(self, video_url):
        self._video_url = video_url

    @brief_description.setter
    def brief_description(self, brief_description):
        self._brief_description = brief_description

    @contributor_id.setter
    def contributor_id(self, contributor_id):
        self._contributor_id = contributor_id
