function obsUAVBL = stepBL_static(action, x1, y1, z1, e1, overlap1, xo, yo, zo, xse, yse, xme1, yme1)
    
    numUAV = 4;
    numStaticEndDevices = length(xse);
    numMobileEndDevices = length(xme1);
    
    
    
    mobilitystepMob =1.5; %%in m/s (5 - 11.1847mph) for ground users
    %%%for pedestrians is about 1.4 m/s, 3.13171mph
    mobilitystep = 20; %% for UAVs
%     matxMax = [400 600 900 250 600 900];
%     matxMin = [100 300 650 0 350 650];
%     matyMax = [400 450 450 900 900 900];
%     matyMin = [100 0 0 550 550 550];
    matxMax = [950 950 950 950 950 950];
    matxMin = [50 50 50 50 50 50];
    matyMax = [950 950 950 950 950 950];
    matyMin = [50 50 50 50 50 50];
    zMax = 400;
    zMin = 200;
    
    matxmeMax = [500 1000 500 1000];
    matxmeMin = [0 500 0 500];
    matymeMax = [500 500 1000 1000];
    matymeMin = [0 0 500 500];
    
    
   
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
    altitudestep = 20;
    
    
        if (action == 1) %means north
            y1 = y1 + mobilitystep;
            e1 = e1 + energydrain;    
        elseif (action == 2) %means south
            y1 = y1 - mobilitystep;
            e1 = e1 + energydrain;
        elseif (action == 3) %means east
            x1 = x1 + mobilitystep;
            e1 = e1 + energydrain;
        elseif (action == 4) %means west
            x1 = x1 - mobilitystep;
            e1 = e1 + energydrain;
        elseif (action == 5) %means up
            z1 = z1 + altitudestep;
            e1 = e1 + energydrainUp;
        elseif (action == 6) %means down
            z1 = z1 - altitudestep;
            e1 = e1 + energydrainDown;
        else %static
            z1 = z1; 
            e1 = e1 + energyfactorstatichover;
        end
        energy1 = e1;
       %stepUAV1 = [[x1,y1,z1], energy1];
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       if (x1 > matxMax(1))
            % It's past the right edge
            distanceBeyond = abs(x1 - matxMax(1));
            % Walk in the x direction.
            x1 = matxMax(1) - distanceBeyond;
        elseif (x1 < matxMin(1))
            % It's past the left edge
            distanceBeyond = abs(matxMin(1) - x1);
            % Walk in the x direction.
            x1 = matxMin(1) + distanceBeyond;
        else
            x1 = x1;
        end

        if (y1 > matyMax(1))
            % It's past the right edge
            distanceBeyond = abs(y1 - matyMax(1));
            % Walk in the x direction.
            y1 = matyMax(1) - distanceBeyond;
        elseif y1 < matyMin(1)
            % It's past the left edge
            distanceBeyond = abs(matyMin(1) - y1);
            % Walk in the x direction.
            y1 = matyMin(1) + distanceBeyond;
        else
            y1 = y1;
        end

        %%%% check for z
        if (z1 > zMax)
            % It's past the right edge
            distanceBeyond = abs(z1 - zMax);
            % Walk in the x direction.
            z1 = zMax - distanceBeyond;
        elseif z1 < zMin
            % It's past the left edge
            distanceBeyond = abs(zMin - z1);
            % Walk in the x direction.
            z1 = zMin + distanceBeyond;
        else
            z1 = z1;
        end
        x1= abs(x1);
        y1 = abs(y1);
        z1 = abs(z1);
       
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% bound for xme
      str_xm1= [];
      str_ym1= [];
         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      for jj1 =1:numMobileEndDevices
           if (xme1(jj1) > matxmeMax(1))
                % It's past the right edge
                distancemBeyond = abs(xme1(jj1) - matxmeMax(1));
                % Walk in the x direction.
                xme1(jj1) = matxmeMax(1) - distancemBeyond;
            elseif (xme1(jj1) < matxmeMin(1))
                % It's past the left edge
                distancemBeyond = abs(matxmeMin(1) - xme1(jj1));
                % Walk in the x direction.
                xme1(jj1) = matxmeMin(1) + distancemBeyond;
            else
                xme1(jj1) = xme1(jj1);
            end

            if (yme1(jj1) > matymeMax(1))
                % It's past the right edge
                distancemBeyond = abs(yme1(jj1) - matymeMax(1));
                % Walk in the x direction.
                yme1(jj1) = matymeMax(1) - distancemBeyond;
            elseif yme1(jj1) < matymeMin(1)
                % It's past the left edge
                distancemBeyond = abs(matymeMin(1) - yme1(jj1));
                % Walk in the x direction.
                yme1(jj1) = matymeMin(1) + distancemBeyond;
            else
                yme1(jj1) = yme1(jj1);
            end

            xme1(jj1)= abs(xme1(jj1));
            yme1(jj1) = abs(yme1(jj1));
            
            str_xm1= [str_xm1 xme1(jj1)];
            str_ym1= [str_ym1 yme1(jj1)];
      end
       xme1= str_xm1;
       yme1= str_ym1;
       
        
       
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       th = 0:pi/50:2*pi;
       %r1 = sqrt((2.11*z1).^2 - z1.^2);
       r1 = sqrt((1.21*z1).^2 - z1.^2);
       xunit1 = r1 .* cos(th) + x1;
       yunit1 = r1 .* sin(th) + y1;
       
       
       geog_area1 = ((22/7)*r1.^2)/1000000; %%%units in sq. km
       
       ff=0;
        if ff ==0
           
            act_str_x = [];
            act_str_y = [];
            test= [];
            for tj = 1:numMobileEndDevices
                test1(tj) =  randi([1 5]);
                test= [test test1(tj)];
            end
            test;
            for j =1:numMobileEndDevices

                %test(j) =  randi([1 5]);

                if (test(j) == 1)
                    move1 ='N';
                    yme1(j) =yme1(j)+mobilitystepMob;
                elseif (test(j) == 2)
                    move1 = 'S';
                    yme1(j)=yme1(j)-mobilitystepMob;
                elseif (test(j) == 3)
                    move1 ='E';
                    xme1(j)=xme1(j)+mobilitystepMob;
                elseif (test(j) == 4)
                    move1 ='W';
                    xme1(j)=xme1(j)-mobilitystepMob;
                elseif (test(j) == 5)
                    move1 ='St';
                    xme1(j)=xme1(j);
                    yme1(j)=yme1(j);        
                end
                act_str_x = [act_str_x, xme1(j)];
                act_str_y = [ act_str_y, yme1(j)];
            end
            xme1 = act_str_x;
            yme1 = act_str_y;


        end
        
       coveragefactorstatic1 = 0;

        
        coveragescore = 0; %initialize
        coveragefactormobile =0;

       
       
       
       uav1distFromgoal = CalcDistance(x1, y1, z1, Xcent(1,1), Xcent(1,2), Xcent(1,3));
       
       overlap1 = logical(CalcDistance(x1, y1, z1, xo, yo, zo)<500);
       %%try to add the 3D positioning
       
       goal1 = logical(energy1 <= 300000 && z1 >= 400);
       
       
       done1 = logical(energy1 <= 300000 && z1 >= 390);  %random and uniform distribution
       
       dead1 = logical(energy1 > 300000); %%% I changed from  30001Joules
    
       
           %%%%%%%%%%%%%%%%%%%%%%%%%
       %obs1 = [energy1, coveragefactorstatic1, geog_area1];
       obsUAVBL = [[x1,y1,z1], [energy1, coveragefactorstatic1, geog_area1], done1, dead1, goal1, uav1distFromgoal, coveragefactormobile, xme1, yme1, overlap1];
       
       %plot(xse,yse,'r.')
       
end
