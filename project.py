import datetime


class Client:

    clients = []

    def __init__(self, address):
        self.address = address
        self.client_accounts = []

    def list_clients():
        for client in Client.clients:
            print(f"\n>>> {str(client)}")

    @staticmethod
    def filter_client():
        ssn = input("\n>>> Enter the SSN (numbers only): ")
        for person in Client.clients:
            if person._ssn == ssn:
                return person
        else:
            return None


class Individual(Client):
    def __init__(self, name, ssn, date_of_birth, address):
        super().__init__(address)
        self._name = name
        self._ssn = ssn
        self._date_of_birth = date_of_birth

        if not Individual.ssn_exists(ssn):
            Individual.clients.append(self)
            print(f"\n>>> Client {self._name} registered successfully.")
        else:
            print(
                "\n>>> Couldn't complete registration. This SSN is already registered."
            )

    def __str__(self):
        accounts_info = "\n".join(str(account) for account in self.client_accounts)
        return f"\n>>> Name: {self._name}   SSN: {self._ssn}\n>>> Accounts:\n>>> {accounts_info}\n"

    def register_client():
        ssn = input("\n>>> Enter the SSN (numbers only): ")
        date_of_birth = input(">>> Enter the date of birth YYYY-MM-DD: ")

        if not validate_date(date_of_birth):
            print("\n>>> Invalid date of birth format")
            return None

        client_name = input(">>> Enter the client's name: ")
        address = input(
            ">>> Enter the complete address (street, number - neighborhood - city/state abbreviation): "
        )

        client = Individual(client_name, ssn, date_of_birth, address)

        return client

    @classmethod
    def ssn_exists(cls, ssn):
        return any(person._ssn == ssn for person in cls.clients)

    @property
    def get_name(self):
        return self._name

    @property
    def get_ssn(self):
        return self._ssn

    @property
    def get_date_of_birth(self):
        return self._date_of_birth

    @property
    def get_accounts(self):
        return self.client_accounts


