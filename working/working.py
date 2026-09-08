import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(?P<start_hour>(1[0-2]|[0-9]))(?P<start_minute>:[0-5][0-9])? (?P<first_ab>[AP]M) to (?P<end_hour>(1[0-2]|[0-9]))(?P<end_minute>:[0-5][0-9])? (?P<second_ab>[AP]M)$"
    if match := re.search(pattern, s):
        if match.group("first_ab") == "AM":
            hour = int(match.group("start_hour"))
            if hour == 12:
                hour = 0
            if match.group("start_minute"):
                minute = int(match.group("start_minute").replace(":", ""))
            else:
                minute = 0  
        else:
            hour = int(match.group("start_hour")) + 12
            if hour == 24:
                hour = 12
            if match.group("start_minute"):  
                minute = int(match.group("start_minute").replace(":", ""))
            else:
                minute = 0
        first_part = f"{hour:02d}:{minute:02d}"
        if match.group("second_ab") == "AM":
            hour = int(match.group("end_hour"))
            if hour == 12:
                hour = 0
            if match.group("end_minute"):
                minute = int(match.group("end_minute").replace(":", ""))
            else:
                minute = 0
        else:
            hour = int(match.group("end_hour")) + 12
            if hour == 24:
                hour = 12
            if match.group("end_minute"):
                minute = int(match.group("end_minute").replace(":", ""))
            else:
                minute = 0
        second_part = f"{hour:02d}:{minute:02d}"
        output = f"{first_part} to {second_part}"
        return output
        
    else:
        raise ValueError("Invalid input")




if __name__ == "__main__":
    main()
