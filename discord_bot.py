import discord
import time
import asyncio
from discord.ext import commands
from discord.utils import get
from discord import Embed
import random


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='8=D~', intents = intents)


@client.event
async def on_ready():
    print('ready as {0.user}'.format(
        client))




@client.command(aliases=['~'])
async def coom(ctx):
    await ctx.send('coom')


@client.command()
async def test(ctx):
    nick = client.get_user(192453447230947330)
    await ctx.send(f'{nick.mention} awdawdada')

@client.command()
async def tonic(ctx):
    await ctx.send('''Tonic is one of the most used drug in the sport industry. The coompound is mainly extracted from a type of plant called Bustling fungus. The IUPAC name for this compound is lysergic diethylamide. Tonic acts by inhibiting the reuptake of serotonin, norepinephrine, and dopamine. This results in greater concentrations of these three neurotransmitters in the brain. It can easily cross the blood–brain barrier and may lead to the breakdown of the barrier. However this drug is currently banned due to the high chance of cardiac failure after consumption. For example, a man named Kira Yoshikage died from a cardiac disease called “sheer heart attack” after consuming 444 grams of Tonic before the 1999 Morioh break down festival. Not long ago, Doctor Kujo and Doctor Huang from Green dolphin medical facility announced a method to overcome the side effect of the drug. Be in bed by 11 PM, and make sure to get eight hours of sleep, no matter what. have a glass of warm milk and doing about twenty minutes of stretches before going to bed, then you have no problems sleeping until morning. By doing that your heart will have lesser chance of breaking down, therefore you are less likely to get sheer heart attack from Tonic.''')

@client.command(aliases=['sh*o'])
async def shio(ctx):
    await ctx.send('''but i still wanna watch
[1:13 AM]
sounds entertaining
ooooh i wanna watch
dont fuckin project that onto others
[1:33 AM]
that just makes it sound less genuine
[1:34 AM]
i was pressing u cuz i noticed it
[1:34 AM]
just be open with me about that
[1:34 AM]
i will respect ur opinions and wishes if ur honest with me

shio — Today at 9:45 PM
sorry for coming off as aggressive/angry, i just find that lying just doesnt benefit both parties in this situation
[9:46 PM]
just remember that if theres smth thats bothering u about me then just straight up tell me what u think and tell me what i should change/improve''')

@client.command()
async def eren_yeager(ctx):
    await ctx.send('''I've become so much like Eren Jaeger it's scary.\n

I wear black cardigans, verbally assault women, and physically assault my friends.\n

When I look in the mirror, I can't help but say "戦い, 戦い" (which means fight fight in american.)\n

I grew my hair out long because I don't care so now I have to wear it in a bun and I don't care what people think so shut the fuck up Hange.\n

I always leave an open wound on my hand, and go out of my way to show it to everyone so they are reminded that I am in control.\n

When I see dogs being taken on walks I get mad at them for not being free like I am.\n

I can't have sex with my girlfriend anymore without forcing her to dress up as Mikasa or Historia, both of whom remind me of Armin.\n

When I order fast food, I refuse to call them french fries and insist on calling them freedom fries.\n

I just keep moving forward, until my enemies are destroyed.''')

@client.command()
async def lego_city(ctx):
    await ctx.send('''niga lai za lego city chong hiei shi yo shi da zhou hu chou
heEEeeeeEeeY!!!!!
che li shi da cho cho chao li wa bing dong xian sao sao shei
shi da takanamou chian chon dingdong
lai zin da shin
shang shi you chi lego city
niga lai za lego city chong hiei shi yo shi da zhou hu chou
heEEeeeeEeeY!!!!!
che li shi da cho cho chao li wa bing dong xian sao sao shei
shi da takanamou chian chon dingdong
lai zin da shin
shang shi you chi lego city
niga lai za lego city chong hiei shi yo shi da zhou hu chou
heEEeeeeEeeY!!!!!
che li shi da cho cho chao li wa bing dong xian sao sao shei
shi da takanamou chian chon dingdong
lai zin da shin
shang shi you chi lego city
niga lai za lego city chong hiei shi yo shi da zhou hu chou
heEEeeeeEeeY!!!!!
che li shi da cho cho chao li wa bing dong xian sao sao shei
shi da takanamou chian chon dingdong
lai zin da shin
shang shi you chi lego city
niga lai za lego city chong hiei shi yo shi da zhou hu chou
heEEeeeeEeeY!!!!!
che li shi da cho cho chao li wa bing dong xian sao sao shei
shi da takanamou chian chon dingdong
lai zin da shin
shang shi you chi lego city
niga lai za lego city chong hiei shi yo shi da zhou hu chou
heEEeeeeEeeY!!!!!
che li shi da cho cho chao li wa bing dong xian sao sao shei
shi da takanamou chian chon dingdong
lai zin da shin
shang shi you chi lego city
        ''')

