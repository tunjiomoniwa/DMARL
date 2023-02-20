function obsUAVBL3 = stepBL3_static(action, x3, y3, z3, e3, overlap3, xo, yo, zo, xse3, yse3, xme3, yme3)
    
    numUAV = 4;
    numStaticEndDevices = 75;
    numMobileEndDevices = 75;
    
    mobilitystepMob =5; %%in m/s (5 - 11.1847mph)
    %%%for pedestrians is about 1.4 m/s, 3.13171mph
    mobilitystep = 20; 
    matxMax = [400 900 500 900 600 900];
    matxMin = [100 600 100 600 350 650];
    matyMax = [400 400 900 900 900 900];
    matyMin = [100 100 600 600 550 550];
    zMax = 400;
    zMin = 200;
    
    matxmeMax = [500 1000 500 1000];
    matxmeMin = [0 500 0 500];
    matymeMax = [500 500 1000 1000];
    matymeMin = [0 0 500 500];
    
    
    %%% Clustering (kmeans unsupervised learning)
%     clusters = 1;
%     Xclus = [xse; yse]';
%     [idx,C] = kmeans(Xclus,clusters); %inbuilt ML toolbox fxn


    Xcent = [200 250 300; 500 250 300; 800 250 300]; 

    %%%%%%
    Utip = 120; %Tip speed of the rotor blade (m/s),
    A = 0.503;   %rotor disc area from zeng
    rho = 1.225;  %Air density in kg/m3
    s = 0.05;  %Rotor solidity, defined as the ratio of the total blade area bcR to the disc area A
    c0 = 0.02;
    ci = 0.03;
    %%%%%%%% Sppeed of drones
