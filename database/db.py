from datetime import datetime
import sqlite3

class Sqlite:

	def __init__(self, db_file: str):
		self.conn = sqlite3.connect(db_file, check_same_thread=False)
		self.cursor = self.conn.cursor()
		self.cursor.executescript("""CREATE TABLE IF NOT EXISTS "users" (
			user_id INTEGER NOT NULL,
			user_name TEXT
			);""")
		self.cursor.executescript("""CREATE TABLE IF NOT EXISTS "anime" (
			id INTEGER NOT NULL,
			series INTEGER,
			name TEXT,
			description TEXT,
			photo TEXT
			);""")
		self.cursor.executescript("""CREATE TABLE IF NOT EXISTS "series" (
			id INTEGER NOT NULL,
			bacground TEXT,
			serie INTEGER,
			url TEXT
			);""")

	def user_in_bd(self, user_id, user_name):
		check = self.cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
		if check.fetchone() is None:
			self.cursor.execute('INSERT INTO "users" (user_id, user_name) VALUES (?, ?)', (user_id, user_name,))
			self.conn.commit()
		else:
			pass

	def get_series(self, id, serie):
		anime_serie = self.cursor.execute("SELECT * FROM series WHERE id = ? AND serie = ?", (id, serie,)).fetchone()
		return anime_serie

	def get_anime(self, id):
		try:
			all_info = self.cursor.execute("SELECT * FROM anime WHERE id=?", (id,)).fetchone()
			return all_info
		except Exception as error:
			print(error)