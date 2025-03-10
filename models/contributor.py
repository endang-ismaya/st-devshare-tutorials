from enum import Enum, auto
import sqlite3
from typing import Optional, Union
import pandas as pd
from pandas import DataFrame
import bcrypt

from _src.settings import DATABASE_PATH


class ContributorKeys(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return f"CONTRIBUTOR__{str(name).upper()}"

    PAGE_NUM = auto()
    USER_DATA = auto()


class Contributor:
    """Represents a contributor object (POJO)"""

    def __init__(self, user_id, username, linkedin_url, hash_password) -> None:
        self.user_id = user_id
        self.username = username
        self.linkedin_url = linkedin_url
        self.hash_password = hash_password

    def __str__(self):
        return self.username

    @property
    def user_id(self) -> int:
        if self._user_id is None:
            raise ValueError("Contributor Id is Not Available")

        return self._user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        self._user_id = value

    @property
    def username(self) -> str:
        if self._username is None:
            raise ValueError("Contributor Name is Not Available")

        return self._username

    @username.setter
    def username(self, value: str) -> None:
        self._username = value

    @property
    def linkedin_url(self) -> str:
        if self._linkedin_url is None:
            raise ValueError("Contributor LinkedIn URL is Not Available")

        return self._linkedin_url

    @linkedin_url.setter
    def linkedin_url(self, value: str) -> None:
        self._linkedin_url = value

    @property
    def hash_password(self) -> str:
        if self._hash_password is None:
            raise ValueError("Contributor Hash Password is Not Available")

        return self._hash_password

    @hash_password.setter
    def hash_password(self, value: str) -> None:
        self._hash_password = value


class ContributorModel:
    """
    Represents a contributor in the database and provides methods for managing contributor data.
    """

    def __init__(self) -> None:
        self.db_path = DATABASE_PATH
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self) -> None:
        """Creates the 'contributors' table in the database if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contributors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                linkedin_url TEXT,
                password TEXT
            )
        """)
        self.conn.commit()

    def hash_password(self, password: str) -> str:
        """Hashes a password using bcrypt."""
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")

    def check_password(self, password: str, hashed_password: str) -> bool:
        """Check is password match with hashed password."""
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

    def add(self, username: str, linkedin_url: str, password: str) -> bool:
        """Adds a new contributor to the database."""
        try:
            h_password = self.hash_password(password)
            self.cursor.execute(
                "INSERT INTO contributors (username, linkedin_url, password) VALUES (?, ?, ?)",
                (username, linkedin_url, h_password),
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error adding contributor: {e}")
            return False

    def get_all(self) -> DataFrame:
        """Retrieves all contributors from the database as a pandas DataFrame."""
        return pd.read_sql_query("SELECT * FROM contributors", self.conn)

    def get_by_id(self, contributor_id: int) -> Union[dict, None]:
        """Retrieves a contributor by their ID."""
        self.cursor.execute(
            "SELECT * FROM contributors WHERE id = ?", (contributor_id,)
        )
        result = self.cursor.fetchone()
        if result:
            columns = [description[0] for description in self.cursor.description]
            return dict(zip(columns, result))
        else:
            return None

    def get_by_id_object(self, contributor_id: int) -> Optional["Contributor"]:
        """Retrieves a contributor by their ID as a Contributor object."""
        self.cursor.execute(
            "SELECT * FROM contributors WHERE id = ?", (contributor_id,)
        )
        result = self.cursor.fetchone()
        if result:
            id, username, linkedin_url, password = result
            contributor_object = Contributor()
            contributor_object.user_id = id
            contributor_object.username = username
            contributor_object.linkedin_url = linkedin_url
            contributor_object.hash_password = password
            return contributor_object
        else:
            return None

    def get_by_username(self, username: str) -> Union[dict, None]:
        """Retrieves a contributor by their name."""
        self.cursor.execute(
            "SELECT * FROM contributors WHERE LOWER(username) = LOWER(?)", (username,)
        )
        result = self.cursor.fetchone()
        if result:
            columns = [description[0] for description in self.cursor.description]
            return dict(zip(columns, result))
        else:
            return None

    def get_by_username_object(self, username: str) -> Optional["Contributor"]:
        """Retrieves a contributor by their name as a Contributor object."""
        self.cursor.execute(
            "SELECT * FROM contributors WHERE LOWER(username) = LOWER(?)", (username,)
        )
        result = self.cursor.fetchone()
        if result:
            id, username, linkedin_url, password = result
            contributor_object = Contributor()
            contributor_object.user_id = id
            contributor_object.username = username
            contributor_object.linkedin_url = linkedin_url
            contributor_object.hash_password = password
            return contributor_object
        else:
            return None

    def update(
        self, contributor_id: int, username: str, linkedin_url: str, password: str
    ) -> bool:
        """Updates an existing contributor's information."""
        try:
            self.cursor.execute(
                "UPDATE contributors SET username = ?, linkedin_url = ?, password = ? WHERE id = ?",
                (username, linkedin_url, password, contributor_id),
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error updating contributor: {e}")
            return False

    def delete(self, contributor_id: int) -> bool:
        """Deletes a contributor from the database by ID."""
        try:
            self.cursor.execute(
                "DELETE FROM contributors WHERE id = ?", (contributor_id,)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting contributor by ID: {e}")
            return False

    def delete_by_username(self, username: str) -> bool:
        """Deletes a contributor from the database by name."""
        try:
            self.cursor.execute(
                "DELETE FROM contributors WHERE username = ?", (username,)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting contributor by username: {e}")
            return False

    def __del__(self):
        """Closes the database connection when the object is destroyed."""
        self.conn.close()
