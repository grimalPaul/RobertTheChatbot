import discord

code_reponse = ['🇦', '🇧', '🇨', '🇩']

def phase2_embed(choice):
    embed = discord.Embed(colour=discord.Colour(0x0000ff))
    for i in range(len(choice)):
        embed.add_field(name=code_reponse[i],
                        value=choice[i][0],
                        inline=False
                        )
    return embed