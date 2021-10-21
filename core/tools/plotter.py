import matplotlib.pyplot as plt
import numpy as np
import os

data_path = '..\\..\\phase_1\\Data\\'
plots_path = '..\\..\\phase_1\\Plots\\'

def plot_all_series():
    for root, dirs, files in os.walk(data_path, topdown=False):
        for filename in files:
            # Get all data from the Data folder
            data_file = open(data_path + os.path.join(filename), "r")
            
            # Read all data line by line
            time_series = []
            for data_line in data_file:
                data = data_line.split(" ")
                data = list(filter(('').__ne__, data))
                for val in data: 
                    time_series.append(float(val))            
            
            # Plot the series
            plt.plot(time_series)
            
            # Calculate mean and std
            mean = np.mean(time_series)
            std = np.std(time_series)
            
            # Plot mean value
            plt.plot([0, len(time_series)], [mean, mean], label="Mean")
            
            # Plot 3*sigma
            plt.plot([0, len(time_series)], [mean + 3 * std, mean + 3 * std],
                                             c="green", ls="-", label="3*Sigma")
            plt.plot([0, len(time_series)], [mean -3 * std, mean -3 * std],
                                             c="green", ls="-")
            
            # Place legend to the top right corned outside the plot
            plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
            plt.subplots_adjust(right=0.75)

            # Save plots to the Plots directory
            try:
                plt.savefig(plots_path + os.path.join(filename).rsplit('.',1)[0] + ".png")
            except OSError:
                print("Can't save plot " +
                     os.path.join(filename).rsplit('.',1)[0] + ".png")
            
            plt.close()

plot_all_series()