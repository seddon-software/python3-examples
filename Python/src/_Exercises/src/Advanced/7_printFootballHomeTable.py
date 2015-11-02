import re


def printHomeTable(lines, teams):
    league = []
    for team, line in zip(teams, lines):
        result, pts = getHomeResults(line)
        output = "{:24s}{:s}".format(team, result)
        league.append([pts, output])
    
    league.sort(key=lambda entry:entry[0], reverse=True)
    for pts, entry in league:
        print entry

def readResultsFile(fileName):
    try:
        with open(fileName, "r") as f:
            allLines = f.readlines()
            return allLines
    except IOError,e:
        print e

def getTeams(lines):
    teams = []
    for line in lines:
        data = re.split("\d", line)
        team = data[0].strip()
        teams.append(team)
    return teams

def getHomeResults(line):
    scores = line
    scores = re.sub('[a-zA-Z]', '', scores)
    scores = re.sub('\s+', ' ', scores)
    scores = scores.strip()
    scores = re.split("\s+", scores)
    pts = p = w = d = l = f = a = 0
    for score in scores:
        home = int(score[0])
        away = int(score[2])
        p += 1
        f += home
        a += away
        if home >  away: pts += 3; w += 1
        if home == away: pts += 1; d += 1
        if home <  away: l += 1
    return "{:2d} {:2d} {:2d} {:2d} {:2d} {:2d} {:2d}".format(p, w, d, l, f, a, pts), pts


lines = readResultsFile("resources/results_2014_15.ascii")
teams = getTeams(lines)
printHomeTable(lines, teams) 
    