%     DJI Mavic Air – 42.5 mph
%     DJI Mavic Pro – 40 mph
%     DJI Phantom 4 Pro – 45 mph
    V = 20; %%%44.7387mph 
    Vh = 0; %hovering velocity which is approx 0m/s
    Vlow = 10;
    v0 = 2;
    d0 = 0.6; %Fuselage drag ratio, defined as d0
    d0n = 0.4;
    b_factor =35;
    energyfactorstatichover = b_factor* (c0*(1 + (3*Vh^2)/Utip^2) + ci*sqrt(sqrt(1 + (Vh^4)/(4*v0^4)) + (Vh^2)/(2*v0^2)) + (rho*d0*s* A*Vh^3)/2);
    %0.2; % energy to hover
    energydrain = b_factor*(c0*(1 + (3*V^2)/Utip^2) + ci*sqrt(sqrt(1 + (V^4)/(4*v0^4)) + (V^2)/(2*v0^2)) + (rho*d0n*s* A*V^3)/2);
    %2.0; %10Joules to move unit step (to insert the model)
    %%powerdrain = c0*(1 + (3*V^2)/Utip^2) + ci*sqrt(sqrt(1 + (V^4)/(4*v0^4)) + (V^2)/(2*v0^2)) + (rho*d0*s* A*V^3)/2
    energydrainUp =b_factor*(c0*(1 + (3*V^2)/Utip^2) + ci*sqrt(sqrt(1 + (V^4)/(4*v0^4)) + (V^2)/(2*v0^2)) + (rho*d0*s* A*V^3)/2);
    %3.4;
    energydrainDown = b_factor*(c0*(1 + (3*Vlow^2)/Utip^2) + ci*sqrt(sqrt(1 + (Vlow^4)/(4*v0^4)) + (Vlow^2)/(2*v0^2)) + (rho*d0*s* A*Vlow^3)/2);
    %1.0;
    dt = 1; %timeslot of 1unit(secs) of time
    altitudestep = 15;
    %%randi
    %%len_action = 7;
    %%numUAV = 6
    %%action= randi(len_action,[1 numUAV])
    %%action= randi(len_action,1)
    
        if (action == 1) %means north
            y3 = y3 + mobilitystep;
            e3 = e3 + energydrain;    
        elseif (action == 2) %means south
            y3 = y3 - mobilitystep;
            e3 = e3 + energydrain;
        elseif (action == 3) %means east
            x3 = x3 + mobilitystep;
            e3 = e3 + energydrain;
        elseif (action == 4) %means west
            x3 = x3 - mobilitystep;
            e3 = e3 + energydrain;
        elseif (action == 5) %means up
            z3 = z3 + altitudestep;
            e3 = e3 + energydrainUp;
        elseif (action == 6) %means down
            z3 = z3 - altitudestep;
            e3 = e3 + energydrainDown;
        else %static
            z3 = z3; 
            e3 = e3 + energyfactorstatichover;
        end
        energy3 = e3;
       %stepUAV1 = [[x1,y1,z1], energy1];
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       if (x3 > matxMax(3))
            % It's past the right edge
            distanceBeyond = abs(x3 - matxMax(3));
            % Walk in the x direction.
            x3 = matxMax(3) - distanceBeyond;
        elseif (x3 < matxMin(3))
            % It's past the left edge
            distanceBeyond = abs(matxMin(3) - x3);
            % Walk in the x direction.
            x3 = matxMin(3) + distanceBeyond;
        else
            x3 = x3;
        end

        if (y3 > matyMax(3))
            % It's past the right edge
            distanceBeyond = abs(y3 - matyMax(3));
            % Walk in the x direction.
            y3 = matyMax(3) - distanceBeyond;
        elseif y3 < matyMin(3)
            % It's past the left edge
            distanceBeyond = abs(matyMin(3) - y3);
            % Walk in the x direction.
            y3 = matyMin(3) + distanceBeyond;
        else
            y3 = y3;
        end

        %%%% check for z
        if (z3 > zMax)
            % It's past the right edge
            distanceBeyond = abs(z3 - zMax);
            % Walk in the x direction.
            z3 = zMax - distanceBeyond;
        elseif z3 < zMin
            % It's past the left edge
            distanceBeyond = abs(zMin - z3);
            % Walk in the x direction.
            z3 = zMin + distanceBeyond;
        else
            z3 = z3;
        end
        x3= abs(x3);
        y3 = abs(y3);
        z3 = abs(z3);
       
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% bound for xme
      str_xm3= [];
      str_ym3= [];
         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      for jj1 =1:numMobileEndDevices
           if (xme3(jj1) > matxmeMax(3))
                % It's past the right edge
                distancemBeyond = abs(xme3(jj1) - matxmeMax(3));
                % Walk in the x direction.
                xme3(jj1) = matxmeMax(3) - distancemBeyond;
            elseif (xme3(jj1) < matxmeMin(3))
                % It's past the left edge
                distancemBeyond = abs(matxmeMin(3) - xme3(jj1));
                % Walk in the x direction.
                xme3(jj1) = matxmeMin(3) + distancemBeyond;
            else
                xme3(jj1) = xme3(jj1);
            end

            if (yme3(jj1) > matymeMax(3))
                % It's past the right edge
                distancemBeyond = abs(yme3(jj1) - matymeMax(3));
                % Walk in the x direction.
                yme3(jj1) = matymeMax(3) - distancemBeyond;
            elseif yme3(jj1) < matymeMin(3)
                % It's past the left edge
                distancemBeyond = abs(matymeMin(3) - yme3(jj1));
                % Walk in the x direction.
                yme3(jj1) = matymeMin(3) + distancemBeyond;
            else
                yme3(jj1) = yme3(jj1);
            end

            xme3(jj1)= abs(xme3(jj1));
            yme3(jj1) = abs(yme3(jj1));
            
            str_xm3= [str_xm3 xme3(jj1)];
            str_ym3= [str_ym3 yme3(jj1)];
      end
       xme3= str_xm3;
       yme3= str_ym3;
       
        
       
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       th = 0:pi/50:2*pi;
       %r1 = sqrt((2.11*z1).^2 - z1.^2);
       r3 = sqrt((1.21*z3).^2 - z3.^2);
       xunit3 = r3 .* cos(th) + x3;
       yunit3 = r3 .* sin(th) + y3;
       
       
       geog_area3 = ((22/7)*r3.^2)/1000000; %%%units in sq. km
       
       ff=0;
        if ff ==0
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Randomly
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% distributed%%%%%
            
