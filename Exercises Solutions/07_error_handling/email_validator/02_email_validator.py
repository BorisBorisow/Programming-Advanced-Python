from custom_exceptions import MyContainAtSymbolError, NameTooShortError, InvalidDomainError

valid_domains = {".com", ".bg", ".org", ".net"}

while True:
    line = input()
    if line == "End":
        break
    email = line

    email_parts = email.split("@")
    if len(email_parts) != 2:
        raise MyContainAtSymbolError("Email must contain @")

    name, domain_name = email_parts

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = f".{domain_name.split('.')[-1]}"

    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

