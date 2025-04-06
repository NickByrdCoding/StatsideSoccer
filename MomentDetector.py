from Moment import Moment
from TeamPossession import TeamPossession

class MomentDetector:
    def detect_moment(self, team_possesion):
        moments = []

        under_pressure_moment = self.detect_under_pressure(team_possesion)
        if under_pressure_moment != None:
            moment = Moment(under_pressure_moment, "Under_Pressure")
            if moment.team_possession.end_frame - moment.team_possession.start_frame < 200:
                current_pp = under_pressure_moment.player_possessions[len(under_pressure_moment.player_possessions) - 1]
                if current_pp.attempted_pass.direction in [1, 3, 4] or current_pp.start_separation >= 5.5 or current_pp.start_zone.number != under_pressure_moment.player_possessions[len(under_pressure_moment.player_possessions) - 2].start_zone.number:
                    #was successful
                    moment.successful_pressure_escape = True

                for player_possession in moment.team_possession.player_possessions:
                    best_pass = player_possession.best_pass
                    att_pass = player_possession.attempted_pass
                    if best_pass and best_pass.receiving_player != att_pass.receiving_player:
                        best_pass_quality = best_pass.x_completion * best_pass.x_threat
                        att_pass_quality = att_pass.x_completion * best_pass.x_threat
                        if best_pass_quality > att_pass_quality:
                            moment.better_pass = best_pass
                            moment.better_pass_frame = best_pass.frame
                            moment.better_pass_passer = player_possession.player.id

                moments.append(moment)

        threatening_play = self.detect_threatening_play(team_possesion)
        if threatening_play != None:
            moment = Moment(threatening_play, "Threatening_Play")
            if moment.team_possession.end_frame - moment.team_possession.start_frame < 200 and moment.team_possession.end_frame != moment.team_possession.start_frame:
                moments.append(moment)

        return moments
    
    def detect_under_pressure(self, team_possession):
        if len(team_possession.player_possessions) < 3:
            return None

        separations_window = []
        count_below_threshold = 0
        under_pressure_possession = None
        i = 0

        while i < len(team_possession.player_possessions):
            if team_possession.player_possessions[i].start_zone.third == 3:
                i += 1
                continue
            if len(separations_window) == 3:
                oldest = separations_window.pop(0)
                if oldest:
                    count_below_threshold -= 1

            current_pp = team_possession.player_possessions[i]
            is_below_threshold = current_pp.start_separation < 3.5

            separations_window.append(is_below_threshold)
            if is_below_threshold:
                count_below_threshold += 1

            if count_below_threshold >= 2 and under_pressure_possession is None:
                under_pressure_possession = TeamPossession()

                # Safely get the last 3 possessions from the team_possession list
                start_index = max(0, i - 2)
                for j in range(start_index, i + 1):
                    # Mark the first one(s) as 'triggering' if you want, others as not
                    is_trigger = j == start_index  # or however you want to define it
                    under_pressure_possession.add_player_possession(team_possession.player_possessions[j], is_trigger)

                i += 1
                break


            i += 1

        while under_pressure_possession and i < len(team_possession.player_possessions):
            current_pp = team_possession.player_possessions[i]
            under_pressure_possession.add_player_possession(current_pp, False)

            if current_pp.attempted_pass.direction in [1, 3, 4]:
                if current_pp.start_separation >= 3.5:
                    break
            else:
                if current_pp.attempted_pass.direction < 3.5:
                    break

            i += 1

        return under_pressure_possession

    def detect_threatening_play(self, team_possession):
        threatening_moment_possession = None

        i = 0
        while i < len(team_possession.player_possessions):
            if team_possession.player_possessions[i].attempted_pass.x_threat >= 0.04:
                threatening_moment_possession = TeamPossession()
                break
            i += 1

        if threatening_moment_possession:
            endI = i
            startI = max(0, endI - 4)

            for j in range(startI, endI + 1):
                is_trigger = j == endI
                threatening_moment_possession.add_player_possession(team_possession.player_possessions[j], is_trigger)

        return threatening_moment_possession
