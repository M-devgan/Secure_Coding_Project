# client/client.py

from email_validator import validate_email, EmailNotValidError

class Customer:
    def __init__(self, cust_id, fname, lname, email):
        # Check cust_id is int
        if type(cust_id) is not int:
            raise ValueError("Customer ID must be integer.")
        self._cust_id = cust_id

        # Clean and check fname
        fn = fname.strip()
        if fn == '':
            raise ValueError("First name can't be empty.")
        self._fname = fn

        # Clean and check lname
        ln = lname.strip()
        if ln == '':
            raise ValueError("Last name can't be empty.")
        self._lname = ln

        # Validate email, fallback if invalid
        try:
            validate_email(email)
            self._email = email
        except EmailNotValidError:
            self._email = "email@pixell-river.com"

    @property
    def cust_id(self):
        return self._cust_id

    @property
    def fname(self):
        return self._fname

    @property
    def lname(self):
        return self._lname

    @property
    def email(self):
        return self._email

    def __str__(self):
        return "{}, {} [{}] - {}\n".format(self._lname, self._fname, self._cust_id, self._email)