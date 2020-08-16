# -*- coding: utf-8 -*-
# # Импортируем созданный нами класс Server
from server import Server
# Получаем из config.py наш api-token
from config import VK_API_GROUP_TOKEN


server1 = Server(VK_API_GROUP_TOKEN, 4569, "server1")
#34014795
# vk_api_token - API токен, который мы ранее создали
# 172998024 - id сообщества-бота
# "server1" - имя сервера

# server1.test()

server1.start()