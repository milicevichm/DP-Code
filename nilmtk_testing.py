# Import the classes and modules to be used for processing energy dataset
from __future__ import print_function, division
from nilmtk import HDFDataStore, DataSet
from nilmtk.disaggregate import CombinatorialOptimisation
import pandas as pd
import matplotlib.pyplot as plt

"""
print("Loading data.... \n")

#declare and load HDF data (REDD)
redd_datastore = HDFDataStore("C:/NILM/Data_Sets/redd_data.h5")

#declare dataset
sample_dataset = DataSet()

#load datastore into dataset
sample_dataset.load(redd_datastore)

print("Sucessfully loaded. \n")



elec = sample_dataset.buildings[1].elec
gs = elec.mains().good_sections(full_results=True)
gs.combined()


print ("\nTraining CO Model...")

co = CombinatorialOptimisation()
co.train(elec)

mains = elec.mains()
output = HDFDataStore('C:/NILM/output.h5','w')

print("Disaggregation")
co.disaggregate(mains,output)

output.store.get('/building1/elec/meter3')[:10]

disag_dataset = DataSet()
disag_dataset.load(output)

elec = disag_dataset.buildings[1].elec
good_sections = elec.mains().good_sections()


redd_datastore.store.get('/building1/elec/meter1')["2011-05-01 10:00":"2011-05-01 12:00"].plot()
output.store.get('/building1/elec/meter1')["2011-05-01":"2011-05-01 12:00"].plot()
plt.show()

#close datastore object 
print("Program finished")
redd_datastore.close()
output.close()
"""

print(dir(plt))