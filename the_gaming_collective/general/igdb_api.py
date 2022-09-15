from igdb.wrapper import IGDBWrapper

wrapper = IGDBWrapper("bggfunr5gravmwck6xc6ftijd9f1sk", "1lq9cqswbvl6wiwqmbi8o4jtnpefd7")

class igdb_api:
    @classmethod
    def api_call(cls):
        byte_array = wrapper.api_request(
            'games',
            'fields id, name; where id = 740;'
        )
        return byte_array

    @classmethod
    def api_get_image_id(cls):
        byte_array = wrapper.api_request(
            'games',
            'fields cover.image_id; where id = 740;'
        )
        return byte_array