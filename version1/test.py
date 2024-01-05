from Api_ip_addr import Api_ip_addr as Api_1
from Api_country import main_country


def main_menu():
    print("\nFullscreen (Windows OS, cmd) -> [ALT + ENTER]")

    print("\nMAIN MENU\n")
    print("1. IPv4")
    print("2. Country info")

    valid = False 
    while not valid:
        user_choice = input("\n> ")
        if user_choice == "1":
            valid = True 
            test_obj = Api_1()
            test_obj.main_section_ip()

        elif user_choice == "2":
            main_country()
            valid = True 

        else:
            print("*invalid input*")
# ======================================

# main_menu()

