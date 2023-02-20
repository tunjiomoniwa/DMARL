function obsUAVBL2 = stepBL2_static(action, x2, y2, z2, e2, overlap2, xo, yo, zo, xse2, yse2, xme2, yme2)
    
    numUAV = 4;
    numStaticEndDevices = 25;
    numMobileEndDevices = 25;
    
    mobilitystepMob =5; %%in m/s (5 - 11.1847mph)
    %%%for pedestrians is about 1.4 m/s, 3.13171mph
    mobilitystep = 20; 
    matxMax = [500 900 400 900 600 900];
    matxMin = [100 500 100 600 350 650];
    matyMax = [500 500 900 900 900 900];
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
            y2 = y2 + mobilitystep;
            e2 = e2 + energydrain;    
        elseif (action == 2) %means south
            y2 = y2 - mobilitystep;
            e2 = e2 + energydrain;
        elseif (action == 3) %means east
            x2 = x2 + mobilitystep;
            e2 = e2 + energydrain;
        elseif (action == 4) %means west
            x2 = x2 - mobilitystep;
            e2 = e2 + energydrain;
        elseif (action == 5) %means up
            z2 = z2 + altitudestep;
            e2 = e2 + energydrainUp;
        elseif (action == 6) %means down
            z2 = z2 - altitudestep;
            e2 = e2 + energydrainDown;
        else %static
            z2 = z2; 
            e2 = e2 + energyfactorstatichover;
        end
        energy2 = e2;
       %stepUAV1 = [[x1,y1,z1], energy1];
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       if (x2 > matxMax(2))
            % It's past the right edge
            distanceBeyond = abs(x2 - matxMax(2));
            % Walk in the x direction.
            x2 = matxMax(2) - distanceBeyond;
        elseif (x2 < matxMin(2))
            % It's past the left edge
            distanceBeyond = abs(matxMin(2) - x2);
            % Walk in the x direction.
            x2 = matxMin(2) + distanceBeyond;
        else
            x2 = x2;
        end

        if (y2 > matyMax(2))
            % It's past the right edge
            distanceBeyond = abs(y2 - matyMax(2));
            % Walk in the x direction.
            y2 = matyMax(2) - distanceBeyond;
        elseif y2 < matyMin(2)
            % It's past the left edge
            distanceBeyond = abs(matyMin(2) - y2);
            % Walk in the x direction.
            y2 = matyMin(2) + distanceBeyond;
        else
            y2 = y2;
        end

        %%%% check for z
        if (z2 > zMax)
            % It's past the right edge
            distanceBeyond = abs(z2 - zMax);
            % Walk in the x direction.
            z2 = zMax - distanceBeyond;
        elseif z2 < zMin
            % It's past the left edge
            distanceBeyond = abs(zMin - z2);
            % Walk in the x direction.
            z2 = zMin + distanceBeyond;
        else
            z2 = z2;
        end
        x2= abs(x2);
        y2 = abs(y2);
        z2 = abs(z2);
       
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% bound for xme
      str_xm2= [];
      str_ym2= [];
         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      for jj1 =1:numMobileEndDevices
           if (xme2(jj1) > matxmeMax(2))
                % It's past the right edge
                distancemBeyond = abs(xme2(jj1) - matxmeMax(2));
                % Walk in the x direction.
                xme2(jj1) = matxmeMax(2) - distancemBeyond;
            elseif (xme2(jj1) < matxmeMin(2))
                % It's past the left edge
                distancemBeyond = abs(matxmeMin(2) - xme2(jj1));
                % Walk in the x direction.
                xme2(jj1) = matxmeMin(2) + distancemBeyond;
            else
                xme2(jj1) = xme2(jj1);
            end

            if (yme2(jj1) > matymeMax(2))
                % It's past the right edge
                distancemBeyond = abs(yme2(jj1) - matymeMax(2));
                % Walk in the x direction.
                yme2(jj1) = matymeMax(2) - distancemBeyond;
            elseif yme2(jj1) < matymeMin(2)
                % It's past the left edge
                distancemBeyond = abs(matymeMin(2) - yme2(jj1));
                % Walk in the x direction.
                yme2(jj1) = matymeMin(2) + distancemBeyond;
            else
                yme2(jj1) = yme2(jj1);
            end

            xme2(jj1)= abs(xme2(jj1));
            yme2(jj1) = abs(yme2(jj1));
            
            str_xm2= [str_xm2 xme2(jj1)];
            str_ym2= [str_ym2 yme2(jj1)];
      end
       xme2= str_xm2;
       yme2= str_ym2;
       
        
       
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       th = 0:pi/50:2*pi;
       %r1 = sqrt((2.11*z1).^2 - z1.^2);
       r2 = sqrt((1.21*z2).^2 - z2.^2);
       xunit2 = r2 .* cos(th) + x2;
       yunit2 = r2 .* sin(th) + y2;
       
       
       geog_area2 = ((22/7)*r2.^2)/1000000; %%%units in sq. km
       
       ff=0;
        if ff ==0
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Randomly
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% distributed%%%%%
            
