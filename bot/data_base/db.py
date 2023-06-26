import psycopg2

from bot.data_base.requests.user_table import UserTable
from bot.data_base.requests.statistics_table import StatisticsTable
from bot import config

try:
    print("Connecting to database...")

    conn = psycopg2.connect(
        dbname=config.DATABASE_NAME,
        user=config.DATABASE_USER,
        password=config.DATABASE_PASSWORD,
        host=config.DATABASE_HOST,
        port=config.DATABASE_PORT)

    print("Connected to database")

    UserTable = UserTable(conn)
    StatisticsTable = StatisticsTable(conn)

except psycopg2.OperationalError:
    print("Error: Unable to connect to database")
    exit(1)
