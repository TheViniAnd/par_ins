#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import random
import time

import instabot


proxylist = ['165.225.66.56:10605', '165.225.66.55:10605', '78.37.94.172:8080', '46.151.108.6:41171', '77.37.131.164:55443',
             '31.44.12.119:5836', '89.223.20.202:5836', '31.44.12.84:5836', '185.70.105.228:5836', '165.225.66.49:10605']

def get_info(login, email, sleep=0.1):

    z = 0

    USERNAME = "intomask"
    PASSWORD = "mistercraft228"

    bot = instabot.Bot()
    try:
        bot.login(username=USERNAME, password=PASSWORD, ask_for_code=True)
    except:
        bot.login(username=USERNAME, password=PASSWORD, ask_for_code=True, proxy=proxylist[z])
        z += 1

    input_account = str(login)

    id_account = bot.get_user_id_from_username(input_account)

    followers_account = bot.get_user_followers(id_account)

    LOOP_WHILE = True

    p = 0

    email = 'result/' + str(email) + '.json'

    list_users = []

    while LOOP_WHILE:  # Получаем инфу пользователей
        TIMEDET = random.randint(30, 70)
        if TIMEDET:
            if p == len(followers_account):
                print("Завершено!")
                list_users = []
                LOOP_WHILE = False
            else:
                # try:
                info_user = bot.get_user_info(followers_account[p])

                if "username" in info_user:
                    user_login = info_user["username"]
                    user_login = str(user_login)
                else:
                    user_login = "Не найдено"

                if "full_name" in info_user:
                    user_full_name = info_user["full_name"]
                else:
                    user_full_name = "Не найдено"

                if "public_email" in info_user:
                    user_public_email = info_user["public_email"]
                else:
                    user_public_email = "Не найдено"

                if "public_phone_number" in info_user:
                    user_public_phone = info_user["public_phone_number"]
                else:
                    user_public_phone = "Не найдено"

                if "contact_phone_number" in info_user:
                    user_contact_phone = info_user["contact_phone_number"]
                else:
                    user_contact_phone = "Не найдено"

                user_follower = info_user["follower_count"]

                if "city_name" in info_user:
                    user_city = info_user["city_name"]
                else:
                    user_city = "Не найдено"

                if "category" in info_user:
                    user_bio = info_user["biography"]
                else:
                    user_bio = "Не найдено"

                if "category" in info_user:
                    user_category = info_user["category"]
                else:
                    user_category = "Не найдено"

                if "is_business" in info_user:
                    user_buisness = str(info_user["is_business"])
                else:
                    user_buisness = "Не найдено"

                print('№P = ', p)
                print('USER:', user_login)
                print('EMAIL_P = ', user_public_email)
                print('PHONE_P = ', user_public_phone)
                print('PHONE = ', user_contact_phone)

                if str(user_public_email) == "Не найдено" or str(user_public_phone) == "Не найдено" or str(
                        user_contact_phone) == "Не найдено":

                    print('-')

                    p += 1

                    time.sleep(TIMEDET)
                else:
                    try:
                        data_result = {
                            "Login": str(user_login),
                            "Full name": str(user_full_name),
                            "Email": str(user_public_email),
                            "Public_number": str(user_public_phone),
                            "Contact_number": str(user_contact_phone),
                            "City": str(user_city),
                            "Bio": str(user_bio),
                            "Category": str(user_category),
                            "Buisnes": str(user_buisness),
                            "Followers": str(user_follower)
                        }

                        print(data_result)
                        list_users.append(data_result)
                        with open(email, 'w', encoding='utf-8') as f_obj:
                            json.dump(list_users, f_obj, ensure_ascii=False, indent=4)

                        p += 1

                        time.sleep(TIMEDET)

                    except:
                        print('Ошибка')
                        p += 1
                        time.sleep(TIMEDET)


    return "Ok"
