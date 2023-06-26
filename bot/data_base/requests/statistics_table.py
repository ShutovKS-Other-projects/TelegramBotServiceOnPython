from bot.data_base.requests.user_table import UserTable


class StatisticsTable:
    def __init__(self, conn):
        print("StatisticsTable init")
        self.conn = conn

        cur = conn.cursor()
        cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)",
                    (self.table_name,))
        result = cur.fetchone()[0]
        cur.close()

        if result is False:
            cur = conn.cursor()
            cur.execute(f"CREATE TABLE {self.table_name} ("
                        f"{self.stat_id} SERIAL PRIMARY KEY, "
                        f"{self.user_id} INT REFERENCES {UserTable.table_name}({UserTable.user_id}), "
                        f"{self.message_count} INT, "
                        f"{self.picture_count} INT, "
                        f"{self.sticker_count} INT"
                        f")")
            self.conn.commit()
            cur.close()
            print("StatisticsTable created")

    table_name = "statistics_table"

    stat_id = "stat_id"
    user_id = "user_id"
    message_count = "message_count"
    picture_count = "picture_count"
    sticker_count = "sticker_count"

    def add_stat(self, user_id, message_count=0, picture_count=0, sticker_count=0):
        """
        :type user_id: int
        :type message_count: int
        :type picture_count: int
        :type sticker_count: int
        """
        cur = self.conn.cursor()
        cur.execute(
            f"INSERT INTO {self.table_name} ({self.user_id}, {self.message_count}, {self.picture_count}, {self.sticker_count}) VALUES ({user_id}, {message_count}, {picture_count}, {sticker_count})")
        self.conn.commit()
        cur.close()

    def get_stat(self, user_id):
        """
        :type user_id: int
        :rtype: tuple of int
        """
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM {self.table_name} WHERE {self.user_id} = {user_id}")
        result = cur.fetchone()
        cur.close()
        return result

    def get_all_stats(self):
        """
        :rtype: list of tuple of int
        """
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM {self.table_name}")
        result = cur.fetchall()
        cur.close()
        return result

    def increase_stat(self, user_id, message_count=0, picture_count=0, sticker_count=0):
        """
        :type user_id: int
        :type message_count: int
        :type picture_count: int
        :type sticker_count: int
        """
        if self.is_stat(user_id) is False:
            add_stat(user_id, message_count, picture_count, sticker_count)
            return
        else:
            cur = self.conn.cursor()
            cur.execute(f"UPDATE {self.table_name} "
                        f"SET {self.message_count} = {message_count} + {message_count}, "
                        f"{self.picture_count} = {picture_count} + {picture_count}, "
                        f"{self.sticker_count} = {sticker_count} + {sticker_count} "
                        f"WHERE {self.user_id} = {user_id}")
            self.conn.commit()
            cur.close()

    def is_stat(self, user_id):
        """
        :type user_id: int
        :rtype: bool
        """
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM {self.table_name} WHERE {self.user_id} = {user_id}")
        result = cur.fetchone()
        cur.close()
        if result is None:
            return False
        else:
            return True

    def delete_stat(self, user_id):
        """
        :type user_id: int
        """
        cur = self.conn.cursor()
        cur.execute(f"DELETE FROM {self.table_name} WHERE {self.user_id} = {user_id}")
        self.conn.commit()
        cur.close()

    def delete_all_stats(self):
        cur = self.conn.cursor()
        cur.execute(f"DELETE FROM {self.table_name}")
        self.conn.commit()
        cur.close()
