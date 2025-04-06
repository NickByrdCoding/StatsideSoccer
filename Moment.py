class Moment:
    def __init__(self, team_possession, moment_type):
        self.team_possession = team_possession

        #MomentType String
        self.moment_type = moment_type

        self.successful_pressure_escape = False
        
        self.better_pass = None
        self.better_pass_frame = None
        self.better_pass_passer = None