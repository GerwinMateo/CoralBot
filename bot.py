import discord
import discord.ext
import responses
import openai
import spotify

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    # Discord
    TOKEN = "Blank"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # Spotify API
    client_id = "Blank"
    client_secret = "Blank"

    # CHATGPT API
    openai.api_key = "Blank"
    openai.organization = "Blank"


    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user or message.author.bot:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[:9].lower() == "j!spotify":
            if len(user_message) == 9:
                response = "Please enter a genre/word next time"
                await message.channel.send(response)
            else:
                options = "track"
                if user_message.split(" ")[-1].lower() == 'album' or user_message.split(" ")[-1].lower() == "albums":
                    options = 'album'

                search_query = user_message[9:]
                access_token = spotify.get_spotify_access_token(client_id, client_secret)
                response = spotify.search_songs(access_token, search_query, options)

                # Extract and print Spotify URIs and names of the first 10 songs found
                result = spotify.spotifyOptions(response, options)

                await message.channel.send(result)

        else:
            if user_message[0] == '~':
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=True)
            else:
                await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

"""
  if user_message == "j!ChatGPT":

               response = openai.ChatCompletion.create(
                   model="gpt-3.5-turbo",
                   messages = [
                       {"role": "system", "content": "Say this a test"},
                       {"role": "user", "content": message.content},
                   ],
               )

               # Extract the generated reply from ChatGPT
               reply = response.choices[0].message.content

               # Send the reply back to the Discord channel
               await message.channel.send(reply)
"""





