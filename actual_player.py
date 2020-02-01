

class Player(object):
    def __init__(self):
        self.user_name = None
        self.coordinates = None # we haven't done coordinates yet

    def get_name_from_player(self, other_players) -> str: # when did we make other players???
        already_used_names = set([player.name for player in
                                      other_players])  # this is a set, removing duplicates .players so we don't have to make a list, just an iterable
        while True:
            name = input('Please enter your name:')
            if name not in already_used_names:
                return name
            else:
                print(f"{name} has already been used. Pick another name.")

    def __str__(self) -> str:
        return self.user_name

    def get_coord_from_player(self):
        #already_used_coord = set([player.coord for player in other_players])
        already_used_coord = [] # empty list of coords
        while True:
            player_coord = input('Choose your ship''s coordinates in the form: row,column').strip() #why are we using strip here
            try:
                stripped_coord = player_coord.strip(",")
                row,col - stripped_coord.split(","_)
                final_coord = (row,col)
                already_used_coord.append(final_coord)
                return row,col
            except:
                print(error)
                continue

        if final_coord in already_used_coord:
            print(f'{final_coord} has already been used. Pick another one.')

        if int(row) or int(col) > 9: # do i have to say len()
            print('Choose a number between 0 and 9 lmao can you count')

        elif final_coord == blank_char:
            print(f"You cannot pick {blank_char}")

        return final_coord # is this the right thing to return???

    def take_turn(self): # but should this be in different class? game class?
        # calls make
