__author__ = "Florian Thiery"
__copyright__ = "MIT Licence 2019, Research Squirrel Engineers, Florian Thiery"
__credits__ = ["Florian Thiery", "Research Squirrel Engineers"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Florian Thiery"
__email__ = "rse@fthiery.de"
__status__ = "draft"

# import dependencies
import uuid
import pandas as pd
import os
import codecs
import datetime

# set paths
dir_path = os.path.dirname(os.path.realpath(__file__))
file_in = dir_path + "\\" + "Finds_VesselTypes.csv"
file_out = dir_path + "\\" + "vesseltypes.ttl"

# read csv file
data = pd.read_csv(
    file_in, # relative python path to subdirectory
    encoding='utf-8',
    sep=',', # deliminiter
    quotechar="'",  # single quote allowed as quote character
    #dtype={"period_counter": int, "period_before": int, "period_after": int}, # parse as an integer
    usecols=['vesselShape', 'vesselName', 'vesselFunction', 'vesselDescription'], # only load the  columns specified
    skiprows=0, # skip X rows of the file
    na_values=['.', '??'] # take any '.' or '??' values as NA
)

# create triples from dataframe
outStr = ""
i = 0
lines = []
for index, row in data.iterrows():
    lines.append("vesseltype:vesseltype" + str(row['vesselShape']) + " " + "rdf:type" + " atlantgis:VesselType .")
    lines.append("vesseltype:vesseltype" + str(row['vesselShape']) + " " + "rdfs:label" + " " + "'" + row['vesselName'] + "'@de" + ".")
    lines.append("vesseltype:vesseltype" + str(row['vesselShape']) + " " + "atlantgis:function" + " " + "vesselfunc:vesselfunc_"+row['vesselFunction']+ " .")
    lines.append("vesselfunc:vesselfunc_"+row['vesselFunction']+ " " + "rdf:type" + " " + "atlantgis:VesselFunction .")
    lines.append("vesselfunc:vesselfunc_"+row['vesselFunction']+ " " + "rdfs:label" + " " + "'" +row['vesselFunction'] +"'@de .")
    lines.append("vesseltype:vesseltype" + str(row['vesselShape']) + " " + "skos:definition" + " " + "'" + row['vesselDescription'] + "'@de" + ".")
    lines.append("")
    i += 1

# write output file
file = codecs.open(file_out, "w", "utf-8")
prefixes = []
prefixes.append("PREFIX atlantgis: <http://atlantgis.squirrel.link/ontology#>")
prefixes.append("PREFIX vesseltype: <http://atlantgis.squirrel.link/data/vesseltype/>")
prefixes.append("PREFIX vesselfunc: <http://atlantgis.squirrel.link/data/vesselfunction/>")
prefixes.append("PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>")
prefixes.append("PREFIX owl: <http://www.w3.org/2002/07/owl#>")
prefixes.append("PREFIX skos: <http://www.w3.org/2004/02/skos/core#>")
prefixes.append("PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>")
prefixes.append("PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>")
prefixes.append("")
file.write("# create triples from" + "\r\n")
file.write("# " + file_in + "\r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n")
file.write("# by python script" + "\r\n\r\n")
for prefix in prefixes:
    file.write(prefix)
    file.write("\r\n")
for line in lines:
    file.write(line)
    file.write("\r\n")
file.close()
