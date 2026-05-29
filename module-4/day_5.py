# Divisibility checker
def check_divisibility(num) -> str:
    try:
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        else:
            return "Number not divisible by 3 or 5"
    except ValueError:
        return "Value has to be a number!"

def main() -> None:
    num = int(input("Enter a number: "))
    
    check_divisibility(num)

if __name__ == "__main__":
    main()
