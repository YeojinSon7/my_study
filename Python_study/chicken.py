age = 19
money = 25000
chicken = 20000
beer = 10000
drink = 5000

if money >= chicken:
    print("치킨을 먹는다.")
    money = money - chicken
    if money >= beer and age >=20:
        print ("맥주를 먹는다.")
        money = money - beer
    if money >= drink:
        print("음료수를 먹는다.")
