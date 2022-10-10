class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ['com', 'bg', 'org', 'net']
while True:
    email = input()
    if email == 'End':
        break
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    else:
        name, domain = email.split('@')
        domain_full = domain.split('.')
        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        if domain_full[-1] not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print('Email is valid')
