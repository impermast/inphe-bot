
import datetime
import discord
import asyncio
from discord.ext import commands

TOKEN = 'NzI0OTI3Mjg0NTU3MTE5NTQw.XvIYlw.gOpygUmj4tc7FRRC66DDzTXv3-Q'
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
        await client.get_channel(chid).send('{} joined.'.format(member.mention))
        
        print('[COMAND] !emb')
        
        emb= discord.Embed(title = 'Добро пожаловть на Discord сервер приемной комиссии Института ядерной физики и технологий НИЯУ МИФИ.', colour = discord.Color.blue())
        emb.set_thumbnail(url = 'https://sun9-61.userapi.com/c837538/v837538137/1abc5/VdZCHNTGdO0.jpg')
        emb.add_field(name = 'Здравствуйте', value = '{0} ,Вы можете задать вопрос в одном из тематических чатов, а также присоединиться к голосовому каналу и пообщаться с {1} лично. Какой вопрос вас интересует?'.format(member.mention,member.guild.get_role(PKid).mention))
        
        async for mes in client.get_channel(zal_ozhidaniya_id).history():
            for embed in mes.embeds:
                if embed.title == emb.title:
                    await mes.delete()
        await client.get_channel(zal_ozhidaniya_id).send(embed = emb)
        
        
    async def on_member_remove(self, member):
        await client.get_channel(chid).send('{} leaved.'.format(member.mention))

    async def on_message(self, message):

# Достижения https://admission.mephi.ru/admission/baccalaureate-and-specialty/personal-achievements#%D0%91%D0%B8%D0%A1
     """
     if ((message.content.startswith('!д'))or(message.content.startswith('!Д'))or(message.content.startswith('!Достижения')))and(message.author != self.user):
         print('[COMAND] !д')
         await message.delete()
           emb= discord.Embed(title = 'Список индивидуальных достижений.'), colour = discord.Color.blue())
           emb.set_thumbnail(url = 'https://sun9-61.userapi.com/c837538/v837538137/1abc5/VdZCHNTGdO0.jpg')
           emb.discription = 'при приеме на обучение по программам бакалавриата, программам специалитета'
           
           emb.add_field(name = 'Название ИД', value = 'Победители олимпиады по предмету направления подготовки /n Призеры олимпиады по предмету направления подготовки /n')
           emb.add_field(name = 'Количество баллов', value = '4 /n 3 /n')
           emb.add_field(name = 'Подтверждающий документ', value = 'Диплом победителя олимпиады 11 класса, полученный не позднее 1 года до начала приема документов (для дипломов, не использованных в особых правах) /n Диплом призера олимпиады 11 класса, полученный не позднее 1 года до начала приема документов (для дипломов, не использованных в особых правах) /n')
           
           await message.channel.send(embed = emb) 
     """


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
            async for mes in message.channel.history():
                ## wait for 0.5 seconds again
                await asyncio.sleep(0.5)
                ## delete the message
                await mes.delete()
            print('[COMMAND] !del over')
#cmdfunc
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
     if (after.channel.id == voice_chid and before.channel.id != voice_chid):
         await client.get_channel(working_chid).send('{} подключился к каналу.'.format(memb.mention))
     if (after.channel.id != voice_chid and before.channel.id == voice_chid):
         await client.get_channel(working_chid).send('{} отключился от канала.'.format(memb.mention))       
            



client = MyClient()
client.run(TOKEN)

