from library.lib import run_statistics


def test_lib_stat():
    testInfo = run_statistics(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    )

    assert testInfo.iloc[0] == 150
    assert testInfo.iloc[3] == 4.3
    assert testInfo.iloc[4] == 5.1
