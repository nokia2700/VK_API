
from VKAPI import Parser


# https://oauth.vk.com/authorize?client_id=7588734&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=notify,friends,photos,audio,video,stories,pages,status,notes,wall,ads,docs,groups,notifications,stats,email,market,stories,photos,app_widget,docs,manage,offline&response_type=token&v=5.131

group_link = 'https://m.vk.com/bass.end.cars'

parser = Parser(
    '')
group_id = parser.get_group_id(group_link)
users = parser.get_users(group_id, 10000)
