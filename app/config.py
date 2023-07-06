import logging
import os
import pathlib

from dotenv import load_dotenv

"""
Example config project class, use to load env and others configuration.

Crate class method to handle individual configuration and been able to scalade
and debug easily
"""


class Config:
    logger = logging.getLogger()

    def __init__(self):
        self.config_logger()
        self.load_env()
        self.load_database_config()
        self.load_example_config()

    def config_logger(self):
        logging.basicConfig(
            format='%(asctime)s %(levelname)s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        log_wp = logging.getLogger(__name__)
        hdlr = logging.StreamHandler()
        fhdlr = logging.FileHandler("app.log")
        log_wp.addHandler(hdlr)
        log_wp.addHandler(fhdlr)
        log_wp.setLevel(logging.DEBUG)

        self.logger = log_wp

    def load_env(self) -> None:
        try:
            load_dotenv()
            env_path = pathlib.Path('.') / '.env'
            load_dotenv(dotenv_path=env_path)
        except Exception as e:
            logging.warning(f"Failed to load .env file: {e}")

    def load_database_config(self) -> None:
        db_user = os.getenv('DB_USER')
        db_pass = os.getenv('DB_PASS')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_name = os.getenv('DB_NAME')

        if all([db_user, db_pass, db_host, db_port, db_name]):
            self.database_url = (
                f'postgresql+psycopg2://{db_user}:{db_pass}@'
                f'{db_host}/{db_port}{db_name}'
            )
        else:
            self.logger.error("Incomplete database configuration."
                              "Please check environment variables.")

    def load_example_config(self) -> None:
        self.example_url = os.getenv("EXAMPLE_URL")
        self.example_users = os.getenv("EXAMPLE_QUEUE_USERS")
        self.example_errors = os.getenv("EXAMPLE_ERROR")

        if not all([
            self.example_url,
            self.example_users,
            self.example_errors
        ]):
            self.logger.warning("Incomplete exampleconfiguration."
                                "Please check environment variables.")


config = Config()
