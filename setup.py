import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import asyncio
import time
import datetime
import sys
import io
import os
import re

RANDOM_STATUS = ['jogar.end-mc.com']

client = discord.Client()
COR = 0x3498DB
testmsgid = None
testmsguser = None

ex = ['407678481670078475', '407678188773179417', '417426253658849281', '407677666750365706']
ajd = '407706417282416641'
gd = ['417426253658849281', '407677666750365706']
geral = ['407706417282416641', '407678481670078475', '407678188773179417', '417426253658849281', '407677666750365706']

msg_id = None
msg_user = None
user_timer = {}
user_spam_count = {}

@client.event
async def on_ready():
    print('Iniciado com sucesso!')
    print(client.user.name)
    print(client.user.id)
    print('Versão 1.0')
    print('Status = {}'.format(RANDOM_STATUS))
    try:
        choice = random.choice(RANDOM_STATUS)
        await client.change_presence(game=discord.Game(name=choice, type=1))
        await client.send_message(client, "Online!")
    except Exception as e:
        print("Todos direitos {}.".format("reservados"))
    print("Copyright ©")

@client.event
async def on_message(message):
    if message.content.startswith('!sugestão'):
        try:
            await client.delete_message(message)
            remover_sugestao = message.content.replace("!sugestão", "")
            separar = remover_sugestao.split("|", 1)
            embed = discord.Embed(
                title="SUGESTÃO 💡",
                color=COR,
                description="Sugestão recebida. \nEnviada por: {}".format(message.author.mention)
            )
            embed.add_field(
                name="Sugestão:",
                value="```%s```" % "".join(separar[0]),
                inline=False
            )
            embed.add_field(
                name="Por quê?",
                value="```%s```" % "".join(separar[1]),
                inline=False
            )
            embed.set_footer(
                text="Sugestão postada com sucesso.",
                icon_url=message.author.avatar_url
            )
            await client.send_message(message.author, "Sua sugestão foi enviada!")
            time.sleep(3)
            botmsg = await client.send_message(message.channel, embed=embed)
            await client.add_reaction(botmsg, "👍")
            await client.add_reaction(botmsg, "👎")
        except IndexError:
            await client.send_message(message.author, "Uso correto do comando: !sugestão <sugestão> | <por quê adicionariamos?>")
            time.sleep(3)
        except:
            await client.send_message(message.author,"Desculpe pelo erro.")
            time.sleep(3)
        finally:
            pass

    if message.content.startswith('!revisão'):
        try:
            await client.delete_message(message)
            remover_revisão = message.content.replace("!revisão ", "")
            separar = remover_revisão.split("|", 2)
            embed = discord.Embed(
                title='REVISÃO ⛔',
                color=COR,
                description='Revisão recebida. \nEnviada por: {}'.format(message.author.mention)
            )
            embed.add_field(
                name='**Nickname:**',
                value='```%s```' % ''.join(separar[0]),
                inline=False
            )
            embed.add_field(
                name='**Motivo:**',
                value='```%s```' % ''.join(separar[1]),
                inline=False
            )
            embed.add_field(
                name='**Por quê está irregular?**',
                value='```%s```' % ''.join(separar[2]),
                inline=False
            )
            embed.set_footer(text='Revisão postada com sucesso.', icon_url=message.author.avatar_url
            )
            await client.send_message(message.author, 'Sua revisão foi enviada')
            time.sleep(3)
            await client.send_message(message.channel, embed=embed)
        except IndexError:
            await client.send_message(message.author, '{}, use !revisão <nickname> | <motivo> | <Por quê está irregular?>'.format(message.author.mention))
            time.sleep(3)
        except:
            await client.send_message(message.author, 'Desculpe pelo erro.')
            time.sleep(3)
            print('Error')
        finally:
            pass


    if message.content.startswith('!reportar'):
        try:
            remover_reportar = message.content.replace("!reportar ", "")
            separar = remover_reportar.split("|", 1)
            tmp1 = datetime.datetime.now()

            utcnow = datetime.time(hour=tmp1.hour, minute=tmp1.minute, second=tmp1.second)
            del tmp1

            embed = discord.Embed(
                title="DENÚNCIA 🔔",
                color=COR,
                description="Denúncia recebida. \nEnviada por: {}".format(message.author.mention)
            )
            embed.add_field(
                name="Suspeito:",
                value="```%s```" % "".join(separar[0]),
                inline=False
            )
            embed.add_field(
                name="Motivo:",
                value="```%s```" % "".join(separar[1]),
                inline=False
            )
            embed.set_footer(
                text="Denúncia postada com sucesso.",
                icon_url=message.author.avatar_url
            )
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except IndexError:
            await client.send_message(message.author, '{}, use !reportar <Suspeito> | <Motivo>'.format(message.author.mention))
            await client.delete_message(message)
        except:
            await client.send_message(message.author, 'Desculpe pelo erro.')
            await client.delete_message(message)
        finally:
            pass

    if message.content.startswith('!ajuda'):
        embed = discord.Embed(
            title='Olá {}!'.format(message.author.name),
            color=COR,
            description='Temos aqui as informações básicas de nossa rede de servidores End.\nSegue abaixo:'
        )
        embed.set_author(
            name=message.server.name,
            icon_url=message.server.icon_url
        )
        embed.set_thumbnail(
            url=message.server.icon_url
        )
        embed.add_field(
            name='',
            value='',
            inline=False
        )
        await client.send_message(message.author, embed=embed)
        await client.delete_message(message)

    if message.content.startswith('!kick'):
        if ex in [role.id for role in message.author.roles]:
            asyncio.sleep(10)
            await client.delete_message(message)
            channel = client.get_channel('425081290941792276')
            user = message.mentions[0]         
            await client.kick(user)
            await client.send_message(channel, 'O usuário **{}#{}**, foi expulso com sucesso!'.format(user.name, user.discriminator))
        else:
            await client.send_message(message.channel, '❌ Você não pode fazer isso!')  

    if message.content.startswith('!ban'):
        if gd in [role.id for role in message.author.roles]:
            asyncio.sleep(10)
            await client.delete_message(message)
            channel1 = client.get_channel('425081290941792276')
            user = message.mentions[0]
            await client.ban(user)
            await client.send_message(channel1, 'O usuário **{}#{}**, foi banido com sucesso!'.format(user.name, user.discriminator))
        else:
            await client.send_message(message.channel, '❌ Você não pode fazer isso!')    


client.run(os.environ.get("BOT_TOKEN"))
