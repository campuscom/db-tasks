from config.config import Config
import mongoengine


class MongoEngine:

    @staticmethod
    def connect():
        return mongoengine.connect(
            Config.MONGODB_DATABASE,
            host=Config.MONGODB_HOST,
            port=Config.MONGODB_PORT,
            username=Config.MONGODB_USERNAME,
            password=Config.MONGODB_PASSWORD,
            authentication_source=Config.MONGODB_AUTH_DATABASE
        )
