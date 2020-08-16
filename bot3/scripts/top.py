# -*- coding: utf-8 -*-
import config
import vk_api
from time import sleep




vk_session = vk_api.VkApi(token=config.VK_USER_TOKEN)
vk = vk_session.get_api()

def first_line(text):
    return text.split("\n")[0].strip()

def top(count, offset):

    response = vk.wall.get(owner_id=-4569, offset = offset, count = count)
    posts = response['items']
    top_string = ''
    top = sorted(posts, key = lambda k: k['likes']['count']+k['reposts']['count']*2, reverse = True)
    top_count = int(count/6 + 4) #просто хочу примерно получить из 100 результатов примерно 20, из 30 примерно 10, из 10 примерно 5, ниже нет смысла делать топы но в таком случае просто отсортирует
    for t in top[:top_count]:
        fl = first_line(t['text']) 
        if fl: #просто картинки без текста пока исключаем - их не представить в текстовом списке
            top_string += (fl + '\n')
            top_string += ('vk.com/wall'+str(t['owner_id'])+'_'+str(t['id']) + '\n')
            top_string += ('---------'+'\n')
    return top_string

if __name__ == "__main__":
    pass
