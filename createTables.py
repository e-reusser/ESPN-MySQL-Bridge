def createTables(cursor):
    # Leagues
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Leagues (
        leagueID INT AUTO_INCREMENT PRIMARY KEY,
        reg_season_count INT NOT NULL,
        team_count INT NOT NULL,
        current_team_count INT NOT NULL,
        playoff_team_count INT NOT NULL,
        name VARCHAR(50) NOT NULL,
        tie_rule INT,
        playoff_tie_rule INT,
        playoff_seed_tie_rule INT,
        playoff_matchup_period_length INT,
        faab BOOLEAN,
        scoringID INT
    );
    """)

    # Teams
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Teams (
        teamID INT AUTO_INCREMENT PRIMARY KEY,
        teamName VARCHAR(100) NOT NULL,
        leagueID INT NOT NULL,
        FOREIGN KEY (leagueID) REFERENCES Leagues (leagueID)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """)

    # Players
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Players (
        playerID INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        position VARCHAR(10) NOT NULL,
        teamID INT NULL,
        injured BOOLEAN,
        posRank INT,
        average_points DECIMAL(5, 2),
        eligible_slots VARCHAR(50),
        FOREIGN KEY (teamID) REFERENCES Teams (teamID)
    );
    """)

    # LeagueTeams
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS LeagueTeams (
        leagueID INT,
        teamID INT,
        PRIMARY KEY (leagueID, teamID),
        FOREIGN KEY (leagueID) REFERENCES Leagues (leagueID)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
        FOREIGN KEY (teamID) REFERENCES Teams (teamID)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """)

    # ScoringFormat
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ScoringFormat (
        entryID INT AUTO_INCREMENT PRIMARY KEY,
        leagueID INT,
        abbr VARCHAR(10),
        label VARCHAR(255),
        points DECIMAL(5, 2),
        FOREIGN KEY (leagueID) REFERENCES Leagues (leagueID)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """)

    # Matches
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Matches (
        matchID INT PRIMARY KEY,
        team1ID INT NOT NULL,
        team2ID INT NOT NULL,
        week INT NOT NULL,
        team1Score INT,
        team2Score INT,
        FOREIGN KEY (team1ID) REFERENCES Teams (teamID)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
        FOREIGN KEY (team2ID) REFERENCES Teams (teamID)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """)

    # PlayerStatistics
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PlayerStatistics (
        statID INT AUTO_INCREMENT PRIMARY KEY,
        playerID INT,
        week INT DEFAULT 0,
        passing_attempts INT DEFAULT 0,
        passing_completions INT DEFAULT 0,
        passing_incompletions INT DEFAULT 0,
        passing_yards INT DEFAULT 0,
        passing_interceptions INT DEFAULT 0,
        rushing_yards INT DEFAULT 0,
        rushing_yards_per_attempt INT DEFAULT 0,
        rushing_touchdowns INT DEFAULT 0,
        receptions INT DEFAULT 0,
        receiving_yards INT DEFAULT 0,
        receiving_touchdowns INT DEFAULT 0,
        receiving_targets INT DEFAULT 0,
        receiving_yards_per_reception INT DEFAULT 0,
        fumbles INT DEFAULT 0,
        fantasy_points DECIMAL(5, 2) NOT NULL,
        defensive0PointsAllowed INT DEFAULT 0,
        defensive1To6PointsAllowed INT DEFAULT 0,
        defensive7To13PointsAllowed INT DEFAULT 0,
        defensive14To17PointsAllowed INT DEFAULT 0,
        defensiveInterceptions INT DEFAULT 0,
        defensiveFumbles INT DEFAULT 0,
        defensiveSacks INT DEFAULT 0,
        defensiveForcedFumbles INT DEFAULT 0,
        defensiveAssistedTackles INT DEFAULT 0,
        defensiveSoloTackles INT DEFAULT 0,
        defensiveTotalTackles INT DEFAULT 0,
        defensivePassesDefensed INT DEFAULT 0,
        kickoffReturnYards INT DEFAULT 0,
        puntReturnYards INT DEFAULT 0,
        puntsReturned INT DEFAULT 0,
        defensivePointsAllowed INT DEFAULT 0,
        defensive18To21PointsAllowed INT DEFAULT 0,
        defensive22To27PointsAllowed INT DEFAULT 0,
        defensive28To34PointsAllowed INT DEFAULT 0,
        defensive35To45PointsAllowed INT DEFAULT 0,
        defensiveYardsAllowed INT DEFAULT 0,
        defensiveLessThan100YardsAllowed INT DEFAULT 0,
        defensive100To199YardsAllowed INT DEFAULT 0,
        defensive200To299YardsAllowed INT DEFAULT 0,
        defensive300To349YardsAllowed INT DEFAULT 0,
        defensive350To399YardsAllowed INT DEFAULT 0,
        defensive400To449YardsAllowed INT DEFAULT 0,
        defensive450To499YardsAllowed INT DEFAULT 0,
        defensive500To549YardsAllowed INT DEFAULT 0,
        defensive550PlusYardsAllowed INT DEFAULT 0,
        madeFieldGoalsFrom50Plus INT DEFAULT 0,
        attemptedFieldGoalsFrom50Plus INT DEFAULT 0,
        madeFieldGoalsFrom40To49 INT DEFAULT 0,
        attemptedFieldGoalsFrom40To49 INT DEFAULT 0,
        missedFieldGoalsFrom40To49 INT DEFAULT 0,
        madeFieldGoalsFromUnder40 INT DEFAULT 0,
        attemptedFieldGoalsFromUnder40 INT DEFAULT 0,
        madeFieldGoals INT DEFAULT 0,
        attemptedFieldGoals INT DEFAULT 0,
        missedFieldGoals INT DEFAULT 0,
        madeExtraPoints INT DEFAULT 0,
        attemptedExtraPoints INT DEFAULT 0,
        FOREIGN KEY (playerID) REFERENCES Players (playerID)
    );
    """)

    # ProjectedPlayerStatistics
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ProjectedPlayerStatistics (
        statID INT AUTO_INCREMENT PRIMARY KEY,
        playerID INT,
        week INT DEFAULT 0,
        passing_attempts INT DEFAULT 0,
        passing_completions INT DEFAULT 0,
        passing_incompletions INT DEFAULT 0,
        passing_yards INT DEFAULT 0,
        passing_interceptions INT DEFAULT 0,
        rushing_yards INT DEFAULT 0,
        rushing_yards_per_attempt INT DEFAULT 0,
        rushing_touchdowns INT DEFAULT 0,
        receptions INT DEFAULT 0,
        receiving_yards INT DEFAULT 0,
        receiving_touchdowns INT DEFAULT 0,
        receiving_targets INT DEFAULT 0,
        receiving_yards_per_reception INT DEFAULT 0,
        fumbles INT DEFAULT 0,
        fantasy_points DECIMAL(5, 2) NOT NULL,
        defensive0PointsAllowed INT DEFAULT 0,
        defensive1To6PointsAllowed INT DEFAULT 0,
        defensive7To13PointsAllowed INT DEFAULT 0,
        defensive14To17PointsAllowed INT DEFAULT 0,
        defensiveInterceptions INT DEFAULT 0,
        defensiveFumbles INT DEFAULT 0,
        defensiveSacks INT DEFAULT 0,
        defensiveForcedFumbles INT DEFAULT 0,
        defensiveAssistedTackles INT DEFAULT 0,
        defensiveSoloTackles INT DEFAULT 0,
        defensiveTotalTackles INT DEFAULT 0,
        defensivePassesDefensed INT DEFAULT 0,
        kickoffReturnYards INT DEFAULT 0,
        puntReturnYards INT DEFAULT 0,
        puntsReturned INT DEFAULT 0,
        defensivePointsAllowed INT DEFAULT 0,
        defensive18To21PointsAllowed INT DEFAULT 0,
        defensive22To27PointsAllowed INT DEFAULT 0,
        defensive28To34PointsAllowed INT DEFAULT 0,
        defensive35To45PointsAllowed INT DEFAULT 0,
        defensiveYardsAllowed INT DEFAULT 0,
        defensiveLessThan100YardsAllowed INT DEFAULT 0,
        defensive100To199YardsAllowed INT DEFAULT 0,
        defensive200To299YardsAllowed INT DEFAULT 0,
        defensive300To349YardsAllowed INT DEFAULT 0,
        defensive350To399YardsAllowed INT DEFAULT 0,
        defensive400To449YardsAllowed INT DEFAULT 0,
        defensive450To499YardsAllowed INT DEFAULT 0,
        defensive500To549YardsAllowed INT DEFAULT 0,
        defensive550PlusYardsAllowed INT DEFAULT 0,
        madeFieldGoalsFrom50Plus INT DEFAULT 0,
        attemptedFieldGoalsFrom50Plus INT DEFAULT 0,
        madeFieldGoalsFrom40To49 INT DEFAULT 0,
        attemptedFieldGoalsFrom40To49 INT DEFAULT 0,
        missedFieldGoalsFrom40To49 INT DEFAULT 0,
        madeFieldGoalsFromUnder40 INT DEFAULT 0,
        attemptedFieldGoalsFromUnder40 INT DEFAULT 0,
        madeFieldGoals INT DEFAULT 0,
        attemptedFieldGoals INT DEFAULT 0,
        missedFieldGoals INT DEFAULT 0,
        madeExtraPoints INT DEFAULT 0,
        attemptedExtraPoints INT DEFAULT 0,
        FOREIGN KEY (playerID) REFERENCES Players (playerID)
    );
    """)

    # AutoSubs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS AutoSubs (
        subID INT AUTO_INCREMENT PRIMARY KEY,
        playerID INT,
        substituteID INT,
        matchID INT,
        FOREIGN KEY (playerID) REFERENCES Players (playerID),
        FOREIGN KEY (substituteID) REFERENCES Players (playerID),
        FOREIGN KEY (matchID) REFERENCES Matches (matchID)
    );
    """)
