def insertPlayerStatistics(cursor, league, playerID, week):
    player = league.player_info(playerId=playerID)

    insertIntoPlayerStatistics = """
    INSERT INTO PlayerStatistics (
        playerID, week, passing_attempts, passing_completions, passing_incompletions,
        passing_yards, passing_interceptions, rushing_yards, rushing_yards_per_attempt,
        rushing_touchdowns, receptions, receiving_yards, receiving_touchdowns,
        receiving_targets, receiving_yards_per_reception, fumbles, fantasy_points,
        defensive0PointsAllowed, defensive1To6PointsAllowed, defensive7To13PointsAllowed,
        defensive14To17PointsAllowed, defensiveInterceptions, defensiveFumbles, defensiveSacks,
        defensiveForcedFumbles, defensiveAssistedTackles, defensiveSoloTackles,
        defensiveTotalTackles, defensivePassesDefensed, kickoffReturnYards, puntReturnYards,
        puntsReturned, defensivePointsAllowed, defensive18To21PointsAllowed, defensive22To27PointsAllowed,
        defensive28To34PointsAllowed, defensive35To45PointsAllowed, defensiveYardsAllowed,
        defensiveLessThan100YardsAllowed, defensive100To199YardsAllowed, defensive200To299YardsAllowed,
        defensive300To349YardsAllowed, defensive350To399YardsAllowed, defensive400To449YardsAllowed,
        defensive450To499YardsAllowed, defensive500To549YardsAllowed, defensive550PlusYardsAllowed,
        madeFieldGoalsFrom50Plus, attemptedFieldGoalsFrom50Plus, madeFieldGoalsFrom40To49,
        attemptedFieldGoalsFrom40To49, missedFieldGoalsFrom40To49, madeFieldGoalsFromUnder40,
        attemptedFieldGoalsFromUnder40, madeFieldGoals, attemptedFieldGoals, missedFieldGoals,
        madeExtraPoints, attemptedExtraPoints
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
    """

    try:
        overallstats = player.stats[week]
        points = overallstats.get('points', 0)
        overallstats = overallstats['breakdown']
    except:
        return

    cursor.execute(insertIntoPlayerStatistics, (
        playerID,
        week,
        overallstats.get('passingAttempts', 0),
        overallstats.get('passingCompletions', 0),
        overallstats.get('passingIncompletions', 0),
        overallstats.get('passingYards', 0),
        overallstats.get('passingInterceptions', 0),
        overallstats.get('rushingYards', 0),
        overallstats.get('rushingYardsPerAttempt', 0),
        overallstats.get('rushingTouchdowns', 0),
        overallstats.get('receivingReceptions', 0),
        overallstats.get('receivingYards', 0),
        overallstats.get('receivingTouchdowns', 0),
        overallstats.get('receivingTargets', 0),
        overallstats.get('receivingYardsPerReception', 0),
        overallstats.get('fumbles', 0),
        points,
        overallstats.get('defensive0PointsAllowed', 0),
        overallstats.get('defensive1To6PointsAllowed', 0),
        overallstats.get('defensive7To13PointsAllowed', 0),
        overallstats.get('defensive14To17PointsAllowed', 0),
        overallstats.get('defensiveInterceptions', 0),
        overallstats.get('defensiveFumbles', 0),
        overallstats.get('defensiveSacks', 0),
        overallstats.get('defensiveForcedFumbles', 0),
        overallstats.get('defensiveAssistedTackles', 0),
        overallstats.get('defensiveSoloTackles', 0),
        overallstats.get('defensiveTotalTackles', 0),
        overallstats.get('defensivePassesDefensed', 0),
        overallstats.get('kickoffReturnYards', 0),
        overallstats.get('puntReturnYards', 0),
        overallstats.get('puntsReturned', 0),
        overallstats.get('defensivePointsAllowed', 0),
        overallstats.get('defensive18To21PointsAllowed', 0),
        overallstats.get('defensive22To27PointsAllowed', 0),
        overallstats.get('defensive28To34PointsAllowed', 0),
        overallstats.get('defensive35To45PointsAllowed', 0),
        overallstats.get('defensiveYardsAllowed', 0),
        overallstats.get('defensiveLessThan100YardsAllowed', 0),
        overallstats.get('defensive100To199YardsAllowed', 0),
        overallstats.get('defensive200To299YardsAllowed', 0),
        overallstats.get('defensive300To349YardsAllowed', 0),
        overallstats.get('defensive350To399YardsAllowed', 0),
        overallstats.get('defensive400To449YardsAllowed', 0),
        overallstats.get('defensive450To499YardsAllowed', 0),
        overallstats.get('defensive500To549YardsAllowed', 0),
        overallstats.get('defensive550PlusYardsAllowed', 0),
        overallstats.get('madeFieldGoalsFrom50Plus', 0),
        overallstats.get('attemptedFieldGoalsFrom50Plus', 0),
        overallstats.get('madeFieldGoalsFrom40To49', 0),
        overallstats.get('attemptedFieldGoalsFrom40To49', 0),
        overallstats.get('missedFieldGoalsFrom40To49', 0),
        overallstats.get('madeFieldGoalsFromUnder40', 0),
        overallstats.get('attemptedFieldGoalsFromUnder40', 0),
        overallstats.get('madeFieldGoals', 0),
        overallstats.get('attemptedFieldGoals', 0),
        overallstats.get('missedFieldGoals', 0),
        overallstats.get('madeExtraPoints', 0),
        overallstats.get('attemptedExtraPoints', 0)
    ))

