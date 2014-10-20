# Import the classes and modules to be used for processing energy dataset
from nilmtk.datastore import *
from nilmtk.dataset import *
from nilmtk.disaggregate import combinatorial_optimisation

#declare and load HDF data (REDD)
redd_datastore = HDFDataStore("C:/NILM/Data_Sets/redd_data.hdf")

#declare dataset
sample_dataset = DataSet()

#load datastore into dataset
sample_dataset.load(redd_datastore)

print (redd_datastore)


redd_datastore.close()
