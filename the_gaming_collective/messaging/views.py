from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Chat, Message, Users

# Create your views here.

def chat_list(request):
    if 'user_id' not in request.session:
        return redirect('/account/login_create')
    try:
        logged_user = Users.objects.get(id=request.session['user_id'])
    except Users.DoesNotExist:
        return redirect('/account/login_create')
    chats = Chat.objects.filter(participants=logged_user)
    if not chats:
        messages.warning(request, "You have no messages yet!")
        chats = None
    context = {'chats': chats}
    return render(request, 'chat/list.html', context)

def chat_detail(request, chat_id):
    if 'user_id' not in request.session:
        return redirect('/account/login_create')
    try:
        logged_user = Users.objects.get(id=request.session['user_id'])
    except Users.DoesNotExist:
        # Handle user not found: maybe logout or redirect to login
        return redirect('/account/login_create')

    # Attempt to retrieve the chat and messages involving the logged-in user
    try:
        chat = Chat.objects.get(id=chat_id, participants=logged_user)
        messages_list = Message.objects.filter(chat=chat).order_by('-timestamp')
    except Chat.DoesNotExist:
        # If the chat doesn't exist or doesn't involve the user
        messages.error(request, "Chat not found.")
        return redirect('name-of-some-error-page')
    
    context = {'chat': chat, 'messages': messages_list}
    return render(request, 'chat/detail.html', context)