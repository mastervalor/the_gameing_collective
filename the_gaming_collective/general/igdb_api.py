from igdb.wrapper import IGDBWrapper

wrapper = IGDBWrapper("bggfunr5gravmwck6xc6ftijd9f1sk", "1lq9cqswbvl6wiwqmbi8o4jtnpefd7")

class igdb_api:
    @classmethod
    def api_get_upcoming_games(cls, data):
        byte_array = wrapper.api_request(
            'games',
            f'fields id, name, cover.image_id; limit 25; where release_dates.date > {data} & (platforms = {167, 169}); sort date asc;'
        )
        return byte_array

    @classmethod
    def api_get_game_pass_games(cls):
        byte_array = wrapper.api_request(
            'games',
            'fields name, release_dates.human, release_dates.region, cover.image_id; limit 25; sort name asc; where external_games.category = 54;'
        )
        return byte_array

    @classmethod
    def api_get_games_by_genre(cls, data):
        byte_array = wrapper.api_request(
            'games',
            f'fields name, cover.image_id; limit 25; sort name asc; where genres = {data} & (platforms = {167, 169});'
        )
        return byte_array