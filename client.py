import discord
import datetime
from datetime import datetime
import asyncio
import os
#from passwords import TOKEN_DISCORD

TOKEN = None
try:
    with open("token.txt","r",encoding="utf-8") as f:
        TOKEN = f.read().strip()
except FileNotFoundError:
    TOKEN = os.getenv("TOKEN")

    
ver='**Launched v6.3**'
#TOKEN1 = TOKEN_DISCORD
chid=724986660890345498 #
zal_ozhidaniya_id=724986660286365709 #zal ozhidaniya channel
PKid=724986659153641505 # role of emploer
info_chid=724986660286365714 #id of info channel
voice_chid=854620086203056128 #id of voice_chat
working_chid=729588749155041290 #time schedule of emploe
qu_chid=724986660286365709 #question channel

with open('greeting.txt', 'r',encoding="utf-8") as f:
    greet1 = f.readline()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_member_join(self, member):
        print('[COMAND] !join')
        
        #????????? ? ????????? ???
        await client.get_channel(chid).send('{} joined.'.format(member.mention))
        #???????? ????????
        await asyncio.sleep(1.5)
        
        #???????? ?????? ???
#        emb= discord.Embed(title = '', colour = discord.Color.blue())
  #      emb.set_thumbnail(url = 'https://sun9-61.userapi.com/c837538/v837538137/1abc5/VdZCHNTGdO0.jpg')
  #      descript = '**????????????**, {0}. ???????? ???????? ????? ????????? ???? ??????, ?????? ?? ?????? ?????? ???? ?????? ? ????????? ?????? {1}.'.format(member.mention, client.get_channel(qu_chid).mention)             descript = '**????????????**, {0}. ???????? ???????? ????? ????????? ???? ??????, ?????? ?? ?????? ?????? ???? ?????? ? ????????? ?????? {1}.'.format(member.mention, client.get_channel(qu_chid).mention)
        descript = greet1.format(member.mention, client.get_channel(qu_chid).mention)

        
        #?????? ???? ?? ?????????? ?????
        chen =  client.get_channel(qu_chid).mention
        async for mes in client.get_channel(zal_ozhidaniya_id).history():
            if chen in mes.channel_mentions:
                await mes.delete()
        #???????? ?????? ????
        await client.get_channel(zal_ozhidaniya_id).send(descript)

    async def on_member_remove(self, member):
        await client.get_channel(chid).send('{} leaved.'.format(member.mention))

    async def on_message(self, message):

#checking role
        if message.guild.get_role(PKid) in message.author.roles:

#writefunc
            if (message.content.startswith('!write'))and(message.author != self.user):
                print('[COMMAND] !write')
                await message.channel.send(message.content[6:])
                await message.delete()
   
    #greettest
            if (message.content.startswith('!greet')):
                print('[COMMAND] !greet')
                await message.channel.send(greet1.format(client.get_channel(qu_chid).mention, client.get_channel(qu_chid).mention, client.get_channel(qu_chid).mention))
                
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
                await message.channel.send('List of coman?ds: !write [text] !delete !commands')
                await message.delete()
                
            if (message.content.startswith('!test'))and(message.author != self.user):
                print('[COMMAND] !test')
                await message.channel.send(ver)

            if message.content.startswith('!emb'):
                print('[COMAND] !emb')
                await message.delete()
                S=message.content.split('/')
                emb= discord.Embed(title = '{}'.format(S[1]), colour = discord.Color.blue())
                emb.set_thumbnail(url = 'https://sun9-61.userapi.com/c837538/v837538137/1abc5/VdZCHNTGdO0.jpg')
                emb.discription = '{}'.format(S[2])       
                await message.channel.send(embed = emb)
    
 #Voicechat time schedule     
    async def on_voice_state_update(self,memb,before,after):
     dt=datetime.now()
     
     if (after.channel != None)and(after.channel.id == voice_chid): 
        if memb.guild.get_role(PKid) in memb.roles:
            pass
        else:
            await client.get_channel(working_chid).send('**ВОШЕЛ АБИТУРИЕНТ**')
            await client.get_channel(chid).send('{}, абитуриент в голосовом канале.'.format(memb.guild.get_role(PKid).mention))
        if (before.channel == None):
          await client.get_channel(working_chid).send('{} подключился к каналу в {}'.format(memb.mention, dt.strftime("%H:%M:%S %d %B")))
        elif (before.channel.id != voice_chid): 
          await client.get_channel(working_chid).send('{} перешел в канал в {}'.format(memb.mention, dt.strftime("%H:%M:%S %d %B")))
     if (before.channel != None)and(before.channel.id == voice_chid): 
        if (after.channel == None):
          await client.get_channel(working_chid).send('{} отключился от канала в {}'.format(memb.mention, dt.strftime("%H:%M:%S %d %B")))
        elif (after.channel.id != voice_chid): 
          await client.get_channel(working_chid).send('{} отошел от канала в {}'.format(memb.mention, dt.strftime("%H:%M:%S %d %B")))

        

intents = discord.Intents.default()
intents.messages=True
intents.members=True
intents.guilds=True
intents.voice_states=True


client = MyClient(intents=intents)
client.run(TOKEN)

