from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Packages.models import Users, Phone_numbers, Base
 
def insert_phonenumber():
    # добавить номер телефона пользователю по его id
    engine = create_engine('sqlite:///sqlalchemy_phone_book.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    kekid = input("ID: ")
    username = session.query(Users).filter_by(id=kekid).first()
    if username:
        c = input("Number: ")
        username_phone_number = Phone_numbers(phone_number=c, user=username)
        session.add(username_phone_number)
        session.commit()
        print(f"\nДобавлен новый номер телефона для ID {kekid}!\n")
        input("Чтобы подолжить нажмите Enter")
    else: 
        print(f"\nПользователя под таким id не существует!\n")
        input("Чтобы подолжить нажмите Enter")
        

if __name__ == "__main__":
    insert_phonenumber()