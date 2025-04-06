class TeamPossession:
    def __init__(self):
        self.start_frame = None
        self.end_frame = None
        self.start_zone = None
        self.end_zone = None
        self.player_possessions = []
        self.position_sequence = []
        self.positions_involved = set()
    
    def add_player_possession(self, player_possession, is_first):
        self.player_possessions.append(player_possession)
        self.position_sequence.append(player_possession.player.position)
        self.positions_involved.add(player_possession.player.position)

        if is_first:
            self.start_frame = player_possession.start_frame
            self.start_zone = player_possession.start_zone
        
        self.end_zone = player_possession.end_zone
        self.end_frame = player_possession.end_frame
        
