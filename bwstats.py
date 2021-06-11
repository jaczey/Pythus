import requests
import mojang
import json
import time

key = '4f3fbe05-9332-4a67-8519-a6bee63acc34'
username = "Synfae"
uuid = mojang.MojangAPI.get_uuid(username)
if not uuid:
    print("invalid")
else:
    skin = 'https://crafatar.com/renders/body/' + str(uuid) + '.png'
    data = requests.get(
        url="https://api.hypixel.net/player",
        params={
            "key": key,
            "uuid": uuid
        }
    ).json()
    playerdata = [username, skin]

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
    print(x)
    time.sleep(15)
    image = requests.get('https://api.bannerbear.com/v2/images/MRj52Zwoa6xqZan2QxWkdO3eE', headers=
    {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer uQxTQfktDcGvBjgr04vygQtt'
    }).json()
    print(image)
    print(image['image_url_png'])
