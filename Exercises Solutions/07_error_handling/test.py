import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()
valid_domains = {".com", ".bg", ".org", ".net"}
pattern = r"([A-Za-z]+)\@([a-z]+)(.[a-z]+)"
result = re.match(pattern, email)

while True:
    name = result.group(1)
    domain = result.group(3)

    if len(name) <= 4:
        raise NameTooShortError(f"Name must be more than 4 characters")

    if "@" not in email:
        raise MustContainAtSymbolError(f"Email must contain @")

    if domain != valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")

    email = input
