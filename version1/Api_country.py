import requests
import time 

class Api_country:
    def __init__(self):
        self.important_info_keys = [ 
            "area", "borders", "capital", "capitalInfo", 
            "continents", "currencies", "languages", "latlng", 
            "maps", "population", "region", "timezones", "tld"
        ]

        self.country_names = []
        self.session_data = dict()

    """
    Some functions are used inside of other functions, instead of being used directly
    """

    # runs in the bg
    # gets called continuously
    def store_session_data(self, dataset):
        program_on = True 
        index = 0
        while program_on:
            self.session_data[1] = dataset
            index += 1

        print(self.session_data)
    # ======================================

    def save_to_file(filename="file", data="testing") -> None:
        with open(filename, "r") as f:
            f.write(data)
    # ======================================

    def internet_connection(self) -> bool:
        try:
            requests.get("https://www.google.com", timeout=5)
            response = requests.get("https://www.google.com", timeout=5)
            # print(response)
            return True
        except requests.ConnectionError:
            return False    
    # ======================================
        
    # def check_connection(self) -> None:
    #     if self.internet_connection():
    #         print("The Internet is connected.")
    #     else:
    #         print("The Internet is not connected.")
    # ======================================
        
    
    def get_all_countries(self) -> list:
        base_url = "https://restcountries.com/v3.1/all"
        response = requests.get(base_url)
        data = response.json()
        return data 
    # ======================================

    def get_data_country(self, name) -> list:
        base_url = f"https://restcountries.com/v3.1/name/{name}"
        response = requests.get(base_url)
        data = response.json()
        return data 
    # ======================================

    def store_country_names(self) -> None:
        countries = self.get_all_countries()

        # adding to country_names list
        for country in countries:
            self.country_names.append(country["name"]["common"].lower())
            self.country_names.append(country["name"]["common"])
    # ======================================


    def display_country_names(self) -> None:
        print("getting data...\n")

        countries = self.get_all_countries()
        count = 0

        # adding to list to organise in alpahbetical order
        list_of_countries = []
        for country in countries:
            country_name = (f'- {country["name"]["common"]} ({country["name"]["official"]})')
            list_of_countries.append(country_name)
            count += 1

        # display countries
        for c in sorted(list_of_countries):
            print(c)

        print(f"\nNumber of countries: {count}")
    # ======================================

    def check_country(self, country_name) -> bool:
        # adding to country_names list
        self.store_country_names()

        # checking if input is a valid country name
        response = False 
        if country_name in self.country_names:
            response = True 

        return response 
    # ======================================

    def present_country_data_all(self, country_name) -> None:
        valid = self.check_country(country_name)

        if valid: 
            data = self.get_data_country(country_name)
            count = 0 

            list_of_details = []
            # adding to list to organise in alpahbetical order
            for detail in data[0]:
                country_detail = (f"- {detail}: {data[0][detail]}")
                list_of_details.append(country_detail)
                count += 1

            # display details
            print()
            print(data[0]["name"]["common"])
            print(data[0]["name"]["official"])
            print()
            time.sleep(1)
            for detail in sorted(list_of_details):
                print(detail)

        else:
            print("*invalid input*")
    # ======================================

    def present_country_data_important(self, country_name) -> None:
        valid = self.check_country(country_name)

        if valid: 
            data = self.get_data_country(country_name)
            count = 0 

            list_of_details = []
            # adding to list to organise in alpahbetical order
            for detail in data[0]:
                if detail in self.important_info_keys:
                    country_detail = (f"- {detail}: {data[0][detail]}")
                    list_of_details.append(country_detail)
                    count += 1
            # print(count)

            # display details
            print()
            print(data[0]["name"]["common"])
            print(data[0]["name"]["official"])
            print()
            time.sleep(1)

            for detail in sorted(list_of_details):
                print(detail)
        
        else:
            print("*invalid input*")
    # ======================================


    # for arg version
    def guide() -> None:
        print("type '' to initialise")
        print("etc...")
    # ======================================

    

# ------------------------------------------
# obj = Api_country()

# obj.display_country_names()
# obj.store_country_names()

# obj.present_country_data_all("Ivory Cost")
# obj.present_country_data_important("venezuela")
# ------------------------------------------


def main_country() -> None:
    # create object
    obj = Api_country()

    close_program = False

    print("\nCOUNTRY INFO")
    print("- Type 'esc' to leave")
    print("- Type 'save' to save data to a text file")
    
    print("\nEnter a country name to display detils about that country")
    print("(use '-important' to display the important information about a country)")
    print("OR 'all' to display all country names")

    # obj.check_connection()
    # print(obj.internet_connection())

    if obj.internet_connection():
        while not close_program:
            user_in = input("\n> ")

            if user_in == "esc":
                close_program = True 
                print("leaving...")
                time.sleep(1)

            elif user_in == "all":
                obj.display_country_names()

            else: 
                try:
                    # check internet connection
                    # obj.check_connection()
                    # print(obj.internet_connection())

                    # check user input
                    a = "-i"
                    if a in user_in:
                        # solution1
                        stop = user_in.index("-")
                        user_in = (user_in[0:stop-1])

                        # solution2
                        # user_in = (user_in.split("-"))[0].strip()

                        obj.present_country_data_important(user_in)
                    else:
                        user_in = user_in.strip()
                        obj.present_country_data_all(user_in)

                # except KeyboardInterrupt:
                    # print("Keyboad...")

                except:
                    print("*INVALID INPUT*")


    else:
        print("\n*ERROR* \n<not connected to the Internet>")
# main_country()                
# ------------------------------------------

