from igdb.wrapper import IGDBWrapper

wrapper = IGDBWrapper("bggfunr5gravmwck6xc6ftijd9f1sk", "1lq9cqswbvl6wiwqmbi8o4jtnpefd7")

class igdb_api:
    @classmethod
    def api_get_upcoming_games(cls, data):
        byte_array = wrapper.api_request(
            'games',
            f'fields id, name, cover.image_id; limit 25; where release_dates.date > {data} & platforms = {167, 169} & cover.image_id != null; sort release_dates.date asc;'
        )
        return byte_array

    @classmethod
    def api_get_game_pass_games(cls):
        byte_array = wrapper.api_request(
            'games',
            'fields name, release_dates.human, release_dates.region, cover.image_id; limit 25; sort release_dates.date asc; where external_games.category = 54;'
        )
        return byte_array

    @classmethod
    def api_get_games_by_genre(cls, data, time):
        byte_array = wrapper.api_request(
            'games',
            f'fields name, cover.image_id; limit 25; where genres = {data} & platforms = {167, 169} & release_dates.date < {time} & cover.image_id != null; sort release_dates.date desc;'
        )
        return byte_array

    @classmethod
    def api_get_games_by_platform(cls, data, time):
        byte_array = wrapper.api_request(
            'games',
            f'fields name, cover.image_id; limit 25; where platforms = {data} & release_dates.date < {time} & cover.image_id != null; sort release_dates.date desc;'
        )
        return byte_array

    @classmethod
    def api_get_one_game(cls, data):
        byte_array = wrapper.api_request(
            'games',
            f'fields name, cover.image_id, genres.name, involved_companies.company.name, platforms.name, summary, game_modes.name; where id = {data};'
        )
        return byte_array