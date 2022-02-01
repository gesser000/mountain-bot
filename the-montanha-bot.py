#bot de montanhas

import tweepy as tp
from tweepy import OAuthHandler
import time
import os

#credenciais de login

consumer_key = 'OACn0wqERXbaEfjvu3jyInq9s'
consumer_secret = 'LVPaeGs04xLJZ27TwLyA0Ed2krPIDjJ8ffnufCS1smFl1iGOs2'
access_token = '1217241633252696066-IzAOAImnwfcQLo1Ayz4UJvdLNXJN5K'
access_secret = 'G5wKchvMthH0S1Ht77O5QIBQ8fNU5Z9xSsval3AsXI2yI'

#login na api do twitter
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

#postando as fotos de montanha da pasta
os.chdir('montanhas')
for montanha_image in os.listdir('.'):
    api.update_with_media(montanha_image)
    time.sleep(1500)
