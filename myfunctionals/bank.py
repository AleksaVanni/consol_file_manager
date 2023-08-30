import os

def bank_account():

    FILE_WALLET_HISTORY = 'wallet_history.txt'
    FILE_ORDERS_HISTORY = 'orders_history.txt'

    wallet_balance = 0
    purchase_history = []

    if os.path.exists(FILE_WALLET_HISTORY):
        with open(FILE_WALLET_HISTORY, 'r') as f:
            wallet_balance = float(f.read())

    if os.path.exists(FILE_ORDERS_HISTORY):
        with open(FILE_ORDERS_HISTORY, 'r') as f:
            for order in f:
                purchase_history.append(order.replace('\n', ''))

    print("Мой кошелек")
    while True:
        try:
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
                for order in purchase_history:
                    print(order)


            elif choice == '4':
                with open(FILE_WALLET_HISTORY, 'w') as f:
                    f.write(str(wallet_balance))

                with open(FILE_ORDERS_HISTORY, 'w') as f:
                    for order in purchase_history:
                        f.write(f'{order}\n')
                break

            else:
                print('Неверный пункт меню. Выберите пункт от 1 до 4.')

        except ValueError:
            print("Некорректный ввод. Введите число .....")