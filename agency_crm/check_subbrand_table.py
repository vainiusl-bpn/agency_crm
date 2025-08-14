from app import create_app, db
from sqlalchemy import inspect

app = create_app()

with app.app_context():
    inspector = inspect(db.engine)
    if inspector.has_table('subbrands'):
        print("✓ Subbrand table already exists in the database!")
        print("  You don't need to run any migration.")
    else:
        print("✗ Subbrand table does not exist.")
        print("  Run: python create_subbrand_table.py")