import json
from channels.generic.websocket import AsyncWebsocketConsumer
from app1.models import Messages  # Ensure your Message model is correctly defined

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = self.scope['user']  # Assuming you have user authentication

        # Save the message to the database
        Messages.objects.create(sender=sender, room_name=self.room_name, description=message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username,
                'time': text_data_json.get('time', '')
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        time = event['time']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'time': time
        }))