@client.command()
async def copypasta(ctx):
    steve = client.get_user(287438025435119618)
    pastas = ['''I try not to but overtime it gets really hard\n
I tried my best not to, trust me\n
And if you were to live in my shoes it naturally comes\n
And by no means do I see myself as something like “the greatest” cause IK for a fact there are so many people who excels in different things\n
But in certain aspects I thrive and tested my theories during my high school years\n
Like you said my life is like an anime character\n
Here are some scenarios\n
1. Grade 9 English teacher was handing out books for the class, two people were the last one to pick from the pile. (Person 1 wanted to pick last cause he wanted to get an old one with notes written inside) (person 2 aka me just didn’t care for completion of rushing in the pile) eventually the teacher saw what 1 was doing and praised him in front of the class. What I did after that was I picked a freshly new book, and then grabbed the notes within all the remaining books and stuck it onto my new one. Became teachers favourite
2. English class, teacher ask us on day 1 to write about who would win, 500 kaynes or 1 500ft Kanye. We were given 30 minutes, only 4 people wrote a page long or more. I wrote 6 pages, 3 scenarios/results. When the teacher got pissy cause everyone was taking he randomly picked from everyone and I was chosen. After reading those 4 people. He apologized to everyone in the class and said “I didn’t realize we have geniuses in this class room”
3. Debate, this debate was about how the human mind is separate vs how they’re the same connected system. The teacher instructed us those who thinks of each two different possibility go on different side of the classroom, where we would make our debate team. I was the only one on the other side, it was the entire class against me. People laughed at first but eventually everyone moved to my side''', '''I’m always giga hard on myself cause I have such high expectations for myself as well as I’m super ambitious. I feel extremely lonely for all my life I’ve been trying to find a girl that would fill this empty feeling. I’ve dated over 300 and yet time after time I still am in the end by myself even though I gave so much effort into each and everyone of them. Some people put me on a pedestal for I just have my ways to people, but I see myself as someone who is incapable of love from others :D. Pain. I’ve fallen down so many times in life, and each time I forced myself back up over and over again. If I wasn’t any stronger or smarter, if I was just a bit more  unlucky at life, honestly. I feel like I wouldn’t be alive at this time.Even though I’m still breathing as of right now, I’m only human. Its really hard for me everyday specially these few months, I’ve hit an all time low. I’m kind of scared that if nothing changes I’ll lose my mind in the future. Um I don’t like that. Maybe I’m over thinking again, it’s 4am. Sorry for bothering you during your studies, and thank you for making me feel better :). Um I think I’m going to just force myself to sleep to ease myself from these negative thoughts. Sweet dreams. Some of them were quite fast cause it wasn’t taken seriously, some of them lasted a few days or a week even though I tried to work things out, but my personality just doesn’t match. Some of them lasted longer but people don’t last past the honey moon phase. If ur asking how umm it’s not like there’s a huge secret that people are missing. It’s just I used to have a habit to hit on everyone I met LOL and I was pretty good at it. I’m the guy that people come to when they need advice in life and relationships.'''
,'''I've made a sevewe and continuous wapse in my judgement and I don't expect to be fowgiven. I'm simpwy hewe to cum. So what we came acwoss that day on the woods was obviouswy unpwanned and the weactions you saw on tape wewe waw, they wewe unfiwtewed. None of us knew how to weact ow how to feew. I shouwd have nevew posted the video. I shouwd have put the camewas down, and stopped wecowding what we wewe going thwough. Thewe's a wot of things I shouwd have done diffewentwy, but I didn't, and fow that fwom the bottom of my heawt, I am sowwy. I want to cum to the intewnet, I want to cum to anyone who's seen the video, I want to cum to anyone who has been affected ow touched by mentaw iwwness, ow depwession, ow suicide. But, most impowtantwy, I want to cum to the victim and his famiwy. Fow, my fans, who awe defending my actions, pwease don't, they do not desewve to be defended. The goaw of my content is awways to entewtain, to push the boundawies, to be aww incwusive and in the wowwd I wive in I shawe awmost evewything I do. The intent is nevew to be heawtwess, cwuew, ow mawicious. Wike I said, I made a huge mistake, I don't expect to be fowgiven, I'm just hewe to cum. I'm ashamed of mysewf. I'm disappointed in mysewf, and I pwomise to be bettew. I wiww be bettew, thank you.'''
, '''I've become so much like Eren Jaeger it's scary.\n

I wear black cardigans, verbally assault women, and physically assault my friends.\n

When I look in the mirror, I can't help but say "戦い, 戦い" (which means fight fight in american.)\n

I grew my hair out long because I don't care so now I have to wear it in a bun and I don't care what people think so shut the fuck up Hange.\n

I always leave an open wound on my hand, and go out of my way to show it to everyone so they are reminded that I am in control.\n

When I see dogs being taken on walks I get mad at them for not being free like I am.\n

I can't have sex with my girlfriend anymore without forcing her to dress up as Mikasa or Historia, both of whom remind me of Armin.\n

When I order fast food, I refuse to call them french fries and insist on calling them freedom fries.\n

I just keep moving forward, until my enemies are destroyed.'''
,'''I'm calling giorno''',
'''Hey, I know you said you wanted to take a break, but my mind was wondering, and it collected stuff as it was doing that, and I wrote something that I really want to share with you.

*puts on a masquerade mask and a posh costume*

words are always quick to betray when one is in love. It can even make one doubt their love because it's unexplainable, and logic tells us that if we cannot explain it, then it does not exit. But yet one feel love. It's there, so real and vivid one could grasp it, put it in their pocket and carry it with them to wherever they may go. Yet this love, this object, cannot be explained by words and thoughts alone. One may meditate upon such a conundrum for their entire life find no explanation, and then check their pocket to find that the love is still as youthful and real as the day it was put there.

*the posh costume starts to fall off, and the mask begins to  to noticeably crack as if it were stone*
''',
'''
what most do not realize is that there is always an explanation for love. However, finding that explanation is the difficult trial that one must go through if they seek it. For some, it is the comfort one feels by simply being near the other, confiding their most secret of interests and ideas. For some, it is a long-lost sense of purpose that one feels, inspired in them by them other.

*the mask cracks and cracks until it finally turns to ash, revealing my face,  the costume has fallen off, revealing my everyday clothing. I am completely vulnerable*

But for me, it is the joy that I give you that makes me fall in love. To see someone as hurt and scared as I am smiling and enjoying the simple pleasure of my company sparks within me joy, happiness, and hope. At times, I admit, it can bring more pressure than happiness, making me believe that I have an obligation to be perfect and a protector, afraid of saying a truth that might hurt you, or discussing or doing something that you might not care for or aren't in the mood for, and thus make you unhappy and I think I'm finally starting to accept that it none of it has to be. I think I'm starting to accept that love doesn't have to be perfect for it to succeed or even just to make you feel good.
And I think that makes me happy.
It at least takes some of pressure off.
I'm sorry if you didn't like this.
I'm not even sure it's a poem
It's too literal
I guess it's a.....meditation, maybe?''',
'''Tonic is one of the most used drug in the sport industry. The coompound is mainly extracted from a type of plant called Bustling fungus. The IUPAC name for this compound is lysergic diethylamide. Tonic acts by inhibiting the reuptake of serotonin, norepinephrine, and dopamine. This results in greater concentrations of these three neurotransmitters in the brain. It can easily cross the blood–brain barrier and may lead to the breakdown of the barrier. However this drug is currently banned due to the high chance of cardiac failure after consumption. For example, a man named Kira Yoshikage died from a cardiac disease called “sheer heart attack” after consuming 444 grams of Tonic before the 1999 Morioh break down festival. Not long ago, Doctor Kujo and Doctor Huang from Green dolphin medical facility announced a method to overcome the side effect of the drug. Be in bed by 11 PM, and make sure to get eight hours of sleep, no matter what. have a glass of warm milk and doing about twenty minutes of stretches before going to bed, then you have no problems sleeping until morning. By doing that your heart will have lesser chance of breaking down, therefore you are less likely to get sheer heart attack from Tonic.'''
,'''niga lai za lego city chong hiei shi yo shi da zhou hu chou
heEEeeeeEeeY!!!!!
che li shi da cho cho chao li wa bing dong xian sao sao shei
shi da takanamou chian chon dingdong
lai zin da shin
shang shi you chi lego city
niga lai za lego city chong hiei shi yo shi da zhou hu chou
heEEeeeeEeeY!!!!!
che li shi da cho cho chao li wa bing dong xian sao sao shei
shi da takanamou chian chon dingdong
lai zin da shin
shang shi you chi lego city
niga lai za lego city chong hiei shi yo shi da zhou hu chou
heEEeeeeEeeY!!!!!
che li shi da cho cho chao li wa bing dong xian sao sao shei
shi da takanamou chian chon dingdong
lai zin da shin
shang shi you chi lego city
niga lai za lego city chong hiei shi yo shi da zhou hu chou
heEEeeeeEeeY!!!!!
che li shi da cho cho chao li wa bing dong xian sao sao shei
shi da takanamou chian chon dingdong
lai zin da shin
shang shi you chi lego city
niga lai za lego city chong hiei shi yo shi da zhou hu chou
heEEeeeeEeeY!!!!!
che li shi da cho cho chao li wa bing dong xian sao sao shei
shi da takanamou chian chon dingdong
lai zin da shin
shang shi you chi lego city
niga lai za lego city chong hiei shi yo shi da zhou hu chou
heEEeeeeEeeY!!!!!
che li shi da cho cho chao li wa bing dong xian sao sao shei
shi da takanamou chian chon dingdong
lai zin da shin
shang shi you chi lego city
''',
f'''I genuinely do not like playing with {steve.mention}'''
,'''but i still wanna watch
[1:13 AM]
sounds entertaining
ooooh i wanna watch
dont fuckin project that onto others
[1:33 AM]
that just makes it sound less genuine
[1:34 AM]
i was pressing u cuz i noticed it
[1:34 AM]
just be open with me about that
[1:34 AM]
i will respect ur opinions and wishes if ur honest with me

shio — Today at 9:45 PM
sorry for coming off as aggressive/angry, i just find that lying just doesnt benefit both parties in this situation
[9:46 PM]
just remember that if theres smth thats bothering u about me then just straight up tell me what u think and tell me what i should change/improve'''
]
    await ctx.send(random.choice(pastas))