%             rng('default')
%             % static end devices
%             %r = (b-a).*rand(1000,1) + a;
%             xse2 = abs(460*rand(1,numStaticEndDevices)) + 520; %x-coordinate of a point
%             yse2 = abs(460*rand(1,numStaticEndDevices)) + 20; %y-coordinate of a point
%             rng shuffle
            % mobile end devices
             
            % mobile end devices
%             xme1 = abs(500*rand(1,numMobileEndDevices)); %x-coordinate of a point
%             yme1 = abs(500*rand(1,numMobileEndDevices)); %y-coordinate of a point

            act_str_x2 = [];
            act_str_y2 = [];
            test= [];
            for tj = 1:numMobileEndDevices
                test2(tj) =  randi([1 5]);
                test= [test test2(tj)];
            end
            test;
            for j =1:numMobileEndDevices

                %test(j) =  randi([1 5]);

                if (test(j) == 1)
                    move2 ='N';
                    yme2(j) =yme2(j)+mobilitystepMob;
                elseif (test(j) == 2)
                    move2 = 'S';
                    yme2(j)=yme2(j)-mobilitystepMob;
                elseif (test(j) == 3)
                    move2 ='E';
                    xme2(j)=xme2(j)+mobilitystepMob;
                elseif (test(j) == 4)
                    move2 ='W';
                    xme2(j)=xme2(j)-mobilitystepMob;
                elseif (test(j) == 5)
                    move2 ='St';
                    xme2(j)=xme2(j);
                    yme2(j)=yme2(j);        
                end
                act_str_x2 = [act_str_x2, xme2(j)];
                act_str_y2 = [ act_str_y2, yme2(j)];
            end
            xme2 = act_str_x2;
            yme2 = act_str_y2;


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
        
       coveragefactorstatic2 = 0;
       for kstaticdev = 1: numStaticEndDevices % to count the number of end-device covered by UAV
               if (xse2(kstaticdev)-x2)^2 + (yse2(kstaticdev)-y2)^2 < r2^2
                    %disp('inside');
                    coveragescore2 = 1;
               elseif (xse2(kstaticdev)-x2)^2 + (yse2(kstaticdev)-y2)^2  == r2^2
                     %disp('on line');
                     coveragescore2 = 1;
               elseif (xse2(kstaticdev)-x2)^2 + (yse2(kstaticdev)-y2)^2 > r2^2
                         %disp('outside');
                         coveragescore2 = 0;
                    
               end
               coveragefactorstatic2 = coveragescore2 + coveragefactorstatic2;
       end
       %%%%%%%%%%%%%%%%%%%%%%%%%%
       
        
        coveragescore = 0; %initialize
        coveragefactormobile =0;
%         for uavdev = 1: numUAV
%            for kmobdev = 1: numMobileEndDevices % to count the number of end-device covered by UAV
%                if (xme2(kmobdev)-x2(uavdev))^2 + (yme2(kmobdev)-y2(uavdev))^2 < r2(uavdev)^2
%                     %disp('inside');
%                     coveragescorem2 = 1;
%                elseif (xme2(kmobdev)-x2(uavdev))^2 + (yme2(kmobdev)-y2(uavdev))^2  == r2(uavdev)^2
%                      %disp('on line');
%                      coveragescorem2 = 1;
%                elseif (xme2(kmobdev)-x2(uavdev))^2 + (yme2(kmobdev)-y2(uavdev))^2 > r2(uavdev)^2
%                          %disp('outside');
%                          coveragescorem2 = 0;
%                     
%                end
%                coveragefactormobile = coveragescorem2 + coveragefactormobile;
%            end
%         end
%        
%        
       %%%%%%%%%%%%%%%%%%%%%%%%%
       
       
       
       uav2distFromgoal = CalcDistance(x2, y2, z2, Xcent(2,1), Xcent(2,2), Xcent(2,3));
       
       overlap2 = logical(CalcDistance(x2, y2, z2, xo, yo, zo)<500);
       %%try to add the 3D positioning
       
       goal2 = logical(energy2 <= 300000 && z2 >= 400 && x2>=700  && x2<800  && y2>=200 && y2<300);
       
       %done1 = logical(energy1 <= 20001 && z1 >= 400 && x1>=230  && x1<280  && y1>=230 && y1<280); %border distribution
       done2 = logical(energy2 <= 300000 && z2 >= 400 && x2>=650  && x2<800  && y2>=200 && y2<300);  %random and uniform distribution
       %done1 = logical(energy1 <= 20001 && z1 >= 400 && x1>=250  && x1<350  && y1>=250 && y1<350); %clumped dist.
       dead2 = logical(energy2 > 300000); %%% I changed from  30001Joules
    
       
           %%%%%%%%%%%%%%%%%%%%%%%%%
      % obs2 = [energy2, coveragefactorstatic2, geog_area2];
       obsUAVBL2 = [[x2,y2,z2], [energy2, coveragefactorstatic2, geog_area2], done2, dead2, goal2, uav2distFromgoal, coveragefactormobile, xme2, yme2, overlap2];
       
       %plot(xse,yse,'r.')
       
end
