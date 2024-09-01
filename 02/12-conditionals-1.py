def calc_ticket_price(age: int) -> float:
    """
    Return ticket price given age
    """
    ADULT_AGE = 18  # < 18 is a child
    SENIOR_AGE = 65
    CHILDREN_TICKET_PRICE = 80.0
    ADULT_TICKET_PRICE = 100.0
    SENIOR_TICKET_PRICE = 50.0
    if age <= 0:
        raise ValueError("Age cannot be negative, or zero")

    if age < ADULT_AGE:  # child
        return CHILDREN_TICKET_PRICE
    elif age < SENIOR_AGE:  # adult
        return ADULT_TICKET_PRICE
    elif age >= SENIOR_AGE:  # senior
        return SENIOR_TICKET_PRICE
    else:
        raise Exception("Something went wrong")



def main():
    age = int(input("Enter your age: "))
    price = calc_ticket_price(age)
    print(price)


if __name__ == "__main__":
    main()