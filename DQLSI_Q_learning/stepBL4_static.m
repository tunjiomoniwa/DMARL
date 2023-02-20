function obsUAVBL4 = stepBL4_static(action, x4, y4, z4, e4, overlap4, xo, yo, zo, xse4, yse4,  xme4, yme4)
    
    numUAV = 4;
    numStaticEndDevices = 25;
    numMobileEndDevices = 25;
    
    mobilitystepMob =5; %%in m/s (5 - 11.1847mph)
    %%%for pedestrians is about 1.4 m/s, 3.13171mph
    mobilitystep = 20; 
    matxMax = [400 900 400 900 600 900];
    matxMin = [100 600 100 510 350 300];
    matyMax = [400 400 900 900 900 900];
    matyMin = [100 100 600 600 550 500];
    zMax = 400;
    zMin = 200;
    
    matxmeMax = [500 100 500 1000];
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
            y4 = y4 + mobilitystep;
            e4 = e4 + energydrain;    
        elseif (action == 2) %means south
            y4 = y4 - mobilitystep;
            e4 = e4 + energydrain;
        elseif (action == 3) %means east
            x4 = x4 + mobilitystep;
            e4 = e4 + energydrain;
        elseif (action == 4) %means west
            x4 = x4 - mobilitystep;
            e4 = e4 + energydrain;
        elseif (action == 5) %means up
            z4 = z4 + altitudestep;
            e4 = e4 + energydrainUp;
        elseif (action == 6) %means down
            z4 = z4 - altitudestep;
            e4 = e4 + energydrainDown;
        else %static
            z4 = z4; 
            e4 = e4 + energyfactorstatichover;
        end
        energy4 = e4;
       %stepUAV1 = [[x1,y1,z1], energy1];
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       if (x4 > matxMax(4))
            % It's past the right edge
            distanceBeyond = abs(x4 - matxMax(4));
            % Walk in the x direction.
            x4 = matxMax(4) - distanceBeyond;
        elseif (x4 < matxMin(4))
            % It's past the left edge
            distanceBeyond = abs(matxMin(4) - x4);
            % Walk in the x direction.
            x4 = matxMin(4) + distanceBeyond;
        else
            x4 = x4;
        end

        if (y4 > matyMax(4))
            % It's past the right edge
            distanceBeyond = abs(y4 - matyMax(4));
            % Walk in the x direction.
            y4 = matyMax(4) - distanceBeyond;
        elseif y4 < matyMin(4)
            % It's past the left edge
            distanceBeyond = abs(matyMin(4) - y4);
            % Walk in the x direction.
            y4 = matyMin(4) + distanceBeyond;
        else
            y4 = y4;
        end

        %%%% check for z
        if (z4 > zMax)
            % It's past the right edge
            distanceBeyond = abs(z4 - zMax);
            % Walk in the x direction.
            z4 = zMax - distanceBeyond;
        elseif z4 < zMin
            % It's past the left edge
            distanceBeyond = abs(zMin - z4);
            % Walk in the x direction.
            z4 = zMin + distanceBeyond;
        else
            z4 = z4;
        end
        x4= abs(x4);
        y4 = abs(y4);
        z4 = abs(z4);
       
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% bound for xme
      str_xm4= [];
      str_ym4= [];
         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      for jj1 =1:numMobileEndDevices
           if (xme4(jj1) > matxmeMax(4))
                % It's past the right edge
                distancemBeyond = abs(xme4(jj1) - matxmeMax(4));
                % Walk in the x direction.
                xme4(jj1) = matxmeMax(4) - distancemBeyond;
            elseif (xme4(jj1) < matxmeMin(4))
                % It's past the left edge
                distancemBeyond = abs(matxmeMin(4) - xme4(jj1));
                % Walk in the x direction.
                xme4(jj1) = matxmeMin(4) + distancemBeyond;
            else
                xme4(jj1) = xme4(jj1);
            end

            if (yme4(jj1) > matymeMax(4))
                % It's past the right edge
                distancemBeyond = abs(yme4(jj1) - matymeMax(4));
                % Walk in the x direction.
                yme4(jj1) = matymeMax(4) - distancemBeyond;
            elseif yme4(jj1) < matymeMin(4)
                % It's past the left edge
                distancemBeyond = abs(matymeMin(4) - yme4(jj1));
                % Walk in the x direction.
                yme4(jj1) = matymeMin(4) + distancemBeyond;
            else
                yme4(jj1) = yme4(jj1);
            end

            xme4(jj1)= abs(xme4(jj1));
            yme4(jj1) = abs(yme4(jj1));
            
            str_xm4= [str_xm4 xme4(jj1)];
            str_ym4= [str_ym4 yme4(jj1)];
      end
       xme4= str_xm4;
       yme4= str_ym4;
       
        
       
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       th = 0:pi/50:2*pi;
       %r1 = sqrt((2.11*z1).^2 - z1.^2);
       r4 = sqrt((1.21*z4).^2 - z4.^2);
       xunit4 = r4 .* cos(th) + x4;
       yunit4 = r4 .* sin(th) + y4;
       
       
       geog_area4 = ((22/7)*r4.^2)/1000000; %%%units in sq. km
       
       ff=0;
        if ff ==0
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Randomly
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% distributed%%%%%
%             %%%%%tryput
%             rng('default')
%             % static end devices
%             xse4 = abs(460*rand(1,numStaticEndDevices)) + 520; %x-coordinate of a point
%             yse4 = abs(460*rand(1,numStaticEndDevices)) + 520; %y-coordinate of a point
%             rng shuffle
            % mobile end devices
             
            % mobile end devices
