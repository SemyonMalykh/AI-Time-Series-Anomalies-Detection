import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

metadata = pd.read_csv("../Time_Series_Anomaly_Detection/metadata.csv", index_col="data_id")
ts_path = "../Time_Series_Anomaly_Detection/phase_1/"

# change the size of the plots
sns.set(rc={'figure.figsize':(70,25)})


def plotTimeSeries(num:int, xstart:int=0, xstop:int=0):
    """ Searches the corresponding timeseries to a number and plots the graph.
        Values until the train_end_idx are colored in green as they cant have an anomaly.
        The anomaly is colored red, the rest of the timeseries in blue.

    Args:
        num (int): number of the time series
        xstart (int): limit the x axis (xstart and xstop need to be bigger than 0)
        xstop (int): limit the x axis (xstart and xstop need to be bigger than 0)
    """
    fna = [fn for fn in os.listdir("../Time_Series_Anomaly_Detection/phase_1/") if fn.startswith(str(num).rjust(3, "0"))]
    if len(fna) == 1:
        test_t = pd.read_csv(ts_path + fna[0], header=None)
        test_c = test_t.copy()
        test_a = test_t.copy()
        test_t.loc[metadata.loc[num, "train_end_idx"]:] = np.nan
        test_c.loc[:metadata.loc[num, "train_end_idx"]] = np.nan
        test_c.loc[metadata.loc[num, "anomaly_start"]:metadata.loc[num, "anomaly_end"]] = np.nan
        test_a.loc[0:metadata.loc[num, "anomaly_start"]] = np.nan
        test_a.loc[metadata.loc[num, "anomaly_end"]:] = np.nan
        plt.plot(test_t, color='g', linewidth=15)
        plt.plot(test_c, color='b', linewidth=15)
        plt.plot(test_a, color='r', linewidth=15)
        if xstart > 0 and xstop > 0:
            plt.xlim(xstart, xstop)
        plt.show()
    else:
        print("no corresponding file found")


# Example calls
plotTimeSeries(237, 88560, 91000)
plotTimeSeries(237)