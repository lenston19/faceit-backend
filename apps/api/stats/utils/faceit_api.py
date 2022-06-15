import requests


class FaceitAPI:
    def __init__(self, pname, game_id) -> None:
        self.pname = pname
        self._player_id = None
        self.game_id = game_id
        self.api_header = {
            "Authorization": "Bearer 882ab0ea-ff0c-4f70-99f1-215836754927",
            "content-type": "application/json",
        }

    @property
    def player_id(self):
        try:
            player_id_request = requests.get(
                f"https://open.faceit.com/data/v4/players?nickname={self.pname}&game={self.game_id}",
                headers=self.api_header,
            )
            player_id_data = player_id_request.json()
            player_id = player_id_data["player_id"]
            return player_id
        except KeyError:
            print("Error Occured", self.pname, "doesnt exist")
            return None

    @player_id.setter
    def player_id(self) -> None:
        self._player_id = self.player_id

    def player_information(self) -> dict:
        try:
            if self.player_id is None:
                raise Exception("Player does not exist")
            player_data = requests.get(
                f"https://open.faceit.com/data/v4/players/{self.player_id}",
                headers=self.api_header,
            )
            player_data_json = player_data.json()
            return player_data_json
        except Exception:
            return None

    def player_stats(self) -> dict:
        try:
            player_stats_request = requests.get(
                f"https://open.faceit.com/data/v4/players/{self.player_id}/stats/{self.game_id}",
                headers=self.api_header,
            )
            player_stats_json = player_stats_request.json()
            return player_stats_json
        except Exception:
            return None

    def player_stats_map(self, pmap) -> dict:
        if "_" not in pmap:
            pmap = "de_" + pmap

        try:
            pdata = self.player_stats()
            map_data = pdata["segments"]
            for map in map_data:
                if map["label"] == pmap:
                    return map

        except Exception:
            return None
