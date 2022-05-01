import json
import requests
import base64
import json

def get_users(api_key : str, guild: str, role : str) -> list:
    headers = {"Authorization" : "Bot " + api_key}
    url = "https://discord.com/api/v9/guilds/" + guild + "/members?limit=1000"
    print("fetching users...")
    try:
        r = requests.get(url, headers=headers)
    except:
        return ["fail"]
    members = json.loads(r.text)
    usernames = " ,".join([user["user"]["username"] for user in members if role in user["roles"]])
    print("found members: ", usernames, "\n")
    return [{
        "username" : user["user"]["username"], 
        "roles" : user["roles"], 
        "avatar" : user["user"]["avatar"],
        "id" : user["user"]["id"]} 
    for user in members if role in user["roles"]]

def get_avatar_bytes(user : dict):
    userId = user["id"]
    avatarId = user["avatar"]
    url = "https://cdn.discordapp.com/avatars/" + userId + "/" + avatarId 
    try:
        r = requests.get(url, stream=True)
    except:
        return ["fail"]
    avatar = r.content
    print("successfully fetched avatar for " + user["username"])
    return avatar
    #with open('avatars/' + userId + '.jpg', 'wb') as handler:
    #    handler.write(avatar)

def upload_server_emoji(name : str, guildId : str, user: dict, image : bytes, api_key : str):
    string_img = "data:image/png;base64," + base64.b64encode(image).decode("utf8")
    headers = {"Authorization" : "Bot " + api_key}
    emoji_data = {
        "name" : name, 
        "image" : string_img,
        "roles" : ["559139679388172304"]
    }
    url = "https://discord.com/api/v9/guilds/" + guildId + "/emojis"
    r = requests.post(url=url, json=emoji_data, headers=headers)
    print(r.status_code, r.text)

def upload_server_emoji_raw(emoji_data: dict, guildId : str, api_key : str):
    headers = {"Authorization" : "Bot " + api_key}
    url = "https://discord.com/api/v9/guilds/" + guildId + "/emojis"
    r = requests.post(url=url, json=emoji_data, headers=headers)
    print(r.status_code, r.text)

def delete_server_emoji(name : str, guildId : str, api_key : str):
    headers = {"Authorization" : "Bot " + api_key}
    #get emoji ID for user emoji
    url = "https://discord.com/api/v9/guilds/" + guildId + "/emojis"
    r = requests.get(url=url, headers=headers)
    emojiId = None
    for emoji in json.loads(r.text):
        if emoji["name"] == name: emojiId = emoji["id"]
    if not emojiId: return "emoji not found"
    print("deleting previous emoji...", emojiId)
    url = "https://discord.com/api/v9/guilds/" + guildId + "/emojis/" + emojiId
    r = requests.delete(url=url, headers=headers)
    print(r.status_code, r.text)
    return r.text 

def delete_user_emoji(guildId : str, user: dict, api_key : str):
    headers = {"Authorization" : "Bot " + api_key}
    emojiId = _get_user_emoji_id(guildId, user, api_key)
    if not emojiId: 
        return "user emoji did not exist for " + user["username"]
    url = "https://discord.com/api/v9/guilds/" + guildId + "/emojis/" + emojiId
    r = requests.delete(url=url, headers=headers)
    return r.text


def _get_user_emoji_id(guildId : str, user: dict, api_key : str):
    #get emoji ID for user emoji
    headers = {"Authorization" : "Bot " + api_key}
    url = "https://discord.com/api/v9/guilds/" + guildId + "/emojis"
    r = requests.get(url=url, headers=headers)
    for emoji in json.loads(r.text):
        if emoji["name"] == user["username"]: return emoji["id"]

def upload (guild, api_key):
  role = "966891817138290699"
  users = get_users(api_key, guild, role)
  for user in users:
        avatar = get_avatar_bytes(user)
        name = user["username"].replace(" ", "")
        print(delete_user_emoji(guildId=guild, user=user, api_key=api_key))
        upload_server_emoji(name=name, guildId=guild, user=user, image=avatar, api_key=api_key)


  

        