%             rng('default')
%             % static end devices
%             xse3 = abs(460*rand(1,numStaticEndDevices)) + 20; %x-coordinate of a point
%             yse3 = abs(460*rand(1,numStaticEndDevices)) + 520; %y-coordinate of a point
%             rng shuffle
            % mobile end devices
             
            % mobile end devices
%             xme1 = abs(500*rand(1,numMobileEndDevices)); %x-coordinate of a point
%             yme1 = abs(500*rand(1,numMobileEndDevices)); %y-coordinate of a point

            act_str_x3 = [];
            act_str_y3 = [];
            test= [];
            for tj = 1:numMobileEndDevices
                test3(tj) =  randi([1 5]);
                test= [test test3(tj)];
            end
            test;
            for j =1:numMobileEndDevices

                %test(j) =  randi([1 5]);

                if (test(j) == 1)
                    move3 ='N';
                    yme3(j) =yme3(j)+mobilitystepMob;
                elseif (test(j) == 2)
                    move3 = 'S';
                    yme3(j)=yme3(j)-mobilitystepMob;
                elseif (test(j) == 3)
                    move3 ='E';
                    xme3(j)=xme3(j)+mobilitystepMob;
                elseif (test(j) == 4)
                    move3 ='W';
                    xme3(j)=xme3(j)-mobilitystepMob;
                elseif (test(j) == 5)
                    move3 ='St';
                    xme3(j)=xme3(j);
                    yme3(j)=yme3(j);        
                end
                act_str_x3 = [act_str_x3, xme3(j)];
                act_str_y3 = [ act_str_y3, yme3(j)];
            end
            xme3 = act_str_x3;
            yme3 = act_str_y3;


            %rng shuffle
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %%%%%%%%%%%%%%%%%%%%%%%%%  Uniform distribution  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%             rng('default')
%             xse = [];
%             yse = [];
%             for ik = 0:50:500
%                 for pk = 0:50:500
%                     xse_clump = ik;
%                     yse_clump = pk;
%                     xse =  [xse; xse_clump];
%                     yse =  [yse; yse_clump];
%                 end
%             end
%             xse;
%             yse;
            %%%%%%%%%%End of uniform distribution%%%%%%%%%%%%
            
%             %%%%%%%%%%%%%%%%%%%%Edge/border distributrion
%             rng('default')
%             rng('default')
%             foc_x = 20;
%             foc_y = 360;
%             focalx = [foc_x foc_x foc_y foc_y];
%             focaly = [foc_x foc_y foc_x foc_y];
% 
% 
%             xse = [];
%             yse = [];
%             for ik = 1:1:4
%                 for pk = 1:1:25
%                     randx_val = randi([1 140], 1, 25);
%                     randy_val = randi([1 140], 1, 25);
%                     xse_clump = focalx(ik) + randx_val(pk); %, 1, 10);
%                     yse_clump = focaly(ik) + randy_val(pk);%, 1, 10);
%                     xse =  [xse; xse_clump];
%                     yse =  [yse; yse_clump];
%                 end
%             end
%             xse;
%             yse;
           
            %%%%%%%%%%%%%%%%%%%%%End of border distribution %%%%%%%%%
            
            %%%%%%%%%%%%%%%%%%%  Clumped distribution %%%%%%%%%%%%%%%%%%%%%%%%%%%

