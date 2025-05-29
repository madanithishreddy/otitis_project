from .models import User
from .schemas import UserCreate
from databases import Database
from src.database import DATABASE_URL

# DATABASE_URL = "postgresql://postgres:password@172.18.0.3:5432/voyage_imaging"
# DATABASE_URL = config('DATABASE_URL')
database = Database(DATABASE_URL)


async def create_admin():
    """ This function creates admin user.
    """
    print("Connecting to db", DATABASE_URL)
    await database.connect()
    print("Creating admin")

    data = {'full_name': 'Admin', 'email': 'admin@admin.com', 'password': 'password'}
    query = User.__table__.select().where(User.email == data['email'])
    existing_user = await database.fetch_one(query)

    if existing_user:
        print(f"Admin user with email {data['email']} already exists.")
    else:
        user = UserCreate(**data)
        user.hash_password()
        query = User.__table__.insert().values(**user.dict()).returning(User)
        try:
            new_user = await database.fetch_one(query)
            print("Admin user created with email: ", new_user.email)
        except Exception as e:
            print("ERROR:", e)

    await database.disconnect()
