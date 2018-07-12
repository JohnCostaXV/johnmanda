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
import base64

RANDOM_STATUS = ['jogar.end-mc.com']
RANDOM_AUTO = ['**TWITTER**\n\nSiga nosso twitter para ter informações exclusívas da nossa rede de servidores End. - https://twitter.com/ServidorEnd']

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
        description='**Redes sociais:**\n\nTwitter: https://twitter.com/ServidoresEnd\nDiscord: https://discord.gg/uhxPeqS\n\n**Endereços:**\n\nEndereço de loja: https://loja.end-mc.com/\nEndereço de ip para conexão ao servidor: jogar.end-mc.com\n\nO servidor encontra-se em desenvolvimento e todas as atualizações são anunciadas aqui, no Discord, e em nosso Twitter.\n\n*Data de lançamento: 21/07/2018*'
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
        if '407677666750365706' or '431189978631110666' or '417426253658849281' or '407678188773179417' in [role.id for role in message.author.roles]:
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
        
    if message.content.lower().startswith('/youtuber'):
        embed = discord.Embed(
            title='YOUTUBER 🔴',
            color=COR,
            description='Abaixo terão os requisitos para você que é youtuber e deseja possuir uma tag.\n\n**Shulker**: *1.000*;\n**End**: *3.000*;\n**Youtuber**: *10.000*;\n**Youtuber+**: *15.000*;\n\nCaso possui um dos requisitos, solicite a tag a um superior.'
        )
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.set_thumbnail(url="https://i.imgur.com/yJey64O.png")
        embed.set_footer(text='End', icon_url="https://i.imgur.com/yJey64O.png")
        await client.send_message(message.channel, embed=embed)
    
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
    
    if message.content.startswith('/tt'):
        if '431189978631110666' in [role.id for role in message.author.roles]:
            await client.delete_message(message)
            auto = random.choice(RANDOM_AUTO)
            canal = client.get_channel('407669684616560650')
            time.sleep(3)
            await client.send_message(canal, auto)

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
            embed.set_footer(
                text="Denúncia postada com sucesso.",
                icon_url=message.author.avatar_url
            )
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except IndexError:
            await client.send_message(message.author, '{}, use /reportar <Suspeito> | <Motivo> | <Prova>'.format(message.author.mention))
            await client.delete_message(message)
        except:
            await client.send_message(message.author, 'Desculpe pelo erro.')
            await client.delete_message(message)
        finally:
            pass

    if message.content.startswith('/ajuda'):
        try:
            embed = discord.Embed(
                title='Você solicitou o comando e aqui estamos enviando umas informações básicas sobre o End.',
                color=COR,
                description='**Seja bem-vindo ao discord da rede End. Segue abaixo informações básicas sobre a rede que podem te ajudar!**\n\nIP: jogar.end-mc.com\n\nLoja: [clique aqui!](http://loja.end-mc.com)\n\nTwitter: [clique aqui!](https://twitter.com/ServidorEnd)\n\nFórum: **Em breve**\n\n***__Caso precise de outro tipo de ajuda contate um membro da equipe__***'
            )
            embed.set_author(name=message.server.name, icon_url='https://i.imgur.com/yJey64O.png')
            embed.set_thumbnail(url='https://i.imgur.com/yJey64O.png')
            embed.set_footer(text='End', icon_url='https://i.imgur.com/yJey64O.png')
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

    if message.content.startswith('/kick'):
        if '407677666750365706' or '431189978631110666' or '417426253658849281' or '407678188773179417' in [role.id for role in message.author.roles]:
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
                url='https://i.imgur.com/yJey64O.png'
            )
            embed.set_footer(text='End', icon_url='https://i.imgur.com/yJey64O.png')
            await client.send_message(channel, embed=embed)
        else:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            time.sleep(10)
            await client.delete_message(message)
            await client.delete_message(msglg)  

    if message.content.startswith('/ban'):
        if '407677666750365706' or '431189978631110666' or '417426253658849281' or '407678188773179417' in [role.id for role in message.author.roles]:
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
                url='https://i.imgur.com/yJey64O.png'
            )
            embed.set_footer(text='End', icon_url='https://i.imgur.com/yJey64O.png')
        else:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            time.sleep(10)
            await client.delete_message(message)
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
        if '407677666750365706' or '431189978631110666' or '417426253658849281' or '407678188773179417' in [role.id for role in message.author.roles]:
            await client.delete_message(message)
            args = message.content.split(" ")
            embed = discord.Embed(
                title="End 📢",
                color=COR,
                description=" ".join(args[1:])
            )
            embed.set_footer(
                text="Enviado por: {} • End".format(message.author.name),
                icon_url='https://i.imgur.com/yJey64O.png'
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

    if message.content.startswith('/serverinfo'):
        embed = discord.Embed(
            title='Informações do Servidor',
            color=0x03c3f5,
            descripition='Essas são as informações\n')
        embed.set_author(name=message.server.name, icon_url='https://i.imgur.com/yJey64O.png')
        embed.add_field(name="Nome:", value=message.server.name, inline=True)
        embed.add_field(name=":crown: Dono:", value=message.server.owner.mention)
        embed.add_field(name="ID:", value=message.server.id, inline=True)
        embed.add_field(name="Cargos:", value=len(message.server.roles), inline=True)
        embed.add_field(name=":family: Membros:", value=len(message.server.members), inline=True)
        embed.add_field(name=":date: Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"))
        embed.add_field(name="Emojis:", value=f"{len(message.server.emojis)}/100")
        embed.add_field(name=":flag_br: Região:", value=str(message.server.region).title())
        embed.set_thumbnail(url='https://i.imgur.com/yJey64O.png')
        embed.set_footer(text="End", icon_url="https://i.imgur.com/yJey64O.png")
        await client.send_message(message.channel, embed=embed)        
            
    if message.content.startswith('/avatar'):
        try:
            user = message.mentions[0]
            embed = discord.Embed(
                title="",
                color=COR,
                description='Clique [aqui](' + user.avatar_url + ') para acessar o avatar do {}.'.format(user.name)
            )
            embed.set_author(
                name=message.server.name,
                icon_url='https://i.imgur.com/yJey64O.png'
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
            

    if message.content.lower().startswith('/userinfo'):
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
                url='https://i.imgur.com/yJey64O.png'
            )
            userembed.set_footer(
                text="End",
                icon_url="https://i.imgur.com/yJey64O.png"
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
     
    if message.content.startswith('/formulário'):
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
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.set_thumbnail(url="https://i.imgur.com/yJey64O.png")
        embed.set_footer(text='End', icon_url="https://i.imgur.com/yJey64O.png")
        await client.send_message(message.channel, embed=embed)
       
    if message.content.startswith('/ip'):
        await client.send_message(message.channel, 'Olá {}! Bom, o ip para conectar-se ao servidor é esse aqui: __jogar.end-mc.com__'.format(message.author.mention))


    if message.content.startswith('/mute'):
        if '407677666750365706' or '431189978631110666' or '417426253658849281' in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            join = (" ".join(args[2:]))
            user = message.mentions[0]
            cargo = discord.utils.find(lambda r: r.name == "Silenciado", message.server.roles)
            canal = client.get_channel('448449971629588481')
            await client.add_roles(user, cargo)
            embed = discord.Embed(
                title='SILENCIADO ⛔',
                color=COR,
                description='O usuário **{}#{}**, foi silenciado!\n\n**Motivo**: {}\n**Autor**: {}'.format(user.name, join, user.discriminator, message.author.mention)
            )
            embed.set_thumbnail(
                url='https://i.imgur.com/yJey64O.png'
            )
            embed.set_footer(text='End', icon_url='https://i.imgur.com/yJey64O.png')
            await client.send_message(canal, embed=embed)
        else:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            time.sleep(10)
            await client.delete_message(message)
            await client.delete_message(msglg)

    if message.content.startswith('/unmute'):
        if '407677666750365706' or '431189978631110666' or '417426253658849281' in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            user = message.mentions[0]
            cargo = discord.utils.get(message.server.roles, name='Silenciado')
            canal = client.get_channel('448449971629588481')
            await client.remove_roles(user, cargo)
            embed = discord.Embed(
                title='DESMUTADO',
                color=COR,
                description='O usuário **{}#{}**, foi desmutado!\n\nAutor: {}'.format(user.name, user.discriminator, message.author.mention)
            )
            embed.set_thumbnail(
                url='https://i.imgur.com/yJey64O.png'
            )
            embed.set_footer(text='End', icon_url='https://i.imgur.com/yJey64O.png')
            await client.send_message(canal, embed=embed)
        else:
            msg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            time.sleep(10)
            await client.delete_message(message)
            await client.delete_message(msg)

    if message.content.startswith('/tempmute'):
        if '407677666750365706' or '417426253658849281' or '431189978631110666' or  '407678188773179417' or '407678481670078475' or '407706417282416641' in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            tempo = (" ".join(args[3:]))
            user = message.mentions[0]
            cargo = discord.utils.get(user.guild.roles, name='Silenciado')
            canal = client.get_channel('448449971629588481')
            await client.add_roles(user, cargo)
            timesquad = int(tempo)
            reallytime = "{}".format(datetime.timedelta(seconds=timesquad))
            embed = discord.Embed(
                title='SILENCIADO ⛔',
                color=COR,
                description='O usuário **{}#{}**, foi silenciado!\n\nDuração: {}\nMotivo: {}\nAutor: {}'.format(user.name, user.discriminator, reallytime, tempo, message.author.mention)
            )
            embed.set_thumbnail(
                url='https://i.imgur.com/yJey64O.png'
            )
            embed.set_footer(text='End', icon_url='https://i.imgur.com/yJey64O.png')
            await client.send_message(canal, embed=embed)
            await client.delete_message(message)
            time.sleep(timesquad)
            cargo = discord.utils.get(user.guild.roles, name='Silenciado')
            await client.remove_roles(user, cargo)
        else:
            msglg = await client.send_message(message.channel, '❌ Você não pode fazer isso!')
            time.sleep(10)
            await client.delete_message(message)
            await client.delete_message(msglg)

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
            description=':ping_pong: Ping: `{ping_sec}` ms.'.format(ping_sec=time_delta.total_seconds())
        )
        embed.set_footer(text='End', icon_url='https://i.imgur.com/yJey64O.png')
        await client.edit_message(bot_msg, embed=embed)


client.run(os.environ.get("BOT_TOKEN"))