%             
%             rng('default')
%             focalx = randi([80 420], 1, 10);
%             focaly = randi([80 420], 1, 10);
%             randx_val = randi([1 70], 1, 10);
%             randy_val = randi([1 70], 1, 10);
%             xse = [];
%             yse = [];
%             for ik = 1:1:10
%                 for pk = 1:1:10
%                     xse_clump = focalx(ik) + randx_val(pk); %, 1, 10);
%                     yse_clump = focaly(ik) + randy_val(pk);%, 1, 10);
%                     xse =  [xse; xse_clump];
%                     yse =  [yse; yse_clump];
%                 end
%             end
%             xse;
%             yse;
           % rng shuffle;
            %%%%%%%%%%%%%%end of clumped distribution&&&&&&&&&&&
        end
        
       coveragefactorstatic3 = 0;
%        for kstaticdev = 1: numStaticEndDevices % to count the number of end-device covered by UAV
%                if (xse3(kstaticdev)-x3)^2 + (yse3(kstaticdev)-y3)^2 < r3^2
%                     %disp('inside');
%                     coveragescore3 = 1;
%                elseif (xse3(kstaticdev)-x3)^2 + (yse3(kstaticdev)-y3)^2  == r3^2
%                      %disp('on line');
%                      coveragescore3 = 1;
%                elseif (xse3(kstaticdev)-x3)^2 + (yse3(kstaticdev)-y3)^2 > r3^2
%                          %disp('outside');
%                          coveragescore3 = 0;
%                     end
%                  
%                coveragefactorstatic3 = coveragescore3 + coveragefactorstatic3;
%        end
       %%%%%%%%%%%%%%%%%%%%%%%%%%
       
        
        coveragescore = 0; %initialize
        coveragefactormobile =0;
%         for uavdev = 1: numUAV
%            for kmobdev = 1: numMobileEndDevices % to count the number of end-device covered by UAV
%                if (xme3(kmobdev)-x3(uavdev))^2 + (yme3(kmobdev)-y3(uavdev))^2 < r3(uavdev)^2
%                     %disp('inside');
%                     coveragescorem3 = 1;
%                elseif (xme3(kmobdev)-x3(uavdev))^2 + (yme3(kmobdev)-y3(uavdev))^2  == r3(uavdev)^2
%                      %disp('on line');
%                      coveragescorem3 = 1;
%                elseif (xme3(kmobdev)-x3(uavdev))^2 + (yme3(kmobdev)-y3(uavdev))^2 > r3(uavdev)^2
%                          %disp('outside');
%                          coveragescorem3 = 0;
%                     
%                end
%                coveragefactormobile = coveragescorem3 + coveragefactormobile;
%            end
%         end
%        
       
       %%%%%%%%%%%%%%%%%%%%%%%%%
       
       
       
       uav3distFromgoal = CalcDistance(x3, y3, z3, Xcent(3,1), Xcent(3,2), Xcent(3,3));
       
       overlap3 = logical(CalcDistance(x3, y3, z3, xo, yo, zo)<500);
       %%try to add the 3D positioning
       
       goal3 = logical(energy3 <= 300000 && z3 >= 400 && x3>=200  && x3<300  && y3>=700 && y3<800);
       
       %done3 = logical(energy1 <= 20001 && z1 >= 400 && x1>=230  && x1<280  && y1>=230 && y1<280); %border distribution
       done3 = logical(energy3 <= 300000 && z3 >= 390 && x3>=200  && x3<300  && y3>=700 && y3<800);  %random and uniform distribution
       %done1 = logical(energy1 <= 20001 && z1 >= 400 && x1>=250  && x1<350  && y1>=250 && y1<350); %clumped dist.
       dead3 = logical(energy3 > 300000); %%% I changed from  30001Joules
    
       
           %%%%%%%%%%%%%%%%%%%%%%%%%
       %obs3 = [energy3, coveragefactorstatic3, geog_area3];
       obsUAVBL3 = [[x3,y3,z3], [energy3, coveragefactorstatic3, geog_area3], done3, dead3, goal3, uav3distFromgoal, coveragefactormobile, xme3, yme3, overlap3];
       
       %plot(xse,yse,'r.')
       
end
