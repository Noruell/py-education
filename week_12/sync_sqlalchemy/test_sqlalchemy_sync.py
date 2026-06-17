from model import SessionLocal, User
from sqlalchemy import text

def main():
    session = SessionLocal()

    try:
    # 1. CREATE
        users = [
            User(name="Максим", age=20),
            User(name="Ваня", age=10),
            User(name="Света", age=23)
        ]

        session.add_all(users)
        session.commit()
    # 2. READ ALL
        print("========= ПОСЛЕ INSERT =========")
        all_users = session.query(User).all()
        for user in all_users:
            print(f"id: {user.id}, name: {user.name}, age: {user.age}")
    # 3. UPDATE
        user_to_update = session.query(User).filter_by(name="Максим").first()
        if user_to_update:
            user_to_update.age = 31
            session.commit()
    # 4. READ ALL (проверить обновление)
        print("========= ПОСЛЕ UPDATE =========")
        all_users = session.query(User).all()
        for user in all_users:
            print(f"id: {user.id}, name: {user.name}, age: {user.age}")
    # 5. DELETE
        user_to_delete = session.query(User).filter_by(name="Ваня").first()
        if user_to_delete:
            session.delete(user_to_delete)
            session.commit()
    # 6. READ ALL (проверить удаление)
        print("========= ПОСЛЕ DELETE =========")
        all_users = session.query(User).all()
        for user in all_users:
            print(f"id: {user.id}, name: {user.name}, age: {user.age}")

    except Exception as e:
        session.rollback()
        print(f"Ошибка: {e}")

    finally:
        session.close()


if __name__ == "__main__":
    main()