def insertPlayerData(cursor, player):
    insertPlayer = """
    INSERT INTO Players (playerID, name, position, teamID, injured, posRank, average_points, eligible_slots)
    VALUES (%s, %s, %s, NULL, %s, %s, %s, %s)
    """

    cursor.execute(insertPlayer, (
        player.playerId,
        player.name,
        player.position,
        player.injured,
        player.posRank,
        player.avg_points,
        ",".join(player.eligibleSlots)
    ))

def refreshPlayerData(cursor, league, playerID):
    checkIfExists = """
        SELECT injured FROM Players WHERE playerID = %s
    """

    player = league.player_info(playerId=playerID)

    cursor.execute(checkIfExists, (playerID,))
    result = cursor.fetchone()
    if result is None:
        insertPlayerData(cursor, player)
        return
    
    previousInjuredStatus = result[0]

    if previousInjuredStatus != player.injured:
        print("Status changed for " + player.name)
        swapSlotsForSubstitute(cursor, playerID)

    updatePlayer = """
        UPDATE Players SET
            name = %s,
            position = %s,
            teamID = NULL,
            injured = %s,
            posRank = %s,
            average_points = %s,
            eligible_slots = %s
        WHERE playerID = %s
        """
    
    cursor.execute(updatePlayer, (
            player.name,
            player.position,
            player.injured,
            player.posRank,
            player.avg_points,
            ",".join(player.eligibleSlots),
            player.playerId
        ))

