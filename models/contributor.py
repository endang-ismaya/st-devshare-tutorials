import sqlite3
from typing import Optional, Union
import pandas as pd
from pandas import DataFrame
import bcrypt

from _src.settings import DATABASE_PATH


class Contributor:
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
                name TEXT,
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

    def add(self, name: str, linkedin_url: str, password: str) -> bool:
        """Adds a new contributor to the database."""
        try:
            self.cursor.execute(
                "INSERT INTO contributors (name, linkedin_url, password) VALUES (?, ?, ?)",
                (name, linkedin_url, password),
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
            id, name, linkedin_url, password = result
            contributor_object = Contributor()
            contributor_object.id = id
            contributor_object.name = name
            contributor_object.linkedin_url = linkedin_url
            contributor_object.password = password
            return contributor_object
        else:
            return None

    def get_by_name(self, name: str) -> Union[dict, None]:
        """Retrieves a contributor by their name."""
        self.cursor.execute("SELECT * FROM contributors WHERE name = ?", (name,))
        result = self.cursor.fetchone()
        if result:
            columns = [description[0] for description in self.cursor.description]
            return dict(zip(columns, result))
        else:
            return None

    def get_by_name_object(self, name: str) -> Optional["Contributor"]:
        """Retrieves a contributor by their name as a Contributor object."""
        self.cursor.execute("SELECT * FROM contributors WHERE name = ?", (name,))
        result = self.cursor.fetchone()
        if result:
            id, name, linkedin_url, password = result
            contributor_object = Contributor()
            contributor_object.id = id
            contributor_object.name = name
            contributor_object.linkedin_url = linkedin_url
            contributor_object.password = password
            return contributor_object
        else:
            return None

    def update(
        self, contributor_id: int, name: str, linkedin_url: str, password: str
    ) -> bool:
        """Updates an existing contributor's information."""
        try:
            self.cursor.execute(
                "UPDATE contributors SET name = ?, linkedin_url = ?, password = ? WHERE id = ?",
                (name, linkedin_url, password, contributor_id),
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error updating contributor: {e}")
            return False

    def delete(self, contributor_id):
        """Deletes a contributor from the database."""
        self.cursor.execute("DELETE FROM contributors WHERE id = ?", (contributor_id,))
        self.conn.commit()

    def __del__(self):
        """Closes the database connection when the object is destroyed."""
        self.conn.close()
