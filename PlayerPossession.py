class PlayerPossession:
    def __init__(
        self,
        start_separation,
        end_separation,
        start_zone,
        end_zone,
        best_pass,
        attempted_pass,
        player,
        start_frame,
        end_frame
):
        self.start_separation = start_separation
        self.end_separation = end_separation
        self.start_zone = start_zone
        self.end_zone = end_zone
        self.best_pass = best_pass
        self.attempted_pass = attempted_pass
        self.player = player
        self.start_frame = start_frame
        self.end_frame = end_frame