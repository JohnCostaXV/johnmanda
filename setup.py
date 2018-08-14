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
import json
import requests
import base64

RANDOM_AUTO = ['**TWITTER**\n\nSiga nosso twitter para ter informações exclusívas da nossa rede de servidores End. - https://twitter.com/ServidorEnd']

client = discord.Client()
COR = 0x3498DB
testmsgid = None
testmsguser = None

datetime.datetime
minutes = 0
hour = 0
msg_id = None
msg_user = None
user_timer = {}
user_spam_count = {}

ip = "jogar.end-mc.com";


def mojang(site, json_retorno):
  site_conectar = requests.get(site)
  if site_conectar.status_code == 200:
       _json = json.loads(site_conectar.content)
       return _json[json_retorno]
  else:
     return


@client.event
async def on_member_join(member):
    canal = client.get_channel('448326795692081152')
    await client.send_message(canal, 'Seja bem-vindo(a) {}!'.format(member.mention))
    embed = discord.Embed(
        title='Seja bem-vindo(a) ao grupo do Discord da rede de servidores End!',
        color=COR,
        description='**Redes sociais:**\n\n[Twitter](https://twitter.com/ServidorEnd) » https://twitter.com/ServidorEnd\n[Discord](https://discord.gg/uhxPeqS) » https://discord.gg/uhxPeqS\n\n**Endereços:**\n\n[Loja](https://loja.end-mc.com/) » https://loja.end-mc.com/\nEndereço de ip para conexão ao servidor: jogar.end-mc.com\n\nO servidor encontra-se em desenvolvimento e todas as atualizações são anunciadas aqui, no Discord, e em nosso Twitter.\n\nAtualmente **' + str(len(member.server.members)) + '** membros!'
    )
    embed.set_author(name='{}#{}'.format(member.name, member.discriminator), icon_url=member.avatar_url)
    embed.set_thumbnail(url="https://i.imgur.com/1iJeEea.jpg")
    embed.set_footer(text='End', icon_url='https://media.giphy.com/media/xUPGGDNsLvqsBOhuU0/giphy.gif')
    await client.send_message(canal, embed=embed)
    role = discord.utils.get(member.server.roles, name="Membro")
    await client.add_roles(member, role)
    print("Adicionado o cargo '" + role.name + "' para " + member.name)


@client.event
async def randommessage():
    canal = client.get_channel('407669684616560650')
    mensagens = ['**TWITTER**\n\nSiga nosso twitter para ter informações exclusívas da nossa rede de servidores End. - https://twitter.com/ServidorEnd', '**LOJA**\nAdquira benefícios no servidor agora mesmo!\n\nPara ter suporte sobre compras, visite https://twitter.com/ServidorEnd?lang=pt e entre em contato via DM.']
    time.sleep(1800)
    await client.send_message(canal, mensagens)

@client.event
async def on_ready():
    print('Iniciado com sucesso!')
    print(client.user.name)
    print(client.user.id)
    print('Versão 1.0')
    try:
        RANDOM_STATUS = ['jogar.end-mc.com']
        choice = random.choice(RANDOM_STATUS)
        await client.change_presence(game=discord.Game(name=choice, url="https://www.twitch.tv/johncostaxv", type=1))
        await client.send_message(client, "Online!")
    except Exception as e:
        print("Todos direitos {}.".format("reservados"))
    print("Copyright ©")

async def tutorial_uptime():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not client.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1


def MCAPI(site):
  site_conectar = requests.get(site)
  if site_conectar.status_code == 200:
       _json = json.loads(site_conectar.content)
       return _json;

#Server
Server = MCAPI('https://mcapi.us/server/status?ip=' + ip);

#Server info
online = True;
jogadores_max = 0;
jogadores_online = 0;
motd = "Nenhum";

if (Server['status'] != "success"):
    online = False;
else:
  jogadores_max = Server['players']['max'];
  jogadores_online = Server['players']['now'];
  motd = Server['motd'];

