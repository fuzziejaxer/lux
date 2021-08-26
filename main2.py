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

@client.command(aliases=['cl','delete'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount+1)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No Reason Provided"):
    await ctx.send(member.name + " was kicked from " + ctx.guild.name)
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No Reason Provided"):
    await ctx.send(member.name + " was banned from " + ctx.guild.name)
    await member.ban(reason=reason)

@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")

client.run("")
