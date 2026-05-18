import sqlite3

from fontTools.ttLib.tables.ttProgram import instructions

from challange import Recipe, RecipeCreate


def create_connection():
    """Creates a connection to the SQLite database."""
    connection = sqlite3.connect("recipe.db")
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    """Creates the movies table in the database if it doesn't exist."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            instructions TEXT NOT NULL,
            author TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()


create_table()


def create_recipe(recipes: RecipeCreate) -> int:
    """
    Adds a new movie to the database.

    Args:
        movie (MovieCreate): A pydantic model containing the title and director of the movie to be created.

    Returns:
        int: The ID of the newly created movie in the database.
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO recipes (name, instructions, author) VALUES (?, ?, ?)", (recipes.name, recipes.instructions, recipes.author))
    connection.commit()
    recipe_id = cursor.lastrowid
    connection.close()
    return recipe_id


def read_recipes():
    """s


    Returns:
        list: A list of recipe models representing all movies in the database.
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM recipes")
    rows = cursor.fetchall()
    connection.close()
    recipes = [
        Recipe(
            id=row[0],
            name=row[1],
            instructions=row[2],
            author=row[3]
        )
        for row in rows
    ]
    return recipes


def read_recipe(recipe_id: int):
    """
    Retrieves a single movie from the database by its ID.

    Args:
        movie_id (int): The ID of the movie to retrieve.

    Returns:
        Movie: A Movie model representing the retrieved movie.
        Returns None if the movie is not found.
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM recipes WHERE id = ?", (recipe_id,))
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return None
    return Recipe(id=row["id"], name=row["name"], instructions=row["instructions"],author=row["author"])


def update_recipe(recipe_id: int, recipes: RecipeCreate) -> bool:
    """
    Updates an existing movie in the database.

    Args:
        movie_id (int): The ID of the movie to update.
        movie (MovieCreate): A pydantic model containing the new title and director of the movie.

    Returns:
        bool: True if the movie was updated successfully, False otherwise.
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE recipes SET name = ?, instructions = ?, author = ? WHERE id = ?",
        (recipes.name, recipes.instructions, recipes.author, recipe_id)
    )
    connection.commit()
    updated = cursor.rowcount
    connection.close()
    return updated > 0


def delete_recipe(recipe_id: int) -> bool:
    """
    Deletes a movie from the database by its ID.

    Args:
        movie_id (int): The ID of the movie to delete.

    Returns:
        bool: True if the movie was deleted successfully, False otherwise.
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted > 0