@client.event
async def on_message(message):
    if message.content.lower().startswith("/status"):
        if (online):
            embed = discord.Embed(
                title='Status do End:',
                color=COR,
                description='Servidor: **ONLINE**'
            )
            embed.add_field(
                name='IP:',
                value=ip,
                inline=True
            )
            embed.add_field(
                name='Jogadores Online:',
                value="{}/{}".format(str(jogadores_online), str(jogadores_max)),
                inline=True
            )
            embed.add_field(
                name='Motd:',
                value=motd,
                inline=True
            )
            embed.set_thumbnail(url='https://i.imgur.com/1iJeEea.jpg')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
            await client.send_message(message.channel, embed=embed)
        else:
            embed1 = discord.Embed(
                title='Status do End:',
                color=COR,
                description='Servidor: **OFFLINE**'
            )
            embed1.add_field(
                name='IP:',
                value=ip,
                inline=True
            )
            embed1.add_field(
                name='Jogadores Online:',
                value="{}/{}".format(str(jogadores_online), str(jogadores_max)),
                inline=True
            )
            embed1.add_field(
                name='Motd:',
                value="*Servidor Offline*",
                inline=True
            )
            embed1.set_thumbnail(url='https://i.imgur.com/1iJeEea.jpg')
            embed1.timestamp = datetime.datetime.utcnow()
            embed1.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
            await client.send_message(message.channel, embed=embed1)



    if message.content.lower().startswith('/staff-'):
        try:
            cargos = [
                # IDs dos cargos:
                "407677666750365706", #Diretor
                "417426253658849281", #Gerente
                "407678188773179417", #Administrador
                "407678481670078475", #Moderador
                "407706417282416641", #Ajudante
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    embed = discord.Embed(
                        title='Comandos para o a `STAFF`:',
                        color=COR,
                        description='**/responder** [usuário] [resposta] » Responda um usuário em *#dúvidas-dos-jogadores*.\n'
                                    'exemplo: `/responder @JohnnCosta O IP do servidor é jogar.end-mc.com`\n\n'
                                    '**/tempmute** [usuário] » Silenciar temporariamente do discord.\n'
                                    'exemplo: `/tempmute @JohnnCosta 28800 Palavras inadequadas`\n\n'
                                    '*Lembrando que os tempmute é contato por segundo! Caso esteja com dúvidas em relação ao tempo de cada punição, envie em `#comandos-dos-bots` ´/helpstaff´.*'
                    )
                    embed.set_author(name=message.server.name, icon_url='https://i.imgur.com/1iJeEea.jpg')
                    embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
                    msg = await client.send_message(message.channel, '{}, enviamos uma mensagem em seu privado!'.format(message.author.mention))
                    await client.send_message(message.author, embed=embed)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/staff-`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            msg1 = await client.send_message(message.channel, embed=embedd)
            time.sleep(20)
            await client.delete_message(msg1)
        except:
            time.sleep(2)
            await client.delete_message(msg)
            asyncio.sleep(21000)
            tst = await client.send_message(message.channel, '{}, libere o privado!'.format(message.author.mention))
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(tst)
        finally:
            pass


    if message.content.lower().startswith('/helpstaff'):
        try:
            cargos = [
                # IDs dos cargos:
                "407677666750365706", #Diretor
                "417426253658849281", #Gerente
                "407678188773179417", #Administrador
                "407678481670078475", #Moderador
                "407706417282416641", #Ajudante
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    embed = discord.Embed(
                        title='PUNIÇÕES & TEMPOS:',
                        color=COR,
                        description='**Uso de caps-lock excessivo** - *__14400__ segundos de tempmute*\n\n'
                                    '**Spam** - *__14400__ segundos de tempmute*\n\n'
                                    '**Flood** - *__14400__ segundos de mute*\n\n'
                                    '**Divulgação/Citação de servidores** - *Ban permanente*\n\n'
                                    '**Iniciativa de flood** - *__21600__ segundos de mute*\n\n'
                                    '**Mensagem fake** - *__10800__ segundos de mute*\n\n'
                                    '**Ameaça ao jogador** - *Ban temporário de __86400__ segundos*\n\n'
                                    '**Ameaça ao servidor** - *Ban permanente*.\n\n'
                                    '**Abuso de bug´s** - *Ban permanente*.\n\n'
                                    '**Uso inadequado do chat** - *__43200__ segundos de mute*\n\n'
                                    '**Discriminação** - *Ban temporário de __172800__ segundos*.\n\n'
                                    '**Anti-Jogo** - *Ban temporário de __43200__ segundos*.\n\n'
                                    '**Falsificação de provas** - *Ban permanente*.\n\n'
                                    '**Chantagem** - *Ban permanente*.\n\n'
                                    '**Ofensa à staff** - *Ban permanente*.\n\n'
                                    '**Uso de hack** - *Ban permanente*.\n\n'
                                    '**Uso de algum programa proibido** - *Ban permanente*.\n\n'
                                    '**Palavras inadequadas** - *__28800__ segundos de mute*.\n\n'
                    )
                    embed.set_author(name=message.server.name, icon_url='https://i.imgur.com/1iJeEea.jpg')
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
                    msg = await client.send_message(message.channel, '{}, enviamos uma mensagem em seu privado!'.format(message.author.mention))
                    await client.send_message(message.author, embed=embed)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/helpstaff`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            time.sleep(2)
            await client.delete_message(msg)
            asyncio.sleep(21000)
            tst = await client.send_message(message.channel, '{}, libere o privado!'.format(message.author.mention))
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(tst)
        finally:
            pass

    if message.content.lower().startswith('/tt'):
        try:
            cargos = [
                # IDs dos cargos:
                "407677666750365706", #Diretor
                "417426253658849281", #Gerente
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    await client.delete_message(message)
                    auto = random.choice(RANDOM_AUTO)
                    canal = client.get_channel('407669684616560650')
                    time.sleep(3)
                    await client.send_message(canal, auto)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/tt`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            await client.delete_message(message)
            embed2 = discord.Embed(
                title='Permissão negada!',
                color=COR,
                description='Você não tem permissão para executar esse comando.'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed2)
        finally:
            pass


    if message.content.lower().startswith('/changenick'):
        try:
            cargos = [
                # IDs dos cargos:
                "407677666750365706", #Diretor
                "417426253658849281", #Gerente
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    await client.delete_message(message)
                    user = message.mentions[0]
                    args = message.content.split(" ")
                    await client.change_nickname(user, " ".join(args[2:]))
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/changenick [username] [nick]`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            await client.delete_message(message)
            embed2 = discord.Embed(
                title='Permissão negada!',
                color=COR,
                description='Você não tem permissão para executar esse comando.'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed2)
        finally:
            pass

    if message.content.lower().startswith('/say'):
        try:
            cargos = [
                # IDs dos cargos:
                "407677666750365706", #Diretor
                "417426253658849281", #Gerente
                "407678188773179417", #Administrador
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    args = message.content.split(" ")
                    await client.send_message(message.channel, (" ".join(args[1:])))
                    asyncio.sleep(1)
                    await client.delete_message(message)
                    asyncio.sleep(1)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/say [mensagem]`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            await client.delete_message(message)
            embed2 = discord.Embed(
                title='Permissão negada!',
                color=COR,
                description='Você não tem permissão para executar esse comando.'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed2)
        finally:
            pass


    if message.content.lower().startswith('/anunciar'):
        try:
            cargos = [
                # IDs dos cargos:
                "407677666750365706", #Diretor
                "417426253658849281", #Gerente
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    await client.delete_message(message)
                    args = message.content.split(" ")
                    embed = discord.Embed(
                        title="",
                        color=COR,
                        description=" ".join(args[1:])
                    )
                    embed.set_author(name='Anúncio', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(
                        text="Enviado por: {}".format(message.author.name),
                        icon_url=message.author.avatar_url
                    )
                    await client.send_message(message.channel, "@everyone")
                    await client.send_message(message.channel, embed=embed)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/anunciar [mensagem]`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            await client.delete_message(message)
            embed2 = discord.Embed(
                title='Permissão negada!',
                color=COR,
                description='Você não tem permissão para executar esse comando.'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed2)
        finally:
            pass



    if message.content.lower().startswith('/stafflist'):
        try:
            cargos = [
                # IDs dos cargos:
                "407677666750365706", #Diretor
                "417426253658849281", #Gerente
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    await client.delete_message(message)
                    args = message.content.split(" ")
                    embed = discord.Embed(
                        title="Lista da Equipe:",
                        color=COR,
                        description=" ".join(args[1:])
                    )
                    embed.set_footer(
                        text="Enviado por: {}".format(message.author.name),
                        icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif'
                    )
                    embed.timestamp = datetime.datetime.utcnow()
                    await client.send_message(message.channel, "@everyone")
                    await client.send_message(message.channel, embed=embed)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/stafflist [mensagem]`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            await client.delete_message(message)
            embed2 = discord.Embed(
                title='Permissão negada!',
                color=COR,
                description='Você não tem permissão para executar esse comando.'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed2)
        finally:
            pass


    if message.content.lower().startswith('/kick'):
        try:
            cargos = [
                # IDs dos cargos:
                "407677666750365706", #Diretor
                "417426253658849281", #Gerente
                "407678188773179417", #Administrador
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    asyncio.sleep(10)
                    await client.delete_message(message)
                    channel = client.get_channel('448449971629588481')
                    user = message.mentions[0]
                    await client.kick(user)
                    embed = discord.Embed(
                        title='EXPULSO ⛔',
                        color=COR,
                        description='O usuário **{}#{}**, foi expulso com sucesso!\nAutor: {}'.format(user.name, user.discriminator, message.author.mention)
                    )
                    embed.set_thumbnail(
                        url='https://i.imgur.com/1iJeEea.jpg'
                    )
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
                    await client.send_message(channel, embed=embed)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/kick [username]`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            await client.delete_message(message)
            embed2 = discord.Embed(
                title='Permissão negada!',
                color=COR,
                description='Você não tem permissão para executar esse comando.'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed2)
        finally:
            pass


    if message.content.lower().startswith('/tempban'):
        try:
            cargos = [
                # IDs dos cargos:
                "407677666750365706", #Diretor
                "417426253658849281", #Gerente
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    args = message.content.split(" ")
                    tempo = (" ".join(args[3:]))
                    await client.delete_message(message)
                    channel1 = client.get_channel('448449971629588481')
                    user = message.mentions[0]
                    temp = args[2]
                    timesquad = int(temp)
                    reallytime = datetime.timedelta(seconds=timesquad)
                    await client.ban(user)
                    join = (" ".join(args[2:]))
                    embed = discord.Embed(
                        title='BANIDO ⛔',
                        color=COR,
                        description='O usuário **{}#{}**, foi banido temporariamente!\n\n**Duração**: {}\n**Motivo**: {}\n**Autor**: {}'.format(user.name, user.discriminator, reallytime, tempo, message.author.mention)
                    )
                    embed.set_thumbnail(
                        url='https://i.imgur.com/1iJeEea.jpg'
                    )
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
                    await client.send_message(canal, embed=embed)
                    time.sleep(timesquad)
                    await client.unban(message.server, user)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/tempban [username] [segundos] [motivo]`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            await client.delete_message(message)
            embed2 = discord.Embed(
                title='Permissão negada!',
                color=COR,
                description='Você não tem permissão para executar esse comando.'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed2)
        finally:
            pass


    if message.content.lower().startswith('/mute'):
        try:
            cargos = [
                # IDs dos cargos:
                "407677666750365706", #Diretor
                "417426253658849281", #Gerente
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    args = message.content.split(" ")
                    join = (" ".join(args[2:]))
                    user = message.mentions[0]
                    canal = client.get_channel('448449971629588481')
                    cargo = discord.utils.get(user.server.roles, name="Silenciado")
                    embed = discord.Embed(
                        title='SILENCIADO 🔈',
                        color=COR,
                        description='O usuário **{}#{}**, foi silenciado!\n\n**Motivo**: {}\n**Autor**: {}'.format(user.name, user.discriminator, join, message.author.mention))
                    embed.set_thumbnail(url='https://i.imgur.com/1iJeEea.jpg')
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
                    await client.send_message(canal, embed=embed)
                    await client.add_roles(user, cargo)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/mute [username] [motivo]`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            await client.delete_message(message)
            embed2 = discord.Embed(
                title='Permissão negada!',
                color=COR,
                description='Você não tem permissão para executar esse comando.'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed2)
        finally:
            pass


    if message.content.lower().startswith('/unmute'):
        try:
            cargos = [
                # IDs dos cargos:
                "407677666750365706", #Diretor
                "417426253658849281", #Gerente
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    args = message.content.split(" ")
                    user = message.mentions[0]
                    cargo = discord.utils.get(user.server.roles, name='Silenciado')
                    canal = client.get_channel('448449971629588481')
                    embed = discord.Embed(
                        title='DESMUTADO 🔊',
                        color=COR,
                        description='O usuário **{}#{}**, não está mais silenciado!\n\nAutor: {}'.format(user.name, user.discriminator, message.author.mention)
                    )
                    embed.set_thumbnail(
                        url='https://i.imgur.com/1iJeEea.jpg'
                    )
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
                    await client.send_message(canal, embed=embed)
                    await client.remove_roles(user, cargo)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/unmute [username]`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            await client.delete_message(message)
            embed2 = discord.Embed(
                title='Permissão negada!',
                color=COR,
                description='Você não tem permissão para executar esse comando.'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed2)
        finally:
            pass


    if message.content.lower().startswith('/ban'):
        try:
            cargos = [
                # IDs dos cargos:
                "407677666750365706", #Diretor
                "417426253658849281", #Gerente
                "407678188773179417", #Administrador
            ]
            for r in message.author.roles:
                if r.id in cargos:
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
                        description='O usuário **{}#{}**, foi banido!\n\n**Motivo**: {}\n**Autor**: {}'.format(user.name, user.discriminator, join, message.author.mention)
                    )
                    embed.set_thumbnail(
                        url='https://i.imgur.com/1iJeEea.jpg'
                    )
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
                    await client.send_message(channel1, embed=embed)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/ban [username] [motivo]`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            await client.delete_message(message)
            embed2 = discord.Embed(
                title='Permissão negada!',
                color=COR,
                description='Você não tem permissão para executar esse comando.'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed2)
        finally:
            pass

    if message.content.lower().startswith('/staff+'):
        try:
            cargos = [
                # IDs dos cargos:
                "407677666750365706", #Diretor
                "417426253658849281", #Gerente
                "407678188773179417", #Administrador
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    embed = discord.Embed(
                        title='Comandos para o cargo `STAFF+`:',
                        color=COR,
                        description='**/ban** [usuário] [motivo] » Banimento permanentemente do discord.\n'
                                    'exemplo: `/ban @{} Divulgação de link´s`\n\n'
                                    '**/kick** [usuário] » Expulsão do discord.\n'
                                    'exemplo: `/kick @{}`\n\n'
                                    '**/mute** [usuário] [motivo] » Mute permanentemente do discord.\n'
                                    'exemplo: `/mute @{} Spam`\n\n'
                                    '**/unmute** [usuário] » Unmute do discord.\n'
                                    'exemplo: `/unmute @{}`\n\n'
                                    '**/tempban** [usuário] [duração] [motivo] » Banimento temporariamente do discord.\n'
                                    'exemplo: `/tempban @{} 172800 Discriminação`\n\n'
                                    '**/tempmute** [usuário] [duração] [motivo] » Mute temporariamente do discord.\n'
                                    'exemplo: `/tempmute @{} 21600 Iniciativa de Flood`\n\n'
                                    '**/say** [mensagem] » bot repete a mensagem.\n'
                                    'exemplo: `/say Olá`\n\n'
                                    '**/stafflist** [mensagem/staff] » Bot repete a mensagem em Embed.\n'
                                    'exemplo: `/stafflist :white_small_square: {}`\n\n'
                                    '**/anunciar** [mensagem] » bot repete em Embed\n'
                                    'exemplo: `/anunciar Olá`\n\n'
                                    '**/changenick** [usuário] [nick] » Altera nick de um usuário.\n'
                                    'exemplo: `/changenick @{} MelhorServidor #END`\n\n'.format(message.author.name, message.author.name, message.author.name, message.author.name, message.author.name, message.author.name, message.author.name, message.author.name)
                    )
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_author(name=message.server.name, icon_url='https://i.imgur.com/1iJeEea.jpg')
                    embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
                    msg = await client.send_message(message.channel, '{}, enviamos uma mensagem em seu privado!'.format(message.author.mention))
                    await client.send_message(message.author, embed=embed)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/staff+`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            time.sleep(2)
            await client.delete_message(msg)
            await asyncio.sleep(21000)
            tst = await client.send_message(message.channel, '{}, libere o privado!'.format(message.author.mention))
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(tst)
        finally:
            pass

    if message.content.lower().startswith('/sugestão'):
        try:
            canal = client.get_channel('467704726411018260')
            await client.delete_message(message)
            remover_sugestao = message.content.replace("/sugestão", "")
            separar = remover_sugestao.split("|", 1)
            embed = discord.Embed(
                title="",
                color=COR,
                description="Sugestão recebida. \nEnviada por: {}".format(message.author.mention)
            )
            embed.set_author(name='Sugestão', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')
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
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(
                text='Sugestão enviada com sucesso.',
                icon_url=message.author.avatar_url
            )
            botmsg = await client.send_message(canal, embed=embed)
            await client.add_reaction(botmsg, "👍")
            await client.add_reaction(botmsg, "👎")
        except IndexError:
            await client.send_message(message.author, "Uso correto do comando: /sugestão <sugestão> | <por quê adicionariamos?>")
        except:
            await client.send_message(message.author, "Desculpe pelo erro.")
        finally:
            pass

    if message.content.lower().startswith('/dado'):
        numr = random.randint(1,6)
        embed = discord.Embed(
            title='Dado',
            color=COR,
            description=':game_die: Joguei o dado, o resultado é: {}'.format(str(numr))
        )
        embed.timestamp = datetime.datetime.utcnow()
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('/moeda'):
        escolha = random.randint(1,2)
        if escolha == 1:
            await client.add_reaction(message, '🌚')
        if escolha == 2:
            await client.add_reaction(message, '👑')


    if message.content.lower().startswith('/comandos'):
        try:
            embed = discord.Embed(
                title='Comandos do bot:',
                color=COR,
                description='*Esses são os comandos que não necessitam de permissão.*\n\n\n'
                            '**/info** [usuário] » Veja as informações de um usuário.\n\n'
                            '**/serverinfo** » Veja as informações do servidor.\n\n'
                            '**/dado** » Role um dado de um número de 1 a 6.\n\n'
                            '**/avatar** [usuário] » Veja o avatar seu ou de um membro.\n\n'
                            '**/convite** » Gere um convite para convidar todos para nossa comunidade.\n\n'
                            '**/ping** » Veja o tempo de resposta do bot.\n\n'
                            '**/ajuda** » Veja as informações básicas do servidor End.\n\n'
                            '**/youtuber** » Veja os requisitos para ter tag youtuber.\n\n'
                            '**/formulário** » Veja os formulários disponíveis do servidor.\n\n'
                            '**/ip** » Veja o IP de conexão ao servidor.\n\n'
                            '**/enviar** [dúvida] » Enviar uma dúvida para a equipe.\n\n'
                            '**/moeda** » Brinque de cara ou coroa.\n\n\n'
                            '**MINECRAFT:** `DESATIVADO!`\n\n'
                            '**/mineinfo** [nickname] » Envia informações de um usuário. `DESATIVADO!`\n\n'
                            '**/skin** [nickname] » Veja a skin de um usuário. `DESATIVADO!`\n\n'
                            '**/head** [nickname] » Veja a cabeça da skin de um usuário. `DESATIVADO!`\n\n\n'
                            '**UTILITÁRIOS:**\n\n'
                            '**/ativarvip** [nickname] | [rank] | [prova] » Crie uma solicitação do seu rank no Discord.\n\n'
                            '**/revisão** [nickname] | [motivo] | [por quê está irregular?] » Crie uma revisão de seu banimento.\n\n'
                            '**/reportar** [usuário/nickname] | [motivo] | [prova] » Denúncie um usuário do discord ou do servidor.\n\n'
                            '**/sugestão** [sugestão] | [por quê adicionariamos?] » Crie uma sugestão.'
                )
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_author(name=message.server.name, icon_url='https://i.imgur.com/1iJeEea.jpg')
            embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
            embed1 = discord.Embed(
                color=COR,
                description='Todos os comandos enviado em seu privado!'
            )
            embed1.set_author(name="End", icon_url="https://i.imgur.com/1iJeEea.jpg")
            apg = await client.send_message(message.channel, embed=embed1)
            await client.send_message(message.author, embed=embed)
        except IndexError:
            await asyncio.sleep(2)
            asyncio.sleep(21000)
            msg1 = await client.send_message(message.channel, 'Error')
            await client.delete_message(message)
            await asyncio.sleep(10)
            await client.delete_message(msg1)
        except:
            await client.delete_message(apg)
            tst = await client.send_message(message.channel, '{}, libere o privado!'.format(message.author.mention))
            await client.delete_message(message)
            await asyncio.sleep(10)
            await client.delete_message(tst)
        finally:
            pass

    if message.content.lower().startswith('/avatar'):
        try:
            user = message.mentions[0]
            embed = discord.Embed(
                title="",
                color=COR,
                description='Clique [aqui](' + user.avatar_url + ') para acessar o avatar do {}.'.format(user.name)
            )
            embed.set_author(
                name=message.server.name,
                icon_url='https://i.imgur.com/1iJeEea.jpg'
            )
            embed.set_image(
                url=user.avatar_url
            )
            await client.send_message(message.channel, embed=embed)
        except IndexError:
            await client.delete_message(message)
            msg = await client.send_message(message.channel, '{}, mencione um usuário existente, por exemplo, `/avatar @JohnnCosta`.'.format(message.author.mention))
            time.sleep(10)
            await client.delete_message(msg)
        except:
            msg1 = await client.send_message(message.channel, 'Desculpe pelo erro.')
            time.sleep(5)
            await client.delete_message(msg1)
        finally:
            pass

    if message.content.lower().startswith('/youtuber'):
        embed = discord.Embed(
            title='YOUTUBER 🔴',
            color=COR,
            description='Abaixo terão os requisitos para você que é youtuber e deseja possuir uma tag.\n\n**Shulker**: *1.000*;\n**End**: *3.000*;\n**Youtuber**: *10.000*;\n**Youtuber+**: *15.000*;\n\nCaso possui um dos requisitos, solicite a tag em nosso [Twitter](https://twitter.com/servidorEnd).'
        )
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.set_thumbnail(url="https://i.imgur.com/1iJeEea.jpg")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='End', icon_url="https://i.imgur.com/1iJeEea.jpg")
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('/ativarvip'):
        try:
            canal = client.get_channel('470390225529602048')
            await client.delete_message(message)
            remover_ativacao = message.content.replace("/ativarvip ", "")
            separar = remover_ativacao.split("|", 2)
            embed = discord.Embed(
                title='',
                color=COR,
                description='Solicitação recebida. \nEnviada por: {}'.format(message.author.mention)
            )
            embed.set_author(name='Ativação de vip', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')
            embed.add_field(
                name="**Nickname:**",
                value="%s" % "".join(separar[0]),
                inline=False
            )
            embed.add_field(
                name="**Rank:**",
                value="%s" % "".join(separar[1]),
                inline=False
            )
            embed.add_field(
                name="**Prova:**",
                value="%s" % "".join(separar[2]),
                inline=False
            )
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(
                text="Solicitação postada com sucesso.",
                icon_url=message.author.avatar_url
            )
            await client.send_message(canal, embed=embed)
            await client.delete_message(message)
        except IndexError:
            await client.send_message(message.author, '{}, use /ativarvip [nickname] | [rank] | [Prova]'.format(message.author.mention))
            await client.delete_message(message)
        except:
            await client.send_message(message.author, 'Desculpe pelo erro.')
            await client.delete_message(message)
        finally:
            pass

    if message.content.lower().startswith('/revisão'):
        try:
            canal = client.get_channel('466666024788295690')
            await client.delete_message(message)
            remover_revisão = message.content.replace("/revisão ", "")
            separar = remover_revisão.split("|", 2)
            embed = discord.Embed(
                title='',
                color=COR,
                description='Revisão recebida. \nEnviada por: {}'.format(message.author.mention)
            )
            embed.set_author(name='Revisão de banimento', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')
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
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text='Revisão postada com sucesso.', icon_url=message.author.avatar_url
            )
            await client.send_message(message.author, 'Sua revisão foi enviada')
            time.sleep(3)
            await client.send_message(canal, embed=embed)
        except IndexError:
            await client.send_message(message.author, '{}, use /revisão <nickname> | <motivo> | <Por quê está irregular?>'.format(message.author.mention))
        except:
            await client.send_message(message.author, 'Desculpe pelo erro.')
            print('Error')
        finally:
            pass

    if message.content.lower().startswith('/reportar'):
        try:
            canal = client.get_channel('466665871218049024')
            remover_reportar = message.content.replace("/reportar ", "")
            separar = remover_reportar.split("|", 2)

            embed = discord.Embed(
                title="",
                color=COR,
                description="Denúncia recebida. \nEnviada por: {}".format(message.author.mention)
            )
            embed.set_author(name='Denúncia', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')
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
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(
                text="Denúncia postada com sucesso.",
                icon_url=message.author.avatar_url
            )
            await client.send_message(canal, embed=embed)
            await client.delete_message(message)
        except IndexError:
            await client.send_message(message.author, '{}, use /reportar <Suspeito> | <Motivo> | <Prova>'.format(message.author.mention))
            await client.delete_message(message)
        except:
            await client.send_message(message.author, 'Desculpe pelo erro.')
            await client.delete_message(message)
        finally:
            pass


    if message.content.lower().startswith('/ajuda'):
        try:
            embed = discord.Embed(
                title='Você solicitou o comando e aqui estamos enviando umas informações básicas sobre o End.',
                color=COR,
                description='**Seja bem-vindo ao discord da rede End. Segue abaixo informações básicas sobre a rede que podem te ajudar!**\n\nIP: jogar.end-mc.com\n\nLoja: [clique aqui!](http://loja.end-mc.com)\n\nTwitter: [clique aqui!](https://twitter.com/ServidorEnd)\n\nFórum: **Em breve**\n\n***__Caso precise de outro tipo de ajuda contate um membro da equipe__***'
            )
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_author(name=message.server.name, icon_url='https://i.imgur.com/1iJeEea.jpg')
            embed.set_thumbnail(url='https://i.imgur.com/1iJeEea.jpg')
            embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
            msg = await client.send_message(message.channel, '{}, enviamos uma mensagem em seu privado!'.format(message.author.mention))
            await client.send_message(message.author, embed=embed)
        except IndexError:
            time.sleep(2)
            await client.delete_message(msg)
            asyncio.sleep(21000)
            msg1 = await client.send_message(message.channel, 'Error')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msg1)
        except:
            time.sleep(2)
            await client.delete_message(msg)
            asyncio.sleep(21000)
            tst = await client.send_message(message.channel, '{}, libere o privado!'.format(message.author.mention))
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(tst)
        finally:
            pass


    if message.content.lower().startswith('/serverinfo'):
        embed = discord.Embed(
            title='Informações do Servidor',
            color=0x03c3f5,
            descripition='Essas são as informações\n')
        embed.set_author(name=message.server.name, icon_url='https://i.imgur.com/1iJeEea.jpg')
        embed.add_field(name="Nome:", value=message.server.name, inline=True)
        embed.add_field(name=":crown: Dono:", value=message.server.owner.mention)
        embed.add_field(name="ID:", value=message.server.id, inline=True)
        embed.add_field(name="Cargos:", value=len(message.server.roles), inline=True)
        embed.add_field(name=":family: Membros:", value=len(message.server.members), inline=True)
        embed.add_field(name=":date: Criado em:", value=message.server.created_at.strftime.format("%d de %beiro de %Y, ás %H:%M:%S"))
        embed.add_field(name="Emojis:", value=f"{len(message.server.emojis)}/100")
        embed.add_field(name=":flag_br: Região:", value=str(message.server.region).title())
        embed.set_thumbnail(url='https://i.imgur.com/1iJeEea.jpg')
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text="End", icon_url="https://i.imgur.com/1iJeEea.jpg")
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('/info'):
        print(message.content)
        try:
            tmp1 = datetime.datetime.now()

            utcnow = datetime.time(hour=tmp1.hour, minute=tmp1.minute, second=tmp1.second)
            del tmp1
            user = message.mentions[0]
            userjoinedat = str(user.joined_at.format("%d de %B de %Y, ás %H:%M:%S")).split('.', 1)[0]
            usercreatedat = str(user.created_at.format("%d de %B de %Y, ás %H:%M:%S")).split('.', 1)[0]

            userembed = discord.Embed(
                title="Informações do usuário",
                description="\n",
                color=COR
            )
            userembed.set_author(
                name=user.server.name,
                icon_url=user.server.icon_url
            )
            userembed.add_field(
                name="Nome de usuário:",
                value=user.name
            )
            userembed.add_field(
                name="Juntou-se ao servidor em:",
                value=userjoinedat
            )
            userembed.add_field(
                name="Usuário criado em:",
                value=usercreatedat
            )
            userembed.add_field(
                name="Identificação:",
                value=user.discriminator
            )
            userembed.add_field(
                name="ID de Usuário:",
                value=user.id
            )
            userembed.set_thumbnail(
                url='https://i.imgur.com/1iJeEea.jpg'
            )
            userembed.timestamp = datetime.datetime.utcnow()
            userembed.set_footer(
                text="End",
                icon_url="https://i.imgur.com/1iJeEea.jpg"
            )
            await client.send_message(message.channel, embed=userembed)
        except IndexError:
            await client.delete_message(message)
            msg = await client.send_message(message.channel, "{}, mencione um usuário existente, por exemplo, `/info @JohnnCosta`.".format(message.author.mention))
            time.sleep(10)
            await client.delete_message(msg)
        except:
            await client.delete_message(message)
            msg1 = await client.send_message(message.channel, "Desculpe pelo erro.")
            time.sleep(5)
            await client.delete_message(msg1)
        finally:
            pass


    if message.content.lower().startswith('/formulário'):
        embed = discord.Embed(
            title='',
            color=COR,
            description='Abaixo terá o link de nossos formulários, lembrando, qualquer um outro não pertence à rede End.'
        )
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author(name='Formulários', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')
        embed.add_field(
            name='Aplicação para a equipe:',
            value='[Clique aqui!](https://t.co/wuIvHTsoAh)\n',
            inline=False
        )
        embed.add_field(
            name='Aplicação para o HRC:',
            value='[Clique aqui!](https://bit.ly/2KSMniB)',
            inline=False
        )
        embed.add_field(
            name='Aplicação para BUILDER:',
            value='[Clique aqui!](https://t.co/DXerrQWXPY)',
            inline=False
        )
        embed.set_footer(text='End', icon_url="https://i.imgur.com/1iJeEea.jpg")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('/ip'):
        await client.send_message(message.channel, 'Olá {}! Bom, o ip para conectar-se ao servidor é esse aqui: __jogar.end-mc.com__'.format(message.author.mention))

    if message.content.lower().startswith('/ping'):
        embed1 = discord.Embed(
            title='Pong! 🎾',
            color=COR,
            description="Pong `calc ms`"
        )
        bot_msg = await client.send_message(message.channel, embed=embed1)
        time_delta = bot_msg.timestamp - message.timestamp
        embed = discord.Embed(
            title='Pong!',
            color=COR,
            description=':ping_pong: Ping - {ping_sec} segundos'.format(ping_sec=time_delta.total_seconds())
        )
        embed.timestamp = datetime.datetime.utcnow()
        await client.edit_message(bot_msg, embed=embed)

    if message.content.lower().startswith('/convite'):
        msg = await client.send_message(message.channel, 'Convite do servidor: https://discord.gg/uhxPeqS')
        time.sleep(50)
        await client.delete_message(msg)

    if message.content.lower().startswith('/enviar'):
        try:
            await client.delete_message(message)
            canal = client.get_channel('470242474850254848')
            remover_duvida = message.content.replace("/enviar", "")
            separar = remover_duvida.split(" ", 1)
            embed = discord.Embed(
                title='',
                color=COR,
                description='Dúvida recebida.\nEnviada por: {}'.format(message.author.mention)
            )
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_author(name='Dúvida', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')
            embed.add_field(name='Dúvida:', value="```%s```" % "".join(separar[1]))
            embed.set_footer(text='End', icon_url=message.server.icon_url)
            await client.send_message(message.author, 'Essa é uma cópia de sua dúvida.')
            await client.send_message(message.author, embed=embed)
            botmsg = await client.send_message(canal, embed=embed)
        except IndexError:
            embed1 = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use, `/enviar [dúvida]`\n\nPor exemplo: /enviar Qual é o ip do servidor?'
            )
            embed1.timestamp = datetime.datetime.utcnow()
            embed1.set_thumbnail(url=message.server.icon_url)
            err = await client.send_message(message.channel, embed=embed1)
            time.sleep(10)
            await client.delete_message(message)
            await client.delete_message(err)
        except:
            tst = await client.send_message(message.channel, '{}, libere seu privado e efetue o comando novamente!'.format(message.author.mention))
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(tst)
        finally:
            pass


    if message.content.lower().startswith('/mineinfo'):
        try:
            remover_mineinfo = message.content.replace("/mineinfo", "")
            separar = remover_mineinfo.split(" ", 1)
            nome = "%s" % "".join(separar[1])

            #UUID
            uuid = mojang('https://api.mojang.com/users/profiles/minecraft/' + nome, 'id');
            #Cabeca
            #cabeca = "https://crafatar.com/renders/head/" + uuid +"?default=HF_Steve&overlay.png"
            #Corpo
            corpo = "https://crafatar.com/renders/body/" + uuid +"?default=HF_Steve&overlay.png"

            embed = discord.Embed(
                title='Informações:',
                color=COR,
                description="**Nickname**: {}\n**UUID**: {}".format(nome, uuid)
            )
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_author(name='Perfil de Minecraft:', icon_url=message.server.icon_url)
            await client.send_message(message.channel, embed=embed)
        except IndexError:
            embed1 = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/mineinfo [nickname]`'
            )
            embed1.timestamp = datetime.datetime.utcnow()
            embed1.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            msg = await client.send_message(message.channel, embed=embed1)
            await client.delete_message(message)
            time.sleep(15)
            await client.delete_message(msg)
        except:
            embed2 = discord.Embed(
                title='Usuário não encontrado!',
                color=COR,
                description='Use `/mineinfo [nickname]`'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            msg1 = await client.send_message(message.channel, embed=embed2)
            await client.delete_message(message)
            time.sleep(15)
            await client.delete_message(msg1)
        finally:
            pass

    if message.content.lower().startswith('/head'):
        try:
            remover_cabeca = message.content.replace("/head", "")
            separar = remover_cabeca.split(" ", 1)
            nome = "%s" % "".join(separar[1])

            #UUID
            uuid = mojang('https://api.mojang.com/users/profiles/minecraft/' + nome, 'id');
            #Cabeca
            cabeca = "https://crafatar.com/renders/head/" + uuid +"?default=HF_Steve&overlay.png"

            head = discord.Embed()
            head.set_image(url=cabeca)
            await client.send_message(message.channel, embed=head)
        except IndexError:
            embed = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/head [nickname]`'
            )
            embed.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            msg = await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
            time.sleep(15)
            await client.delete_message(msg)
        except:
            embed1 = discord.Embed(
                title='Usuário não encontrado!',
                color=COR,
                description='Use `/head [nickname]`'
            )
            embed1.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            msg1 = await client.send_message(message.channel, embed=embed1)
            await client.delete_message(message)
            time.sleep(15)
            await client.delete_message(msg1)
        finally:
            pass

    if message.content.lower().startswith('/skin'):
        try:
            remover_mineinfo = message.content.replace("/skin", "")
            separar = remover_mineinfo.split(" ", 1)
            nome = "%s" % "".join(separar[1])

            #UUID
            uuid = mojang('https://api.mojang.com/users/profiles/minecraft/' + nome, 'id');
            #Corpo
            corpo = "https://crafatar.com/renders/body/" + uuid +"?default=HF_Steve&overlay.png"

            await client.send_file(message.channel, '{}.png'.format(corpo))
        except IndexError:
            embed = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/skin [nickname]`'
            )
            embed.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            msg = await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
            time.sleep(15)
            await client.delete_message(msg)
        except:
            embed1 = discord.Embed(
                title='Usuário não encontrado!',
                color=COR,
                description='Use `/skin [nickname]`'
            )
            embed1.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            msg1 = await client.send_message(message.channel, embed=embed1)
            await client.delete_message(message)
            time.sleep(15)
            await client.delete_message(msg1)
        finally:
            pass

    if message.content.lower().startswith('/responder'):
        try:
            cargos = [
                # IDs dos cargos:
                "407677666750365706", #Diretor
                "417426253658849281", #Gerente
                "407678188773179417", #Administrador
                "407678481670078475", #Moderador
                "407706417282416641", #Ajudante
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    canal = client.get_channel('470242474850254848')
                    await client.delete_message(message)
                    user = message.mentions[0]
                    remover_resposta = message.content.replace("/responder", "")
                    separar = remover_resposta.split(" ", 2)
                    embed = discord.Embed(
                        title='',
                        color=COR,
                        description='Dúvida respondida.\nRespondida por: {}'.format(message.author.mention)
                    )
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_author(name='Dúvida', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')
                    embed.add_field(name='Resposta:', value="```%s```" % "".join(separar[2]))
                    embed.set_footer(text='End', icon_url=message.server.icon_url)
                    await client.send_message(user, embed=embed)
                    emb = await client.send_message(canal, embed=embed)
        except IndexError:
            embed1 = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use, `/responder [usuário] [resposta]`\nPor exemplo: /responder {} O ip do servidor é jogar.end-mc.com'.format(message.author.mention)
            )
            embed1.timestamp = datetime.datetime.utcnow()
            embed1.set_thumbnail(url=message.server.icon_url)
            er = await client.send_message(message.channel, embed=embed1)
            time.sleep(50)
            await client.delete_message(message)
            await client.delete_message(er)
        except:
            await client.delete_message(emb)
            asd = await client.send_message(message.channel, 'O {}, está com a dm privada!'.format(user.mention))
            time.sleep(10)
            await client.delete_message(message)
            await client.delete_message(asd)
        finally:
            pass

    if message.content.lower().startswith('/tempmute'):
        try:
            cargos = [
                # IDs dos cargos:
                "407677666750365706", #Diretor
                "417426253658849281", #Gerente
                "407678188773179417", #Administrador
                "407678481670078475", #Moderador
                "407706417282416641", #Ajudante
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    args = message.content.split(" ")
                    tempo = (" ".join(args[3:]))
                    user = message.mentions[0]
                    cargo = discord.utils.get(user.server.roles, name='Silenciado')
                    canal = client.get_channel('448449971629588481')
                    await client.add_roles(user, cargo)
                    print('O {} foi mutado temporariamente.'.format(user))
                    temp = args[2]
                    timesquad = int(temp)
                    reallytime = datetime.timedelta(seconds=timesquad)
                    embed = discord.Embed(
                        title='SILENCIADO 🔈',
                        color=COR,
                        description='O usuário **{}#{}**, foi silenciado!\n\n**Duração**: {}\n**Motivo**: {}\n**Autor**: {}'.format(user.name, user.discriminator, reallytime, tempo, message.author.mention)
                    )
                    embed.set_thumbnail(
                        url='https://i.imgur.com/1iJeEea.jpg'
                    )
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
                    await client.send_message(canal, embed=embed)
                    time.sleep(timesquad)
                    cargo = discord.utils.get(user.server.roles, name='Silenciado')
                    await client.remove_roles(user, cargo)
                    print('O {} foi desmutado.'.format(user))
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/tempmute [username] [segundos] [motivo]`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            await client.delete_message(message)
            embed2 = discord.Embed(
                title='Permissão negada!',
                color=COR,
                description='Você não tem permissão para executar esse comando.'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed2)
        finally:
            pass

client.run(os.environ.get("BOT_TOKEN"))
