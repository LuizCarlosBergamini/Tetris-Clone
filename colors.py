class Colors:
    black = ('#000000')
    green = ('#58ff00')
    blue = ('#586ef9')
    yellow = ('#fdff00')
    cyan = ('#63d0e4')
    magenta = ('#e478e4')
    orange = ('#e49410')
    red = ('#ff0000')

    @classmethod
    def get_cell_colors(cls):
        return [cls.black, cls.green, cls.blue, cls.yellow, cls.cyan, cls.magenta, cls.orange, cls.red]