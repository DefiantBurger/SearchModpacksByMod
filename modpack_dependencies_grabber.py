import json
import time

import requests as req

with open("modpacks.json", "r") as fp:
    modpacks = json.load(fp)

modpack_dependencies = {}
modpack_count = len(modpacks)
for im, modpack in enumerate(modpacks):
    start = time.time()

    resp = req.get(
        f"https://api.modrinth.com/v2/project/{modpack['project_id']}/dependencies",
        headers={
            'User-Agent': 'DefiantBurger/SearchModpacksByMod/1.0 (joseph.cicalese@gmail.com)'
        }
    ).json()
    modpack_dependencies[modpack['slug']] = resp["projects"]
    print(f"Grabbed {im + 1}/{modpack_count} : {modpack['slug']}...")

    end = time.time()
    wait_time_needed = 0.25 - (end - start)
    if wait_time_needed > 0:
        time.sleep(wait_time_needed)

with open("modpack_dependencies.json", "w") as fp:
    json.dump(modpack_dependencies, fp, indent=2)