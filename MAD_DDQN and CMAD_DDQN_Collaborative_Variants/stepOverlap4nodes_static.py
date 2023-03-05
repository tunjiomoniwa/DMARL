import random
import math
# importing the required module
import matplotlib.pyplot as plt
from math import sin, pi, cos
import numpy as np
from numpy import array
from CalcDistance import CalcDistance

def stepOverlap4nodes_static(xo1, yo1, zo1, xo2, yo2, zo2,xo3, yo3, zo3, xo4, yo4, zo4, xsef, ysef):
    #numStaticEndDevices =100
        
    outxsef=xsef
    outysef=ysef


    th = np.array(range(int(0), int(2*180), int(180/50)))
    lenl = np.array(range(0,len(outysef)))

    #print(th)

    powRange = 1.21

    r1_ = pow((powRange*zo1), 2) - pow(zo1,2)
    r1 = pow(r1_, 0.5)
    tl = np.cos(th)

    #print(tl)
    xunit1 = r1* np.array(np.cos(th)) + xo1
    yunit1 = r1* np.array(np.sin(th)) + yo1
    #print(xunit1)


    r2_ = pow((powRange*zo2), 2) - pow(zo2,2)
    r2 = pow(r2_, 0.5)
    xunit2 = r2 * np.array(np.cos(th)) + xo2
    yunit2 = r2 * np.array(np.sin(th)) + yo2


    r3_ = pow((powRange*zo3), 2) - pow(zo3,2)
    r3 = pow(r3_, 0.5)
    xunit3 = r3 * np.array(np.cos(th)) + xo3
    yunit3 = r3 * np.array(np.sin(th)) + yo3


    r4_ = pow((powRange*zo4), 2) - pow(zo4,2)
    r4 = pow(r4_, 0.5)
    xunit4 = r4 * np.array(np.cos(th)) + xo4
    yunit4 = r4 * np.array(np.sin(th)) + yo4

    
      

    
    u1_assoc = 0
    u2_assoc = 0
    u3_assoc = 0
    u4_assoc = 0
    
    

    u1_assoc_con1 = 0
    u2_assoc_con1 = 0
    u3_assoc_con1 = 0
    u4_assoc_con1 = 0
    
    

    def count_covered(xp1, yp1, r):
        Overlap_container = set()   
        coveragefactorstatic = 0
        in_dev =0
        for kstaticdev in lenl:# # to count the number of end-device covered by UAV
            if pow((xsef[kstaticdev]-xp1), 2) + pow((ysef[kstaticdev]-yp1),2) <= pow(r,2):
                    #disp('inside')
                coveragescore = 1
                in_dev = kstaticdev


            else:
                    #disp('outside')
                coveragescore = 0

            #Overlap_container1 = [Overlap_container1, in_dev1]
            Overlap_container.add(in_dev)	
            coveragefactorstatic = coveragescore + coveragefactorstatic


        ans = [coveragefactorstatic, Overlap_container]
        return ans


    fac1 = count_covered(xo1, yo1, r1)
    coveragefactorstatic1 = fac1[0]
    Overlap_container1 = fac1[1]
    ##
    fac2 = count_covered(xo2, yo2, r2)
    coveragefactorstatic2 = fac2[0]
    Overlap_container2 = fac2[1]
    ##
    fac3 = count_covered(xo3, yo3, r3)
    coveragefactorstatic3 = fac3[0]
    Overlap_container3 = fac3[1]
    ##
    fac4 = count_covered(xo4, yo4, r4)
    coveragefactorstatic4 = fac4[0]
    Overlap_container4 = fac4[1]
    ##
    
    
    


    Cov_UAV1 = coveragefactorstatic1# -set({0})
    Cov_UAV2 = coveragefactorstatic2
    Cov_UAV3 = coveragefactorstatic3
    Cov_UAV4 = coveragefactorstatic4
    
    ### removed redundant zeros in the set
    if 0 in Overlap_container1:
        Overlap_container1.remove(0)
    else:
        Overlap_container1

    ### removed redundant zeros in the set
    if 0 in Overlap_container2:
        Overlap_container2.remove(0)
    else:
        Overlap_container2

    ### removed redundant zeros in the set
    if 0 in Overlap_container3:
        Overlap_container3.remove(0)
    else:
        Overlap_container3

    ### removed redundant zeros in the set
    if 0 in Overlap_container4:
        Overlap_container4.remove(0)
    else:
        Overlap_container4
       
    

    Overgroup = [Overlap_container1, Overlap_container2, Overlap_container3, Overlap_container4]

    def intersectingdevices(devcon, Overgroup):
        dev_gp_val = []
        for gp in np.array(range(0, len(Overgroup))):
            device_gp_ID = set.intersection(devcon, Overgroup[gp])
            dev_gp_val.append(device_gp_ID)        
        return dev_gp_val

    ##########################
    ### Create the list of sets
    #lst = [{1, 2, 3}, {1, 4}, {2, 3, 5}]

    ### One-Liner to union a list of sets
    #print(set().union(*lst))
    ###########################
    dev_id1a = intersectingdevices(Overlap_container1, Overgroup)
    dev_id2a = intersectingdevices(Overlap_container2, Overgroup)
    dev_id3a = intersectingdevices(Overlap_container3, Overgroup)
    dev_id4a = intersectingdevices(Overlap_container4, Overgroup)
     
    
    
    #print(dev_id1)
    device_ID1 = set().union(*dev_id1a)
    device_ID2 = set().union(*dev_id2a)
    device_ID3 = set().union(*dev_id3a)
    device_ID4 = set().union(*dev_id4a)
     




    ####
    d1_over_ids = len(device_ID1)
    d2_over_ids = len(device_ID2)
    d3_over_ids = len(device_ID3)
    d4_over_ids = len(device_ID4)
     
    
    cov_di_1 = Overlap_container1 - device_ID1
    cov_di_2 = Overlap_container2 - device_ID2
    cov_di_3 = Overlap_container3 - device_ID3
    cov_di_4 = Overlap_container4 - device_ID4
     
    
    #print(Overlap_container1)
    #print(device_ID1)
    #print(cov_di_1)

    


    covScr_without_inter_u1 = len(cov_di_1)
    covScr_without_inter_u2 = len(cov_di_2)
    covScr_without_inter_u3 = len(cov_di_3)
    covScr_without_inter_u4 = len(cov_di_4)
     
    
    

    ##########################
    ### Create the list of sets
    #lst = [{1, 2, 3}, {1, 4}, {2, 3, 5}]

    ### One-Liner to union a list of sets
    #print(set().union(*lst))
    ###########################

    totdev_lst = [device_ID1, device_ID2, device_ID3, device_ID4]
    
    ####take note
    tot_deviceID = set().union(*totdev_lst)
    tot_deviceID = list(tot_deviceID)
    tot_deviceID = np.array(tot_deviceID)
    xsef = np.array(xsef)
    ysef = np.array(ysef)
    

        #####################
    connected_overlap_u1 = []
    connected_overlap_u2 = []
    connected_overlap_u3 = []
    connected_overlap_u4 = []
     

    devg = np.array(range(0,len(tot_deviceID)))

    ###for assoc_i in tot_deviceID:
    for assoc_i in devg:
        
         rss_dist1 = CalcDistance(xo1, yo1, zo1, xsef[assoc_i], ysef[assoc_i], 0)
         rss_dist2 = CalcDistance(xo2, yo2, zo3, xsef[assoc_i], ysef[assoc_i], 0)
         rss_dist3 = CalcDistance(xo3, yo3, zo3, xsef[assoc_i], ysef[assoc_i], 0)
         rss_dist4 = CalcDistance(xo4, yo4, zo4, xsef[assoc_i], ysef[assoc_i], 0)
          
         
           ########
         val = [rss_dist1, rss_dist2, rss_dist3, rss_dist4]

         ind = np.argsort(val)
         ###ind = [i for i, value in enumerate(val) if value == min(val)]

         ##print(ind)
         
         if ind[0]== 0:
             connected_overlap_u1.append(tot_deviceID[assoc_i])# = [connected_overlap_u1, tot_deviceID[assoc_i]]
         elif ind[0] == 1:
             connected_overlap_u2.append(tot_deviceID[assoc_i])# = [connected_overlap_u2, tot_deviceID[assoc_i]]
         elif ind[0] ==2:
             connected_overlap_u3.append(tot_deviceID[assoc_i])# = [connected_overlap_u3, tot_deviceID[assoc_i]]
         elif ind[0]==3:
             connected_overlap_u4.append(tot_deviceID[assoc_i])# = [connected_overlap_u4, tot_deviceID[assoc_i]]
          
                          
    
    connections_uav1 = set.union(cov_di_1, connected_overlap_u1) 
    connections_uav2 = set.union(cov_di_2, connected_overlap_u2)
    connections_uav3 = set.union(cov_di_3, connected_overlap_u3)
    connections_uav4 = set.union(cov_di_4, connected_overlap_u4)

    ################
    fair_index = [connections_uav1, connections_uav2, connections_uav3, connections_uav4]
    fair_set = set().union(*fair_index)
    #print(fair_set)

    fcon = []
    for fin in lenl:
        if fin in fair_set:
            fans = 1
        else:
            fans = 0 
        fcon.append(fans)
    #print(fcon)
    #print(len(fcon))
    

    connectionCount_uav1 = len(connections_uav1)
    connectionCount_uav2 = len(connections_uav2)
    connectionCount_uav3 = len(connections_uav3)
    connectionCount_uav4 = len(connections_uav4)
     
    
    return [connectionCount_uav1, connectionCount_uav2, connectionCount_uav3, connectionCount_uav4, fcon]

    
