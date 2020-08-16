# -*- coding: utf-8 -*-
import config
import vk_api
from time import sleep

VK_TOKEN = '9b778d9a0a4d6b24bdd3c3ae1cdf59185e9e163902090df400ef7d9eb288c19619cedc9f1fcef39f4a86d'


vk_session = vk_api.VkApi(token=VK_TOKEN)
# vk_session.auth()

vk = vk_session.get_api()

# response = vk.wall.get(count=1)
# if response['items']:
#     print(response['items'][0])


# response = vk.users.get()
# print (response)
# #получить записи со стены


# https://vk.com/wall-4569_273672
# isLiked = vk.likes.IsLiked(owner_id = -4569, item_id = 273672)
# print (isLiked)

# isLiked = vk.likes.isLiked(type = 'post', owner_id = -4569, item_id = 273672)


#как мне дать рекомендацию?
#попробую на Лене
#https://vk.com/eshchetinina
#https://vk.com/eshchetinina?w=wall375997_1071





def first_line(text):
    return text.split("\n")[0].strip()

def top(count, offset):

    response = vk.wall.get(owner_id=-4569, offset = offset, count = count)
    print (count, offset)
    posts = response['items']
    print (len(posts))
    top_string = ''
    top = sorted(posts, key = lambda k: k['likes']['count']+k['reposts']['count']*2, reverse = True)
    print (len(top))
    top_count = int(count/6 + 4) #просто хочу примерно получить из 100 результатов примерно 20, из 30 примерно 10, из 10 примерно 5, ниже нет смысла делать топы но в таком случае просто отсортирует
    print ('выдал', top_count, 'из', count)
    for t in top[:top_count]:
        fl = first_line(t['text']) 
        if fl: #просто картинки без текста пока исключаем - их не представить в текстовом списке
            top_string += (fl + '\n')
            top_string += ('vk.com/wall'+str(t['owner_id'])+'_'+str(t['id']) + '\n')
            top_string += ('---------'+'\n')
    return top_string

if __name__ == "__main__":
    pass
    # print(top())

# print (post['likes'])    

# lena_id = 375997
# for post in posts:
#     pid = (post['id'])
#     # isLiked = vk.likes.IsLiked(type = 'post', owner_id = -4569, item_id = pid)
#     # isLiked = vk.likes.isLiked(user_id = lena_id, type = 'post', owner_id = -4569, item_id = pid)
#     likers = vk.likes.getList(type = 'post', owner_id = -4569, item_id = pid,count = 500)
#     likers = likers['items']
#     print ('*', end='')
#     if lena_id in likers:
#         print (post['text'][:30])
#         # print (likers['items'][:5])
#         # print (len (likers['items']))
#         print (post['likes'])
#         print ('---------------')
#     sleep(0.33)
    # if isLiked['liked'] == 1:
    #     print (pid)
    # print (pid, isLiked)


#способ1:
# пройтись по всем записям и найти её лайки



# print (response['items'][0]['text'][:100])
# print (response['items'][0]['likes']['count'])
# print (response['items'][0]['likes']['user_likes'])

#проверить что он залайкал