@client.command()
async def lifementor(ctx, *, question):
    ethan = client.get_user(296808294872514560)
    responses = [
        'haha what a fucking loser', 'do it', 'no', 'yes', 'decide later',
        'of course not', 'do it pussy', f'{ethan.mention}'
    ]
    await ctx.send(
        f' Question: {question}\n Answer: {random.choice(responses)}')


@client.command(aliases=['ge'])
async def go_eat(ctx, *, pingnum=3):
    izzy = client.get_user(400412073609396237)

    if int(pingnum) >= 11:
        await ctx.send(f"bro what the fuck, don't ping over 10 times")
        return
    for x in range(pingnum):
        await ctx.send(f"{izzy.mention} go eat")


@client.command(aliases=['ethan', 'em'])
async def ethan_moment(ctx, *, pingnum2=10):
    ethan = client.get_user(296808294872514560)
    embed = discord.Embed()
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/581662628720410645/850251844605444106/unknown.png'
    )
    if int(pingnum2) >= 51:
        await ctx.send(
            'pinging him 50 times is the limit bc bot can crash from too many')
        return
    for x in range(pingnum2):
        await ctx.send(embed=embed)
        await ctx.send(f"{ethan.mention}")

@client.command(aliases = ['/v'])
async def vergil(ctx):
    embed = discord.Embed()
    embed.set_image(url='https://cdn.discordapp.com/attachments/849495004455895073/850549159114309652/ff390870b2b9cd855a271222f4afbdc6.jpg')
    await ctx.send(embed=embed)