def swapSlotsForSubstitute(cursor, playerID):
    findSubstituteTeamsQuery = """
        SELECT pt.teamID, ps.playerID, ps.substituteID
        FROM AutoSubs as ps
        JOIN PlayerTeam as pt ON pt.playerID = ps.playerID
        WHERE ps.substituteID = %s
    """
    
    cursor.execute(findSubstituteTeamsQuery, (playerID,))
    result = cursor.fetchall()

    for teamID, playerID, substituteID in result:
        getSlotsQuery = """
            SELECT pt.slot
            FROM PlayerTeam as pt
            WHERE pt.teamID = %s AND pt.playerID IN (%s, %s)
        """
        
        cursor.execute(getSlotsQuery, (teamID, playerID, substituteID))
        slots = cursor.fetchall()
        
        if len(slots) == 2:
            playerSlot, substituteSlot = slots[0][0], slots[1][0]

            updateSlotQuery = """
                UPDATE PlayerTeam SET slot = %s WHERE teamID = %s AND playerID = %s
            """
            cursor.execute(updateSlotQuery, (substituteSlot, teamID, playerID))
            cursor.execute(updateSlotQuery, (playerSlot, teamID, substituteID))

            print(f"Swapped slots for player {playerID} and substitute {substituteID} on team {teamID}.")
            
            # Delete the entry from AutoSubs table after the swap
            deleteAutoSubsQuery = """
                DELETE FROM AutoSubs WHERE playerID = %s AND substituteID = %s
            """
            cursor.execute(deleteAutoSubsQuery, (playerID, substituteID))
            print(f"Deleted AutoSubs entry for player {playerID} and substitute {substituteID}.")


