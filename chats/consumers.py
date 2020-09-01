import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async

from .models import *

class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type": "websocket.accept"
        })
        other_user_username = self.scope['url_route']['kwargs']['username']
        my_username = self.scope['user']
        other_user = await self.get_user(other_user_username)
        me = await self.get_user(my_username)
        print(other_user, me)

    async def websocket_receive(self, event):
        print("receive", event)

    async def websocket_disconnect(self, event):
        print("disconnected", event)

    @database_sync_to_async
    def get_user(self, username):
        # return User.objects.get(username=username)
        return Profile.objects.get(user__username = username)         