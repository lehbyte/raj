from flask import Flask

# def create_app(test_config=None):
raj = Flask(__name__)
    # if test_config is None:
raj.config.from_object('config')
    # else:
        # raj.config.from_mapping(test_config)
# db = SQLAlchemy(raj)
    # try:
        # os.makedirs(app.instance_path)
    # except OSError:
        # print "OSError"    
    # return raj



from app import models, auth, views #, blog
raj.register_blueprint(auth.bp)
# raj.register_blueprint(blog.bp)
