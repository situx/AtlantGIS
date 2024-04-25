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
file_in = dir_path + "\\" + "Finds.csv"
file_out = dir_path + "\\" + "finds.ttl"

# read csv file
data = pd.read_csv(
    file_in, # relative python path to subdirectory
    encoding='utf-8',
    sep=',', # deliminiter
    quotechar="'",  # single quote allowed as quote character
    dtype={"muendungsD": float, "muendungsH": float, "minD": float, "minD_H": float, "maxD": float, "maxD_H": float, "bodenD": float, "size": int, "wall": int, "temperSize": object}, # parse as an integer
    #usecols=['site', 'feature', 'objectF', 'classF', 'sherd', 'vesselShape'], # only load the  columns specified
    skiprows=0, # skip X rows of the file
    na_values=['.', '??'] # take any '.' or '??' values as NA
)

# create triples from dataframe
outStr = ""
i = 0
lines = []
lines.append("atlantgis:sherdtype_G rdf:type atlantgis:SherdType .")
lines.append("atlantgis:sherdtype_G rdfs:label \"Gefäß\"@de .")
lines.append("atlantgis:sherdtype_G rdfs:label \"Vessel\"@en .")
lines.append("atlantgis:sherdtype_R rdf:type atlantgis:SherdType .")
lines.append("atlantgis:sherdtype_R rdfs:label \"Rand\"@de .")
lines.append("atlantgis:sherdtype_R rdfs:label \"Edge\"@en .")
lines.append("atlantgis:sherdtype_W rdf:type atlantgis:SherdType .")
lines.append("atlantgis:sherdtype_W rdfs:label \"Wall\"@en .")
lines.append("atlantgis:sherdtype_W rdfs:label \"Wand\"@de .")
lines.append("atlantgis:sherdtype_B rdf:type atlantgis:SherdType .")
lines.append("atlantgis:sherdtype_B rdfs:label \"Boden\"@de .")
lines.append("atlantgis:sherdtype_B rdfs:label \"Floor\"@en .")
for index, row in data.iterrows():
    lines.append("find:find" + str(i) + " " + "rdf:type" + " atlantgis:Find .")
    lines.append("find:find" + str(i) + " " + "rdfs:label" + "'Find " +str(i)+"'@en" + ".")
    lines.append("find:find" + str(i) + " " + "rdfs:label" + "'Fund " +str(i)+"'@de" + ".")
    lines.append("find:find" + str(i) + " " + "atlantgis:site" + " site:" + row['site'] + " .")
    lines.append("find:find" + str(i) + " " + "atlantgis:vesselShape" + " vesseltype:" + str(row['vesselShape']) + " .")
    lines.append("find:find" + str(i) + " " + "atlantgis:feature" + " " + "'" + row['feature'] + "'@en" + ".")
    lines.append("find:find" + str(i) + " " + "atlantgis:object" + " " + "'" + str(row['objectF']) + "'" + ".")
    lines.append("find:find" + str(i) + " " + "atlantgis:class" + " " + "'" + str(row['classF']) + "'" + ".")
    lines.append("find:find" + str(i) + " " + "atlantgis:sherd" + " " + "atlantgis:sherdtype_" + str(row['sherd']) + "'" + ".")
    lines.append("find:find"+str(i)+"_quantity " + "rdf:type" + " om:Quantity .")
    lines.append("find:find"+str(i)+"_quantity " + "rdfs:label " + "'Anzahl von Objekten von Fund " + str(i) + "'@de .")
    lines.append("find:find"+str(i)+"_quantity " + "rdfs:label " + "'Quantity of objects of find " + str(i) + "'@en .")
    lines.append("find:find"+str(i)+"_quantity " + "om:hasNumericalValue " + "'" + str(row['qty']) + "'^^xsd:double .")
    lines.append("find:find" + str(i) + " " + "atlantgis:weight" + " " + "find:find"+str(i)+"_weight"+ ".")
    lines.append("find:find"+str(i)+"_weight"+" " + "rdf:type" + " " + "om:Quantity .")
    lines.append("find:find"+str(i)+"_weight"+" " + "rdfs:label" + " 'Weight of Find " + str(i) + " (g)'@en .")
    lines.append("find:find"+str(i)+"_weight"+" " + "rdfs:label" + " 'Gewicht von Fund " + str(i) + " (g)'@de .")
    lines.append("find:find"+str(i)+"_weight " + "om:hasValue " + "find:find"+str(i)+"_weight_value .")
    lines.append("find:find"+str(i)+"_weight_value " + "rdf:type " + "om:Quantity .")
    lines.append("find:find"+str(i)+"_weight_value " + "rdfs:label " + "'Measurement Value of weight of find "+str(i)+"'@en .")
    lines.append("find:find"+str(i)+"_weight_value " + "rdfs:label " + "'Messwert des Gewichts von Fund "+str(i)+"'@de .")
    lines.append("find:find"+str(i)+"_weight"+"_value " + "om:hasNumericalValue" + " " "'" + str(row['wt']) + "'^^xsd:double"+" .")
    lines.append("find:find"+str(i)+"_weight"+"_value " + "om:unit" + " " "om:gram .")
    lines.append("find:" + str(i) + " " + "atlantgis:temperSize" + " " + "'" + str(row['temperSize']) + "'" + ".")
    if row['size'] != -1:
        lines.append("find:find" + str(i) + " " + "atlantgis:size" + " " + "'" + str(row['size']) + "'" + ".")
    if row['wall'] != -1:
        lines.append("find:find" + str(i) + " " + "atlantgis:wall" + " " + "find:find"+str(i)+"_wall .")
        lines.append("find:find"+str(i)+"_wall " + "rdf:type" + " om:Measure .")
        lines.append("find:find"+str(i)+"_wall " + "rdfs:label " + "'Wandungsdicke von Fund " + str(i) + " (cm)'@de .")
        lines.append("find:find"+str(i)+"_wall " + "rdfs:label " + "'Wall thickness of find " + str(i) + " (cm)'@en .")
        lines.append("find:find"+str(i)+"_wall " + "om:hasValue " + "find:find"+str(i)+"_wall_value .")
        lines.append("find:find"+str(i)+"_wall_value " + "rdf:type " + "om:Quantity .")
        lines.append("find:find"+str(i)+"_wall_value " + "rdfs:label " + "'Measurement Value of wall thickness of find "+str(i)+"'@en .")
        lines.append("find:find"+str(i)+"_wall_value " + "rdfs:label " + "'Messwert der Wandungsdicke von ´Fund "+str(i)+"'@de .")
        lines.append("find:find"+str(i)+"_wall_value " + "om:unit " + "om:centimetre .")
        lines.append("find:find"+str(i)+"_wall_value " + "om:hasNumericalValue " + "'" + str(row['wall']) + "'^^xsd:double .")
    if row['muendungsD'] != -1.0:
        lines.append("find:find" + str(i) + " " + "atlantgis:muendungsD" + " " + "find:find"+str(i)+"_muendungsD .")
        lines.append("find:find"+str(i)+"_muendungsD " + "rdf:type" + " om:Measure .")
        lines.append("find:find"+str(i)+"_muendungsD " + "rdfs:label " + "'Mündungsdurchmesser von Fund " + str(i) + " (cm)'@de .")
        lines.append("find:find"+str(i)+"_muendungsD " + "rdfs:label " + "'Orifice diameter of find " + str(i) + " (cm)'@en .")
        lines.append("find:find"+str(i)+"_muendungsD " + "om:hasValue " + "find:find"+str(i)+"_muendungsD_value .")
        lines.append("find:find"+str(i)+"_muendungsD_value " + "rdf:type " + "om:Quantity .")
        lines.append("find:find"+str(i)+"_muendungsD_value " + "rdfs:label " + "'Messwert des Mündungsdurchmessers von Fund "+str(i)+"'@de .")
        lines.append("find:find"+str(i)+"_muendungsD_value " + "rdfs:label " + "'Measurement Value of orifice diameter of find "+str(i)+"'@en .")
        lines.append("find:find"+str(i)+"_muendungsD_value " + "om:unit " + "om:centimetre .")
        lines.append("find:find"+str(i)+"_muendungsD_value " + "om:hasNumericalValue " + "'" + str(row['muendungsD']) + "'^^xsd:double .")
    if row['muendungsH'] != -1.0:
        lines.append("find:find" + str(i) + " " + "atlantgis:muendungsH" + " " + "find:find"+str(i)+"_muendungsH .")
        lines.append("find:find"+str(i)+"_muendungsH " + "rdf:type" + " om:Measure .")
        lines.append("find:find"+str(i)+"_muendungsH " + "rdfs:label " + "'Höhe des Mündungsdurchmessers von Fund " + str(i) + " (cm)'@de .")
        lines.append("find:find"+str(i)+"_muendungsH " + "rdfs:label " + "'Height of the orifice diameter of find " + str(i) + " (cm)'@en .")
        lines.append("find:find"+str(i)+"_muendungsH " + "om:hasValue " + "find:find"+str(i)+"_muendungsH_value .")
        lines.append("find:find"+str(i)+"_muendungsH_value " + "rdfs:label " + "'Messwert der Höhe des Mündungsdurchmessers von Fund " + str(i) + " (cm)'@de .")
        lines.append("find:find"+str(i)+"_muendungsH_value " + "rdfs:label " + "'Measurement Value of the height of the orifice diameter of find " + str(i) + " (cm)'@en .")
        lines.append("find:find"+str(i)+"_muendungsH_value " + "om:unit " + "om:centimetre .")
        lines.append("find:find"+str(i)+"_muendungsH_value " + "om:hasNumericalValue " + "'" + str(row['muendungsH']) + "'^^xsd:double .")
        lines.append("find:find"+str(i)+"_muendungsH_value " + "rdf:type " + "om:Quantity .")
    if row['minD'] != -1.0:
        lines.append("find:find" + str(i) + " " + "atlantgis:minD" + " " + "find:find"+str(i)+"_minD .")
        lines.append("find:find"+str(i)+"_minD " + "rdf:type" + " om:Measure .")
        lines.append("find:find"+str(i)+"_minD " + "rdfs:label " + "'Minimaler Durchmesser von Fund " + str(i) + " (cm)'@de .")
        lines.append("find:find"+str(i)+"_minD " + "rdfs:label " + "'Minimum diameter of find " + str(i) + " (cm)'@en .")
        lines.append("find:find"+str(i)+"_minD " + "om:hasValue " + "find:find"+str(i)+"_minD_value .")
        lines.append("find:find"+str(i)+"_minD_value " + "rdf:type " + "om:Quantity .")
        lines.append("find:find"+str(i)+"_minD_value " + "rdfs:label " + "'Messwert für den minimalen Durchmesser von Fund " + str(i) + " (cm)'@de .")
        lines.append("find:find"+str(i)+"_minD_value " + "rdfs:label " + "'Measurement value for the minimum diameter of find " + str(i) + " (cm)'@en .")
        lines.append("find:find"+str(i)+"_minD_value " + "om:unit " + "om:centimetre .")
        lines.append("find:find"+str(i)+"_minD_value " + "om:hasNumericalValue " + "'" + str(row['minD']) + "'^^xsd:double .")
    if row['minD_H'] != -1.0:
        lines.append("find:find" + str(i) + " " + "atlantgis:minD_H" + " " + "find:find" + str(i) + "_minD_H .")
        lines.append("find:find" + str(i) + "_minD_H " + "rdf:type" + " " + "om:Measure .")
        lines.append("find:find" + str(i) + "_minD_H " + "rdfs:label" + " " + "'Height of the minimum diameter of find " + str(i) + " (cm)'@en .")
        lines.append("find:find" + str(i) + "_minD_H " + "rdfs:label" + " " + "'Höhe des minimalen Durchmessers von Fund " + str(i) +" (cm)'@de .")
        lines.append("find:find" + str(i) + "_minD_H " + "om:hasValue " + "find:find"+str(i)+"_minD_H_value .")
        lines.append("find:find" + str(i) + "_minD_H_value " + "rdf:type" + " " + "om:Quantity .")
        lines.append("find:find" + str(i) + "_minD_H_value " + "rdfs:label" + " " + "'Measurement value of the height of the minimum diameter of find " + str(i) + "'@en .")
        lines.append("find:find" + str(i) + "_minD_H_value " + "rdfs:label" + " " + "'Messwert der Höhe des minimalen Durchmessers von Fund " + str(i) +"'@de .")
        lines.append("find:find" + str(i) + "_minD_H_value " + "om:hasNumericalValue" + " " + "'" + str(row['minD_H']) + "'^^xsd:double .")
        lines.append("find:find" + str(i) + "_minD_H_value " + "om:unit" + " om:centimetre .")
    if row['maxD'] != -1.0:
        lines.append("find:find" + str(i) + " " + "atlantgis:maxD" + " find:find"+str(i)+"_maxD .")
        lines.append("find:find"+str(i)+"_maxD " + "rdf:type" + " om:Measure .")
        lines.append("find:find"+str(i)+"_maxD " + "rdfs:label " + "'Maximaler Durchmesser von Fund " + str(i) + " (cm)'@de .")
        lines.append("find:find"+str(i)+"_maxD " + "rdfs:label " + "'Maximum diameter of find " + str(i) + " (cm)'@en .")
        lines.append("find:find" + str(i) + "_maxD " + "om:hasValue " + "find:find"+str(i)+"_maxD_value .")
        lines.append("find:find" + str(i) + "_maxD_value " + "rdf:type" + " " + "om:Quantity .")
        lines.append("find:find"+str(i)+"_maxD_value " + "rdfs:label " + "'Messwert des maximalen Durchmessers von Fund " + str(i) + "'@de .")
        lines.append("find:find"+str(i)+"_maxD_value " + "rdfs:label " + "'Measurement value of the maximum diameter of find " + str(i) + "'@en .")
        lines.append("find:find"+str(i)+"_maxD_value " + "om:unit " + "om:centimetre .")
        lines.append("find:find"+str(i)+"_maxD_value " + "om:hasNumericalValue " + "'" + str(row['maxD']) + "'^^xsd:double .")
    if row['maxD_H'] != -1.0:
        lines.append("find:find" + str(i) + " " + "atlantgis:maxD_H" + " find:find"+str(i)+"_maxD_H .")
        lines.append("find:find" + str(i) + "_maxD_H " + "rdf:type" + " " + "om:Measure .")
        lines.append("find:find" + str(i) + "_maxD_H " + "rdfs:label" + " " + "'Height of the maximum diameter of find " + str(i) + " (cm)'@en .")
        lines.append("find:find" + str(i) + "_maxD_H " + "rdfs:label" + " " + "'Höhe des maximalen Durchmessers von Fund " + str(i) +" (cm)'@de .")
        lines.append("find:find" + str(i) + "_maxD_H " + "om:hasValue " + "find:find"+str(i)+"_maxD_H_value .")
        lines.append("find:find" + str(i) + "_maxD_H_value " + "rdf:type" + " om:Quantity .")
        lines.append("find:find" + str(i) + "_maxD_H_value " + "rdfs:label" + " " + "'Measurement value of height of the maximum diameter of find " + str(i) + "'@en .")
        lines.append("find:find" + str(i) + "_maxD_H_value " + "rdfs:label" + " " + "'Messwert der Höhe des maximalen Durchmessers von Fund " + str(i) +"'@de .")
        lines.append("find:find" + str(i) + "_maxD_H_value " + "om:hasNumericalValue" + " " + "'" + str(row['maxD_H']) + "'^^xsd:double .")
        lines.append("find:find" + str(i) + "_maxD_H_value " + "om:unit" + " om:centimetre .")
    if row['bodenD'] != -1.0:
        lines.append("find:find" + str(i) + " " + "atlantgis:bodenD" + " find:find"+str(i)+"_bodenD .")
        lines.append("find:find" + str(i) + "_bodenD " + "rdf:type" + " " + "om:Measure .")
        lines.append("find:find" + str(i) + "_bodenD " + "rdfs:label" + " " + "'Bodendurchmesser von Fund " + str(i) +" (cm)'@de .")
        lines.append("find:find" + str(i) + "_bodenD " + "rdfs:label" + " " + "'Diameter of the bottom of find " + str(i) + " (cm)'@en .")
        lines.append("find:find" + str(i) + "_bodenD " + "om:hasValue " + "find:find"+str(i)+"_bodenD_value .")
        lines.append("find:find" + str(i) + "_bodenD_value " + "rdf:type" + " om:Quantity .")
        lines.append("find:find" + str(i) + "_bodenD_value " + "rdfs:label" + " " + "'Messwert für den Bodendurchmesser von Fund " + str(i) +"'@de .")
        lines.append("find:find" + str(i) + "_bodenD_value " + "rdfs:label" + " " + "'Measurement value for the diameter of the bottom of find " + str(i) + "'@en .")
        lines.append("find:find" + str(i) + "_bodenD_value " + "om:hasNumericalValue" + " " + "'" + str(row['bodenD']) + "'^^xsd:double .")
        lines.append("find:find" + str(i) + "_bodenD_value " + "om:unit" + " om:centimetre .")
    lines.append("")
    i += 1

# write output file
file = codecs.open(file_out, "w", "utf-8")
prefixes = []
prefixes.append("PREFIX atlantgis: <http://atlantgis.squirrel.link/ontology#>")
prefixes.append("PREFIX site: <http://atlantgis.squirrel.link/site#>")
prefixes.append("PREFIX find: <http://atlantgis.squirrel.link/find#>")
prefixes.append("PREFIX vesseltype: <http://atlantgis.squirrel.link/vesseltype#>")
prefixes.append("PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>")
prefixes.append("PREFIX owl: <http://www.w3.org/2002/07/owl#>")
prefixes.append("PREFIX om: <http://www.ontology-of-units-of-measure.org/resource/om-2/>")
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