def refreshScores(cursor, league, playerID, week):
    checkIfExists = """
    SELECT COUNT(*) FROM PlayerStatistics WHERE playerID = %s AND week = %s
    """

    cursor.execute(checkIfExists, (playerID, week))
    exists = cursor.fetchone()[0]
    if (not exists):
        insertPlayerStatistics(cursor, league, playerID, week)
    else:
        updatePlayerStatistics = """
        UPDATE PlayerStatistics SET
            passing_attempts = %s,
            passing_completions = %s,
            passing_incompletions = %s,
            passing_yards = %s,
            passing_interceptions = %s,
            rushing_yards = %s,
            rushing_yards_per_attempt = %s,
            rushing_touchdowns = %s,
            receptions = %s,
            receiving_yards = %s,
            receiving_touchdowns = %s,
            receiving_targets = %s,
            receiving_yards_per_reception = %s,
            fumbles = %s,
            fantasy_points = %s,
            defensive0PointsAllowed = %s,
            defensive1To6PointsAllowed = %s,
            defensive7To13PointsAllowed = %s,
            defensive14To17PointsAllowed = %s,
            defensiveInterceptions = %s,
            defensiveFumbles = %s,
            defensiveSacks = %s,
            defensiveForcedFumbles = %s,
            defensiveAssistedTackles = %s,
            defensiveSoloTackles = %s,
            defensiveTotalTackles = %s,
            defensivePassesDefensed = %s,
            kickoffReturnYards = %s,
            puntReturnYards = %s,
            puntsReturned = %s,
            defensivePointsAllowed = %s,
            defensive18To21PointsAllowed = %s,
            defensive22To27PointsAllowed = %s,
            defensive28To34PointsAllowed = %s,
            defensive35To45PointsAllowed = %s,
            defensiveYardsAllowed = %s,
            defensiveLessThan100YardsAllowed = %s,
            defensive100To199YardsAllowed = %s,
            defensive200To299YardsAllowed = %s,
            defensive300To349YardsAllowed = %s,
            defensive350To399YardsAllowed = %s,
            defensive400To449YardsAllowed = %s,
            defensive450To499YardsAllowed = %s,
            defensive500To549YardsAllowed = %s,
            defensive550PlusYardsAllowed = %s,
            madeFieldGoalsFrom50Plus = %s,
            attemptedFieldGoalsFrom50Plus = %s,
            madeFieldGoalsFrom40To49 = %s,
            attemptedFieldGoalsFrom40To49 = %s,
            missedFieldGoalsFrom40To49 = %s,
            madeFieldGoalsFromUnder40 = %s,
            attemptedFieldGoalsFromUnder40 = %s,
            madeFieldGoals = %s,
            attemptedFieldGoals = %s,
            missedFieldGoals = %s,
            madeExtraPoints = %s,
            attemptedExtraPoints = %s
        WHERE playerID = %s AND week = %s
        """

        player = league.player_info(playerId=playerID)
        try:
            overallstats = player.stats[week]
            points = overallstats.get('points', 0)
            overallstats = overallstats['breakdown']
        except:
            return

        cursor.execute(updatePlayerStatistics, (
            playerID,
            week,
            overallstats.get('passingAttempts', 0),
            overallstats.get('passingCompletions', 0),
            overallstats.get('passingIncompletions', 0),
            overallstats.get('passingYards', 0),
            overallstats.get('passingInterceptions', 0),
            overallstats.get('rushingYards', 0),
            overallstats.get('rushingYardsPerAttempt', 0),
            overallstats.get('rushingTouchdowns', 0),
            overallstats.get('receivingReceptions', 0),
            overallstats.get('receivingYards', 0),
            overallstats.get('receivingTouchdowns', 0),
            overallstats.get('receivingTargets', 0),
            overallstats.get('receivingYardsPerReception', 0),
            overallstats.get('fumbles', 0),
            points,
            overallstats.get('defensive0PointsAllowed', 0),
            overallstats.get('defensive1To6PointsAllowed', 0),
            overallstats.get('defensive7To13PointsAllowed', 0),
            overallstats.get('defensive14To17PointsAllowed', 0),
            overallstats.get('defensiveInterceptions', 0),
            overallstats.get('defensiveFumbles', 0),
            overallstats.get('defensiveSacks', 0),
            overallstats.get('defensiveForcedFumbles', 0),
            overallstats.get('defensiveAssistedTackles', 0),
            overallstats.get('defensiveSoloTackles', 0),
            overallstats.get('defensiveTotalTackles', 0),
            overallstats.get('defensivePassesDefensed', 0),
            overallstats.get('kickoffReturnYards', 0),
            overallstats.get('puntReturnYards', 0),
            overallstats.get('puntsReturned', 0),
            overallstats.get('defensivePointsAllowed', 0),
            overallstats.get('defensive18To21PointsAllowed', 0),
            overallstats.get('defensive22To27PointsAllowed', 0),
            overallstats.get('defensive28To34PointsAllowed', 0),
            overallstats.get('defensive35To45PointsAllowed', 0),
            overallstats.get('defensiveYardsAllowed', 0),
            overallstats.get('defensiveLessThan100YardsAllowed', 0),
            overallstats.get('defensive100To199YardsAllowed', 0),
            overallstats.get('defensive200To299YardsAllowed', 0),
            overallstats.get('defensive300To349YardsAllowed', 0),
            overallstats.get('defensive350To399YardsAllowed', 0),
            overallstats.get('defensive400To449YardsAllowed', 0),
            overallstats.get('defensive450To499YardsAllowed', 0),
            overallstats.get('defensive500To549YardsAllowed', 0),
            overallstats.get('defensive550PlusYardsAllowed', 0),
            overallstats.get('madeFieldGoalsFrom50Plus', 0),
            overallstats.get('attemptedFieldGoalsFrom50Plus', 0),
            overallstats.get('madeFieldGoalsFrom40To49', 0),
            overallstats.get('attemptedFieldGoalsFrom40To49', 0),
            overallstats.get('missedFieldGoalsFrom40To49', 0),
            overallstats.get('madeFieldGoalsFromUnder40', 0),
            overallstats.get('attemptedFieldGoalsFromUnder40', 0),
            overallstats.get('madeFieldGoals', 0),
            overallstats.get('attemptedFieldGoals', 0),
            overallstats.get('missedFieldGoals', 0),
            overallstats.get('madeExtraPoints', 0),
            overallstats.get('attemptedExtraPoints', 0)
        ))

