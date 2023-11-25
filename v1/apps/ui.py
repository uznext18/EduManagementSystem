from datetime import datetime

from v1.apps import User, sequence_id
from v1.common import UserRole

session_user: User | None = None


class UI:
    def main(self):
        menu = input("""
        1. Register
        2. Login
        3. Exit
        >>> """)
        match menu:
            case "1":
                self.register()
            case "2":
                self.login()
            case "3":
                print("Goodbye!")
            case _:
                print("Wrong input")

    def register(self):
        user = {
            "id": sequence_id(),
            "username": input("Enter new username: "),
            "email": input("Enter new email: "),
            "password": input("Enter new password: "),
            "join_date": str(datetime.now().strftime("%d/%m/%Y"))
        }
        try:
            user_dto = User(**user)
            try:
                user_dto.save()
                # print(user_dto.__dict__)
                print(f"You are now logged in as a guest.\n"
                      f"Wait until the invitation message comes to your email.\n"
                      f"Our moderators will register you within 3 days.")
            except Exception as e:
                print(e)
            # print(user_dto.__dict__)
            self.main()
        except Exception as e:
            print(e)

    def login(self):
        global session_user
        user = {
            "username": input("Enter your username: \n>>> "),
            "password": input("Enter your password \n>>> "),
        }
        user = User(**user)
        try:
            session_user = user.has_login()
            print("You are logged in successfully")
            match session_user['role']:
                case UserRole.ADMIN.value:
                    self.admin_menu()
                case UserRole.MODERATOR.value:
                    self.moderator_menu()
                case UserRole.TEACHER.value:
                    self.teacher_menu()
                case UserRole.STUDENT.value:
                    self.student_menu()
                case UserRole.GUEST.value:
                    self.guest_menu()
        except Exception as e:
            print(e)
            self.main()

    def admin_menu(self):
        pass

    def moderator_menu(self):
        pass

    def teacher_menu(self):
        pass

    def student_menu(self):
        pass

    def guest_menu(self):
        pass
