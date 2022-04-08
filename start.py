import re
import json
import os
import projects


class user:
    logged_in_email = ""
    users_file = "users.json"
    projects_file = "projects.json"
    
    @classmethod
    def user_exists(cls, email):
        if os.path.isfile(cls.users_file) == 0:
            return False
        else:
            all_users = cls.get_all_users()
            for user in all_users:
                if user["email"] == email:
                    print("User Already Exists")
                    return True
            return False

    # ================================================= #
    @classmethod
    def get_all_users(cls):
        if os.path.getsize(cls.users_file) == 0:
            return []
        else:
            file = None
            try:
                file = open(cls.users_file, "r")
                all_users = json.loads(file.read())
                return all_users
            except Exception as e:
                print("Exception Getting Users: ", e)
            finally:
                if file is not None:
                    file.close()

    # ================================================= #
    @classmethod
    def validate_login(cls, email, password):
        if os.path.getsize(cls.users_file) == 0:
            return False
        else:
            file = None
            try:
                file = open(cls.users_file, "r")
                all_users = json.load(file)
            except Exception as e:
                print("Exception: ", e)
            finally:
                if file is not None:
                    file.close()

            for user in all_users:
                if user["email"] == email and user["password"] == password:
                    print("Logged In Successfully")
                    return True
            return False

    # ================================================= #
    # First Name
    def get_first_name():
        first_name = input("Enter your first name: ")

        while not first_name.isalpha():
            print("Enter valid first name!")
            first_name = input("Enter your first name: ")

        return(first_name)

    # ================================================= #
    # Last Name
    def get_last_name():
        last_name = input("Enter your last name: ")

        while not last_name.isalpha():
            print("Enter valid last name!")
            last_name = input("Enter your last name: ")

        return(last_name)

    # ================================================= #
    # Email
    def get_email():
        email = input("Enter your email: ")

        while email.isdigit():
            print("Enter valid email!")
            email = input("Enter your email: ")

        return(email)

    # ================================================= #
    # Password
    def get_password():
        password = input("Enter your password: ")

        while len(password) < 6:
            print("Password Can't Be Less than 6 Charachters!!")
            password = input("Enter your password: ")

        confirm_password = input("Confirm Password: ")

        while confirm_password != password:
            print("Passwords didn't match")
            confirm_password = input("Confirm your password: ")

        return password

    # ================================================= #
    # Mobile
    def get_mobile():
        mobile = input("Enter your mobile: ")

        while not mobile.isdigit() or len(mobile) < 11:
            # print("Invalid Mobile Number")

            if not mobile.isdigit():
                print("Enter valid mobile number!")
            elif len(mobile) < 11:
                print("Mobile Can't Be Less than 11 number!!")

            mobile = input("Enter your mobile: ")

        return mobile

    # ================================================= #
    # Login
    @classmethod
    def login(cls):
        email = input("Email: ")
        password = input("Password: ")

        while len(password) < 6:
            print("Password Can't Be Less than 6 Charachters!!")
            password = input("Password: ")

        if cls.validate_login(email, password):
            cls.logged_in_email = email
            projects.project.project_options(cls.logged_in_email)
        else:
            print("Wrong credentials!!")

    # ================================================= #
    # Register
    @classmethod
    def register(cls):
        first_name = cls.get_first_name()
        last_name = cls.get_last_name()
        email = cls.get_email()
        password = cls.get_password()
        mobile = cls.get_mobile()

        new_user = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "mobile": mobile
        }

        all_users = cls.get_all_users()

        if not cls.user_exists(email):
            all_users.append(new_user)

            file = None
            try:
                file = open(cls.users_file, "w")
                file.write(json.dumps(all_users))
                print("User Registered Successfully")
            except Exception as e:
                print("Register Exception: ", e)
            finally:
                if file is not None:
                    file.close()

# ================================================= #
# Home Choices
def start_menu():
    print("\n", "Select your choice: ")
    print("\t", "1- Login")
    print("\t", "2- Register")
    choice = input("")

    if choice.isdigit() and int(choice) in [1, 2]:
        # login
        if int(choice) == 1:
            user.login()
        elif int(choice) == 2:
            user.register()
    else:
        print("\n" * 3)
        print("Enter valid choice!")


start_menu()