def insertProjectedScores(cursor, player, week):
    insertIntoProjectedPlayerStatistics = """
    INSERT INTO ProjectedPlayerStatistics (
        playerID, week, passing_attempts, passing_completions, passing_incompletions,
        passing_yards, passing_interceptions, rushing_yards, rushing_yards_per_attempt,
        rushing_touchdowns, receptions, receiving_yards, receiving_touchdowns,
        receiving_targets, receiving_yards_per_reception, fumbles, fantasy_points,
        defensive0PointsAllowed, defensive1To6PointsAllowed, defensive7To13PointsAllowed,
        defensive14To17PointsAllowed, defensiveInterceptions, defensiveFumbles, defensiveSacks,
        defensiveForcedFumbles, defensiveAssistedTackles, defensiveSoloTackles,
        defensiveTotalTackles, defensivePassesDefensed, kickoffReturnYards, puntReturnYards,
        puntsReturned, defensivePointsAllowed, defensive18To21PointsAllowed, defensive22To27PointsAllowed,
        defensive28To34PointsAllowed, defensive35To45PointsAllowed, defensiveYardsAllowed,
        defensiveLessThan100YardsAllowed, defensive100To199YardsAllowed, defensive200To299YardsAllowed,
        defensive300To349YardsAllowed, defensive350To399YardsAllowed, defensive400To449YardsAllowed,
        defensive450To499YardsAllowed, defensive500To549YardsAllowed, defensive550PlusYardsAllowed,
        madeFieldGoalsFrom50Plus, attemptedFieldGoalsFrom50Plus, madeFieldGoalsFrom40To49,
        attemptedFieldGoalsFrom40To49, missedFieldGoalsFrom40To49, madeFieldGoalsFromUnder40,
        attemptedFieldGoalsFromUnder40, madeFieldGoals, attemptedFieldGoals, missedFieldGoals,
        madeExtraPoints, attemptedExtraPoints
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
    """

    try:
        overallstats = player.stats[week]
        points = overallstats.get('projected_points', 0)
        overallstats = overallstats['projected_breakdown']
    except:
        return

    cursor.execute(insertIntoProjectedPlayerStatistics, (
        player.playerId,
        week,
        overallstats.get('passingAttempts', 0),
        overallstats.get('passingCompletions', 0),
        overallstats.get('passingIncompletions', 0),
        overallstats.get('passingYards', 0),
        overallstats.get('passingInterceptions', 0),
        overallstats.get('rushingYards', 0),
        overallstats.get('rushingYardsPerAttempt', 0),
        overallstats.get('rushingTouchdowns', 0),
        overallstats.get('receivingReceptions', 0),
        overallstats.get('receivingYards', 0),
        overallstats.get('receivingTouchdowns', 0),
        overallstats.get('receivingTargets', 0),
        overallstats.get('receivingYardsPerReception', 0),
        overallstats.get('fumbles', 0),
        points,
        overallstats.get('defensive0PointsAllowed', 0),
        overallstats.get('defensive1To6PointsAllowed', 0),
        overallstats.get('defensive7To13PointsAllowed', 0),
        overallstats.get('defensive14To17PointsAllowed', 0),
        overallstats.get('defensiveInterceptions', 0),
        overallstats.get('defensiveFumbles', 0),
        overallstats.get('defensiveSacks', 0),
        overallstats.get('defensiveForcedFumbles', 0),
        overallstats.get('defensiveAssistedTackles', 0),
        overallstats.get('defensiveSoloTackles', 0),
        overallstats.get('defensiveTotalTackles', 0),
        overallstats.get('defensivePassesDefensed', 0),
        overallstats.get('kickoffReturnYards', 0),
        overallstats.get('puntReturnYards', 0),
        overallstats.get('puntsReturned', 0),
        overallstats.get('defensivePointsAllowed', 0),
        overallstats.get('defensive18To21PointsAllowed', 0),
        overallstats.get('defensive22To27PointsAllowed', 0),
        overallstats.get('defensive28To34PointsAllowed', 0),
        overallstats.get('defensive35To45PointsAllowed', 0),
        overallstats.get('defensiveYardsAllowed', 0),
        overallstats.get('defensiveLessThan100YardsAllowed', 0),
        overallstats.get('defensive100To199YardsAllowed', 0),
        overallstats.get('defensive200To299YardsAllowed', 0),
        overallstats.get('defensive300To349YardsAllowed', 0),
        overallstats.get('defensive350To399YardsAllowed', 0),
        overallstats.get('defensive400To449YardsAllowed', 0),
        overallstats.get('defensive450To499YardsAllowed', 0),
        overallstats.get('defensive500To549YardsAllowed', 0),
        overallstats.get('defensive550PlusYardsAllowed', 0),
        overallstats.get('madeFieldGoalsFrom50Plus', 0),
        overallstats.get('attemptedFieldGoalsFrom50Plus', 0),
        overallstats.get('madeFieldGoalsFrom40To49', 0),
        overallstats.get('attemptedFieldGoalsFrom40To49', 0),
        overallstats.get('missedFieldGoalsFrom40To49', 0),
        overallstats.get('madeFieldGoalsFromUnder40', 0),
        overallstats.get('attemptedFieldGoalsFromUnder40', 0),
        overallstats.get('madeFieldGoals', 0),
        overallstats.get('attemptedFieldGoals', 0),
        overallstats.get('missedFieldGoals', 0),
        overallstats.get('madeExtraPoints', 0),
        overallstats.get('attemptedExtraPoints', 0)
    ))

