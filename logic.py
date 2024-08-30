import sqlite3
import matplotlib

matplotlib.use('Agg')  # Установка бэкенда Matplotlib для сохранения файлов в памяти без отображения окна
import matplotlib.pyplot as plt
import cartopy.crs as ccrs  # Импорт модуля для работы с картографическими проекциями


class DB_Map():
    def __init__(self, database):
        self.database = database  # Инициализация пути к базе данных

    def create_user_table(self):
        conn = sqlite3.connect(self.database)  # Подключение к базе данных
        with conn:
            # Создание таблицы, если она не существует, для хранения городов пользователей
            conn.execute('''CREATE TABLE IF NOT EXISTS users_cities (
                                user_id INTEGER,
                                city_id TEXT,
                                FOREIGN KEY(city_id) REFERENCES cities(id)
                            )''')
            conn.commit()  # Подтверждение изменений

    def add_city(self, user_id, city_name):
        conn = sqlite3.connect(self.database)
        with conn:
            cursor = conn.cursor()
            # Запрос к базе данных на наличие города по имени
            cursor.execute("SELECT id FROM cities WHERE city=?", (city_name,))
            city_data = cursor.fetchone()
            if city_data:
                city_id = city_data[0]
                # Добавление города в список городов пользователя
                conn.execute('INSERT INTO users_cities VALUES (?, ?)', (user_id, city_id))
                conn.commit()
                return 1  # Возврат успеха операции
            else:
                return 0  # Город не найден

    def select_cities(self, user_id):
        conn = sqlite3.connect(self.database)
        with conn:
            cursor = conn.cursor()
            # Выбор всех городов пользователя
            cursor.execute('''SELECT cities.city 
                            FROM users_cities  
                            JOIN cities ON users_cities.city_id = cities.id
                            WHERE users_cities.user_id = ?''', (user_id,))
            cities = [row[0] for row in cursor.fetchall()]
            return cities  # Возврат списка городов пользователя

    def get_coordinates(self, city_name):
        conn = sqlite3.connect(self.database)
        with conn:
            cursor = conn.cursor()
            # Получение координат города по его имени
            cursor.execute('''SELECT lat, lng
                            FROM cities  
                            WHERE city = ?''', (city_name,))
            coordinates = cursor.fetchone()
            return coordinates  # Возврат координат города

    def create_graph(self, path, cities):
        pass

    def draw_distance(self, city1, city2):
        # Рисование линии между двумя городами для отображения расстояния
        pass


if __name__ == "__main__":
    m = DB_Map("database.db")  # Создание объекта для работы с базой данных
    m.create_user_table()  # Создание таблицы пользователей и городов, если она еще не существует
