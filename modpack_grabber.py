import requests as req
import json

offset = 0
modpacks = []
while True:
    resp = req.get(
        "https://api.modrinth.com/v2/search?"
        "limit=100&"
        "index=downloads&"
        "facets=[[%22project_type:modpack%22]]&"
        f"offset={offset}",
        headers={
            'User-Agent': 'DefiantBurger/SearchModpacksByMod/1.0 (joseph.cicalese@gmail.com)'
        }
    ).json()
    modpacks += resp["hits"]
    offset += 100
    if len(resp["hits"]) < 100:
        break

with open("modpacks.json", "w") as fp:
    json.dump(modpacks, fp, indent=2)