def refreshProjectedScores(cursor, player, week):
    checkIfExists = """
    SELECT COUNT(*) FROM ProjectedPlayerStatistics WHERE playerID = %s AND week = %s
    """

    cursor.execute(checkIfExists, (player.playerId, week))
    exists = cursor.fetchone()[0]
    if (not exists):
        insertProjectedScores(cursor, player, week)
    else:
        updateProjectedPlayerStatistics = """
        UPDATE ProjectedPlayerStatistics SET
            passing_attempts = %s,
            passing_completions = %s,
            passing_incompletions = %s,
            passing_yards = %s,
            passing_interceptions = %s,
            rushing_yards = %s,
            rushing_yards_per_attempt = %s,
            rushing_touchdowns = %s,
            receptions = %s,
            receiving_yards = %s,
            receiving_touchdowns = %s,
            receiving_targets = %s,
            receiving_yards_per_reception = %s,
            fumbles = %s,
            fantasy_points = %s,
            defensive0PointsAllowed = %s,
            defensive1To6PointsAllowed = %s,
            defensive7To13PointsAllowed = %s,
            defensive14To17PointsAllowed = %s,
            defensiveInterceptions = %s,
            defensiveFumbles = %s,
            defensiveSacks = %s,
            defensiveForcedFumbles = %s,
            defensiveAssistedTackles = %s,
            defensiveSoloTackles = %s,
            defensiveTotalTackles = %s,
            defensivePassesDefensed = %s,
            kickoffReturnYards = %s,
            puntReturnYards = %s,
            puntsReturned = %s,
            defensivePointsAllowed = %s,
            defensive18To21PointsAllowed = %s,
            defensive22To27PointsAllowed = %s,
            defensive28To34PointsAllowed = %s,
            defensive35To45PointsAllowed = %s,
            defensiveYardsAllowed = %s,
            defensiveLessThan100YardsAllowed = %s,
            defensive100To199YardsAllowed = %s,
            defensive200To299YardsAllowed = %s,
            defensive300To349YardsAllowed = %s,
            defensive350To399YardsAllowed = %s,
            defensive400To449YardsAllowed = %s,
            defensive450To499YardsAllowed = %s,
            defensive500To549YardsAllowed = %s,
            defensive550PlusYardsAllowed = %s,
            madeFieldGoalsFrom50Plus = %s,
            attemptedFieldGoalsFrom50Plus = %s,
            madeFieldGoalsFrom40To49 = %s,
            attemptedFieldGoalsFrom40To49 = %s,
            missedFieldGoalsFrom40To49 = %s,
            madeFieldGoalsFromUnder40 = %s,
            attemptedFieldGoalsFromUnder40 = %s,
            madeFieldGoals = %s,
            attemptedFieldGoals = %s,
            missedFieldGoals = %s,
            madeExtraPoints = %s,
            attemptedExtraPoints = %s
        WHERE playerID = %s AND week = %s
        """

        try:
            overallstats = player.stats[week]
            points = overallstats.get('projected_points', 0)
            overallstats = overallstats['projected_breakdown']
        except:
            return

        cursor.execute(updateProjectedPlayerStatistics, (
            player.playerId,
            week,
            overallstats.get('passingAttempts', 0),
            overallstats.get('passingCompletions', 0),
            overallstats.get('passingIncompletions', 0),
            overallstats.get('passingYards', 0),
            overallstats.get('passingInterceptions', 0),
            overallstats.get('rushingYards', 0),
            overallstats.get('rushingYardsPerAttempt', 0),
            overallstats.get('rushingTouchdowns', 0),
            overallstats.get('receivingReceptions', 0),
            overallstats.get('receivingYards', 0),
            overallstats.get('receivingTouchdowns', 0),
            overallstats.get('receivingTargets', 0),
            overallstats.get('receivingYardsPerReception', 0),
            overallstats.get('fumbles', 0),
            points,
            overallstats.get('defensive0PointsAllowed', 0),
            overallstats.get('defensive1To6PointsAllowed', 0),
            overallstats.get('defensive7To13PointsAllowed', 0),
            overallstats.get('defensive14To17PointsAllowed', 0),
            overallstats.get('defensiveInterceptions', 0),
            overallstats.get('defensiveFumbles', 0),
            overallstats.get('defensiveSacks', 0),
            overallstats.get('defensiveForcedFumbles', 0),
            overallstats.get('defensiveAssistedTackles', 0),
            overallstats.get('defensiveSoloTackles', 0),
            overallstats.get('defensiveTotalTackles', 0),
            overallstats.get('defensivePassesDefensed', 0),
            overallstats.get('kickoffReturnYards', 0),
            overallstats.get('puntReturnYards', 0),
            overallstats.get('puntsReturned', 0),
            overallstats.get('defensivePointsAllowed', 0),
            overallstats.get('defensive18To21PointsAllowed', 0),
            overallstats.get('defensive22To27PointsAllowed', 0),
            overallstats.get('defensive28To34PointsAllowed', 0),
            overallstats.get('defensive35To45PointsAllowed', 0),
            overallstats.get('defensiveYardsAllowed', 0),
            overallstats.get('defensiveLessThan100YardsAllowed', 0),
            overallstats.get('defensive100To199YardsAllowed', 0),
            overallstats.get('defensive200To299YardsAllowed', 0),
            overallstats.get('defensive300To349YardsAllowed', 0),
            overallstats.get('defensive350To399YardsAllowed', 0),
            overallstats.get('defensive400To449YardsAllowed', 0),
            overallstats.get('defensive450To499YardsAllowed', 0),
            overallstats.get('defensive500To549YardsAllowed', 0),
            overallstats.get('defensive550PlusYardsAllowed', 0),
            overallstats.get('madeFieldGoalsFrom50Plus', 0),
            overallstats.get('attemptedFieldGoalsFrom50Plus', 0),
            overallstats.get('madeFieldGoalsFrom40To49', 0),
            overallstats.get('attemptedFieldGoalsFrom40To49', 0),
            overallstats.get('missedFieldGoalsFrom40To49', 0),
            overallstats.get('madeFieldGoalsFromUnder40', 0),
            overallstats.get('attemptedFieldGoalsFromUnder40', 0),
            overallstats.get('madeFieldGoals', 0),
            overallstats.get('attemptedFieldGoals', 0),
            overallstats.get('missedFieldGoals', 0),
            overallstats.get('madeExtraPoints', 0),
            overallstats.get('attemptedExtraPoints', 0)
        ))