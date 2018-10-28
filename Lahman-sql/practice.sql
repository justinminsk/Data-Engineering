SELECT nameFirst, nameLast, Batting.playerID, Batting.yearID, Batting.teamID, name, Batting.HR
FROM Batting INNER JOIN Master
ON Batting.playerID = Master.playerID
INNER JOIN Teams
ON Batting.teamID = Teams.teamID AND Batting.yearID = Teams.yearID
WHERE Batting.playerID = "ruthba01";
