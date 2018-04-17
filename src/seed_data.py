from passlib.hash import pbkdf2_sha256

from src.models import db, User


def seed_data():
    user = User.query.all()
    if not user:
        try:
            admin_user = User()
            admin_user.username = 'admin'
            admin_user.password = pbkdf2_sha256.encrypt('admin', rounds=20000, salt_size=20)
            admin_user.email = 'anwarroyhan@gmail.com'
            admin_user.name = 'Royhan Anwar'
            admin_user.is_admin = True
            db.session.add(admin_user)
            db.session.commit()
        except:
            print('failed to add new admin user')
        
    