@client.command(aliases=['steven', 'sd'])
async def steven_destiny(ctx, *, pingnum3=10):
    steven = client.get_user(395658116693229568)
    embed = discord.Embed()
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/849497062970097684/850488327043809340/unknown.png'
    )
    if int(pingnum3) >= 51:
        await ctx.send(
            'pinging him 50 times is the limit bc bot can crash from too many')
        return
    for x in range(pingnum3):
        await ctx.send(embed=embed)
        await ctx.send(f"{steven.mention}")


@client.command(aliases=['p'])
async def purge(ctx, member: discord.Member, *, num3=10):
    channel = client.get_channel(850629819388788737)
    channel2 = client.get_channel(856997069072105482)
    nick = client.get_user(192453447230947330)
    ella = client.get_user(485858637760299008)
    ethan = client.get_user(296808294872514560)
    if ctx.author == ethan:
        await ctx.send('''Steve told me to put a function where if ethan uses the purge command ethan gets kicked''')
        await ctx.author.send('''i made it so that if you specifically use the purge command you get kicked haha''')
        await ctx.author.kick(reason = 'ethan')
    if member == nick and ctx.author != nick and ctx.author != ella:
      await ctx.send('you dare threaten the supreme king?')
      if not ctx.author.voice:
        await ctx.send('not happening')
        return
      member = ctx.author
    #if member == ella and ctx.author != ella and ctx.author != nick:
      #await ctx.send('no one executes ella, get fucked')
      #member = ctx.author


    if not member.voice:
        await ctx.send(
            f"{member.mention} is not connected to a voice channel, execution cannot begin"
        )
        return
    if num3 >= 51:
        await ctx.send(
            'cannot purge for more than 50 times, or else bot will crash, commencing purge 10 times'
        )
        num3 = 10
    embed = discord.Embed()
    embed.set_image(
        url=
        'https://media.tenor.com/images/770915dca7bde73cfc04b2db0712f6b3/tenor.gif'
    )
    await ctx.send(f"terminating {member.mention}")
    await ctx.send(embed=embed)

    line = [
        'Fool, you have been kicked for attempting to escape the purge',
        'haha, weakling, you cannot escape the purge, get kicked',
        'there is no escape from the purge',
        'https://www.youtube.com/watch?v=6XvYiBhG2NA'
    ]

    for x in range(num3):
        await asyncio.sleep(1)
        #if not member.voice:
        #await ctx.send(f"{member.mention} tried to escape purgatory, commencing execution")
        #await member.kick(reason='escaping purge')
        try:
            await member.edit(voice_channel=channel)
        except:
            await ctx.send(
                f"{member.mention} tried to escape purgatory, commencing execution"
            )
            try:
              await member.send(f'{random.choice(line)} \n https://discord.gg/zqZgmkaYnr')
            except:
              pass
            await member.kick(reason='escaping purge')
            return
        await asyncio.sleep(1)
        #if not member.voice:
        #await ctx.send(f"{member.mention} tried to escape purgatory, commencing execution")
        #await member.kick(reason='escaping purge')
        try:
            await member.edit(voice_channel=channel2)
        except:
            await ctx.send(
                f"{member.mention} tried to escape purgatory, commencing execution"
            )
            try:
              await member.send(f'{random.choice(line)} \n https://discord.gg/zqZgmkaYnr')
            except:
              pass
            await member.kick(reason='escaping purge')
            return
    await ctx.send(f"{member.mention}'s purge has been completed")

