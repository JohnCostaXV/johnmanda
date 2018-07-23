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

RANDOM_STATUS = ['jogar.end-mc.com']
RANDOM_AUTO = ['**TWITTER**\n\nSiga nosso twitter para ter informações exclusívas da nossa rede de servidores End. - https://twitter.com/ServidorEnd']

client = discord.Client()
COR = 0x3498DB
testmsgid = None
testmsguser = None

minutes = 0
hour = 0
msg_id = None
msg_user = None
user_timer = {}
user_spam_count = {}

def mojang(site, json_retorno):
  site_conectar = requests.get(site)
  if site_conectar.status_code == 200:
       _json = json.loads(site_conectar.content)
       return _json[json_retorno]
  else:
     return "cbe7af2b61da46e3aa7d3da39bd55b93"


@client.event
async def on_member_join(member):
    canal = client.get_channel('448326795692081152')
    await client.send_message(canal, 'Seja bem-vindo(a) {}!'.format(member.mention))
    embed = discord.Embed(
        title='Seja bem-vindo(a) ao grupo do Discord da rede de servidores End!',
        color=COR,
        description='**Redes sociais:**\n\nTwitter: https://twitter.com/ServidoresEnd\nDiscord: https://discord.gg/uhxPeqS\n\n**Endereços:**\n\nEndereço de loja: https://loja.end-mc.com/\nEndereço de ip para conexão ao servidor: jogar.end-mc.com\n\nO servidor encontra-se em desenvolvimento e todas as atualizações são anunciadas aqui, no Discord, e em nosso Twitter.\n\nData de lançamento: *Em breve*'
    )
    embed.set_author(name='{}#{}'.format(member.name, member.discriminator), icon_url=member.avatar_url)
    embed.set_thumbnail(url="https://i.imgur.com/1iJeEea.jpg")
    embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
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
    print('Status = {}'.format(RANDOM_STATUS))
    try:
        choice = random.choice(RANDOM_STATUS)
        await client.change_presence(game=discord.Game(name=choice, type=1))
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


@client.event
@commands.has_any_role('Diretor', 'Gerente', 'Desenvolvedor', 'Administrador', 'Moderador',  'Ajudante')
async def on_message(message):
    if message.content.lower().startswith('/staff-'):
        try:
            embed = discord.Embed(
                title='Comandos para o cargo `STAFF`:',
                color=COR,
                description='/tempmute [usuário] » Silenciar temporariamente do discord.\n'
                            'exemplo: `/tempmute @JohnnCosta 28800 Palavras inadequadas`\n\n'
                            '*Lembrando que os tempmute é contato por segundo! Caso esteja com dúvidas em relação ao tempo de cada punição, envie em `#comandos-dos-bots` ´/helpstaff´.*'
            )
            embed.set_author(name=message.server.name, icon_url='https://i.imgur.com/1iJeEea.jpg')
            embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
            msg = await client.send_message(message.channel, '{}, enviamos uma mensagem em seu privado!'.format(message.author.mention))
            await client.send_message(message.author, embed=embed)
        except IndexError:
            time.sleep(2)
            await client.delete_message(msg)
            asyncio.sleep(21000)
            msg1 = await client.send_message(message.channel, 'Comando incorreto!')
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


    if message.content.lower().startswith('/tempmute'):
        try:
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
            embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
            await client.send_message(canal, embed=embed)
            time.sleep(timesquad)
            cargo = discord.utils.get(user.server.roles, name='Silenciado')
            await client.remove_roles(user, cargo)
        #else:
            #msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            #time.sleep(10)
            #await client.delete_message(message)
            #await client.delete_message(msglg)
        except IndexError:
            msg = await client.send_message(message.channel, 'O usuário não é existente ou saiu!')
            time.sleep(10)
            await client.delete_message(msg)
        except:
            msg1 = await client.send_message(message.channel, 'Sem permissão!')
            time.sleep(10)
            await client.delete_message(msg1)
        finally:
            pass

    if message.content.lower().startswith('/responder'):
        try:
            await client.delete_message(message)
            user = message.mentions[0]
            remover_resposta = message.content.replace("/responder", "")
            separar = remover_resposta.split(" ", 2)
            embed = discord.Embed(
                title='DÚVIDA 🔍',
                color=COR,
                description='Dúvida respondida.\nRespondida por: {}'.format(message.author.mention)
            )
            embed.add_field(name='Resposta:', value="```%s```" % "".join(separar[2]))
            embed.set_footer(text='End', icon_url=message.server.icon_url)
            await client.send_message(user, embed=embed)
            await client.send_message(message.channel, embed=embed)
            await client.add_reaction(user, '✅')
        except IndexError:
            embed1 = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use, `/responder [usuário] [resposta]`\nPor exemplo: /responder @JohnnCosta O ip do servidor é jogar.end-mc.com'
            )
            embed1.set_thumbnail(url=message.server.icon_url)
            er = await client.send_message(message.channel, embed=embed1)
            time.sleep(50)
            await client.delete_message(message)
            await client.delete_message(er)
        except:
            asd = await client.send_message(message.channel, 'O {}, está com a dm privada!'.format(user.mention))
            time.sleep(10)
            await client.delete_message(message)
            await client.delete_message(asd)
        finally:
            pass

    if message.content.lower().startswith('/helpstaff'):
        try:
            await client.delete_message(message)
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
            embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
            msg = await client.send_message(message.channel, '{}, enviamos uma mensagem em seu privado!'.format(message.author.mention))
            await client.send_message(message.author, embed=embed)
        except IndexError:
            time.sleep(2)
            await client.delete_message(msg)
            asyncio.sleep(21000)
            msg1 = await client.send_message(message.channel, 'Comando incorreto!')
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



