import random
import math
# importing the required module
import matplotlib.pyplot as plt
from math import sin, pi, cos
import numpy as np
from numpy import array
from CalcDistance import CalcDistance

def TP(xo1, yo1, zo1, xo2, yo2, zo2,xo3, yo3, zo3, xo4, yo4, zo4, xo5, yo5, zo5, xo6, yo6, zo6, xo7, yo7, zo7, xo8, yo8, zo8, xo9, yo9, zo9, xo10, yo10, zo10, xsef, ysef, noise, beta, P, Bw):
    #numStaticEndDevices =100
        
    outxsef=xsef
    outysef=ysef


    th = np.array(range(int(0), int(2*180), int(180/50)))
    lenl = np.array(range(0,len(outysef)))

    #print(th)

    powRange = 1.1 #1.21

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

    r5_ = pow((powRange*zo5), 2) - pow(zo5,2)
    r5 = pow(r5_, 0.5)
    xunit5 = r5 * np.array(np.cos(th)) + xo5
    yunit5 = r5 * np.array(np.sin(th)) + yo5

    r6_ = pow((powRange*zo6), 2) - pow(zo6,2)
    r6 = pow(r6_, 0.5)
    xunit6 = r6 * np.array(np.cos(th)) + xo6
    yunit6 = r6 * np.array(np.sin(th)) + yo6

    r7_ = pow((powRange*zo7), 2) - pow(zo7,2)
    r7 = pow(r7_, 0.5)
    xunit7 = r7 * np.array(np.cos(th)) + xo7
    yunit7 = r7 * np.array(np.sin(th)) + yo7

    r8_ = pow((powRange*zo8), 2) - pow(zo8,2)
    r8 = pow(r8_, 0.5)
    xunit8 = r8 * np.array(np.cos(th)) + xo8
    yunit8 = r8 * np.array(np.sin(th)) + yo8

    r9_ = pow((powRange*zo9), 2) - pow(zo9,2)
    r9 = pow(r9_, 0.5)
    xunit9 = r9 * np.array(np.cos(th)) + xo9
    yunit9 = r9 * np.array(np.sin(th)) + yo9

    r10_ = pow((powRange*zo10), 2) - pow(zo10,2)
    r10 = pow(r10_, 0.5)
    xunit10 = r10 * np.array(np.cos(th)) + xo10
    yunit10 = r10 * np.array(np.sin(th)) + yo10

        

    
    u1_assoc = 0
    u2_assoc = 0
    u3_assoc = 0
    u4_assoc = 0
    u5_assoc = 0
    u6_assoc = 0
    u7_assoc = 0
    u8_assoc = 0
    u9_assoc = 0
    u10_assoc = 0
    

    u1_assoc_con1 = 0
    u2_assoc_con1 = 0
    u3_assoc_con1 = 0
    u4_assoc_con1 = 0
    u5_assoc_con1 = 0
    u6_assoc_con1 = 0
    u7_assoc_con1 = 0
    u8_assoc_con1 = 0
    u9_assoc_con1 = 0
    u10_assoc_con1 = 0
    

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
    fac5 = count_covered(xo5, yo5, r5)
    coveragefactorstatic5 = fac5[0]
    Overlap_container5 = fac5[1]
    ##
    fac6 = count_covered(xo6, yo6, r6)
    coveragefactorstatic6 = fac6[0]
    Overlap_container6 = fac6[1]
    ##
    fac7 = count_covered(xo7, yo7, r7)
    coveragefactorstatic7 = fac7[0]
    Overlap_container7 = fac7[1]
    ##
    fac8 = count_covered(xo8, yo8, r8)
    coveragefactorstatic8 = fac8[0]
    Overlap_container8 = fac8[1]
    ##
    fac9 = count_covered(xo9, yo9, r9)
    coveragefactorstatic9 = fac9[0]
    Overlap_container9 = fac9[1]
    ##
    fac10 = count_covered(xo10, yo10, r10)
    coveragefactorstatic10 = fac10[0]
    Overlap_container10 = fac10[1]


    Cov_UAV1 = coveragefactorstatic1# -set({0})
    Cov_UAV2 = coveragefactorstatic2
    Cov_UAV3 = coveragefactorstatic3
    Cov_UAV4 = coveragefactorstatic4
    Cov_UAV5 = coveragefactorstatic5
    Cov_UAV6 = coveragefactorstatic6
    Cov_UAV7 = coveragefactorstatic7
    Cov_UAV8 = coveragefactorstatic8
    Cov_UAV9 = coveragefactorstatic9
    Cov_UAV10 = coveragefactorstatic10
    
    
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

    ### removed redundant zeros in the set
    if 0 in Overlap_container5:
        Overlap_container5.remove(0)
    else:
        Overlap_container5

    ### removed redundant zeros in the set
    if 0 in Overlap_container6:
        Overlap_container6.remove(0)
    else:
        Overlap_container6

    ### removed redundant zeros in the set
    if 0 in Overlap_container7:
        Overlap_container7.remove(0)
    else:
        Overlap_container7

    ### removed redundant zeros in the set
    if 0 in Overlap_container8:
        Overlap_container8.remove(0)
    else:
        Overlap_container8

    ### removed redundant zeros in the set
    if 0 in Overlap_container9:
        Overlap_container9.remove(0)
    else:
        Overlap_container9

    ### removed redundant zeros in the set
    if 0 in Overlap_container10:
        Overlap_container10.remove(0)
    else:
        Overlap_container10
    
    Overgroup = [Overlap_container1, Overlap_container2, Overlap_container3, Overlap_container4, Overlap_container5, Overlap_container6, Overlap_container7, Overlap_container8, Overlap_container9, Overlap_container10]

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
    dev_id5a = intersectingdevices(Overlap_container5, Overgroup)
    dev_id6a = intersectingdevices(Overlap_container6, Overgroup)
    dev_id7a = intersectingdevices(Overlap_container7, Overgroup)
    dev_id8a = intersectingdevices(Overlap_container8, Overgroup)
    dev_id9a = intersectingdevices(Overlap_container9, Overgroup)
    dev_id10a = intersectingdevices(Overlap_container10, Overgroup)
    
    #print(dev_id1)
    device_ID1 = set().union(*dev_id1a)
    device_ID2 = set().union(*dev_id2a)
    device_ID3 = set().union(*dev_id3a)
    device_ID4 = set().union(*dev_id4a)
    device_ID5 = set().union(*dev_id5a)
    device_ID6 = set().union(*dev_id6a)
    device_ID7 = set().union(*dev_id7a)
    device_ID8 = set().union(*dev_id8a)
    device_ID9 = set().union(*dev_id9a)
    device_ID10 = set().union(*dev_id10a)
    
    




    ####
    d1_over_ids = len(device_ID1)
    d2_over_ids = len(device_ID2)
    d3_over_ids = len(device_ID3)
    d4_over_ids = len(device_ID4)
    d5_over_ids = len(device_ID5)
    d6_over_ids = len(device_ID6)
    d7_over_ids = len(device_ID7)
    d8_over_ids = len(device_ID8)
    d9_over_ids = len(device_ID9)
    d10_over_ids = len(device_ID10)
    

    cov_di_1 = Overlap_container1 - device_ID1
    cov_di_2 = Overlap_container2 - device_ID2
    cov_di_3 = Overlap_container3 - device_ID3
    cov_di_4 = Overlap_container4 - device_ID4
    cov_di_5 = Overlap_container5 - device_ID5
    cov_di_6 = Overlap_container6 - device_ID6
    cov_di_7 = Overlap_container7 - device_ID7
    cov_di_8 = Overlap_container8 - device_ID8
    cov_di_9 = Overlap_container9 - device_ID9
    cov_di_10 = Overlap_container10 - device_ID10
    
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
    covScr_without_inter_u5 = len(cov_di_5)
    covScr_without_inter_u6 = len(cov_di_6)
    covScr_without_inter_u7 = len(cov_di_7)
    covScr_without_inter_u8 = len(cov_di_8)
    covScr_without_inter_u9 = len(cov_di_9)
    covScr_without_inter_u10 = len(cov_di_10)
    

    ##########################
    ### Create the list of sets
    #lst = [{1, 2, 3}, {1, 4}, {2, 3, 5}]

    ### One-Liner to union a list of sets
    #print(set().union(*lst))
    ###########################

    totdev_lst = [device_ID1, device_ID2, device_ID3, device_ID4, device_ID5, device_ID6, device_ID7, device_ID8, device_ID9, device_ID10]
    
    ###tot_deviceID =   set.union(device_ID8, set.union(device_ID7, set.union(device_ID6, set.union(device_ID5, set.union(device_ID4, set.union(device_ID3, set.union(device_ID1, device_ID2)))))))

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
    connected_overlap_u5 = []
    connected_overlap_u6 = []
    connected_overlap_u7 = []
    connected_overlap_u8 = []
    connected_overlap_u9 = []
    connected_overlap_u10 = []
    

    devg = np.array(range(0,len(tot_deviceID)))

    ###for assoc_i in tot_deviceID:
    for assoc_i in devg:
        
         rss_dist1 = CalcDistance(xo1, yo1, zo1, xsef[assoc_i], ysef[assoc_i], 0)
         rss_dist2 = CalcDistance(xo2, yo2, zo3, xsef[assoc_i], ysef[assoc_i], 0)
         rss_dist3 = CalcDistance(xo3, yo3, zo3, xsef[assoc_i], ysef[assoc_i], 0)
         rss_dist4 = CalcDistance(xo4, yo4, zo4, xsef[assoc_i], ysef[assoc_i], 0)
         rss_dist5 = CalcDistance(xo5, yo5, zo5, xsef[assoc_i], ysef[assoc_i], 0)
         rss_dist6 = CalcDistance(xo6, yo6, zo6, xsef[assoc_i], ysef[assoc_i], 0)
         rss_dist7 = CalcDistance(xo7, yo7, zo7, xsef[assoc_i], ysef[assoc_i], 0)
         rss_dist8 = CalcDistance(xo8, yo8, zo8, xsef[assoc_i], ysef[assoc_i], 0)
         rss_dist9 = CalcDistance(xo9, yo9, zo9, xsef[assoc_i], ysef[assoc_i], 0)
         rss_dist10 = CalcDistance(xo10, yo10, zo10, xsef[assoc_i], ysef[assoc_i], 0)
         
         
           ########
         val = [rss_dist1, rss_dist2, rss_dist3, rss_dist4, rss_dist5, rss_dist6, rss_dist7, rss_dist8, rss_dist9, rss_dist10]

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
         elif ind[0]==4:
             connected_overlap_u5.append(tot_deviceID[assoc_i])# = [connected_overlap_u5, tot_deviceID[assoc_i]]
         elif ind[0]==5:
             connected_overlap_u6.append(tot_deviceID[assoc_i])# = [connected_overlap_u6, tot_deviceID[assoc_i]]
         elif ind[0]==6:
             connected_overlap_u7.append(tot_deviceID[assoc_i])# = [connected_overlap_u7, tot_deviceID[assoc_i]]
         elif ind[0]==7:
             connected_overlap_u8.append(tot_deviceID[assoc_i])
         elif ind[0]==8:
             connected_overlap_u9.append(tot_deviceID[assoc_i])
         elif ind[0]==9:
             connected_overlap_u10.append(tot_deviceID[assoc_i])
                 
    
    connections_uav1 = set.union(cov_di_1, connected_overlap_u1) 
    connections_uav2 = set.union(cov_di_2, connected_overlap_u2)
    connections_uav3 = set.union(cov_di_3, connected_overlap_u3)
    connections_uav4 = set.union(cov_di_4, connected_overlap_u4)
    connections_uav5 = set.union(cov_di_5, connected_overlap_u5)
    connections_uav6 = set.union(cov_di_6, connected_overlap_u6)
    connections_uav7 = set.union(cov_di_7, connected_overlap_u7)
    connections_uav8 = set.union(cov_di_8, connected_overlap_u8)
    connections_uav9 = set.union(cov_di_9, connected_overlap_u9)
    connections_uav10 = set.union(cov_di_10, connected_overlap_u10)
    

    ################
    m1 = list(connections_uav1)
    m2 = list(connections_uav2)
    m3 = list(connections_uav3)
    m4 = list(connections_uav4)
    m5 = list(connections_uav5)
    m6 = list(connections_uav6)
    m7 = list(connections_uav7)
    m8 = list(connections_uav8)
    m9 = list(connections_uav9)
    m10 = list(connections_uav10)
    
    #print(m1)

    connectionCount_uav1 = len(connections_uav1)
    connectionCount_uav2 = len(connections_uav2)
    connectionCount_uav3 = len(connections_uav3)
    connectionCount_uav4 = len(connections_uav4)
    connectionCount_uav5 = len(connections_uav5)
    connectionCount_uav6 = len(connections_uav6)
    connectionCount_uav7 = len(connections_uav7)
    connectionCount_uav8 = len(connections_uav8)
    connectionCount_uav9 = len(connections_uav9)
    connectionCount_uav10 = len(connections_uav10)

    dm1 = []
    dm2 = []
    dm3 = []
    dm4 = []
    dm5 = []
    dm6 = []
    dm7 = []
    dm8 = []
    dm9 = []
    dm10 = []
    

    
    

    for kk in m1:
        distm1 = CalcDistance(xo1, yo1, zo1, xsef[kk], ysef[kk], 0)
        distm1_Ia = CalcDistance(xo2, yo2, zo2, xsef[kk], ysef[kk], 0)
        distm1_Ib = CalcDistance(xo3, yo3, zo3, xsef[kk], ysef[kk], 0)
        distm1_Ic = CalcDistance(xo4, yo4, zo4, xsef[kk], ysef[kk], 0)
        distm1_Id = CalcDistance(xo5, yo5, zo5, xsef[kk], ysef[kk], 0)
        distm1_Ie = CalcDistance(xo6, yo6, zo6, xsef[kk], ysef[kk], 0)
        distm1_If = CalcDistance(xo7, yo7, zo7, xsef[kk], ysef[kk], 0)
        distm1_Ig = CalcDistance(xo8, yo8, zo8, xsef[kk], ysef[kk], 0)
        distm1_Ih = CalcDistance(xo9, yo9, zo9, xsef[kk], ysef[kk], 0) ##
        distm1_Ii = CalcDistance(xo10, yo10, zo10, xsef[kk], ysef[kk], 0)        
        sinr1 = (beta * P * pow(distm1,-2))/(beta*P*(pow(distm1_Ia, -2)+ pow(distm1_Ib, -2)+pow(distm1_Ic, -2)+pow(distm1_Id, -2)+pow(distm1_Ie, -2)+pow(distm1_If, -2)+pow(distm1_Ig, -2) + pow(distm1_Ih, -2)+pow(distm1_Ii, -2)) + noise)
        dr_new1 =  Bw*math.log(1 + sinr1)
        dm1.append(dr_new1)
    sum_dm1 = sum(dm1)
    #print(sum_dm1) 
    for kk2 in m2:
        distm2 = CalcDistance(xo2, yo2, zo2, xsef[kk2], ysef[kk2], 0)
        distm2_Ia = CalcDistance(xo1, yo1, zo1, xsef[kk2], ysef[kk2], 0)
        distm2_Ib = CalcDistance(xo3, yo3, zo3, xsef[kk2], ysef[kk2], 0)
        distm2_Ic = CalcDistance(xo4, yo4, zo4, xsef[kk2], ysef[kk2], 0)
        distm2_Id = CalcDistance(xo5, yo5, zo5, xsef[kk2], ysef[kk2], 0)
        distm2_Ie = CalcDistance(xo6, yo6, zo6, xsef[kk2], ysef[kk2], 0)
        distm2_If = CalcDistance(xo7, yo7, zo7, xsef[kk2], ysef[kk2], 0)
        distm2_Ig = CalcDistance(xo8, yo8, zo8, xsef[kk2], ysef[kk2], 0)
        distm2_Ih = CalcDistance(xo9, yo9, zo9, xsef[kk2], ysef[kk2], 0) ##
        distm2_Ii = CalcDistance(xo10, yo10, zo10, xsef[kk2], ysef[kk2], 0)
        sinr2 = (beta * P * pow(distm2,-2))/(beta*P*(pow(distm2_Ia, -2)+ pow(distm2_Ib, -2)+pow(distm2_Ic, -2)+pow(distm2_Id, -2)+pow(distm2_Ie, -2)+pow(distm2_If, -2)+pow(distm2_Ig, -2) + pow(distm2_Ih, -2)+pow(distm2_Ii, -2)) + noise)
        dr_new2 =  Bw*math.log(1 + sinr2)
        dm2.append(dr_new2)
    sum_dm2 = sum(dm2)
     
    for kk3 in m3:
        distm3 = CalcDistance(xo3, yo3, zo3, xsef[kk3], ysef[kk3], 0)
        distm3_Ia = CalcDistance(xo2, yo2, zo2, xsef[kk3], ysef[kk3], 0)
        distm3_Ib = CalcDistance(xo1, yo1, zo1, xsef[kk3], ysef[kk3], 0)
        distm3_Ic = CalcDistance(xo4, yo4, zo4, xsef[kk3], ysef[kk3], 0)
        distm3_Id = CalcDistance(xo5, yo5, zo5, xsef[kk3], ysef[kk3], 0)
        distm3_Ie = CalcDistance(xo6, yo6, zo6, xsef[kk3], ysef[kk3], 0)
        distm3_If = CalcDistance(xo7, yo7, zo7, xsef[kk3], ysef[kk3], 0)
        distm3_Ig = CalcDistance(xo8, yo8, zo8, xsef[kk3], ysef[kk3], 0)
        distm3_Ih = CalcDistance(xo9, yo9, zo9, xsef[kk3], ysef[kk3], 0) ##
        distm3_Ii = CalcDistance(xo10, yo10, zo10, xsef[kk3], ysef[kk3], 0)
        sinr3 = (beta * P * pow(distm3,-2))/(beta*P*(pow(distm3_Ia, -2)+ pow(distm3_Ib, -2)+pow(distm3_Ic, -2)+pow(distm3_Id, -2)+pow(distm3_Ie, -2)+pow(distm3_If, -2)+pow(distm3_Ig, -2) + pow(distm3_Ih, -2)+pow(distm3_Ii, -2)) + noise)
        dr_new3 =  Bw*math.log(1 + sinr3)
        dm3.append(dr_new3)
    sum_dm3 = sum(dm3)
    for kk4 in m4:
        distm4 = CalcDistance(xo4, yo4, zo4, xsef[kk4], ysef[kk4], 0)
        distm4_Ia = CalcDistance(xo2, yo2, zo2, xsef[kk4], ysef[kk4], 0)
        distm4_Ib = CalcDistance(xo3, yo3, zo3, xsef[kk4], ysef[kk4], 0)
        distm4_Ic = CalcDistance(xo1, yo1, zo1, xsef[kk4], ysef[kk4], 0)
        distm4_Id = CalcDistance(xo5, yo5, zo5, xsef[kk4], ysef[kk4], 0)
        distm4_Ie = CalcDistance(xo6, yo6, zo6, xsef[kk4], ysef[kk4], 0)
        distm4_If = CalcDistance(xo7, yo7, zo7, xsef[kk4], ysef[kk4], 0)
        distm4_Ig = CalcDistance(xo8, yo8, zo8, xsef[kk4], ysef[kk4], 0)
        distm4_Ih = CalcDistance(xo9, yo9, zo9, xsef[kk4], ysef[kk4], 0) ##
        distm4_Ii = CalcDistance(xo10, yo10, zo10, xsef[kk4], ysef[kk4], 0)
        sinr4 = (beta * P * pow(distm4,-2))/(beta*P*(pow(distm4_Ia, -2)+ pow(distm4_Ib, -2)+pow(distm4_Ic, -2)+pow(distm4_Id, -2)+pow(distm4_Ie, -2)+pow(distm4_If, -2)+pow(distm4_Ig, -2) + pow(distm4_Ih, -2)+pow(distm4_Ii, -2)) + noise)
        dr_new4 =  Bw*math.log(1 + sinr4)
        dm4.append(dr_new4)
    sum_dm4 = sum(dm4)
    for kk5 in m5:
        distm5 = CalcDistance(xo5, yo5, zo5, xsef[kk5], ysef[kk5], 0)
        distm5_Ia = CalcDistance(xo2, yo2, zo2, xsef[kk5], ysef[kk5], 0)
        distm5_Ib = CalcDistance(xo3, yo3, zo3, xsef[kk5], ysef[kk5], 0)
        distm5_Ic = CalcDistance(xo4, yo4, zo4, xsef[kk5], ysef[kk5], 0)
        distm5_Id = CalcDistance(xo1, yo1, zo1, xsef[kk5], ysef[kk5], 0)
        distm5_Ie = CalcDistance(xo6, yo6, zo6, xsef[kk5], ysef[kk5], 0)
        distm5_If = CalcDistance(xo7, yo7, zo7, xsef[kk5], ysef[kk5], 0)
        distm5_Ig = CalcDistance(xo8, yo8, zo8, xsef[kk5], ysef[kk5], 0)
        distm5_Ih = CalcDistance(xo9, yo9, zo9, xsef[kk5], ysef[kk5], 0) ##
        distm5_Ii = CalcDistance(xo10, yo10, zo10, xsef[kk5], ysef[kk5], 0)
        sinr5 = (beta * P * pow(distm5,-2))/(beta*P*(pow(distm5_Ia, -2)+ pow(distm5_Ib, -2)+pow(distm5_Ic, -2)+pow(distm5_Id, -2)+pow(distm5_Ie, -2)+pow(distm5_If, -2)+pow(distm5_Ig, -2)+ pow(distm5_Ih, -2)+pow(distm5_Ii, -2)) + noise)
        dr_new5 =  Bw*math.log(1 + sinr5)
        dm5.append(dr_new5)
    sum_dm5 = sum(dm5)
    for kk6 in m6:
        distm6 = CalcDistance(xo6, yo6, zo6, xsef[kk6], ysef[kk6], 0)
        distm6_Ia = CalcDistance(xo2, yo2, zo2, xsef[kk6], ysef[kk6], 0)
        distm6_Ib = CalcDistance(xo3, yo3, zo3, xsef[kk6], ysef[kk6], 0)
        distm6_Ic = CalcDistance(xo4, yo4, zo4, xsef[kk6], ysef[kk6], 0)
        distm6_Id = CalcDistance(xo5, yo5, zo5, xsef[kk6], ysef[kk6], 0)
        distm6_Ie = CalcDistance(xo1, yo1, zo1, xsef[kk6], ysef[kk6], 0)
        distm6_If = CalcDistance(xo7, yo7, zo7, xsef[kk6], ysef[kk6], 0)
        distm6_Ig = CalcDistance(xo8, yo8, zo8, xsef[kk6], ysef[kk6], 0)
        distm6_Ih = CalcDistance(xo9, yo9, zo9, xsef[kk6], ysef[kk6], 0) ##
        distm6_Ii = CalcDistance(xo10, yo10, zo10, xsef[kk6], ysef[kk6], 0)        
        sinr6 = (beta * P * pow(distm6,-2))/(beta*P*(pow(distm6_Ia, -2)+ pow(distm6_Ib, -2)+pow(distm6_Ic, -2)+pow(distm6_Id, -2)+pow(distm6_Ie, -2)+pow(distm6_If, -2)+pow(distm6_Ig, -2)+ pow(distm6_Ih, -2)+pow(distm6_Ii, -2)) + noise)
        dr_new6 =  Bw*math.log(1 + sinr6)
        dm6.append(dr_new6)
    sum_dm6 = sum(dm1)
    for kk7 in m7:
        distm7 = CalcDistance(xo7, yo7, zo7, xsef[kk7], ysef[kk7], 0)
        distm7_Ia = CalcDistance(xo2, yo2, zo2, xsef[kk7], ysef[kk7], 0)
        distm7_Ib = CalcDistance(xo3, yo3, zo3, xsef[kk7], ysef[kk7], 0)
        distm7_Ic = CalcDistance(xo4, yo4, zo4, xsef[kk7], ysef[kk7], 0)
        distm7_Id = CalcDistance(xo5, yo5, zo5, xsef[kk7], ysef[kk7], 0)
        distm7_Ie = CalcDistance(xo6, yo6, zo6, xsef[kk7], ysef[kk7], 0)
        distm7_If = CalcDistance(xo1, yo1, zo1, xsef[kk7], ysef[kk7], 0)
        distm7_Ig = CalcDistance(xo8, yo8, zo8, xsef[kk7], ysef[kk7], 0)
        distm7_Ih = CalcDistance(xo9, yo9, zo9, xsef[kk7], ysef[kk7], 0) ##
        distm7_Ii = CalcDistance(xo10, yo10, zo10, xsef[kk7], ysef[kk7], 0)
        sinr7 = (beta * P * pow(distm7,-2))/(beta*P*(pow(distm7_Ia, -2)+ pow(distm7_Ib, -2)+pow(distm7_Ic, -2)+pow(distm7_Id, -2)+pow(distm7_Ie, -2)+pow(distm7_If, -2)+pow(distm7_Ig, -2)+ pow(distm7_Ih, -2)+pow(distm7_Ii, -2)) + noise)
        dr_new7 =  Bw*math.log(1 + sinr7)
        dm7.append(dr_new7)
    sum_dm7 = sum(dm7)
    for kk8 in m8:
        distm8 = CalcDistance(xo8, yo8, zo8, xsef[kk8], ysef[kk8], 0)
        distm8_Ia = CalcDistance(xo2, yo2, zo2, xsef[kk8], ysef[kk8], 0)
        distm8_Ib = CalcDistance(xo3, yo3, zo3, xsef[kk8], ysef[kk8], 0)
        distm8_Ic = CalcDistance(xo4, yo4, zo4, xsef[kk8], ysef[kk8], 0)
        distm8_Id = CalcDistance(xo5, yo5, zo5, xsef[kk8], ysef[kk8], 0)
        distm8_Ie = CalcDistance(xo6, yo6, zo6, xsef[kk8], ysef[kk8], 0)
        distm8_If = CalcDistance(xo7, yo7, zo7, xsef[kk8], ysef[kk8], 0)
        distm8_Ig = CalcDistance(xo1, yo1, zo1, xsef[kk8], ysef[kk8], 0)
        distm8_Ih = CalcDistance(xo9, yo9, zo9, xsef[kk8], ysef[kk8], 0) ##
        distm8_Ii = CalcDistance(xo10, yo10, zo10, xsef[kk8], ysef[kk8], 0)
        sinr8 = (beta * P * pow(distm8,-2))/(beta*P*(pow(distm8_Ia, -2)+ pow(distm8_Ib, -2)+pow(distm8_Ic, -2)+pow(distm8_Id, -2)+pow(distm8_Ie, -2)+pow(distm8_If, -2)+pow(distm8_Ig, -2)+ pow(distm8_Ih, -2)+pow(distm8_Ii, -2)) + noise)
        dr_new8 =  Bw*math.log(1 + sinr8)
        dm8.append(dr_new8)
    sum_dm8 = sum(dm8)
    for kk9 in m9:
        distm9 = CalcDistance(xo9, yo9, zo9, xsef[kk9], ysef[kk9], 0)
        distm9_Ia = CalcDistance(xo2, yo2, zo2, xsef[kk9], ysef[kk9], 0)
        distm9_Ib = CalcDistance(xo3, yo3, zo3, xsef[kk9], ysef[kk9], 0)
        distm9_Ic = CalcDistance(xo4, yo4, zo4, xsef[kk9], ysef[kk9], 0)
        distm9_Id = CalcDistance(xo5, yo5, zo5, xsef[kk9], ysef[kk9], 0)
        distm9_Ie = CalcDistance(xo6, yo6, zo6, xsef[kk9], ysef[kk9], 0)
        distm9_If = CalcDistance(xo7, yo7, zo7, xsef[kk9], ysef[kk9], 0)
        distm9_Ig = CalcDistance(xo1, yo1, zo1, xsef[kk9], ysef[kk9], 0)
        distm9_Ih = CalcDistance(xo8, yo8, zo8, xsef[kk9], ysef[kk9], 0) ##
        distm9_Ii = CalcDistance(xo10, yo10, zo10, xsef[kk9], ysef[kk9], 0)
        sinr9 = (beta * P * pow(distm9,-2))/(beta*P*(pow(distm9_Ia, -2)+ pow(distm9_Ib, -2)+pow(distm9_Ic, -2)+pow(distm9_Id, -2)+pow(distm9_Ie, -2)+pow(distm9_If, -2)+pow(distm9_Ig, -2)+ pow(distm9_Ih, -2)+pow(distm9_Ii, -2)) + noise)
        dr_new9 =  Bw*math.log(1 + sinr9)
        dm9.append(dr_new9)
    sum_dm9 = sum(dm9)
    for kk10 in m10:
        distm10 = CalcDistance(xo10, yo10, zo10, xsef[kk10], ysef[kk10], 0)
        distm10_Ia = CalcDistance(xo2, yo2, zo2, xsef[kk10], ysef[kk10], 0)
        distm10_Ib = CalcDistance(xo3, yo3, zo3, xsef[kk10], ysef[kk10], 0)
        distm10_Ic = CalcDistance(xo4, yo4, zo4, xsef[kk10], ysef[kk10], 0)
        distm10_Id = CalcDistance(xo5, yo5, zo5, xsef[kk10], ysef[kk10], 0)
        distm10_Ie = CalcDistance(xo6, yo6, zo6, xsef[kk10], ysef[kk10], 0)
        distm10_If = CalcDistance(xo7, yo7, zo7, xsef[kk10], ysef[kk10], 0)
        distm10_Ig = CalcDistance(xo1, yo1, zo1, xsef[kk10], ysef[kk10], 0)
        distm10_Ih = CalcDistance(xo9, yo9, zo9, xsef[kk10], ysef[kk10], 0) ##
        distm10_Ii = CalcDistance(xo8, yo8, zo8, xsef[kk10], ysef[kk10], 0)
        sinr10 = (beta * P * pow(distm10,-2))/(beta*P*(pow(distm10_Ia, -2)+ pow(distm10_Ib, -2)+pow(distm10_Ic, -2)+pow(distm10_Id, -2)+pow(distm10_Ie, -2)+pow(distm10_If, -2)+pow(distm10_Ig, -2)+ pow(distm10_Ih, -2)+pow(distm10_Ii, -2)) + noise)
        dr_new10 =  Bw*math.log(1 + sinr10)
        dm10.append(dr_new10)
    sum_dm10 = sum(dm10)    
        

    
    
    
    return [sum_dm1, sum_dm2, sum_dm3, sum_dm4, sum_dm5, sum_dm6, sum_dm7, sum_dm8, sum_dm9, sum_dm10]

    
