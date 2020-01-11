import discord
from discord.ext import commands
from os import environ

client = commands.Bot(command_prefix = '/')
game = discord.Game("in goodstuff!")
lastHost = ''
lastStarting = ''
lastMessageID = ''
lastTitle = ''
discordToken = environ.get('discordToken')

@client.event
async def on_ready():
    print ('Bot is ready.')
    await client.change_presence(activity=game)
    embed = discord.Embed(
       title = '**:white_check_mark: Market Logger is Online!**',
       colour = discord.Colour.green()
    )
        
    channel = client.get_channel(664965790037966897)
    await channel.send(embed=embed)

@client.event
async def on_message(message):
    channel = client.get_channel(665331323996733441)
    postChannel = client.get_channel(665346430298488845)
    msgChannel = str(message.channel)
    goodchannel = 'event-logs'
    goodchannel2 = 'event-logs-checking'
    if msgChannel not in goodchannel:
        pass
    else:
        botAuthor = 'Market Logger#2183'
        msgAuthor = str(message.author)
        if msgAuthor not in botAuthor:
            listofstuff = message.content.split('\n')
            if 'Username:' in listofstuff[0]:
                username = listofstuff[0]
                newUsername = username.split(': ')
                finalUsername = str(newUsername[1])

                if 'Attendees:' in listofstuff[1]:
                    attendees = listofstuff[1]
                    newattendees = attendees.split(': ')
                    finalattendees = str(newattendees[1])
                
                    if 'Type of Event:' in listofstuff[2]:
                        typeofevent = listofstuff[2]
                        newToE = typeofevent.split(': ')
                        finalToE = str(newToE[1])
                    
                        if 'Proof:' in listofstuff[3]:
                            proof = listofstuff[3]
                            newProof = proof.split(': ')
                            finalProof = str(newProof[1])
                            
                            embed = discord.Embed(
                                title = '**:pencil: New Event Log :pencil:**',
                                colour = discord.Colour.blue()
                            )
                            embed.add_field(name = 'Username', value = '{}'.format(finalUsername), inline = 'false')
                            embed.add_field(name = 'Attendees', value = '{}'.format(finalattendees), inline = 'false')
                            embed.add_field(name = 'Type of Event', value = '{}'.format(finalToE), inline = 'false')
                            embed.add_field(name = 'Proof', value = '{}'.format(finalProof), inline = 'false')
                            
                            await postChannel.send(embed=embed)
                            await postChannel.send('<@&663190515323371540> <@&663192507936538664>')
                            await channel.send(':white_check_mark: Your log has been accepted! Wait up to 24 hours for a HoD+ to review your log and allocate points. '+message.author.mention)
                            await message.add_reaction('✅')

                        else:
                            await channel.send(':warning: Your log has been denied due to formatting issues! Read pinned messages. The format is case sensitive! , '+message.author.mention)
                        
                    else:
                        await channel.send(':warning: Your log has been denied due to formatting issues! Read pinned messages. The format is case sensitive! , '+message.author.mention)
                    
                else:
                    await channel.send(':warning: Your log has been denied due to formatting issues! Read pinned messages. The format is case sensitive! , '+message.author.mention)
    
            else:
                await channel.send(':warning: Your log has been denied due to formatting issues! Read pinned messages. The format is case sensitive! , '+message.author.mention)
            
            
        else:
            pass
        
    
client.run(discordToken)