class Account:

    bank_accounts = []
    total_accounts = 1
    withdrawal_requested = False
    deposit_requested = False

    def __init__(self, client):
        if client:
            self._balance = 0
            self._agency = "0001"
            self._number = Account.total_accounts
            self._client = client
            self._ssn = client._ssn
            self._statement = ""
            self._num_withdrawals = 0
            self._withdrawal_limit = 3
            self._limit_per_withdrawal = 500
            client.client_accounts.append(self)
            print(
                f"\n>>> Account no. {self._number} opened successfully for SSN {client._ssn}."
            )
            self.bank_accounts.append(self)
            Account.total_accounts += 1
        else:
            print(f"\n>>> SSN not found.")

    def open_new_account():
        client = Client.filter_client()
        if client:
            Account(client)
        else:
            print(f"\n>>> SSN not found.")

    def check_account():
        filtered_client = Client.filter_client()

        if filtered_client:
            for client in Client.clients:
                if client.client_accounts:
                    ssn = filtered_client._ssn
                    for account in Account.bank_accounts:
                        if account._ssn == ssn:
                            return account
                    else:
                        return False

                else:
                    print("\n>>> Client found, but does not have an account.")
                    return False

        else:
            print(f"\n>>> SSN not found.")
            return False

    def deposit(self, deposited_amount):
        self._balance += deposited_amount
        self.deposit_requested = True
        print(
            f"\n>>> You deposited $ {deposited_amount:.2f} successfully.\n>>> Your current balance is $ {self._balance:.2f}"
        )

    def check_deposit():
        verified_account = Account.check_account()

        if verified_account:
            deposit_amount = input("\n>>> Amount to deposit: ")
            if is_number(deposit_amount):

                validated_deposit_amount = float(deposit_amount)

                if validated_deposit_amount > 0:
                    verified_account.deposit(validated_deposit_amount)
                    verified_account.update_statement(validated_deposit_amount)

                else:
                    return "\n>>> Invalid deposit amount."

            else:
                return "\n>>> Invalid deposit amount."
        else:
            return

    def withdraw(self, withdrawn_amount):
        self._balance -= withdrawn_amount
        self.withdrawal_requested = True
        print(
            f"\n>>> You withdrew $ {withdrawn_amount:.2f} successfully.\n>>> Your current balance is $ {self._balance:.2f}"
        )
        self._num_withdrawals += 1

    def check_withdrawal():
        verified_account = Account.check_account()
        if verified_account:
            withdrawal_amount = input("\n>>> Amount you want to withdraw: ")

            if is_number(withdrawal_amount):
                validated_withdrawal_amount = float(withdrawal_amount)

            if validated_withdrawal_amount > verified_account._balance:
                print("\n>>> Withdrawal not made. Insufficient balance.")

            elif validated_withdrawal_amount > verified_account._limit_per_withdrawal:
                print(
                    "\n>>> Withdrawal not made. Amount exceeds the limit per transaction."
                )

            elif validated_withdrawal_amount <= 0:
                print("\n>>> Withdrawal not made. The amount entered is invalid.")

            elif (
                verified_account._num_withdrawals >= verified_account._withdrawal_limit
            ):
                print(
                    "\n>>> Withdrawal not made. Maximum number of withdrawals already reached."
                )

            else:
                verified_account.withdraw(validated_withdrawal_amount)
                verified_account.update_statement(validated_withdrawal_amount)
        else:
            return

    def update_statement(self, value):

        if self.deposit_requested == True:
            self._statement += f"Deposit: + $ {value:.2f}\n"
            self.deposit_requested = False

        if self.withdrawal_requested == True:
            self._statement += f"Withdrawal: - $ {value:.2f}\n"
            self.withdrawal_requested = False

    def display_statement():
        verified_account = Account.check_account()
        if verified_account:
            statement_title = " STATEMENT ".center(41, "=")
            print()
            print(statement_title)
            print()
            print(
                "\nNo transactions have been made."
                if not verified_account._statement
                else verified_account._statement
            )
            print(f"\nBalance: $ {verified_account._balance:,.2f}")
            print()
            footer_statement = "=".center(41, "=")
            print(footer_statement)

    def list_accounts():
        filtered_client = Client.filter_client()

        if filtered_client:
            for client in Client.clients:
                if client.client_accounts:
                    ssn = filtered_client._ssn
                    print(
                        f"\n>>> Client: {filtered_client._name}. SSN: {filtered_client._ssn}."
                    )
                    for account in Account.bank_accounts:
                        if account._ssn == ssn:
                            print(f"\n>>> Account number: {account}", end="")
                        else:
                            print("\n>>> Client found, but does not have an account.")
                    else:
                        break

            else:
                print("\n>>> Client found, but does not have an account.")
                return False

        else:
            print(f"\n>>> SSN not found.")
            return False

    def __str__(self):
        return f"Agency: {self._agency} Account: {self._number}\n"


def menu():
    menu_text = f"""
    {" MENU ".center(41, "=")}

    Choose the desired option and press enter:\n
    [1] Deposit
    [2] Withdraw
    [3] Statement
    [4] Open new account (if you already have a registered SSN)
    [5] List your accounts
    [6] Register new Client/SSN
    [7] Exit
    
    Option: """

    return input(menu_text)


def check_option(n):
    if n.isdigit():
        n = int(n)
        if 0 < n < 8:
            return n

        else:
            return "Invalid number"

    else:
        return "Invalid option"


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def validate_date(date_string):

    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def main():

    while True:

        option = menu()

        validated_option = check_option(option)

        if validated_option == "Invalid number" or validated_option == "Invalid option":
            print(f"\n>>> {validated_option}, try again.")
            continue

        else:

            if validated_option == 1:
                Account.check_deposit()

            elif validated_option == 2:
                Account.check_withdrawal()

            elif validated_option == 3:
                Account.display_statement()

            elif validated_option == 4:
                Account.open_new_account()

            elif validated_option == 5:
                Account.list_accounts()

            elif validated_option == 6:
                Individual.register_client()

            elif validated_option == 7:
                break


if __name__ == "__main__":
    main()
