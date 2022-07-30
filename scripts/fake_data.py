import os
import random

from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

import django
django.setup()
### Modellerimize ve django içeriklerine erişmek için yukarıdaki gibi ayarlamaları yapmamız lazım
### SIRALAMA ÇOK ÖNEMLİ
import secrets
files = os.listdir(os.path.join(settings.MEDIA_ROOT, "media/avartar"))
print(files)
# https://stackoverflow.com/questions/37270170/iterate-through-a-static-image-folder-in-django
from store.models import Post, Room, UserProfile,Hashtag
from django.contrib.auth.models import User

from faker import Faker

users=[]
hashtags=[]
rooms=[]

def set_user():
    fake=Faker(['en_US'])   

    name = fake.first_name()
    surname = fake.last_name()
    email = f'{name}_{surname}@{fake.domain_name()}'
    city=fake.city()
    country=fake.country()
    bio=fake.sentence(nb_words=10)
    date_of_birth=fake.date()
    phone=fake.random_number(digits=7)
    batch=fake.random_element(elements=('user', 'Dr', 'Psk', 'Dt','Dt','Dyt'))
    # print(name, surname, email, city, country, bio,date_of_birth )
    

    user = UserProfile(
        name = name,
        surname = surname,
        email = email,
        city=city,
        country=country,
        bio=bio,
        date_of_birth=date_of_birth,
        phone_number=phone,
        # profile_avatar=
        # background_image=
        batch=batch
    )
    user.save()
    users.append(user)
    # print(type(users))

def set_hashtag():
    fake=Faker(['en_US'])   
    words=fake.words(nb=3,unique=True)

    result=''
    for word in words:
        result += str(word).title()
    name=f'#{result}'
    
    hashtag = Hashtag(
        name=name
    )
    hashtag.save()
    hashtags.append(hashtag)


def set_room():
    fake=Faker(['en_US'])   
    sentence=fake.sentence(nb_words=3, variable_nb_words=False)

    room = Room(
        title=sentence
    )
    room.save()
    rooms.append(room)

def set_post():
    fake=Faker(['en_US'])
    content=fake.paragraph(nb_sentences=5, variable_nb_sentences=False)
    # room=rooms listesinden random eleman alma
    room=secrets.choice(rooms)
    # hashtag=secrets.choice(hashtags)
    user=secrets.choice(users)

    post=Post(
        content=content,
        user=user,
        # hashtag=hashtag,
        room=room,
    )
    print(post)
    post.save()
      
def fake_data():
    for i in range(0,100):
        set_user()
    for i in range(0,20):
        set_room()
    for i in range(0,20):
        set_hashtag()









# from scripts.fake_data import set_hashtag
# from scripts.fake_data import set_user
from scripts.fake_data import set_room,set_hashtag,set_user,set_post,fake_data
from store.models import UserProfile,Hashtag,Room
# set_hashtag()
# set_user()
# set_room()
# set_post()