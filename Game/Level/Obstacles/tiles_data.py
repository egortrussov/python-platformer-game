
class Tile_data:
    def __init__(self, tile_type, sprite, is_animated, max_animation_frames = 0):
        self.type = tile_type 
        self.sprite = sprite  
        self.is_animated = is_animated 
        self.max_animation_frames = max_animation_frames


tiles_data = {
    'grass': Tile_data('decoration', 'sprites/decoration/grass_1.png', True, 2),
    'dirt_stalagmites': Tile_data('decoration', 'sprites/decoration/dirt_stalagmite.png', False, 0),
    'dirt_block': Tile_data('solid', 'sprites/tiles/dirt.png', False, 0),
    'grass_block': Tile_data('solid', 'sprites/tiles/grass.png', False, 0),
}