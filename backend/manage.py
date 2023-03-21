# from os.path import join, dirname
# from dotenv import load_dotenv
# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand

# from app.models import db
# from server import app

# from app.models.url import Url

# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

# migrate = Migrate(app, db)
# manager = Manager(app)

# manager.add_command('db', MigrateCommand)

# if __name__ == '__main__':
#     manager.run()