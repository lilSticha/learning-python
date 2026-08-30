def main():
    age = int(input("Enter your age: "))
    promo = input("Enter your promo code: ")
    choose_price(age, promo)
    

def choose_price(x:int, y):
    price = 0
    if x < 0 or x > 120:
        print("Error")
        return
    elif x >= 65:
        price = 45
    elif x >= 18:
        price = 100
    elif x >= 7:
        price = 50
    else:
        price = 0

    if y in ( "STUDENT" or "LEARNER") and price != 0:
        price = price * 0.9
    elif y == "HOGWARTS":
        price = 0

    print(f"Your ticket price is {price} grn" )
    return
    

if __name__ == "__main__":
    main()


    

































"""
# LESSON TRAINING 
#Compare two numbers
x = int(input("Enter x: "))
y = int(input("ENter y: "))

if x > y or x < y: # if x == 0 adn y == x: print("x is equel to y and it equals 0")
    print("x is not equal to y")
    
   # print("x is greater than y")
#elif x < y:
  #  print("y is greater than x")
    
else:
    print("x is equal to y")
 
# What grade is student got
grade = int(input("Enter your grade: "))
if grade > 100 or grade < 0:
    print("Wrong grade")
elif 90 <= grade < 100:
    print("Your mark is: A") 
elif 80 <= grade < 90:
    print("Your mark is: B")
elif 70 <- grade < 80:
    print("Your mark is: C")
elif 60 <= grade < 70: 
    print("Your mark is: D")
else:
    print("Your mark is: F")
   
   # The number is even or odd 
def main():
    x = int(input("Enter x: "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

def is_even(n):
    return (n % 2 == 0)

if __name__ == "__main__":
    main()

#Where persone live?

name = input("Enter your name: ")

match name:
    case "Garry" | "Ivan" | "Hermione":
        print("You live in Hogwarts")
    case "John" | "Jane" | "Jack":
        print("You live in London")
    case _:
        print("Who?")
        """