def check_cartasian_plane(x, y) -> str:
    try:
        if x < 0 and y > 0:
            return "Top right quadrant"
        elif x > 0 and y > 0:
            return "Top left quadrant"
        elif x > 0 and y < 0:
            return "Bottom left quadrant"
        else:
            return "Bottom right quadrant"
    except ValueError:
        return "Value has to be a number!"

def main():
    x = int(input("Enter an X axis number: "))
    y = int(input("Enter a Y axis number: "))

    print(check_cartasian_plane(x, y))

if __name__ == "__main__":
    main()
