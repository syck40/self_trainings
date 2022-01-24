MENU = {
    'sandwich': 10,
    'tea': 5,
    'salad': 9
}

def restaurant():
    bill = 0
    while True:
        answer = input("What would you like? ").strip()
        if not answer:
            print(f'Total bill is {bill}.')
            break
        if answer in MENU:
            bill = bill + MENU[answer]

restaurant()
        