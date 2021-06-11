import requests
import mojang
import json
import time

key = '4f3fbe05-9332-4a67-8519-a6bee63acc34'


async def isonline(key, username: str):
    username = username
    uuid = mojang.MojangAPI.get_uuid(username)
    if not uuid:
        invalid = ['Invalid Username']
        return invalid
    else:
        skin = 'https://crafatar.com/renders/body/' + str(uuid) + '.png'
        data = requests.get(
            url="https://api.hypixel.net/status",
            params={
                "key": key,
                "uuid": uuid
            }
        ).json()
        playerdata = [username, skin]
        if data['session']['online']:
            playerdata.append("Online")
            playerdata.append("None")
            playerdata.append("None")
            playerdata.append("None")
            if 'gameType' in data['session']: playerdata[3] = data['session']['gameType']
            if 'map' in data['session']: playerdata[4] = data['session']['map']
            if 'mode' in data['session']: playerdata[5] = data['session']['mode']
            return playerdata
        else:
            playerdata.append("Offline")
            return playerdata


async def bwstats(key, username: str):
    username = username.capitalize()
    uuid = mojang.MojangAPI.get_uuid(username)
    if not uuid:
        invalid = ['Invalid Username']
        return invalid
    else:
        skin = 'https://crafatar.com/renders/body/' + str(uuid) + '.png'
        data = requests.get(
            url="https://api.hypixel.net/player",
            params={
                "key": key,
                "uuid": uuid
            }
        ).json()
        bedslost = data["player"]["stats"]["Bedwars"]["beds_lost_bedwars"]
        bedsbroken = data["player"]["stats"]["Bedwars"]["beds_broken_bedwars"]
        finalkills = data["player"]["stats"]["Bedwars"]["final_kills_bedwars"]
        finaldeaths = data["player"]["stats"]["Bedwars"]["final_deaths_bedwars"]
        wins = data["player"]["stats"]["Bedwars"]["wins_bedwars"]
        lose = data["player"]["stats"]["Bedwars"]["losses_bedwars"]

        gamesplayed = data["player"]["stats"]["Bedwars"]["games_played_bedwars"]
        fkdratio = round((int(finalkills) / int(finaldeaths)), 2)
        bblratio = round((int(bedsbroken) / int(bedslost)), 2)
        winstreak = str(data["player"]["stats"]["Bedwars"]["winstreak"])
        winloseratio = round((int(wins) / int(lose)), 2)
        lvl = str(data["player"]["achievements"]["bedwars_level"])

        # send post request
        url = 'https://api.bannerbear.com/v2/images'
        obj = json.dumps({
            "template": "8BK3vWZJEPJbJzk1aX",
            "modifications": [
                {
                    "name": "username",
                    "text": username
                },
                {
                    "name": "avatar",
                    "image_url": skin
                },
                {
                    "name": "level",
                    "text": lvl
                },
                {
                    "name": "wstreak",
                    "text": winstreak
                },
                {
                    "name": "wlratio",
                    "text": winloseratio
                },
                {
                    "name": "fkdratio",
                    "text": fkdratio
                },
                {
                    "name": "bedblratio",
                    "text": bblratio
                },
                {
                    "name": "gplayed",
                    "text": gamesplayed
                }
            ]
        })

        x = requests.post(url, data=obj, headers=
        {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer uQxTQfktDcGvBjgr04vygQtt'
        }).json()
        if x['message'] == 'Upgrade required: This account has reached its Image API quota':
            errormsg = ['402', username.capitalize(), skin, gamesplayed, fkdratio, bblratio, winstreak, winloseratio,
                        lvl]
            return errormsg
        elif x.status_code == 202 or x.status_code == 200:
            time.sleep(15)
            x = x.json()
            # get the image
            urll = 'https://api.bannerbear.com/v2/images/' + x['uid']
            image = requests.get(urll, headers=
            {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer uQxTQfktDcGvBjgr04vygQtt'
            }).json()

            return image['image_url_png']
