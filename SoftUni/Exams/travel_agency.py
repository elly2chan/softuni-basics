town = input()
package_type = input()
vip_discount = input()
days = int(input())
total = 0

while True:
    if days > 7:
        days -= 1
    elif days < 1:
        print("Days must be positive number!")
        break

    if town in ("Bansko", "Borovets"):
        if package_type == "withEquipment":
            price = 100
            if vip_discount == "yes":
                price -= price * 10 / 100
            total = price * days
        elif package_type == "noEquipment":
            price = 80
            if vip_discount == "yes":
                price -= price * 5 / 100
            total = price * days
        else:
            print("Invalid input!")
            break
    elif town in ("Varna", "Burgas"):
        if package_type == "withBreakfast":
            price = 130
            if vip_discount == "yes":
                price -= price * 12 / 100
            total = price * days
        elif package_type == "noBreakfast":
            price = 100
            if vip_discount == "yes":
                price -= price * 7 / 100
            total = price * days
        else:
            print("Invalid input!")
            break
    else:
        print("Invalid input!")
        break

    print(f'The price is {total:.2f}lv! Have a nice time!')
    break