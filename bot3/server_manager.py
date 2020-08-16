# -*- coding: utf-8 -*-
# # Импортируем созданный нами класс Server
from server import Server
# Получаем из config.py наш api-token
from config import vk_api_token


server1 = Server(vk_api_token, 4569, "server1")
#34014795
# vk_api_token - API токен, который мы ранее создали
# 172998024 - id сообщества-бота
# "server1" - имя сервера

# server1.test()

server1.start()