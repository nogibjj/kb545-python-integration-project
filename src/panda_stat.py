import sys
import os
try:
    from library.lib import run_statistics
except ModuleNotFoundError:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    sys.path.insert(0, parent_dir)

    from library.lib import run_statistics


def getDescStats():
    filePath = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    return run_statistics(filePath)
