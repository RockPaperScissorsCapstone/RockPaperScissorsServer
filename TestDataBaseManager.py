import pytest
from DataBaseManager import DBManager 

def test_updateMatchHistory_AI_Wins():
    dbm = DBManager()
    AIid = 20
    pID = 1
    winnerId = AIid
    matchHistoryInfo = []
    matchHistoryInfo.append(AIid)
    matchHistoryInfo.append(pID)
    matchHistoryInfo.append(winnerId)
    matchHistoryInfo.append("2016-10-25")
    result = dbm.updateMatchHistory(matchHistoryInfo)
    print(result)
    #assert result == "0"

test_updateMatchHistory_AI_Wins()
