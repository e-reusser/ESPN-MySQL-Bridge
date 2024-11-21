from espn_api.football import League
from insertQueries import refreshScores, refreshPlayerData, refreshProjectedScores
from createTables import createTables
from dotenv import load_dotenv
import os
import mysql.connector
import time

print("Connecting to ESPN API...")
league = League(league_id=354198803, year=2024, espn_s2='AEAIZWXmXz%2B3llbOAtfqrtzW3f%2B4wEkEpDS%2BpNlM8fhs9KcPv%2FWzPO1ekTYUepb5yFfl%2FLcG7ftwfAdB56J%2BKwlMx16ayKOvKfrQisVluqXZl4Uw%2F6c4cQBUFsfuauyq1cY7eXoXQDHZKzwGhvHRCKJOc5ON%2Burx2aT69hs3BNxQnNmuECgPPNzUDgI6myej5Aqqw85zUfO4C6lHh8b%2BVhCqRhDiZy2gOExNWqEZ2Ahc8wXQ6wlN3zh44zYsu%2Fz2hBC8NJ6n8PL6l3qE4M8inY5cE8XpKaBI0k6CQhH%2BgWst4Q%3D%3D', swid='{9BC0B2D2-78ED-4395-87C5-776E8EFB14FC}')

load_dotenv()

deleteFirst = os.getenv('DELETEFIRST')
size = os.getenv('SIZE')

print("Connecting to MySQL server...")
db = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(buffered=True)
tables = {
    "Teams",
    "Leagues",
    "LeagueTeams",
    "ScoringFormat",
    "Matches",
    "AutoSubs",
    "LeagueUser",
    "TeamUser"
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