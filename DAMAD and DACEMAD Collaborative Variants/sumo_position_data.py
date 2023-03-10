import csv
import numpy
import re

def update_low(kk): 
        
        x= []
        y= []
        
        with open("sumo_M50_freeflow.csv",newline='') as f:
                ereader = csv.DictReader(f)                
                for row in ereader:
                    if float(row['time']) == kk:
                        x.append(float(row['xnew'])*1000)
                        y.append(float(row['ynew'])*1000)                        
        return x, y


def update_high(kk): 
        
        x= []
        y= []
        
        with open("sumo_M50_freeflow.csv",newline='') as f:
                ereader = csv.DictReader(f)                
                for row in ereader:
                        #print(type(float(row['time'])))
                        if float(row['time']) == kk:
                                x.append(float(row['xnew'])*1000)
                                y.append(float(row['ynew'])*1000)                        
        return x, y

def update_M50(kk): 
        
        x= []
        y= []
        #m50_saturation_done
        #m50_congested_done.csv
        #N7_saturation
        #N7_freeflow
        #N7_congested
        #with open("sumo_M50_freeflow.csv",newline='') as f:
        with open("N7_congested.csv",newline='') as f:
                ereader = csv.DictReader(f)                
                for row in ereader:
                        #print(type(float(row['time'])))
                        if float(row['time']) == kk:
                                x.append(float(row['xnew'])*1000)
                                y.append(float(row['ynew'])*1000)                        
        return x, y


def update_DCC_Ped(kk, file): 
        
        x= []
        y= []
        #m50_saturation_done
        #m50_congested_done.csv
        #N7_saturation
        #N7_freeflow
        #DCC_freeflow_A
        #N7_congested
        #with open("sumo_M50_freeflow.csv",newline='') as f:
        with open(file,newline='') as f:
                ereader = csv.DictReader(f)                
                for row in ereader:
                        #print(type(float(row['time'])))
                        if float(row['time']) == kk:                                 
                                x.append(float(row['xnew'])*1000)
                                y.append(float(row['ynew'])*1000)                        
        return x, y

