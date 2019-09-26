import migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import SQLALCHEMY_DATABASE_URI
import os.path

db.create__all()

if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'db_repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_MIGRATE_REPO, SQLALCHEMY_MIGRATE_REPO, api.version_control(SQLALCHEMY_MIGRATE_REPO))