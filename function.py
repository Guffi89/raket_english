# #
from classes import RaketEnglish

user_info = RaketEnglish.USER_INFO


def pars_user_input(user_info: dict[str, str]):
    """


    """
    user_login = input("Введите имя пользователя:> ").strip()
    user_info['login'] = user_login
    user_email = input("Введите свой email адрес:> ").strip().lower()
    user_info['email'] = user_email
    user_password = input("Введите пароль:> ").strip()
    user_info['password'] = user_password

    return user_info



