# -*- coding: utf-8 -*-
import vk_api.vk_api

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType

from scripts import top

class Server:

    def __init__(self, api_token, group_id, server_name: str = "Empty"):
        print (group_id)

        # Даем серверу имя
        self.server_name = server_name

        # Для Long Poll
        self.vk = vk_api.VkApi(token=api_token)
        print('self vk')
        # Для использования Long Poll API
        self.long_poll = VkBotLongPoll(self.vk, group_id)
        print ('self longpoll')

        # Для вызова методов vk_api
        self.vk_api = self.vk.get_api()

    def send_msg(self, send_id, message):
        """
        Отправка сообщения через метод messages.send
        :param send_id: vk id пользователя, который получит сообщение
        :param message: содержимое отправляемого письма
        :return: None
        """
        self.vk_api.messages.send(peer_id=send_id,
                                  random_id=0,
                                  message=message)
                                #   ,attachment="wall-4569_273770")

                                      

    def test(self):
        # Посылаем сообщение пользователю с указанным ID
        self.send_msg(16200, "Привет-привет!")

    def start(self):
        for event in self.long_poll.listen():   # Слушаем сервер

            # Пришло новое сообщение
            if event.type == VkBotEventType.MESSAGE_NEW:
                print (event)
                user_id = (event.object.message['from_id'])
                username = self.get_user_name(user_id)
                print("Username: " + username)
                print("From: " + self.get_user_city(user_id))
                text = event.object.message['text'].lower().strip()
                print("Text: " + text)
                print("Type: ", end="")
                if int(event.object.message['id']) > 0:
                    print("private message")
                else:
                    print("group message")
                print(" --- ")

                text =  text.split()
                print (text)
                print (len(text))

                top_function = False

                if text[0] == ("топ" or "top"):
                    top_function = True
                if len(text)>1 and text[1].isdigit():
                    count = int(text[1])
                else: count = 100
                if len(text)>2 and text[2].isdigit():
                    offset = int(text[2])
                else: offset = 1
                
                if top_function:
                    self.send_msg(user_id, message = top.top(count=count, offset=offset))
                # else:
                    # self.send_msg(user_id, f"{username}, я получил ваше сообщение!")

    def get_user_name(self, user_id):
        """ Получаем имя пользователя"""
        return self.vk_api.users.get(user_id=user_id)[0]['first_name']


    def get_user_city(self, user_id):
        """ Получаем город пользователя"""
        return self.vk_api.users.get(user_id=user_id, fields="city")[0]["city"]['title']
