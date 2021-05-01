# Checking Usernames
current_users = ["Jasur", "Hamid", "admin", "Erkin", "ever"]
new_users = ["Jasur", "Vohid", "Bilol", "Shoyad", "Erkin"]

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken please use other name.")
    else:
        print("Great, " + new_user + " is still available.")
