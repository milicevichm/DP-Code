#Author: Michael Milicevich
#Created: 10/29/2014
#Script will test basic functionality of the dissagregation system used
#in the NILM toolkit.

'''
Instructions: 		Simply run to have two plots displayed: one of the aggregate mains
					energy found in REDD Building 1, and one of the appliance chosen 
					through typing the applaince name into the variable disag_apl.
					*To get a list of all appliance names run the function 
					kmap.list_appliances().

Troubleshooting:	Before running ensure that all file paths used below in the system
					also exist on your system. You need a converted redd dataset of the
					filetype .h5 (HDF).

'''


# Import the classes and modules to be used for processing energy dataset
from __future__ import print_function, division
from nilmtk import HDFDataStore, DataSet
from nilmtk.disaggregate import CombinatorialOptimisation
import pandas as pd
import matplotlib.pyplot as plt
from key_map import *
from nilmtk.disaggregate.hart_85 import *

#start and end times for plotting data
t_start = "2011-05-1 1:00"
t_end   = "2011-05-01 12:00"

#same day but smaller scale for more refined data plots
t1 ="2011-05-1 6:00"
t2 ="2011-05-1 7:00"

#initialize key map for building 1
kmap = Key_map()

#set the disaggregated plot here
disag_apl = 'fridge'
disag_key = kmap.get_key(disag_apl)

#First we must load in the converted REDD Dataset
print ("Loading DataSet.....")

#declare datastore and load converted HDF that stores REDD data
r_datastore = HDFDataStore("C:/NILM/Data_Sets/redd_data.h5")

#declare dataset object to work with and load datastore into Dataset
r_dataset = DataSet()
r_dataset.load(r_datastore)

#output sucessfull loading of data to user
print("DataSet Sucessfully Loaded!")

#now we take the data and elminate all sections with no samples
print("Conditioning Data... \n")

#load the metergroup from building one (house1 in REDD)
r_elec = r_dataset.buildings[1].elec


print("\nConditioning Finished.")

#now we must train the disaggregation model to ensure accuracy
print("Training disaggregation model...")

#declare a cominatorial optimization disaggregation object
disag = CombinatorialOptimisation()

#train the model on the building 1 meter 1 dataset (using every appliance)
disag.train(r_elec)

print("Model Sucessfully Trained!")

#the data will now be disaggregated and placed into an output HDF file
print("Disaggregating data...")

#load the mains of building 1
r1_mains = r_elec.mains()

#declare an output HDF datastore
output_store = HDFDataStore('C:/NILM/Data_Sets/redd_b1_output.h5','w')

#disaggregate the mains data using the combinatorial optimization algorithm
disag.disaggregate(r1_mains, output_store)

#close the output store
output_store.close()

#open new datastore to load data
output_load = HDFDataStore('C:/NILM/Data_Sets/redd_b1_output.h5')

print ("Disaggregation Complete!")

print ("Printing Data....")

#format axis names


#plot mains data vs disaggregated data based on appliance key
r_datastore.store.get(kmap.get_key('mains1'))[t_start : t_end].plot()
plt.title("Aggregated Mains Energy") 
plt.legend().set_visible(False)
plt.ylabel('Apparent Power [W]')
plt.xlabel('Time')

output_load.store.get(disag_key)[t_start:t_end].plot()
plt.title("Disaggregated "+ disag_apl.capitalize() +" Energy") 
plt.legend().set_visible(False)
plt.ylabel('Apparent Power [W]')
plt.xlabel('Time')
plt.show()


print("Data Sucessfully Printed!")
#close all open datastore files and terminate program
print("Closing files...")
r_datastore.close()
output_store.close()
output_load.close()
print("Program Finished.")

