import discord
from datetime import datetime


def data_load(result):
    data = ""
    if result['data'] != '':
        for i in result['data']:
            detail = "\n[{}]({})\n-{}\n".format(i['name'], i['href'], i['modder'])
            data = data + detail
        data = "\n请注意NSFW已开启，查询结果共{}条，此处最大显示5条，其余请点击上方搜索结果\n".format(result["count"].split('Result')[0]) + data

        embed = discord.Embed(title="对{}的搜索结果：\n\n".format(result["search_content"]),
                              colour=discord.Colour(0x2d0095), url=result['url'],
                              description=data,
                              timestamp=datetime.utcnow())
    else:
        embed = discord.Embed(title="未查到与{}有关的内容".format(result["search_content"]),
                              colour=discord.Colour(0x2d0095),
                              timestamp=datetime.utcnow())

    embed.set_author(name="查询结果 | FFXIV Mod Archive", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
    embed.set_footer(text="FFXIV Mod 查询")
    return embed
