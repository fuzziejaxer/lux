import discord
import json
from discord.ext import commands

client = commands.Bot(command_prefix="~", case_insensitive=True)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Watching Member Joins"))
    print(f"{client.user.name} is ready.")

@client.command(aliases=['hello'])
async def hi(ctx):
    await ctx.send("haiiiiiiii")



@client.event
async def on_member_join(member):
    embed = discord.Embed(
        title="Thank you for joining!",
        color=discord.Colour.purple()
    )
    embed.set_image(url="https://media.giphy.com/media/3HJDD34eUL1uwWWQkF/giphy.gif")
    embed.add_field(name="welcome", value=f"Welcome {member.mention}")
    embed.add_field(name="rules", value="Make sure you read <#864613407894536212>")
    embed.add_field(name="roles", value=f"Get em roles! <#865052846830518272>")

    await client.get_channel(864611657819619330).send(embed=embed)

@client.command()
async def test_join(ctx, member):
    member = ctx.author
    emb = discord.Embed(
        title="Thank you for joining!",
        color=discord.Colour.purple()
    )
    emb.set_image(url="https://media.giphy.com/media/3HJDD34eUL1uwWWQkF/giphy.gif")
    emb.add_field(name="welcome", value=f"Welcome {member.mention}")
    emb.add_field(name="rules", value="Make sure you read <#864613407894536212>")
    emb.add_field(name="roles", value=f"Get em roles! <#865052846830518272>")

    await client.get_channel(864611657819619330).send(embed=emb)



client.run("ODcxMDU5MzgxMDc5Mzk2Mzky.YQVzQw.FMBZ0C655pyQHVWAEkmpX4IIzGs")