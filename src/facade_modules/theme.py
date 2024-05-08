import os
import sqlite3
from datetime import datetime
from time import sleep
from src.director import Director

class SeasonThemeManager:
    DB_PATH = os.path.join('assets', 'data', 'smark.db')
    
    def __init__(self):
        self._create_tables()
        
    def _create_tables(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS season_dates (
                    id INT PRIMARY KEY,
                    hemisphere VARCHAR(50),
                    spring_start VARCHAR(5),
                    summer_start VARCHAR(5),
                    autumn_start VARCHAR(5),
                    winter_start VARCHAR(5),
                    is_selected BOOLEAN
                );
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS themes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    season VARCHAR(50),
                    year INT,
                    theme TEXT
                );
            ''')
            cursor.execute("SELECT COUNT(*) FROM season_dates")
            if cursor.fetchone()[0] == 0:
                cursor.execute('''
                    INSERT INTO season_dates (id, hemisphere, spring_start, summer_start, autumn_start, winter_start, is_selected)
                    VALUES
                        (1, 'Northern', '03-20', '06-21', '09-22', '12-21', FALSE),
                        (2, 'Southern', '09-22', '12-21', '03-20', '06-21', FALSE);
                ''')
            conn.commit()
    
    def manage_theme(self):
        if not self._is_hemisphere_set():
            self._set_hemisphere()
        
        current_theme = self.get_current_theme()
        if current_theme is None:
            self._update_theme()
        else:
            Director().print(f"Season: {self._get_current_season()}\nTheme: {current_theme}")
            sleep(1)
    
    def _is_hemisphere_set(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM season_dates WHERE is_selected = TRUE")
            return cursor.fetchone()[0] == 1
    
    def _set_hemisphere(self):
        hemisphere = input("Enter your hemisphere (Northern/Southern): ")
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE season_dates SET is_selected = FALSE")
            cursor.execute("UPDATE season_dates SET is_selected = TRUE WHERE hemisphere = ?", (hemisphere,))
            conn.commit()
    
    def _get_current_season(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT hemisphere, spring_start, summer_start, autumn_start, winter_start FROM season_dates WHERE is_selected = TRUE")
            data = cursor.fetchone()
            
            month_day = datetime.now().strftime('%m-%d')
            spring, summer, autumn, winter = data[1:5]
            
            if spring <= month_day < summer:
                return 'spring'
            elif summer <= month_day < autumn:
                return 'summer'
            elif autumn <= month_day < winter:
                return 'autumn'
            else:
                return 'winter'
    
    def get_current_theme(self):
        season = self._get_current_season()
        year = datetime.now().year
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT theme FROM themes WHERE season = ? AND year = ?", (season, year))
            result = cursor.fetchone()
            return result[0] if result else None
    
    def _update_theme(self):
        season = self._get_current_season()
        year = datetime.now().year
        new_theme = input(f"Enter the new theme for {season} {year}: ")
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO themes (season, year, theme) VALUES (?, ?, ?)", (season, year, new_theme))
            conn.commit()
            print("Theme updated successfully.")