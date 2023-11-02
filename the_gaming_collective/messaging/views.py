from django.shortcuts import render
from .models import Chat, Message

# Create your views here.

def chat_list(request):
    chats = Chat.objects.filter(users=request.user)
    context = {'chats': chats}
    return render(request, 'chat/list.html', context)

def chat_detail(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    messages = Message.objects.filter(chat=chat).order_by('-timestamp')
    context = {'chat': chat, 'messages': messages}
    return render(request, 'chat/detail.html', context)