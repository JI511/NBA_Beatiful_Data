# ----------------------------------------------------------------------------------------------------------------------
# Box Score
# ----------------------------------------------------------------------------------------------------------------------

# imports


class TeamBoxScore(object):
    """
    Class for a team box score object
    """
    def __init__(self, box_scores, team_box_score, team_name):
        """
        Setup for the TeamBoxScore class.

        :param list box_scores: Player box scores.
        :param list team_box_score: Team box score stats.
        :param str team_name: The team name of the associated box scores.
        """
        self.box_scores = box_scores
        self.team_box_score = team_box_score
        self.team = team_name
        self.players = self.__get_box_score_items('name')

    def to_string(self):
        """
        Converts the team box score object into a human readable string.

        :return: Team box score data.
        :rtype: str
        """
        builder = "Team: %s\n" % self.team
        builder += '\tPlayers: %s\n' % str(self.players)
        return builder

    def __get_box_score_items(self, key):
        """
        Gets a specific box score item from a list of players.

        :param str key: The key to use within the box score dict.
        :return: The items for each player.
        :rtype: list
        """
        return_val = []
        for box_score in self.box_scores:
            return_val.append(box_score[key])
        return return_val

# ----------------------------------------------------------------------------------------------------------------------
# End
# ----------------------------------------------------------------------------------------------------------------------