@client.event
@commands.has_any_role('Diretor', 'Gerente', 'Desenvolvedor', 'Administrador')
async def on_message(message):
    if message.content.lower().startswith('/tt'):
        try:
            await client.delete_message(message)
            auto = random.choice(RANDOM_AUTO)
            canal = client.get_channel('407669684616560650')
            time.sleep(3)
            await client.send_message(canal, auto)
        except IndexError:
            msglg = await client.send_message(message.channel, 'Comando incorreto.')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        except:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        finally:
            pass


    if message.content.lower().startswith('/end'):
        try:
            await client.delete_message(message)
            user = message.mentions[0]
            args = message.content.split(" ")
            await client.change_nickname(user, " ".join(args[2:]))
        except IndexError:
            msglg = await client.send_message(message.channel, 'Comando incorreto.')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        except:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        finally:
            pass

    if message.content.lower().startswith('/say'):
        try:
            args = message.content.split(" ")
            await client.send_message(message.channel, (" ".join(args[1:])))
            asyncio.sleep(1)
            await client.delete_message(message)
            asyncio.sleep(1)
        except IndexError:
            msglg = await client.send_message(message.channel, 'Comando incorreto.')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        except:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        finally:
            pass


    if message.content.lower().startswith('/anunciar'):
        try:
            await client.delete_message(message)
            args = message.content.split(" ")
            embed = discord.Embed(
                title="End  📢",
                color=COR,
                description=" ".join(args[1:])
            )
            embed.set_footer(
                text="Enviado por: {}  •  End".format(message.author.name),
                icon_url='https://media3.giphy.com/media/qi29MoLjWNPUI/giphy.gif'
            )
            await client.send_message(message.channel, "@everyone")
            await client.send_message(message.channel, embed=embed)
        except IndexError:
            msglg = await client.send_message(message.channel, 'Comando incorreto.')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        except:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        finally:
            pass



    if message.content.lower().startswith('/stafflist'):
        try:
            await client.delete_message(message)
            args = message.content.split(" ")
            embed = discord.Embed(
                title="Lista da Equipe:",
                color=COR,
                description=" ".join(args[1:])
            )
            embed.set_footer(
                text="Enviado por: {}  •  End".format(message.author.name),
                icon_url='https://media3.giphy.com/media/qi29MoLjWNPUI/giphy.gif'
            )
            await client.send_message(message.channel, "@everyone")
            await client.send_message(message.channel, embed=embed)
        except IndexError:
            msglg = await client.send_message(message.channel, 'Comando incorreto.')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        except:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        finally:
            pass


    if message.content.lower().startswith('/kick'):
        try:
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
            embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
            await client.send_message(channel, embed=embed)
        except IndexError:
            msglg = await client.send_message(message.channel, 'Comando incorreto.')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        except:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        finally:
            pass


    if message.content.lower().startswith('/tempban'):
        try:
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
            embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
            await client.send_message(canal, embed=embed)
            time.sleep(timesquad)
            await client.unban(message.server, user)
        except IndexError:
            msg = await client.send_message(message.channel, 'O usuário não é existente ou saiu!')
            time.sleep(10)
            await client.delete_message(msg)
        except:
            msg1 = await client.send_message(message.channel, 'Sem permissão!')
            time.sleep(10)
            await client.delete_message(msg1)
        finally:
            pass


    if message.content.lower().startswith('/mute'):
        try:
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
            embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
            await client.send_message(canal, embed=embed)
            await client.add_roles(user, cargo)
        except IndexError:
            msglg = await client.send_message(message.channel, 'Comando incorreto.')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        except:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        finally:
            pass


    if message.content.lower().startswith('/unmute'):
        try:
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
            embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
            await client.send_message(canal, embed=embed)
            await client.remove_roles(user, cargo)
        except IndexError:
            msglg = await client.send_message(message.channel, 'Comando incorreto.')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        except:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        finally:
            pass


    if message.content.lower().startswith('/ban'):
        try:
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
            embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
            await client.send_message(channel1, embed=embed)
        except IndexError:
            msglg = await client.send_message(message.channel, 'Comando incorreto.')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        except:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msglg)
        finally:
            passs

    if message.content.lower().startswith('/staff+'):
        try:
            await client.delete_message(message)
            embed = discord.Embed(
                title='Comandos para o cargo `STAFF+`:',
                color=COR,
                description='/ban [usuário] [motivo] » Banimento permanentemente do discord.\n'
                            'exemplo: `/ban @JohnnCosta Divulgação de link´s`\n\n'
                            '/kick [usuário] » Expulsão do discord.\n'
                            'exemplo: `/kick @JohnnCosta`\n\n'
                            '/mute [usuário] [motivo] » Mute permanentemente do discord.\n'
                            'exemplo: `/mute @JohnnCosta Spam`\n\n'
                            '/unmute [usuário] » Unmute do discord.\n'
                            'exemplo: `/unmute @JohnnCosta`\n\n'
                            '/tempban [usuário] [duração] [motivo] » Banimento temporariamente do discord.\n'
                            'exemplo: `/tempban @JohnnCosta 172800 Discriminação`\n\n'
                            '/tempmute [usuário] [duração] [motivo] » Mute temporariamente do discord.\n'
                            'exemplo: `/tempmute @JohnnCosta 21600 Iniciativa de Flood`\n\n'
                            '/say [mensagem] » bot repete a mensagem.\n'
                            'exemplo: `/say Olá`\n\n'
                            '/anunciar [mensagem] » bot repete em Embed\n'
                            'exemplo: `/anunciar Olá`\n\n'
            )
            embed.set_author(name=message.server.name, icon_url='https://i.imgur.com/1iJeEea.jpg')
            embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
            msg = await client.send_message(message.channel, '{}, enviamos uma mensagem em seu privado!'.format(message.author.mention))
            await client.send_message(message.author, embed=embed)
        except IndexError:
            time.sleep(2)
            await client.delete_message(msg)
            await asyncio.sleep(21000)
            msg1 = await client.send_message(message.channel, 'Comando incorreto!')
            await client.delete_message(message)
            time.sleep(10)
            await client.delete_message(msg1)
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




