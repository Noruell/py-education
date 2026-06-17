from week_12.sync_sqlalchemy.model_prac import SessionLocal, User

def print_all_users(session):
    all_users = session.query(User).all()
    for user in all_users:
        print(f"id: {user.id}, name: {user.name}, age: {user.age}")


def main():
    session = SessionLocal()

    users = [
        User(name="Абдалбек", age=33),
        User(name="Дэни", age=21)
    ]
    try:
        session.add_all(users)
        session.commit()
        print_all_users(session) # Добавление новых

        user_to_update = session.query(User).filter_by(name="Света").first()
        if user_to_update:
            user_to_update.age = 11
            session.commit()
        print_all_users(session)

        user_to_delete = session.query(User).filter_by(name="Дэни").first()
        if user_to_delete:
            session.delete(user_to_delete)
            session.commit()
        print_all_users(session)
        
    except Exception as e:
        session.rollback()
        print(f"Ошибка: {e}")

    finally:
        session.close()

    

if __name__ == "__main__":
    main()

