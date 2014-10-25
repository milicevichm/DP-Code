# Import the classes and modules to be used for processing energy dataset
from __future__ import print_function, division
from nilmtk import HDFDataStore, DataSet
from nilmtk.disaggregate import CombinatorialOptimisation
from nilmtk.plots import plot_series
import pandas as pd
import matplotlib.pyplot as plt

print("Loading data.... \n")

#declare and load HDF data (REDD)
redd_datastore = HDFDataStore("C:/NILM/Data_Sets/redd_data.h5")

print("Sucessfully loaded. \n")

#load meter 1 instance in bulding 1 instance and plot (returned object is of type: meterGroup)
redd_datastore.store.get('/building1/elec/meter1').plot()

#show the plot
plt.show()

#close program
print("Program Closed.")
redd_datastore.close()
