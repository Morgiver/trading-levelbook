import math

class Book:
    def __init__(self, columns: int = 2, granularity: int = 2):
         self.levels      = {}
         self.columns     = columns
         self.granularity = granularity
         self.view_range  = 1000

    def load_snapshot(self, snapshot: dict):
        # TODO
        pass

    def round_down(self, x: float):
        """ Rounding down the value respecting the level granularity """
        return math.floor(x * self.granularity) / self.granularity

    def add_level(self, price: float, column: int, volume: float):
        """ Add level that's not in the levels dict """
        # Setting columns volume list
        volume_levels         = [0] * self.columns
        volume_levels[column] = volume

        # Add the new level
        self.levels[self.round_down(price)] = volume_level

        # Rearrange the dict in ascending order
        self.levels = dict(sorted(self.levels.items()))

        return self

    def update_level(self, price: float, column: int, volume: float):
        """ Update the volume of a column at a defined level """
        self.levels[self.round_down(price)][column] = volume
        return self

    def level_exist(self, price: float):
        """ Check if the level is in prices dict """
        return self.round_down(price) in self.levels

    def feed(self, *args):
        """ Feeding the levels, every arguments have to be a list that contain a list containing level and volume. e.g. [[level, volume], ...]"""
        for column in args:
            """ Here we browse all columns feeding datas """
            id_column = 0

            for level in column:
                """ Here we browse all given levels and update them """
                price = float(level[0])
                volume = float(level[1])

                if self.level_exist(price):
                    # If level is already in prices dict
                    self.update_level(price, id_column, volume)
                else:
                    # If level is not in prices dict
                    self.add_level(price, id_column, volume)

            id_column += 1

        return self

    def set_view_range(self, levels: int):
        """ Setting the number of levels we want to see in the generated view """
        self.view_range = levels

    def filter_prices_levels(self, min_level, max_level):
        """ Return a dict that include all levels between the min_level and the max_level """
        return {k: v for k, v in self.levels.items() if min_level <= k <= max_level}

    def get_range(self, market_price: float):
        """ Calculate the min_level and max_level by the view_range """
        current_level = self.round_down(market_price)
        max_level     = self.round_down(current_level + (self.view_range / 2))
        min_level     = self.round_down(current_level - (self.view_range / 2))
        return min_level, max_level

    def view(self, market_price: float):
        """ Return a dict that represent a view determined by a view_range """
        min_level, max_level = self.get_range(market_price)
        return self.filter_prices_levels(min_level, max_level)
