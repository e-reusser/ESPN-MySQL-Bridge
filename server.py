from espn_api.football import League
from insertQueries import refreshScores, refreshPlayerData, refreshProjectedScores
from createTables import createTables
import mysql.connector
import time

deleteFirst = False
size = 300

print("Connecting to ESPN API...")
league = League(league_id=417113629, year=2024, espn_s2='AEA3ovoQfgtnAzAQnu9tNfKaEMySnEGJKOvLmnUZqAXhdouMb4q2N1JkD4jjfX%2BqVxiXlErUb6fX6godNrr%2F%2FHYDMbqQIDZ%2FUNKLgxftU%2B37T6tW3ouCmkYDFVKqSPdQ8IVqYx%2BlGfhIhsAXQ9RIawInKaL9ddoByXEkU%2BMDoSbwOJfWtm2KW1m%2FpUHdnbEahQ01PA74u2Y6mBtqTJ%2BF1WM3VjC2mVwAPwkN0W8rewQdwsAYUYAq7MY8iAzOpfKVXUYn5TbEji4MYWQcEZDOXJWCj3LQlKNL7Fr4c3h2sG3qJg%3D%3D', swid='{9BC0B2D2-78ED-4395-87C5-776E8EFB14FC}')

print("Connecting to MySQL server...")
db = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    database="database"
)

cursor = db.cursor(buffered=True)
tables = {
    "Players",
    "Teams",
    "Leagues",
    "LeagueTeams",
    "ScoringFormat",
    "Matches",
    "PlayerStatistics",
    "AutoSubs"
}

if (deleteFirst):
    print("Dropping existing tables...")
    cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
    for table in tables:
        try:
            cursor.execute("DROP TABLE " + table + ";")
        except:
            print("Could not drop table " + table)
    cursor.execute("SET FOREIGN_KEY_CHECKS=1;")

print("Creating tables if not existing...")

createTables(cursor)

print("Inserting overall player data...")

for player in league.free_agents(size=size):
    print("Inserting player data for " + player.name + "...")
    week = 0
    refreshPlayerData(cursor=cursor, league=league, playerID=player.playerId)
    while (week <= league.current_week):
        refreshScores(cursor=cursor, league=league, playerID=player.playerId, week=week)
        refreshProjectedScores(cursor=cursor, player=player, week=week)
        week += 1
    db.commit()

while True:
    print("Updating in 1 hour...")
    time.sleep(1800)
    print("Updating in 30 minutes...")
    time.sleep(1740)
    print("Updating in 1 minute...")
    time.sleep(60)
    for player in league.free_agents(size=size):
        print("Updating " + player.name + "...")
        refreshPlayerData(cursor=cursor, league=league, playerID=player.playerId)
        refreshScores(cursor=cursor, league=league, playerID=player.playerId, week=league.current_week)
        refreshProjectedScores(cursor=cursor, player=player, week=week)
        db.commit()