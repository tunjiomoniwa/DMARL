function obsUAVoverlapStatic4 = stepOverlap_static(xo1, yo1, zo1, xo2, yo2, zo2,xo3, yo3, zo3, xo4, yo4, zo4, xsef, ysef)
    

   % numStaticEndDevices =100;
%         rng('default')
%         % static end devices
%         xse = abs(460*rand(1,numStaticEndDevices)) + 20; %x-coordinate of a point
%         xse2 = abs(460*rand(1,numStaticEndDevices)) + 520; 
%         xse3 = abs(460*rand(1,numStaticEndDevices)) + 20; 
%         xse4 = abs(460*rand(1,numStaticEndDevices)) + 520; 
%         yse = abs(460*rand(1,numStaticEndDevices)) + 20;  %y-coordinate of a point
%         yse2 = abs(460*rand(1,numStaticEndDevices)) + 20; 
%         yse3 = abs(460*rand(1,numStaticEndDevices)) + 520;
%         yse4 = abs(460*rand(1,numStaticEndDevices)) + 520;
%         rng shuffle;
    
    outxsef=xsef;
    outysef=ysef;
    %plot(outxsef, outysef, 'ro')

    len = length(xsef);
%     x1= 100;
%     y1= 300;
%     z1=300;
    th = 0:pi/50:2*pi;
    %r1 = sqrt((2.11*z1).^2 - z1.^2);
    r1 = sqrt((1.21*zo1).^2 - zo1.^2);
    xunit1 = r1 .* cos(th) + xo1;
    yunit1 = r1 .* sin(th) + yo1;

%     x2= 400;
%     y2= 350;
%     z2=400;
    th = 0:pi/50:2*pi;

    r2 = sqrt((1.21*zo2).^2 - zo2.^2);
    xunit2 = r2 .* cos(th) + xo2;
    yunit2 = r2 .* sin(th) + yo2;

%     x3= 200;
%     y3= 650;
%     z3=300;
    th = 0:pi/50:2*pi;

    r3 = sqrt((1.21*zo3).^2 - zo3.^2);
    xunit3 = r3 .* cos(th) + xo3;
    yunit3 = r3 .* sin(th) + yo3;

%     x4= 600;
%     y4= 650;
%     z4=300;
    th = 0:pi/50:2*pi;

    r4 = sqrt((1.21*zo4).^2 - zo4.^2);
    xunit4 = r4 .* cos(th) + xo4;
    yunit4 = r4 .* sin(th) + yo4;


    Overlap_container1 = [];   
    coveragefactorstatic1 = 0;
    u1_assoc = 0;
    u2_assoc = 0;
    u3_assoc = 0;
    u4_assoc = 0;

    u1_assoc_con1 = 0;
    u2_assoc_con1 = 0;
    u3_assoc_con1 = 0;
    u4_assoc_con1 = 0;
    in_dev1 =0;
    for kstaticdev1 = 1: len % to count the number of end-device covered by UAV

            if (xsef(kstaticdev1)-xo1)^2 + (ysef(kstaticdev1)-yo1)^2 <= r1^2
                %disp('inside');
                coveragescore1 = 1;
                 in_dev1 = kstaticdev1;


            else
                %disp('outside');
                coveragescore1 = 0;
             end
          Overlap_container1 = [Overlap_container1, in_dev1];      
           coveragefactorstatic1 = coveragescore1 + coveragefactorstatic1;

    end
    coveragefactorstatic1;
    Overlap_container1;



    Overlap_container2 = [];   
    coveragefactorstatic2 = 0;
    in_dev2 =0;
    for kstaticdev2 = 1: len % to count the number of end-device covered by UAV

            if (xsef(kstaticdev2)-xo2)^2 + (ysef(kstaticdev2)-yo2)^2 <= r2^2
                %disp('inside');
                coveragescore2 = 1;
                 in_dev2 = kstaticdev2;
            else
                %disp('outside');
                coveragescore2 = 0;
             end
          Overlap_container2 = [Overlap_container2, in_dev2];

           coveragefactorstatic2 = coveragescore2 + coveragefactorstatic2;
    end
    coveragefactorstatic2;
    Overlap_container2;

    Overlap_container3 = [];   
    coveragefactorstatic3 = 0;
    in_dev3 =0;
    for kstaticdev3 = 1: len % to count the number of end-device covered by UAV

            if (xsef(kstaticdev3)-xo3)^2 + (ysef(kstaticdev3)-yo3)^2 <= r3^2
                %disp('inside');
                coveragescore3 = 1;
                 in_dev3 = kstaticdev3;
            else
                %disp('outside');
                coveragescore3 = 0;
             end
          Overlap_container3 = [Overlap_container3, in_dev3];

           coveragefactorstatic3 = coveragescore3 + coveragefactorstatic3;
    end
    coveragefactorstatic3;
    Overlap_container3;

    Overlap_container4 = [];   
    coveragefactorstatic4 = 0;
    in_dev4 =0;
    for kstaticdev4 = 1: len % to count the number of end-device covered by UAV

            if (xsef(kstaticdev4)-xo4)^2 + (ysef(kstaticdev4)-yo4)^2 <= r4^2
                %disp('inside');
                coveragescore4 = 1;
                 in_dev4 = kstaticdev4;
            else
                %disp('outside');
                coveragescore4 = 0;
             end
          Overlap_container4 = [Overlap_container4, in_dev4];

           coveragefactorstatic4 = coveragescore4 + coveragefactorstatic4;
    end
    coveragefactorstatic4;
    Overlap_container4;



    Cov_UAV1 = coveragefactorstatic1;
    Cov_UAV2 = coveragefactorstatic2;
    Cov_UAV3 = coveragefactorstatic3;
    Cov_UAV4 = coveragefactorstatic4;

    device_12_ID = nonzeros(intersect(Overlap_container1, Overlap_container2));
    device_13_ID = nonzeros(intersect(Overlap_container1, Overlap_container3));
    device_14_ID = nonzeros(intersect(Overlap_container1, Overlap_container4));
    device_21_ID = nonzeros(intersect(Overlap_container2, Overlap_container1));
    device_23_ID = nonzeros(intersect(Overlap_container2, Overlap_container3));
    device_24_ID = nonzeros(intersect(Overlap_container2, Overlap_container4));
    device_31_ID = nonzeros(intersect(Overlap_container3, Overlap_container1));
    device_32_ID = nonzeros(intersect(Overlap_container3, Overlap_container2));
    device_34_ID = nonzeros(intersect(Overlap_container3, Overlap_container4));
    device_41_ID = nonzeros(intersect(Overlap_container4, Overlap_container1));
    device_42_ID = nonzeros(intersect(Overlap_container4, Overlap_container2));
    device_43_ID = nonzeros(intersect(Overlap_container4, Overlap_container3));


    device_ID1 = union(device_12_ID, union(device_13_ID, device_14_ID));
    device_ID2 = union(device_21_ID, union(device_23_ID, device_24_ID));
    device_ID3 = union(device_31_ID, union(device_32_ID, device_34_ID));
    device_ID4 = union(device_41_ID, union(device_42_ID, device_43_ID));
