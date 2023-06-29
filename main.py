import requests as req

req.get(
    "https://api.modrinth.com/v2/search?"
    "limit=100&"
    "index=downloads&"
    "facets=[[%22project_type:modpack%22]]&"
    "offset=100",
    headers={
        'User-Agent': 'DefiantBurger/SearchModpacksByMod/'
    }
)
