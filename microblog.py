# We can change 'import app' to app1 because we are importing Flask instance variable
from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Post': Post} 