%             xme1 = abs(500*rand(1,numMobileEndDevices)); %x-coordinate of a point
%             yme1 = abs(500*rand(1,numMobileEndDevices)); %y-coordinate of a point

            act_str_x4 = [];
            act_str_y4 = [];
            test= [];
            for tj = 1:numMobileEndDevices
                test4(tj) =  randi([1 5]);
                test= [test test4(tj)];
            end
            test;
            for j =1:numMobileEndDevices

                %test(j) =  randi([1 5]);

                if (test(j) == 1)
                    move4 ='N';
                    yme4(j) =yme4(j)+mobilitystepMob;
                elseif (test(j) == 2)
                    move4 = 'S';
                    yme4(j)=yme4(j)-mobilitystepMob;
                elseif (test(j) == 3)
                    move4 ='E';
                    xme4(j)=xme4(j)+mobilitystepMob;
                elseif (test(j) == 4)
                    move4 ='W';
                    xme4(j)=xme4(j)-mobilitystepMob;
                elseif (test(j) == 5)
                    move4 ='St';
                    xme4(j)=xme4(j);
                    yme4(j)=yme4(j);        
                end
                act_str_x4 = [act_str_x4, xme4(j)];
                act_str_y4 = [ act_str_y4, yme4(j)];
            end
            xme4 = act_str_x4;
            yme4 = act_str_y4;


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
        
       coveragefactorstatic4 = 0;
       for kstaticdev = 1: numStaticEndDevices % to count the number of end-device covered by UAV
               if (xse4(kstaticdev)-x4)^2 + (yse4(kstaticdev)-y4)^2 < r4^2
                    %disp('inside');
                    coveragescore4 = 1;
               elseif (xse4(kstaticdev)-x4)^2 + (yse4(kstaticdev)-y4)^2  == r4^2
                     %disp('on line');
                     coveragescore4 = 1;
               elseif (xse4(kstaticdev)-x4)^2 + (yse4(kstaticdev)-y4)^2 > r4^2
                         %disp('outside');
                         coveragescore4 = 0;
                    
               end
               coveragefactorstatic4 = coveragescore4 + coveragefactorstatic4;
       end
       %%%%%%%%%%%%%%%%%%%%%%%%%%
       
        
        coveragescore = 0; %initialize
        coveragefactormobile =0;
%         for uavdev = 1: numUAV
%            for kmobdev = 1: numMobileEndDevices % to count the number of end-device covered by UAV
%                if (xme4(kmobdev)-x4(uavdev))^2 + (yme4(kmobdev)-y4(uavdev))^2 < r4(uavdev)^2
%                     %disp('inside');
%                     coveragescorem4 = 1;
%                elseif (xme4(kmobdev)-x4(uavdev))^2 + (yme4(kmobdev)-y4(uavdev))^2  == r4(uavdev)^2
%                      %disp('on line');
%                      coveragescorem4 = 1;
%                elseif (xme4(kmobdev)-x4(uavdev))^2 + (yme4(kmobdev)-y4(uavdev))^2 > r4(uavdev)^2
%                          %disp('outside');
%                          coveragescorem4 = 0;
%                    end
%                coveragefactormobile = coveragescorem4 + coveragefactormobile;
%            end
%         end
%        
       
       %%%%%%%%%%%%%%%%%%%%%%%%%
       
       
       
       uav4distFromgoal = CalcDistance(x4, y4, z4, Xcent(3,1), Xcent(3,2), Xcent(3,3));
       
       overlap4 = logical(CalcDistance(x4, y4, z4, xo, yo, zo)<500);
       %%try to add the 3D positioning
       
       goal4 = logical(energy4 <= 300000 && z4 >= 400 && x4>=700  && x4<800  && y4>=700 && y4<800);  %random and uniform distribution
      
       done4 = logical(energy4 <= 300000 && z4 >= 400 && x4>=650  && x4<800  && y4>=700 && y4<800);  %random and uniform distribution
       dead4 = logical(energy4 > 300000); %%% I changed from  30001Joules
    
       
           %%%%%%%%%%%%%%%%%%%%%%%%%
       %obs4 = [energy4, coveragefactorstatic4, geog_area4];
       obsUAVBL4 = [[x4,y4,z4], [energy4, coveragefactorstatic4, geog_area4], done4, dead4, goal4, uav4distFromgoal, coveragefactormobile, xme4, yme4, overlap4];
       
       %plot(xse,yse,'r.')
       
end