%%%% copy
%%%%
d1_over_ids = length(device_ID1);
d2_over_ids = length(device_ID2);
d3_over_ids = length(device_ID3);
d4_over_ids = length(device_ID4);
cov_di_1 = nonzeros(setdiff(Overlap_container1,device_ID1));
cov_di_2 = nonzeros(setdiff(Overlap_container2,device_ID2));
cov_di_3 = nonzeros(setdiff(Overlap_container3,device_ID3));
cov_di_4 = nonzeros(setdiff(Overlap_container4,device_ID4));



covScr_without_inter_u1 = length(cov_di_1);
covScr_without_inter_u2 = length(cov_di_2);
covScr_without_inter_u3 = length(cov_di_3);
covScr_without_inter_u4 = length(cov_di_4);
tot_deviceID =  union(device_ID4, union(device_ID3, union(device_ID1, device_ID2)));
finx = xsef(tot_deviceID);
finy = ysef(tot_deviceID);
    %%%%%%%%%%%%%%%%%%%%%
connected_overlap_u1 = [];
connected_overlap_u2 = [];
connected_overlap_u3 = [];
connected_overlap_u4 = [];

for assoc_i = 1: length(tot_deviceID)
     rss_dist1 = CalcDistance(xo1, yo1, zo1, finx(assoc_i), finy(assoc_i), 0);
     rss_dist2 = CalcDistance(xo2, yo2, zo3, finx(assoc_i), finy(assoc_i), 0);
     rss_dist3 = CalcDistance(xo3, yo3, zo3, finx(assoc_i), finy(assoc_i), 0);
     rss_dist4 = CalcDistance(xo4, yo4, zo4, finx(assoc_i), finy(assoc_i), 0);
     val = [rss_dist1 rss_dist2 rss_dist3 rss_dist4];
     ind = find(val == min(val));
     if ind==1
         u1_assoc = 1;
         u2_assoc = 0;
         u3_assoc = 0;
         u4_assoc = 0;
         connected_overlap_u1 = [connected_overlap_u1 tot_deviceID(assoc_i)];
     elseif ind == 2
         u1_assoc = 0;
         u2_assoc = 1;
         u3_assoc = 0;
         u4_assoc = 0;
         connected_overlap_u2 = [connected_overlap_u2 tot_deviceID(assoc_i)];
     elseif ind ==3
         u1_assoc = 0;
         u2_assoc = 0;
         u3_assoc = 1;
         u4_assoc = 0;
         connected_overlap_u3 = [connected_overlap_u3 tot_deviceID(assoc_i)];
     elseif ind==4
         u1_assoc = 0;
         u2_assoc = 0;
         u3_assoc = 0;
         u4_assoc = 1;
         connected_overlap_u4 = [connected_overlap_u4 tot_deviceID(assoc_i)];
     end
    u1_assoc_con1 = u1_assoc_con1 + u1_assoc;
   u2_assoc_con1 = u2_assoc_con1 + u2_assoc;
   u3_assoc_con1 = u3_assoc_con1 + u3_assoc;
   u4_assoc_con1 = u4_assoc_con1 + u4_assoc;
end
u1_assoc_con1;
u2_assoc_con1;
u3_assoc_con1;
u4_assoc_con1;

connected_overlap_u1;
connected_overlap_u2;
connected_overlap_u3;
connected_overlap_u4;

connections_uav1 = union(cov_di_1, connected_overlap_u1); 
connections_uav2 = union(cov_di_2, connected_overlap_u2);
connections_uav3 = union(cov_di_3, connected_overlap_u3);
connections_uav4 = union(cov_di_4, connected_overlap_u4); 

connectionCount_uav1 = length(connections_uav1);
connectionCount_uav2 = length(connections_uav2);
connectionCount_uav3 = length(connections_uav3);
connectionCount_uav4 = length(connections_uav4);
%
[covScr_without_inter_u1 covScr_without_inter_u2 covScr_without_inter_u3 covScr_without_inter_u4];
[connectionCount_uav1 connectionCount_uav2 connectionCount_uav3 connectionCount_uav4];
Overlapping = length(tot_deviceID);



obsUAVoverlapStatic4 = [connectionCount_uav1, connectionCount_uav2, connectionCount_uav3, connectionCount_uav4, Overlapping, outxsef, outysef];

