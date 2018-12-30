from marshmallow.validate import Email


def is_valid_email(value):

    if not value or '@' not in value:
        return False

    user_part, domain_part = value.rsplit('@', 1)

    if not Email.USER_REGEX.match(user_part):
        return False

    if domain_part not in Email.DOMAIN_WHITELIST:
        if not Email.DOMAIN_REGEX.match(domain_part):
            try:
                domain_part = domain_part.encode('idna').decode('ascii')
            except UnicodeError:
                pass
            else:
                if Email.DOMAIN_REGEX.match(domain_part):
                    return True
            return False

    return True
