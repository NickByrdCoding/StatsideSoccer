class Trends:
    def __init__(self, pressure_moments, threatening_moments):
        self.pressure_moments = pressure_moments
        self.threatening_moments = threatening_moments
        # zones: starting zone + ending zone + zone chains
        # tempo: time of sequence + one touch passes
        # pass directions in creativity
        # identify top players
        # player chains
        # are there better passes?
        # overall zones of pressure and attack
        # check if switching field is a common trend or attack one side?

        #integrate llm for insights?
    
    def get_zone_insights(self):
        zone_chains_fail = {}
        starting_zones_fail = {}
        ending_zones_fail = {}
        
        zone_chains_success = {}
        starting_zones_success = {}
        ending_zones_success = {}
        for moment in self.pressure_moments:
            if moment.pressure_escape:
            starting_zone_success = moment.team_possesion.player_possessions[0].start_zone
            
        for moment in self.threatening_moments:
            ending_zone = moment.team_possesion.player_possessions[-1].end_zone

