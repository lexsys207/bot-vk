#! /usr/bin/env python
# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

vk_session = vk_api.VkApi(token = 'a134acb8191ccc367f82d181d650ea009a40a6b18f8712192fa102174d4c6dc6e3e00057e7e99496777c5')
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(id, text):
    vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0})

def idea():
    list1 = ['Злой', 'Умный', 'Ленивый', 'Влюблённый', 'обаятельный', 'стильный', 'элегантный', 'высокий', 'толстый', 'старый', 'длинноволосый', 'кудрявый', 'лысый', 'веснушчатый', 'большеротый', 'большеглазый', 'авторитетный', 'веселый', 'игривый']
    list2 = ['Кот', 'Сапог', 'Пёс', 'Доктор', 'Человек', 'Парень', 'Жрец', 'автомобиль']
    text = random.choice(list1) + " " + random.choice(list2)
    sender(id, text)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id

            if msg == 'идея':
                idea()
            else: sender(id, 'Введите слово "идея')