@client.command(aliases=['infinite_tsukuyomi','inf_p'])
async def infinite_purge(ctx, member: discord.Member):
    channel = client.get_channel(850629819388788737)
    channel2 = client.get_channel(856997069072105482)
    nick = client.get_user(192453447230947330)
    ella = client.get_user(485858637760299008)
    if member == nick and ctx.author != nick and ctx.author != ella:
      await ctx.send('you wanna kick the king?')
      if not ctx.author.voice:
        await ctx.send('not happening')
        await ctx.author.kick(reason='using infinite tsukuyomi on nick')
        return
      member = ctx.author
    #if member == ella and ctx.author != ella and ctx.author != nick:
      #await ctx.send('no one executes ella, get fucked')
      #member = ctx.author


    if not member.voice:
        await ctx.send(
            f"user is not connected to a voice channel, {member.mention} get executed anyways"
        )
        try:
            await member.send('you have been targeted by the infinite tsukuyomi \nhttps://discord.gg/zqZgmkaYnr'
                )
        except:
            pass
        await member.kick(reason = 'infinite_tsukuyomi but no in vc')
        return
    await ctx.send(f"{member.mention} will now be executed")

    line = [
        'get fucked',
        'death comes to all',
        'https://www.youtube.com/watch?v=6XvYiBhG2NA'
    ]


    death_counter = 0
    while death_counter ==0:
        await asyncio.sleep(1)
        #if not member.voice:
        #await ctx.send(f"{member.mention} tried to escape purgatory, commencing execution")
        #await member.kick(reason='escaping purge')
        try:
            await member.edit(voice_channel=channel)
        except:
            await ctx.send(
                f"{member.mention} is officially pronounced dead"
            )
            try:
              await member.send(f'{random.choice(line)} \n https://discord.gg/zqZgmkaYnr')
            except:
              pass
            await member.kick(reason='infinite_tsukuyomi-ed')
            death_counter += 1
            return
        await asyncio.sleep(1)
        #if not member.voice:
        #await ctx.send(f"{member.mention} tried to escape purgatory, commencing execution")
        #await member.kick(reason='escaping purge')
        try:
            await member.edit(voice_channel=channel2)
        except:
            await ctx.send(
                f"{member.mention} is officially pronounced dead"
            )
            try:
              await member.send(f'{random.choice(line)} \n https://discord.gg/zqZgmkaYnr')
            except:
              pass
            await member.kick(reason='infinite_tsukuyomi-ed')
            death_counter += 1
            return


