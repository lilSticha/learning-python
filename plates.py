def main():
    plates = input("Enter plate: ")
    if is_valid(plates):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    list_s = list(s)
    # Validation len
    if len(s) < 2 or len(s) > 6:
        return False
    #check if all letter are Uper
    elif s.islower():
        return False
    # Check or is invalid sumbols
    # Check if text have only letter
    elif s.isalpha():
        return True
    #check or line are not number
    elif s.isdigit():
        return False
    else:
    # Check on number existing
        for i, char  in enumerate(s):
            if char.isdigit():
                if s[i:].isdigit() and char != '0':
                    return True
                else:
                    return False

    return False
if __name__ == "__main__":
    main()