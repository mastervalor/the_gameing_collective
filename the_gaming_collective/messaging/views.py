from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Chat, Message

# Create your views here.

def chat_list(request):
    if 'user_id' not in request.session:
        return redirect('/account/login_create')
    
    chats = Chat.objects.filter(participants=request.user)
    if not chats:
        messages.warning(request, "You have no messages yet!")
        chats = None
    context = {'chats': chats}
    return render(request, 'chat/list.html', context)

def chat_detail(request, chat_id):
    if 'user_id' not in request.session:
        return redirect('/account/login_create')
    chat = Chat.objects.get(id=chat_id)
    messages = Message.objects.filter(chat=chat).order_by('-timestamp')
    context = {'chat': chat, 'messages': messages}
    return render(request, 'chat/detail.html', context)