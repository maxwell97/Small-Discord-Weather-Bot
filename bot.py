// Andrei-Radu Manea Copyright 2021
import discord
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.bot == True: # checking if the message is sent from a bot
        return
        
    # !weather <cityName>
    if message.content.startswith("!weather"):
        cityName = message.content.replace("!weather ", "")

        # requesting data from the API
        request = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&appid=1095ec19ff71a7563157bd7c71fd7174&units=metric")
        responseContent = json.loads(request.content)

        # retrieving embedded message icon from API
        weatherIcon = str(responseContent['weather'][0]['icon'])
        weatherIconUrl = "http://openweathermap.org/img/wn/"+weatherIcon+"@2x.png"

        # saving weather data
        weather = responseContent['weather'][0]['description']
        temperature = responseContent['main']['temp']
        feelsLike = responseContent['main']['feels_like']
        cityName = responseContent['name']

        # building embedded message and assigning the data
        embedMessage = discord.Embed(title="Weather", color=0xFF0000)
        embedMessage.set_thumbnail(url=weatherIconUrl)
        embedMessage.add_field(name="City Name ", value=cityName, inline=False)
        embedMessage.add_field(name="Weather", value=weather, inline=True)
        embedMessage.add_field(name="Temperature", value=temperature, inline=True)
        embedMessage.add_field(name="Feels Like", value=feelsLike, inline=True)
        
        await message.channel.send(embed=embedMessage)


        

client.run('OTE2ODIyNDEyMDY1MTQwODA3.YavvaA.GI-Ty7ig6aL2fxB5y0LWAlzoOTM')   
