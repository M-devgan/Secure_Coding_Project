class BankAcct:
    def __init__(self, acct_num, cust_id, start_bal):
        # Confirm acct_num is int
        if type(acct_num) is not int:
            raise ValueError("Account number must be integer.")
        self._acct_num = acct_num

        # Confirm cust_id is int
        if type(cust_id) is not int:
            raise ValueError("Customer ID must be integer.")
        self._cust_id = cust_id

        # Try to convert start_bal to float, else set to 0.0
        try:
            self._bal = float(start_bal)
        except Exception:
            self._bal = 0.0   
    @property
    def acct_num(self):
        return self._acct_num

    @property
    def cust_id(self):
        return self._cust_id

    @property
    def bal(self):
        return self._bal

    def change_bal(self, amt):
        try:
            self._bal += float(amt)
        except Exception:
            # Ignore invalid amount
            pass

    def add_funds(self, amt):
        # Try convert to float
        try:
            val = float(amt)
        except Exception:
            raise ValueError("Deposit must be numeric: {}".format(amt))
        if val <= 0:
            raise ValueError("Deposit must be positive: ${:,.2f}".format(val))
        self.change_bal(val)

    def take_funds(self, amt):
        try:
            val = float(amt)
        except Exception:
            raise ValueError("Withdraw must be numeric: {}".format(amt))
        if val <= 0:
            raise ValueError("Withdraw must be positive: ${:,.2f}".format(val))
        if val > self._bal:
            raise ValueError("Withdraw ${:,.2f} exceeds balance ${:,.2f}.".format(val, self._bal))
        self.change_bal(-val)

    def __str__(self):
        return "Acct#: {} Bal: ${:,.2f}\n".format(self._acct_num, self._bal)   