def registration_new_user(id_user: str):
    path = f'.\\users\\{id_user}.json'
    user = Users(id_user, path)
    return user