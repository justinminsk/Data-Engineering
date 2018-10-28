SELECT Master.nameFirst, Master.nameLast, Teams.name AS teamName, Batting.*
FROM Batting INNER JOIN Master
ON Batting.playerID = Master.playerID
INNER JOIN Teams
ON Batting.teamID = Teams.teamID AND Batting.yearID = Teams.yearID;
