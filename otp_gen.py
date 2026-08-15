import secrets

def  random_OTP()

    chars = "ABCDEFGHJKMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz23456789"

    code = ""

    for i in range(6):
        code += secrets.choice(chars)

    return(code)
