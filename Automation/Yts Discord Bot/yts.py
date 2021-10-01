import requests, discord
from discord.ext import commands

client = commands.Bot(command_prefix='$')

async def machine(search_mov):
    raw_query = requests.get(f'https://yts.mx/api/v2/list_movies.json?query_term={search_mov}').json()
    finalResult = ""
    setStatus = ""
    # print(f"{raw_query['data']['movie_count']} Results Found!!!")
    finalResult += f"**{raw_query['data']['movie_count']} Result(s) Found!!!**\n\n"

    if raw_query['data']['movie_count']!=0:
        setStatus += raw_query['data']['movies'][0]['title_english']
        for movie in raw_query['data']['movies']:
            # print(f"Name: {movie['title_long']}")
            finalResult += f"**Name:** {movie['title_long']}\n"
            # print('Genres: ', end='')
            finalResult += '**Genres:** '
            for genre in movie['genres']:
                # print(f'{genre}\t')
                finalResult += f'{genre}\t'
            # print(f"\n\nSummary: {movie['summary']}")
            finalResult += f"\n**Summary:** {movie['summary']}\n"
            for torrent in movie['torrents']:
                # print(f"{torrent['quality']} {torrent['type']} {torrent['size']}")
                finalResult += f"**Quality | Size:** {torrent['quality']} {torrent['type']} | {torrent['size']}\n"
                # print(f"Magnet URL: magnet:?xt=urn:btih:{torrent['hash']}&dn={movie['title_long']} {torrent['quality']} {torrent['type']}&tr=udp://open.demonii.com:1337/announce&tr=udp://tracker.openbittorrent.com:80&tr=udp://tracker.coppersurfer.tk:6969&tr=udp://glotorrents.pw:6969/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://torrent.gresille.org:80/announce&tr=udp://p4p.arenabg.com:1337&tr=udp://tracker.leechers-paradise.org:6969")
                finalResult += f"**Magnet URL:** magnet:?xt=urn:btih:{torrent['hash']}&dn={movie['title_long']} {torrent['quality']} {torrent['type']}&tr=udp://open.demonii.com:1337/announce&tr=udp://tracker.openbittorrent.com:80&tr=udp://tracker.coppersurfer.tk:6969&tr=udp://glotorrents.pw:6969/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://torrent.gresille.org:80/announce&tr=udp://p4p.arenabg.com:1337&tr=udp://tracker.leechers-paradise.org:6969\n\n"
            finalResult += '-'*100 + '\n\n'
    return (finalResult, setStatus)

@client.event
async def on_ready():
    print("Bot Ready!")

@client.command()
async def search(ctx, mov1="",  mov2="", mov3="", mov4="", mov5="", mov6="", mov7="", mov8="", mov9="", mov10=""):
    search_mov = mov1 + " " + mov2 + " " + mov3 + " " + mov4 + " " + mov5 + " " + mov6 + " " + mov7 + " " + mov8 + " " + mov9 + " " + mov10
    if mov1 == "":
        await ctx.send(f"Please Enter **Movie** Name, like: `/search The Vault`")
    else:
        (finalResult, setStatus) = await machine(search_mov)
        await watching(ctx, setStatus)
        if len(finalResult)>2000:
            chunk=0
            while True:
                try:
                    await ctx.send(f"{finalResult[chunk:2000+chunk]}")
                    chunk += 2000
                except discord.errors.HTTPException:
                    pass
                except:
                    await ctx.send(f'{finalResult[chunk:]}')
                    break
        else:
            await ctx.send(f"{finalResult}")

@client.command()
async def ping(ctx):
    latency = str(int(client.latency * 1000))
    await ctx.send(f'Pong :)\t{latency}ms')

@client.command()
async def watching(ctx, setStatus):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=setStatus.upper()))

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)

client.run("Your Token Here")