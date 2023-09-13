from src.panda_stat import getDescStats


def test_get_stat():
    testDf = getDescStats()
    assert testDf.iloc[0] == 150
    assert testDf.iloc[3] == 4.3
    assert testDf.iloc[4] == 5.1
