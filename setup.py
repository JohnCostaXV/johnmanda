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
gd = '417426253658849281', '407677666750365706', '423639365621645322'
geral = ['407706417282416641', '407678481670078475', '407678188773179417', '417426253658849281', '407677666750365706']

msg_id = None
msg_user = None
user_timer = {}
user_spam_count = {}

@client.event
async def on_member_join(member):
    canal = client.get_channel('448326795692081152')
    await client.send_message(canal, 'Seja bem-vindo(a) {}!'.format(member.mention))
    embed = discord.Embed(
        title='Seja bem-vindo(a) ao grupo do Discord da rede de servidores End!',
        color=COR,
        description='**Redes sociais:**\n\nTwitter: https://twitter.com/ServidoresEnd\nDiscord: https://discord.gg/uhxPeqS\n\n**Endereços:**\n\nEndereço de loja: https://loja.end-mc.com/\nEndereço de ip para conexão ao servidor: jogar.end-mc.com\n\nO servidor encontra-se em desenvolvimento e todas as atualizações são anunciadas aqui, no Discord, e em nosso Twitter.\n\nData de lançamento: 08/07/2018 às 17:00.'
    )
    embed.set_author(name='{}#{}'.format(member.name, member.discriminator), icon_url=member.avatar_url)
    embed.set_thumbnail(url="https://i.imgur.com/yJey64O.png")
    embed.set_footer(text='End', icon_url=member.server.icon_url)
    await client.send_message(canal, embed=embed)
    role = discord.utils.get(member.server.roles, name="Membro")
    await client.add_roles(member, role)
    print("Adicionado o cargo '" + role.name + "' para " + member.name)

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
    if message.content.startswith('/sugestão'):
        try:
            await client.delete_message(message)
            remover_sugestao = message.content.replace("/sugestão", "")
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
            await client.send_message(message.author, "Uso correto do comando: /sugestão <sugestão> | <por quê adicionariamos?>")
            time.sleep(3)
        except:
            await client.send_message(message.author,"Desculpe pelo erro.")
            time.sleep(3)
        finally:
            pass
        
    if message.content.startswith('/say'):
        if '407677666750365706' in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            await client.send_message(message.channel, (" ".join(args[1:])))
            asyncio.sleep(1)
            await client.delete_message(message)
            asyncio.sleep(1)
        else:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        
    #if message.content.lower().startswith('/youtuber'):
        #try:
            #embed = discord.Embed(
                #title='YOUTUBE 🔴',
                #color=COR,
                #description='Abaixo terão os requisitos para você que é youtuber e deseja possuir uma tag.\n\n**Shulker**: ***1.000***;\n**End**: ***3.000***;\n**Youtuber**: ***10.000***;\n**Youtuber+**: ***15.000***;\n\nCaso possui um dos requisitos, solicite a tag a um superior.'
            #)
            #embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            #embed.set_thumbnail(url="https://i.imgur.com/yJey64O.png")
            #embed.set_footer(text='End', icon_url="https://i.imgur.com/yJey64O.png")
            #try:
                #apg = await client.send_message(message.channel, '{}, foi enviada uma mensagem em seu privado!'.format(message.author.mention))
                #time.sleep(10)
                #await client.delete_message(apg)
            #finally:
                #pass
            #await client.send_message(message.author, embed=embed)
        #except IndexError:
            #print('error')
            #await client.send_message(message.channel, "Use o comando corretamente! `/youtuber`.")
        #except:
            #await client.delete_message(apg)
            #await client.send_message(message.channel, "{}, libere seu privado para poder enviar as informações!".format(message.author.mention))
        #finally:
            #pass
    
    if message.content.startswith('/revisão'):
        try:
            await client.delete_message(message)
            remover_revisão = message.content.replace("/revisão ", "")
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
            await client.send_message(message.author, '{}, use /revisão <nickname> | <motivo> | <Por quê está irregular?>'.format(message.author.mention))
            time.sleep(3)
        except:
            await client.send_message(message.author, 'Desculpe pelo erro.')
            time.sleep(3)
            print('Error')
        finally:
            pass


    if message.content.startswith('/reportar'):
        try:
            remover_reportar = message.content.replace("/reportar ", "")
            separar = remover_reportar.split("|", 2)
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
                value="%s" % "".join(separar[0]),
                inline=False
            )
            embed.add_field(
                name="Motivo:",
                value="%s" % "".join(separar[1]),
                inline=False
            )
            embed.add_field(
                name="Prova:",
                value="%s" % "".join(separar[2]),
                inline=False
            )
            embed.set_thumbnail(
                url="%s.png" % "".join(separar[2])
            )
            embed.set_footer(
                text="Denúncia postada com sucesso.",
                icon_url=message.author.avatar_url
            )
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except IndexError:
            await client.send_message(message.author, '{}, use /reportar <Suspeito> | <Motivo>'.format(message.author.mention))
            await client.delete_message(message)
        except:
            await client.send_message(message.author, 'Desculpe pelo erro.')
            await client.delete_message(message)
        finally:
            pass

    if message.content.startswith('/ajuda'):
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
            url='https://i.imgur.com/yJey64O.png'
        )
        embed.add_field(
            name='teste',
            value='',
            inline=False
        )
        await client.send_message(message.author, embed=embed)
        await client.delete_message(message)

    if message.content.startswith('/kick'):
        if '407677666750365706' in [role.id for role in message.author.roles]:
            asyncio.sleep(10)
            await client.delete_message(message)
            channel = client.get_channel('448449971629588481')
            user = message.mentions[0]         
            await client.kick(user)
            embed = discord.Embed(
                title='EXPULSO ⛔',
                color=COR,
                description='O usuário **{}#{}**, foi expulso com sucesso!'.format(user.name, user.discriminator)
            )
            embed.set_thumbnail(
                url='https://i.imgur.com/yJey64O.png'
            )
            embed.set_footer(text='End', icon_url='https://i.imgur.com/yJey64O.png')
            await client.send_message(channel, embed=embed)
        else:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)  

    if message.content.startswith('/ban'):
        if '407677666750365706' in [role.id for role in message.author.roles]:
            asyncio.sleep(10)
            args = message.content.split(" ")
            await client.delete_message(message)
            channel1 = client.get_channel('448449971629588481')
            user = message.mentions[0]
            await client.ban(user)
            join = (" ".join(args[2:]))
            embed = discord.Embed(
                title='BANIDO ⛔',
                color=COR,
                description='O usuário **{}#{}**, foi banido por: {}!'.format(user.name, user.discriminator, join)
            )
            embed.set_thumbnail(
                url='https://i.imgur.com/yJey64O.png'
            )
            embed.set_footer(text='End', icon_url='https://i.imgur.com/yJey64O.png')
        else:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)    
        try:
            await client.send_message(channel1, embed=embed)
        except IndexError:
            msg = await client.send_message(message.channel, '{}, use /ban <@>.'.format(message.author.mention))
            time.sleep(10)
            await client.delete_message(msg)
        except:
            a = await client.send_message(message.channel, '{}, use /ban <@> <motivo>.'.format(message.author.mention))
            time.sleep(5)
            await client.delete_message(a)
        finally:
            pass
   
    if message.content.startswith('/anunciar'):
        if '407677666750365706' in [role.id for role in message.author.roles]:
            await client.delete_message(message)
            args = message.content.split(" ")
            embed = discord.Embed(
                title="End 📢",
                color=COR,
                description=" ".join(args[1:])
            )
            embed.set_footer(
                text="Enviado por: {}".format(message.author.name),
                icon_url=message.author.avatar_url
            )
            embed.set_thumbnail(
                url='https://i.imgur.com/yJey64O.png'
            )
            await client.send_message(message.channel, "@everyone")
            await client.send_message(message.channel, embed=embed)
        else:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
            
    if message.content.startswith('/ping'):
        now = datetime.datetime.utcnow()
        delta = now-client.message.timestamp
        await client.send_message('{}ms'.format(delta(microseconds=1)))
        
client.run(os.environ.get("BOT_TOKEN"))
