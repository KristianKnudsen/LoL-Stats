class Summoner:
    def __init__(self, id, account_id, puuid, name, profile_icon_id, revision_date, summoner_level):
        self.summoner_level = summoner_level
        self.revision_date = revision_date
        self.puuid = puuid
        self.profile_icon_id = profile_icon_id
        self.name = name
        self.id = id
        self.account_id = account_id
