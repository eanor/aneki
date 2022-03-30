#!/usr/bin/env python
# coding: utf-8

# In[1]:


import markovify


# In[3]:


def make_new_themed_anek(t):
    with open(f"{t}.txt", encoding='utf-8') as f:
        text = f.read()
    text_model = markovify.Text(text)
    
    generated_anek = []
    
    for i in range(2):
        a = text_model.make_sentence()
        if a != None:
            generated_anek.append(str(a))
    
    text = '\n'.join(generated_anek)
    
    return text


# In[4]:


inp = 'piter'
text = make_new_themed_anek(inp)
print(str(text))


# In[5]:


import telebot
bot = telebot.TeleBot("5248946987:AAEgWI5LUojBD6S5nqcn7VwklC5WuzPtyFU", parse_mode=None)

dict_users_states = {}


# In[6]:


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.add("/help", "привет", "пока", "рандомный анек про вовочку", 'рандомный анек 18+', 'рандомный анек про компьютеры', 'рандомный анек про блондинок', 'рандомный анек про петю', 'черный юмор', 'про детей', 'габровский анек', 'про медиков', 'про школьников и студентов', 'про алкоголь', 'политический анек', 'про автомобили', 'для детей', 'про русских', 'про евреев', 'про штирлица', 'разное', 'про спорт', 'скинь анек поностальгировать')


# In[7]:


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.add("/help", "привет", "пока", "рандомный анек про вовочку", 'рандомный анек 18+', 'рандомный анек про компьютеры', 'рандомный анек про блондинок', 'рандомный анек про петю', 'черный юмор', 'про детей', 'габровский анек', 'про медиков', 'про школьников и студентов', 'про алкоголь', 'политический анек', 'про автомобили', 'для детей', 'про русских', 'про евреев', 'про штирлица', 'разное', 'про спорт', 'скинь анек поностальгировать')


# In[8]:


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привет!/start", reply_markup=keyboard1)


# In[9]:


@bot.message_handler(commands=["help"])
def bot_messages(message):
    text = '''этот бот рассказывает сгенерированный нейросетью анекдот по выбранной теме'''
    bot.send_message(message.chat.id, text)


# In[10]:


@bot.message_handler(content_types=["text"])
def send_text(message):
    if dict_users_states.get(message.chat.id) != "stop_now_word":
        if message.text.lower() == "привет":
            bot.send_message(message.chat.id, "— Привет, как в кино сходила? У Маринки как дела? Кошка нашлась? Ребенок не болеет? Жалко, что вы с Ваней расстались, он нормальный был.\n— А ты вообще кто?\n— А я статусы твои читаю…\n")
        elif message.text.lower() == "пока":
            bot.send_message(message.chat.id, "- Здгавствуйте...\n- До свидания!")
        elif message.text.lower() == 'рандомный анек про вовочку':
            inp = 'vova'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'рандомный анек 18+':
            inp = 'adults'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'рандомный анек про компьютеры':
            inp = 'computers'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'рандомный анек про блондинок':
            inp = 'blondes'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'рандомный анек про петю':
            inp = 'piter'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'черный юмор':
            inp = 'black'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'про детей':
            inp = 'kinder'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'габровский анек':
            inp = 'gabrovska'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'про медиков':
            inp = 'medical'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'про школьников и студентов':
            inp = 'school'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'про алкоголь':
            inp = 'alcohol'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'политический анек':
            inp = 'political'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'про автомобили':
            inp = 'auto'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'для детей':
            inp = 'child'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'про русских':
            inp = 'russians'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'про евреев':
            inp = 'jews'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'про штирлица':
            inp = 'stirlitz'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'разное':
            inp = 'different'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'про спорт':
            inp = 'sport'
            annekdot = make_new_themed_anek(inp)
            bot.send_message(message.chat.id, annekdot)
        elif message.text.lower() == 'скинь анек поностальгировать':
            bot.send_photo(message.chat.id, photo=open('ded.jpg', "rb"))


# In[11]:


bot.polling()


# In[ ]:




