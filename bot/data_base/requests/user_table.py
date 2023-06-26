class UserTable:
    def __init__(self, conn):
        print("UserTable init")
        self.conn = conn

        cur = self.conn.cursor()
        cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)",
                    (self.table_name,))
        result = cur.fetchone()[0]
        cur.close()

        if result is False:
            cur = self.conn.cursor()
            cur.execute(f"CREATE TABLE {self.table_name} ("
                        f"{self.user_id} SERIAL PRIMARY KEY, "
                        f"{self.user_name} VARCHAR(255), "
                        f"{self.email} VARCHAR(255), "
                        f"{self.phone_number} VARCHAR(20), "
                        f"{self.vk_link} VARCHAR(255))"
                        )
            self.conn.commit()
            cur.close()
            print("UserTable created")

    table_name = "user_table"

    user_id = "user_id"
    user_name = "username"
    email = "email"
    phone_number = "phone_number"
    vk_link = "vk_link"

    def add_user(self, user_id, user_name=None, email=None, phone_number=None, vk_link=None):
        """
        :type user_id: int
        :type user_name: str
        :type email: str
        :type phone_number: str
        :type vk_link: str
        """
        if self.is_user(user_id): return
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO {self.table_name} "
                    f"VALUES ({user_id}, '{user_name}', '{email}', '{phone_number}', '{vk_link}')")
        self.conn.commit()
        cur.close()

    def is_user(self, user_id):
        """
        :type user_id: int
        :rtype: bool
        """
        cur = self.conn.cursor()
        cur.execute(f"SELECT EXISTS (SELECT 1 FROM {self.table_name} "
                    f"WHERE {self.user_id} = {user_id})")
        result = cur.fetchone()[0]
        cur.close()
        return result

    def delete_user(self, user_id):
        """
        :type user_id: int
        """
        if self.is_user(user_id) is False: return
        cur = self.conn.cursor()
        cur.execute(f"DELETE FROM {self.table_name} "
                    f"WHERE {self.user_id} = {user_id}")
        self.conn.commit()
        cur.close()

    def delete_all_users(self, ):
        cur = self.conn.cursor()
        cur.execute(f"DELETE FROM {self.table_name}")
        self.conn.commit()
        cur.close()

    def get_all_user_id(self, ):
        """
        :rtype: list of int
        """
        cur = self.conn.cursor()
        cur.execute(f"SELECT {self.user_id} FROM {self.table_name}")
        users = cur.fetchall()
        cur.close()
        return [user[0] for user in users]

    def get_user_name(self, user_id):
        """
        :type user_id: int
        :rtype: str
        """
        if self.is_user(user_id) is False: return
        cur = self.conn.cursor()
        cur.execute(f"SELECT user_name FROM {self.table_name} WHERE {self.user_id} = {user_id}")
        user_name = cur.fetchone()
        cur.close()
        return user_name[0]

    def get_user_email(self, user_id):
        """
        :type user_id: int
        :rtype: str
        """
        if self.is_user(user_id) is False: return
        cur = self.conn.cursor()
        cur.execute(f"SELECT email FROM {self.table_name} WHERE {self.user_id} = {user_id}")
        email = cur.fetchone()
        cur.close()
        return email[0]

    def get_user_phone_number(self, user_id):
        """
        :type user_id: int
        :rtype: str
        """
        if self.is_user(user_id) is False: return
        cur = self.conn.cursor()
        cur.execute(f"SELECT phone_number FROM {self.table_name} WHERE {self.user_id} = {user_id}")
        phone_number = cur.fetchone()
        cur.close()
        return phone_number[0]

    def get_user_vk_link(self, user_id):
        """
        :type user_id: int
        :rtype: str
        """
        if self.is_user(user_id) is False: return
        cur = self.conn.cursor()
        cur.execute(f"SELECT vk_link FROM {self.table_name} WHERE {self.user_id} = {user_id}")
        vk_link = cur.fetchone()
        cur.close()
        return vk_link[0]

    def get_user_info(self, user_id):
        """
        :type user_id: int
        :rtype: dict
        """
        if self.is_user(user_id) is False: return
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM {self.table_name} WHERE {self.user_id} = {user_id}")
        user_info = cur.fetchone()
        cur.close()
        return {
            user_id: user_info[0],
            user_name: user_info[1],
            email: user_info[2],
            phone_number: user_info[3],
            vk_link: user_info[4]
        }
