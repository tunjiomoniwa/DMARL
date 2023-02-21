import random
import math
# importing the required module
import matplotlib.pyplot as plt
from math import sin, pi, cos
import numpy as np
from numpy import array
from CalcDistance import CalcDistance



def TP(xo1, yo1, zo1, xo2, yo2, zo2,xo3, yo3, zo3, xo4, yo4, zo4, xsef, ysef, noise, beta, P, Bw):
    numStaticEndDevices =100
        
    outxsef=xsef
    outysef=ysef


    th = np.array(range(int(0), int(2*180), int(180/50)))
    lenl = np.array(range(0,len(outysef)))

    #print(th)

    r1_ = pow((1.21*zo1), 2) - pow(zo1,2)
    r1 = pow(r1_, 0.5)
    tl = np.cos(th)

    #print(tl)
    xunit1 = r1* np.array(np.cos(th)) + xo1
    yunit1 = r1* np.array(np.sin(th)) + yo1
    #print(xunit1)


    r2_ = pow((1.21*zo2), 2) - pow(zo2,2)
    r2 = pow(r2_, 0.5)
    xunit2 = r2 * np.array(np.cos(th)) + xo2
    yunit2 = r2 * np.array(np.sin(th)) + yo2


    r3_ = pow((1.21*zo3), 2) - pow(zo3,2)
    r3 = pow(r3_, 0.5)
    xunit3 = r3 * np.array(np.cos(th)) + xo3
    yunit3 = r3 * np.array(np.sin(th)) + yo3


    r4_ = pow((1.21*zo4), 2) - pow(zo4,2)
    r4 = pow(r4_, 0.5)
    xunit4 = r4 * np.array(np.cos(th)) + xo4
    yunit4 = r4 * np.array(np.sin(th)) + yo4

    #set1 = set(list1)
    Overlap_container1 = set()   
    coveragefactorstatic1 = 0
    u1_assoc = 0
    u2_assoc = 0
    u3_assoc = 0
    u4_assoc = 0

    u1_assoc_con1 = 0
    u2_assoc_con1 = 0
    u3_assoc_con1 = 0
    u4_assoc_con1 = 0
    in_dev1 =0
    #print(lenl)
    #print(xsef[5])
    #print((xsef(5)-xo1)^2 + (ysef(5)-yo1)^2)
    for kstaticdev1 in lenl:# # to count the number of end-device covered by UAV
        if pow((xsef[kstaticdev1]-xo1), 2) + pow((ysef[kstaticdev1]-yo1),2) <= pow(r1,2):
                #disp('inside')
            coveragescore1 = 1
            in_dev1 = kstaticdev1


        else:
                #disp('outside')
            coveragescore1 = 0

        #Overlap_container1 = [Overlap_container1, in_dev1]
        Overlap_container1.add(in_dev1)	
        coveragefactorstatic1 = coveragescore1 + coveragefactorstatic1


    coveragefactorstatic1
    Overlap_container1
    #####

    Overlap_container2 = set()   
    coveragefactorstatic2 = 0
    in_dev2 =0
    for kstaticdev2 in lenl: # to count the number of end-device covered by UAV

            if pow((xsef[kstaticdev2]-xo2),2) + pow((ysef[kstaticdev2]-yo2),2) <= pow(r2,2):
                #disp('inside')
                coveragescore2 = 1
                in_dev2 = kstaticdev2
            else:
                #disp('outside')
                coveragescore2 = 0

            #Overlap_container2 = [Overlap_container2, in_dev2]
            Overlap_container2.add(in_dev2)
            coveragefactorstatic2 = coveragescore2 + coveragefactorstatic2

    coveragefactorstatic2
    Overlap_container2

    Overlap_container3 = set()   
    coveragefactorstatic3 = 0
    in_dev3 =0
    for kstaticdev3 in lenl: # to count the number of end-device covered by UAV

            if pow((xsef[kstaticdev3]-xo3),2) + pow((ysef[kstaticdev3]-yo3),2) <= pow(r3,2):
                #disp('inside')
                coveragescore3 = 1
                in_dev3 = kstaticdev3
            else:
                #disp('outside')
                coveragescore3 = 0

            #Overlap_container3 = [Overlap_container3, in_dev3]
            Overlap_container3.add(in_dev3)

            coveragefactorstatic3 = coveragescore3 + coveragefactorstatic3

    coveragefactorstatic3
    Overlap_container3

    Overlap_container4 = set()   
    coveragefactorstatic4 = 0
    in_dev4 =0
    for kstaticdev4 in lenl: # to count the number of end-device covered by UAV

            if pow((xsef[kstaticdev4]-xo4),2) + pow((ysef[kstaticdev4]-yo4),2) <= pow(r4,2):
                #disp('inside')
                coveragescore4 = 1
                in_dev4 = kstaticdev4
            else:
                #disp('outside')
                coveragescore4 = 0

            #Overlap_container4 = [Overlap_container4, in_dev4]
            Overlap_container4.add(in_dev4)

            coveragefactorstatic4 = coveragescore4 + coveragefactorstatic4

    coveragefactorstatic4
    Overlap_container4



    Cov_UAV1 = coveragefactorstatic1# -set({0})
    Cov_UAV2 = coveragefactorstatic2
    Cov_UAV3 = coveragefactorstatic3
    Cov_UAV4 = coveragefactorstatic4

    #print(Cov_UAV1)
    #print(Cov_UAV2)
    #print(Cov_UAV3)
    #print(Cov_UAV4)

    ### removed redundant zeros in the set
    Overlap_container1.remove(0)
    Overlap_container2.remove(0)
    Overlap_container3.remove(0)
    Overlap_container4.remove(0)

    #print(len(Overlap_container1))
    #print(len(Overlap_container2))
    #print(len(Overlap_container3))
    #print(len(Overlap_container4))

    device_12_ID = set.intersection(Overlap_container1, Overlap_container2)
    device_13_ID = set.intersection(Overlap_container1, Overlap_container3)
    device_14_ID = set.intersection(Overlap_container1, Overlap_container4)
    device_21_ID = set.intersection(Overlap_container2, Overlap_container1)
    device_23_ID = set.intersection(Overlap_container2, Overlap_container3)
    device_24_ID = set.intersection(Overlap_container2, Overlap_container4)
    device_31_ID = set.intersection(Overlap_container3, Overlap_container1)
    device_32_ID = set.intersection(Overlap_container3, Overlap_container2)
    device_34_ID = set.intersection(Overlap_container3, Overlap_container4)
    device_41_ID = set.intersection(Overlap_container4, Overlap_container1)
    device_42_ID = set.intersection(Overlap_container4, Overlap_container2)
    device_43_ID = set.intersection(Overlap_container4, Overlap_container3)


    ##print(device_13_ID)

    device_ID1 = set.union(device_12_ID, set.union(device_13_ID, device_14_ID))
    device_ID2 = set.union(device_21_ID, set.union(device_23_ID, device_24_ID))
    device_ID3 = set.union(device_31_ID, set.union(device_32_ID, device_34_ID))
    device_ID4 = set.union(device_41_ID, set.union(device_42_ID, device_43_ID))
    #### copy
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

    #cov_di_1 = np.nonzero(setdiff(Overlap_container1,device_ID1))
    #cov_di_2 = np.nonzero(setdiff(Overlap_container2,device_ID2))
    #cov_di_3 = np.nonzero(setdiff(Overlap_container3,device_ID3))
    #cov_di_4 = np.nonzero(setdiff(Overlap_container4,device_ID4))



    covScr_without_inter_u1 = len(cov_di_1)
    covScr_without_inter_u2 = len(cov_di_2)
    covScr_without_inter_u3 = len(cov_di_3)
    covScr_without_inter_u4 = len(cov_di_4)
    tot_deviceID =  set.union(device_ID4, set.union(device_ID3, set.union(device_ID1, device_ID2)))

    tot_deviceID = list(tot_deviceID)
    tot_deviceID = np.array(tot_deviceID)
    xsef = np.array(xsef)
    ysef = np.array(ysef)
    
    

        #####################
    connected_overlap_u1 = []
    connected_overlap_u2 = []
    connected_overlap_u3 = []
    connected_overlap_u4 = []

    for assoc_i in tot_deviceID:

         rss_dist1 = CalcDistance(xo1, yo1, zo1, xsef[assoc_i], ysef[assoc_i], 0)
         rss_dist2 = CalcDistance(xo2, yo2, zo3, xsef[assoc_i], ysef[assoc_i], 0)
         rss_dist3 = CalcDistance(xo3, yo3, zo3, xsef[assoc_i], ysef[assoc_i], 0)
         rss_dist4 = CalcDistance(xo4, yo4, zo4, xsef[assoc_i], ysef[assoc_i], 0)
        ########
         val = [rss_dist1, rss_dist2, rss_dist3, rss_dist4]

         ind = [i for i, value in enumerate(val) if value == min(val)]

         #print(ind)
         
         if ind==0:
             u1_assoc = 1
             u2_assoc = 0
             u3_assoc = 0
             u4_assoc = 0
             connected_overlap_u1 = [connected_overlap_u1, tot_deviceID(assoc_i)]
         elif ind == 1:
             u1_assoc = 0
             u2_assoc = 1
             u3_assoc = 0
             u4_assoc = 0
             connected_overlap_u2 = [connected_overlap_u2, tot_deviceID(assoc_i)]
         elif ind ==2:
             u1_assoc = 0
             u2_assoc = 0
             u3_assoc = 1
             u4_assoc = 0
             connected_overlap_u3 = [connected_overlap_u3, tot_deviceID(assoc_i)]
         elif ind==3:
             u1_assoc = 0
             u2_assoc = 0
             u3_assoc = 0
             u4_assoc = 1
             connected_overlap_u4 = [connected_overlap_u4, tot_deviceID(assoc_i)]

    u1_assoc_con1 = u1_assoc_con1 + u1_assoc
    u2_assoc_con1 = u2_assoc_con1 + u2_assoc
    u3_assoc_con1 = u3_assoc_con1 + u3_assoc
    u4_assoc_con1 = u4_assoc_con1 + u4_assoc

    u1_assoc_con1
    u2_assoc_con1
    u3_assoc_con1
    u4_assoc_con1

    connected_overlap_u1
    connected_overlap_u2
    connected_overlap_u3
    connected_overlap_u4

    connections_uav1 = set.union(cov_di_1, connected_overlap_u1) 
    connections_uav2 = set.union(cov_di_2, connected_overlap_u2)
    connections_uav3 = set.union(cov_di_3, connected_overlap_u3)
    connections_uav4 = set.union(cov_di_4, connected_overlap_u4)

    m1 = list(connections_uav1)
    m2 = list(connections_uav2)
    m3 = list(connections_uav3)
    m4 = list(connections_uav4)
    
    #print(m1)

    connectionCount_uav1 = len(connections_uav1)
    connectionCount_uav2 = len(connections_uav2)
    connectionCount_uav3 = len(connections_uav3)
    connectionCount_uav4 = len(connections_uav4)

    dm1 = []
    dm2 = []
    dm3 = []
    dm4 = []

    
    

    for kk in m1:
        distm1 = CalcDistance(xo1, yo1, zo1, xsef[kk], ysef[kk], 0)
        distm1_Ia = CalcDistance(xo2, yo2, zo2, xsef[kk], ysef[kk], 0)
        distm1_Ib = CalcDistance(xo3, yo3, zo3, xsef[kk], ysef[kk], 0)
        distm1_Ic = CalcDistance(xo4, yo4, zo4, xsef[kk], ysef[kk], 0)
        sinr = (beta * P * pow(distm1,-2))/(beta*P*(pow(distm1_Ia, -2)+ pow(distm1_Ib, -2)+pow(distm1_Ic, -2)) + noise)
        dr_new1 =  Bw*math.log(1 + sinr)
        dm1.append(dr_new1)
    sum_dm1 = sum(dm1)
    #print(sum_dm1) 
    for kk2 in m2:
        distm2 = CalcDistance(xo2, yo2, zo2, xsef[kk2], ysef[kk2], 0)
        distm2_Ia = CalcDistance(xo1, yo1, zo1, xsef[kk], ysef[kk], 0)
        distm2_Ib = CalcDistance(xo3, yo3, zo3, xsef[kk], ysef[kk], 0)
        distm2_Ic = CalcDistance(xo4, yo4, zo4, xsef[kk], ysef[kk], 0)
        sinr2 = (beta * P * pow(distm2,-2))/(beta*P*(pow(distm2_Ia, -2)+ pow(distm2_Ib, -2)+pow(distm2_Ic, -2)) + noise)
        dr_new2 =  Bw*math.log(1 + sinr2)
        dm2.append(dr_new2)
    sum_dm2 = sum(dm2)
     
    for kk3 in m3:
        distm3 = CalcDistance(xo3, yo3, zo3, xsef[kk3], ysef[kk3], 0)
        distm3_Ia = CalcDistance(xo2, yo2, zo2, xsef[kk], ysef[kk], 0)
        distm3_Ib = CalcDistance(xo3, yo3, zo3, xsef[kk], ysef[kk], 0)
        distm3_Ic = CalcDistance(xo4, yo4, zo4, xsef[kk], ysef[kk], 0)
        sinr3 = (beta * P * pow(distm3,-2))/(beta*P*(pow(distm3_Ia, -2)+ pow(distm3_Ib, -2)+pow(distm3_Ic, -2)) + noise)
        dr_new3 =  Bw*math.log(1 + sinr3)
        dm3.append(dr_new3)
    sum_dm3 = sum(dm3)
    for kk4 in m4:
        distm4 = CalcDistance(xo4, yo4, zo4, xsef[kk4], ysef[kk4], 0)
        distm4_Ia = CalcDistance(xo2, yo2, zo2, xsef[kk], ysef[kk], 0)
        distm4_Ib = CalcDistance(xo3, yo3, zo3, xsef[kk], ysef[kk], 0)
        distm4_Ic = CalcDistance(xo4, yo4, zo4, xsef[kk], ysef[kk], 0)
        sinr4 = (beta * P * pow(distm4,-2))/(beta*P*(pow(distm4_Ia, -2)+ pow(distm4_Ib, -2)+pow(distm4_Ic, -2)) + noise)
        dr_new4 =  Bw*math.log(1 + sinr4)
        dm4.append(dr_new4)
    sum_dm4 = sum(dm4) 
        
        
    
    
    return [sum_dm1, sum_dm2, sum_dm3, sum_dm4]

   