@client.event
@commands.has_any_role('Diretor', 'Gerente', 'Desenvolvedor', 'Administrador', 'Bots', 'Moderador',  'Ajudante', 'Designer', 'Construtor', 'Youtuber+', 'Youtuber', 'Beta', 'End', 'Dragon', 'Shulker', 'Membro')
async def on_message(message):
    if message.content.lower().startswith('/sugestão'):
        try:
            canal = client.get_channel('467704726411018260')
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
                text=datetime.datetime.now(),
                icon_url=message.author.avatar_url
            )
            botmsg = await client.send_message(canal, embed=embed)
            await client.add_reaction(botmsg, "👍")
            await client.add_reaction(botmsg, "👎")
        except IndexError:
            await client.send_message(message.author, "Uso correto do comando: /sugestão <sugestão> | <por quê adicionariamos?>")
        except:
            await client.send_message(message.author,"Desculpe pelo erro.")
        finally:
            pass

    if message.content.lower().startswith('/dado'):
        numr = random.randint(1,6)
        embed = discord.Embed(
            title='Dado',
            color=COR,
            description=':game_die: Joguei o dado, o resultado é: {}'.format(str(numr))
        )
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
                            '**/dado** » Role um dado de um número de 1 á 6.\n\n'
                            '**/avatar** [usuário] » Veja o avatar seu ou de um membro.\n\n'
                            '**/convite** » Gere um convite para convidar todos para nossa comunidade.\n\n'
                            '**/ping** » Veja o tempo de resposta do bot.\n\n'
                            '**/ajuda** » Veja as informações básicas do servidor End.\n\n'
                            '**/youtuber** » Veja os requisitos para ter tag youtuber.\n\n'
                            '**/formulário** » Veja os formulários disponíveis do servidor.\n\n'
                            '**/ip** » Veja o IP de conexão ao servidor.\n\n'
                            '**/enviar** [dúvida] » Enviar uma dúvida para a equipe.\n\n'
                            '**/moeda** » Brinque de cara ou coroa.\n\n\n'
                            '**UTILITÁRIOS:**\n\n'
                            '**/ativarvip** [nickname] | [rank] | [prova] » Crie uma solicitação do seu rank no Discord.\n\n'
                            '**/revisão** [nickname] | [motivo] | [por quê está irregular?] » Crie uma revisão de seu banimento.\n\n'
                            '**/reportar** [usuário/nickname] | [motivo] | [prova] » Denúncie um usuário do discord ou do servidor.\n\n'
                            '**/sugestão** [sugestão] | [por quê adicionariamos?] » Crie uma sugestão.'
                )
            embed.set_author(name=message.server.name, icon_url='https://i.imgur.com/1iJeEea.jpg')
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
            description='Abaixo terão os requisitos para você que é youtuber e deseja possuir uma tag.\n\n**Shulker**: *1.000*;\n**End**: *3.000*;\n**Youtuber**: *10.000*;\n**Youtuber+**: *15.000*;\n\nCaso possui um dos requisitos, solicite a tag a um superior.'
        )
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.set_thumbnail(url="https://i.imgur.com/1iJeEea.jpg")
        embed.set_footer(text='End', icon_url="https://i.imgur.com/1iJeEea.jpg")
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('/ativarvip'):
        try:
            canal = client.get_channel('470390225529602048')
            await client.delete_message(message)
            remover_ativacao = message.content.replace("/ativarvip ", "")
            separar = remover_ativacao.split("|", 2)
            embed = discord.Embed(
                title='ATIVAÇÃO DE RANKS 💎',
                color=COR,
                description='Solicitação recebida. \nEnviada por: {}'.format(message.author.mention)
            )
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
        embed.add_field(name=":date: Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"))
        embed.add_field(name="Emojis:", value=f"{len(message.server.emojis)}/100")
        embed.add_field(name=":flag_br: Região:", value=str(message.server.region).title())
        embed.set_thumbnail(url='https://i.imgur.com/1iJeEea.jpg')
        embed.set_footer(text="End", icon_url="https://i.imgur.com/1iJeEea.jpg")
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('/info'):
        try:
            tmp1 = datetime.datetime.now()

            utcnow = datetime.time(hour=tmp1.hour, minute=tmp1.minute, second=tmp1.second)
            del tmp1
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]

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
            userembed.set_footer(
                text="End",
                icon_url="https://i.imgur.com/1iJeEea.jpg"
            )
            await client.send_message(message.channel, embed=userembed)
        except IndexError:
            await client.delete_message(message)
            msg = await client.send_message(message.channel, "{}, mencione um usuário existente, por exemplo, `/userinfo @JohnnCosta`.".format(message.author.mention))
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
            title='FORMULÁRIOS 📝',
            color=COR,
            description='Abaixo terá o link de nossos formulários, lembrando, qualquer um outro não pertence à rede End.'
        )
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
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.set_thumbnail(url="https://i.imgur.com/1iJeEea.jpg")
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
                title='DÚVIDA 🔍',
                color=COR,
                description='Dúvida recebida.\nEnviada por: {}'.format(message.author.mention)
            )
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
        remover_mineinfo = message.content.replace("/enviar", "")
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
        embed.set_image(url=corpo)
        embed.set_author(name='Perfil de Minecraft:', icon_url=message.server.icon_url)
        await client.send_message(message.channel, embed=embed)



client.run(os.environ.get("BOT_TOKEN"))
