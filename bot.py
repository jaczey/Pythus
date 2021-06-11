import discord
import discord.ext.commands
from discord.ext.commands import Bot
import test

Client = Bot('pyth$')
commands = discord.ext.commands


@Client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('If yall could just subscribe to **Technoblade**: https://www.youtube.com/c/technoblade'
                               '`\nFree Minecraft accounts, Hypixel ranks and lunar/badlion cosmetics '
                               '\n-->https://rollrewards.com')
        break


@Client.event
async def on_message(message):
    if message.author == Client.user:
        return
    if "technoblade" in message.content.lower():
        await message.channel.send("https://www.youtube.com/c/technoblade")
    await Client.process_commands(message)


@Client.command(name="purge", help="Clear Messages")
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    await ctx.send(f"Cleared by {ctx.message.author.name}")
    await ctx.channel.purge(limit=int(amount))

@Client.command(name='bw', help="Get User's bedwars stats")
async def bedwars(ctx, username: str):
    await ctx.send("Working...", delete_after= 5)
    value = await test.bwstats(test.key, username)
    print('hi')
    if value[0] == 'Invalid Username':
        await ctx.send(':negative_squared_cross_mark: Invalid Username : `' + username.capitalize() + '`')
        return
    print("helo")
    if value[0] == "402":
        print('hiii')
        embed = discord.Embed(
            title=value[1].capitalize(),
            color=discord.Color.blue(),
        )
        embed.set_image(url=value[2])
        embed.add_field(
            name="Username",
            value=value[1]
        )
        embed.add_field(
            name="Games Played",
            value=value[3]
        )
        embed.add_field(
            name="Final K/D Ratio",
            value=value[4]
        )
        embed.add_field(
            name="Bed Broken/Lose Ratio",
            value=value[5]
        )
        embed.add_field(
            name="Winstreak",
            value=value[6]
        )
        embed.add_field(
            name="Win/Lose Ratio",
            value=value[7]
        )
        embed.add_field(
            name="Level",
            value=value[8]
        )
        await ctx.send("Bot has reached its Image API quota", delete_after=2)
        await ctx.send("Valid username, getting stats", delete_after=5)
        await ctx.send(embed=embed)
        await ctx.send("**Please donate so i can keep this bot running"
                   "\n Paypal = https://paypal.me/danielsynf"
                   "\n Bitcoin = `32bC3pD4mgXZriGoLFbtE3KNQZj6GjXrtj`**")
        return
    await ctx.send("Valid username, getting stats", delete_after= 5)
    e = discord.Embed()
    e.set_image(url=value)
    await ctx.send(embed=e)
    await ctx.send("Please donate so i can keep this bot running"
                   "\n Paypal = https://paypal.me/danielsynf"
                   "\n Bitcoin = 32bC3pD4mgXZriGoLFbtE3KNQZj6GjXrtj")
    return

@Client.command(name='online', help="Check if player is online")
async def online(ctx, username: str):
    value = await test.isonline(test.key, username)
    if value[0] == 'Invalid Username':
        await ctx.send(':negative_squared_cross_mark: Invalid Username : `' + username.capitalize() + '`')
        return
    embed = discord.Embed(
        title=value[0].capitalize(),
        color=discord.Color.blue(),
    )
    embed.set_image(url=value[1])
    if value[2] == "Offline":
        embed.add_field(
            name="Status",
            value=value[2]
        )
        await ctx.send(embed=embed)
        return
    else:
        embed.add_field(
            name="Status",
            value=value[2]
        )
        embed.add_field(
            name="Game Type",
            value=value[3]
        )
        embed.add_field(
            name="Map",
            value=value[4]
        )
        embed.add_field(
            name="Mode",
            value=value[5]
        )
        await ctx.send(embed=embed)
        await ctx.send("Please donate so i can keep this bot running"
                       "/n Paypal = https://paypal.me/danielsynf"
                       "/n Bitcoin = 32bC3pD4mgXZriGoLFbtE3KNQZj6GjXrtj")
        return


# Errors
@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(":negative_squared_cross_mark: You can't use that command.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":negative_squared_cross_mark: **Missing required argument(s).** `!purge <amount>`")

@bedwars.error
async def online_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":negative_squared_cross_mark: **Missing required argument(s).** `!bw <username>`")
@online.error
async def online_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":negative_squared_cross_mark: **Missing required argument(s).** `!online <username>`")


Client.run("ODUwMjIxNjU4MjYxNTUzMTY0.YLmknw.WjtTjaeJXR3XCTaw9ghvu5xNwkU")
