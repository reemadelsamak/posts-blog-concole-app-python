import os
import json
# import start as main


class project:
    users_file = "users.json"
    projects_file = "projects.json"

    def edit_options(project):
        print("\n", "Select your choice: ")
        print("\t", "1- Edit Title")
        print("\t", "2- Edit Details")
        print("\t", "3- Edit Total Target")
        print("\t", "4- Edit Start Date")
        print("\t", "5- Edit End Date")
        choice = input("")
        if choice.isdigit() and int(choice) in [1, 2, 3, 4, 5]:
            # login
            if int(choice) == 1:
                project["title"] = input("Enter New Title: ")
            elif int(choice) == 2:
                project["details"] = input("Enter New details: ")
            elif int(choice) == 3:
                project["total_target"] = input("Enter New Total Target: ")
                while not project["total_target"].isdigit():
                    print("Enter Valid Total Target!")
                    project["total_target"] = input("Enter New Total Target: ")
            elif int(choice) == 4:
                project["start_date"] = input("Enter New Start Date: ")
            elif int(choice) == 5:
                project["end_date"] = input("Enter New End Date: ")
        else:
            print("\n")
            print("Enter valid choice!")

    # ================================================= #
    @classmethod
    def project_options(cls, logged_in_email):
        print("\n", "Select your choice: ")
        print("\t", "1- Create Project")
        print("\t", "2- View All Projects")
        print("\t", "3- Edit Project")
        print("\t", "4- Delete Project")
        choice = input("")

        if choice.isdigit() and int(choice) in [1, 2, 3, 4]:
            # login
            if int(choice) == 1:
                cls.create_project(logged_in_email)
                # pass
            elif int(choice) == 2:
                all_projects = cls.get_all_projects()
                if all_projects == []:
                    print('No Projects Yet')
                else:
                    for line in all_projects:
                        print(line)
            elif int(choice) == 3:
                cls.edit_project(logged_in_email)
            elif int(choice) == 4:
                cls.delete_project(logged_in_email)
            elif int(choice) == 5:
                pass
        else:
            print("\n")
            print("Enter valid choice!")

    # ================================================= #
    @classmethod
    def project_exists(cls, logged_in_email, project_title):
        all_projects = cls.get_all_projects()
        if len(all_projects) == 0:
            return False
        for project in all_projects:
            if project["title"] == project_title and project["user_email"] == logged_in_email:
                return True
        return False

    # ================================================= #
    @classmethod
    def create_project(cls, logged_in_email):
        user_email = logged_in_email
        title = input("Enter Project Title: ")
        details = input("Enter project details: ")

        total_target = input("Enter Total Target: ")

        while not total_target.isdigit():
            print("Enter Valid Total Target!")
            total_target = input("Enter Total Target: ")

        start_date = input("Enter Start Date: ")
        end_date = input("Enter End Date: ")

        all_projects = cls.get_all_projects()

        project = {
            "user_email": user_email,
            "title": title,
            "details": details,
            "total_target": total_target,
            "start_date": start_date,
            "end_date": end_date,
        }

        all_projects.append(project)

        file = None
        try:
            file = open(cls.projects_file, "w")
            file.write(json.dumps(all_projects))
            print("Project Created Successfully")
        except Exception as e:
            print("Creating Project Exception: ", e)
        finally:
            if file is not None:
                file.close()

    # ================================================= #
    @classmethod
    def get_all_projects(cls):
        if os.path.getsize(cls.projects_file) == 0:
            return []
        else:
            file = None
            try:
                file = open(cls.projects_file, "r")
                all_projects = json.loads(file.read())
                return all_projects
            except Exception as e:
                print("Exception Getting Projects: ", e)
            finally:
                if file is not None:
                    file.close()

    # ================================================= #
    @classmethod
    def get_user_projects(cls, logged_in_email):
        all_projects = cls.get_all_projects()
        for project in all_projects:
            if project["user_email"] == logged_in_email:
                print(project)

    # ================================================= #
    @classmethod
    def edit_project(cls, logged_in_email):
        cls.get_user_projects(logged_in_email)
        project_title = input("Enter project title: ")

        if not cls.project_exists(logged_in_email, project_title):
            print("Project not exists!")
            return

        all_projects = cls.get_all_projects()
        for project in all_projects:
            if project["title"] == project_title and project["user_email"] == logged_in_email:
                cls.edit_options(project)
                file = None
                try:
                    file = open(cls.projects_file, "w")
                    file.write(json.dumps(all_projects))
                    print("Project Edited Successfully")
                except Exception as e:
                    print("Edit Project Exception: ", e)
                finally:
                    if file is not None:
                        file.close()
                break

    # ================================================= #
    @classmethod
    def delete_project(cls, logged_in_email):
        all_projects = cls.get_user_projects(logged_in_email)
        project_title = input("Enter project title: ")

        if not cls.project_exists(logged_in_email, project_title):
            print("Project not exists!")
            return

        all_projects = cls.get_all_projects()
        for project in all_projects:
            if project["title"] == project_title and project["user_email"] == logged_in_email:
                all_projects.remove(project)
                file = None
                try:
                    file = open(cls.projects_file, "w")
                    file.write(json.dumps(all_projects))
                    print("Project Deleted Successfully")
                except Exception as e:
                    print("Delete Project Exception: ", e)
                finally:
                    if file is not None:
                        file.close()
                break
