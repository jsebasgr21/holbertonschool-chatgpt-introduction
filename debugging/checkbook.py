class Checkbook:
    """
    Una clase que representa una chequera para manejar depósitos, retiros y consultar saldo.
    """

    def __init__(self):
        """
        Inicializa el balance de la chequera en 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Depósito de una cantidad en el balance.

        Parámetros:
        amount (float): El monto a depositar.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retira una cantidad del balance si los fondos son suficientes.

        Parámetros:
        amount (float): El monto a retirar.

        Retorna:
        None: Si los fondos son insuficientes, muestra un mensaje de error.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Muestra el balance actual de la cuenta.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Función principal que permite al usuario interactuar con la chequera para realizar depósitos,
    retiros, consultar el saldo, o salir del programa. Incluye manejo de errores para entradas no válidas.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("You cannot deposit a negative amount. Please try again.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("You cannot withdraw a negative amount. Please try again.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