@client.command()
async def pfp(ctx,*,member: discord.ext.commands.MemberConverter):
    yas = client.get_user(519387321146015754)
    if member == yas:
        embed= discord.Embed()
        embed.set_image(url='https://cdn.discordapp.com/attachments/581662628720410645/852700647030652948/pfpfried.png')
        await ctx.send(embed=embed)
        return
    profile_picture = member.avatar_url
    embed=discord.Embed()
    embed.set_image(url=profile_picture)
    await ctx.send(embed=embed)

snipe_message_content = None
snipe_message_author = None
snipe_message_id = None
snipe_message = None

@client.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_id
    global snipe_message

    snipe_message = message
    snipe_message_content = message.content
    snipe_message_author = message.author.id
    snipe_message_id = message.id
    await asyncio.sleep(300)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None
        sninpe_message = None

@client.command(aliases = ['btd'])
async def bites_the_dust(ctx):
    if snipe_message_content==None:
        await ctx.channel.send("There has been no deleted messages in the last 5 minutes (or since when doombot last went online)")
    else:
        guy = client.get_user(snipe_message_author)
        try:
            attach=snipe_message.attachments[0].url
            await ctx.channel.send(attach)
            await ctx.channel.send(f'{guy.mention} sent the attachment above and deleted it like a pussy')
        except:
            await ctx.channel.send(f'{guy.mention} said "{snipe_message_content}" and deleted it like a pussy')


client.run('***********************************' )
