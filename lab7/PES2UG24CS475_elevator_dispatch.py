def parse_request(text):
    try:
        start, end = text.split('->')
        return int(start), int(end)
    except (AttributeError, ValueError):
        return None

def total_travel(floors_csv):
    try:
        floors = [int(f) for f in floors_csv.split(',')]
    except (AttributeError, ValueError):
        return None
    return sum(abs(floors[i + 1] - floors[i]) for i in range(len(floors) - 1))

def load_percent(text):
    try:
        load, capacity = text.split(' of ')
        return int(load) * 100 // int(capacity)
    except (AttributeError, ValueError, ZeroDivisionError):
        return None

def main():
    print("==== Running parse_request ====")
    user_input = input("Enter a request as FROM->TO (e.g. 5->9): ")
    result = parse_request(user_input)
    if result is None:
        print("Invalid input")
    else:
        print("From and To:", result)

    print("\n==== Running total_travel ====")
    user_input = input("Enter floors visited as CSV (e.g. 1,5,3,9): ")
    result = total_travel(user_input)
    if result is None:
        print("Invalid input")
    else:
        print("Floors Travelled:", result)

    print("\n==== Running load_percent ====")
    user_input = input("Enter load as 'X of Y' (e.g. 450 of 630): ")
    result = load_percent(user_input)
    if result is None:
        print("Invalid input")
    else:
        print("Load Percent:", result)

if __name__ == "__main__":
    main()
