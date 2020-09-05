import discord
import datetime
from datetime import datetime
import asyncio

TOKEN = 'NzI0OTI3Mjg0NTU3MTE5NTQw.XxhGmA.YiofcsB8mmEB29rBLILSEnWGtfs'
chid=724986660890345498 #Канал системных сообщений
zal_ozhidaniya_id=724986660286365709 #Канал зал ожидания
PKid=724986659153641505 #Роль Сотрудника ПК 
info_chid=724986660286365714 #Канал
voice_chid=724986660286365710 #Канал получить консультацию
working_chid=729588749155041290 #Канал учета времени

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_member_join(self, member):
        print('[COMAND] !emb')
        
        #Сообщение в системный чат
        await client.get_channel(chid).send('{} joined.'.format(member.mention))
        #Создание задержки
        await asyncio.sleep(1.5)
        
        #Создание нового емб
        emb= discord.Embed(title = 'Добро пожаловть на Discord сервер приемной комиссии Института ядерной физики и технологий НИЯУ МИФИ.', colour = discord.Color.blue())
        emb.set_thumbnail(url = 'https://sun9-61.userapi.com/c837538/v837538137/1abc5/VdZCHNTGdO0.jpg')
        descript = '**Здравствуйте** {0}.  Приёмная комиссия НИЯУ МИФИ завершила свою работу, однако Вы можете задать интересующий Вас вопрос в чате или связаться с нами Вконтакте: vk.com/inphe.mephi'.format(member.mention, member.guild.get_role(PKid).mention)
        #Цикл добавляющий имена приемщиков из войсканала
#        for memb in client.get_channel(voice_chid).members:
 #           if memb.guild.get_role(PKid) in memb.roles:
  #              descript = descript + '{}, '.format(memb.mention)
        emb.description = descript
        #Чистка чата от предыдущих ембов
        async for mes in client.get_channel(zal_ozhidaniya_id).history():
            for embed in mes.embeds:
                if embed.title == emb.title:
                    await mes.delete()
        #Отправка нового эмба
        await client.get_channel(zal_ozhidaniya_id).send(embed = emb)

    async def on_member_remove(self, member):
        await client.get_channel(chid).send('{} leaved.'.format(member.mention))

    async def on_message(self, message):

#Проверка роли
     if message.guild.get_role(PKid) in message.author.roles:

#writefunc
        if (message.content.startswith('!write'))and(message.author != self.user):
            print('[COMMAND] !w')
            await message.channel.send(message.content[6:])
            await message.delete()

#delfunc
        if (message.content.startswith('!delete')) and(message.channel.id != chid):
            print('[COMMAND] !del')
            number = int(message.content[8:])
            i=0
            async for mes in message.channel.history():
                if (i > number):
                    break
                i=i+1
                ## wait for 0.5 seconds again
                await asyncio.sleep(0.5)
                ## delete the message
                await mes.delete()
            print('[COMMAND] !del over')
        if (message.content.startswith('!commands'))and(message.author != self.user):
            print('[COMMAND] !cmd')
            await message.channel.send('List of comanеds: !write [text] !delete !commands')
            await message.delete()
            
        if (message.content.startswith('!test'))and(message.author != self.user):
            print('[COMMAND] !test')
            await message.channel.send('**Launched**')

        if message.content.startswith('!emb'):
           print('[COMAND] !emb')
           await message.delete()
           
           S=message.content.split('|')
           emb= discord.Embed(title = '{}'.format(S[1]), colour = discord.Color.blue())
           emb.set_thumbnail(url = 'https://sun9-61.userapi.com/c837538/v837538137/1abc5/VdZCHNTGdO0.jpg')
           emb.discription = '{}'.format(S[2])
           
           await message.channel.send(embed = emb)
 
 #Вход выход в аудиоканал          
    async def on_voice_state_update(self,memb,before,after):
     dt=datetime.now()
     
     if (after.channel != None)and(after.channel.id == voice_chid): 
        if memb.guild.get_role(PKid) in memb.roles:
            pass
        else:
            await client.get_channel(working_chid).send('**ВОШЕЛ АБИТУРИЕНТ**')
        if (before.channel == None):
          await client.get_channel(working_chid).send('{} подключился к каналу в {}'.format(memb.mention, dt.strftime("%H:%M:%S %d %B")))
        elif (before.channel.id != voice_chid): 
          await client.get_channel(working_chid).send('{} перешел в канал в {}'.format(memb.mention, dt.strftime("%H:%M:%S %d %B")))
     if (before.channel != None)and(before.channel.id == voice_chid): 
        if (after.channel == None):
          await client.get_channel(working_chid).send('{} отключился от канала в {}'.format(memb.mention, dt.strftime("%H:%M:%S %d %B")))
        elif (after.channel.id != voice_chid): 
          await client.get_channel(working_chid).send('{} отошел от канала в {}'.format(memb.mention, dt.strftime("%H:%M:%S %d %B")))

client = MyClient()
client.run(TOKEN)

