import requests


class Api_ip_addr:
    def __init__(self):
        self.important_info_keys = [
            "ip", "type", "continent", "continent_code", "country", 
            "country_code", "region", "region_code", "city", 
            "latitude", "longitude", "is_eu", "calling_code", "capital",
            "connection", "timezone",  
        ]

    """
    """
    
    
    def get_data_ip(self, ipv4) -> dict:
        # base_url = f"https://ipapi.co/{ipv4}/json/" # has a limit
        base_url = f"http://ipwho.is/{ipv4}"

        response = requests.get(base_url)
        data = response.json()
        
        # if data["success"] is False:
        #     print("<Invalid IP address>")
        
        # else:
        #     return data 

        if data["success"] is True:
            return data 
    # ======================================

    def displayData(self, data_ip) -> None:
        print(f"IP Address: {data_ip['ip']}\n")

        data_ip_keys = list(data_ip.keys())
        for key in sorted(data_ip_keys):
            if key in self.important_info_keys:

                if key == "timezone":
                    print(f"{key}")
                    print(f"- Zone offset: {data_ip['timezone']['offset']}")
                    print(f"- UTC: {data_ip['timezone']['utc']}")
                    print(f"- Current_time: {data_ip['timezone']['current_time']}")

                elif key == "connection":
                    print(f"{key}")
                    # print(f"ASN: {data_ip[key]}")

                    print(f"- ASN (Autonomous System Number): {data_ip[key]['asn']}")
                    print(f"- Org: {data_ip['connection']['org']}")
                    print(f"- ISP: {data_ip['connection']['isp']}")
                    print(f"- Domain: {data_ip['connection']['domain']}")


                else:
                    print(f"{key}: {data_ip[key]}")
    # ======================================

    def main_section_ip(self) -> None:
        close_program = False

        print("\nIP ADDRESS SEARCH")
        print("Type 'esc' to leave")
        
        while not close_program:
            input_ip = input("\nEnter an IPv4 address: ")

            if input_ip == "esc":
                close_program = True 
                print("leaving...")

            else: 
                try:
                    data_ip = self.get_data_ip(input_ip)
                    self.displayData(data_ip)

                except:
                    print("<Invalid IP address>")
                    # print("*an error occurred*")
    # ======================================
    # main_section_ip()
# ------------------------------------------


# test_obj = Api_ip_addr()

# test_obj.main_section_ip()


# use loop to generate a max of 100 ip addresss at a time and request info OR

# genrate as many ip addresse, and select a random one

# for n in range(255):
#     print(n, end=" ")

# print(256 ** 4)
# print(type(256 ** 4))
