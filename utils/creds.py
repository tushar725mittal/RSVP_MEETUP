def get_credentials():
    """Reads the credentials from the auth_info file and returns them as a tuple in email and password order"""
    with open("./auth_info.txt", "r") as f:
        email = f.readline().strip().split("=")[1].replace('"', "")
        password = f.readline().strip().split("=")[1].replace('"', "")

    return email, password
