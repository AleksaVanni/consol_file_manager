def bank_account():
    wallet_balance = 0
    purchase_history = []
    history_price = []

    print("Мой кошелек")
    while True:
        print("Баланс: ", wallet_balance)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')



        if choice == '1':
            print("Пополнение счета")
            denaro = float(input("На какую сумму пополнить счет: "))
            wallet_balance += denaro


        elif choice == '2':
            print("Покупка")
            purchase = float(input('На какую сумму хотите совершить покупку?: '))
            if purchase <= wallet_balance:
                name_purchase = input("Введите название покупки: ")
                wallet_balance -= purchase
                purchase_history.append((name_purchase, purchase))
            else:
                print("Недостаточно средств")


        elif choice == '3':
            print("История покупок: ")
            print(purchase_history)


        elif choice == '4':
            break

        else:
            print('Неверный пункт меню')