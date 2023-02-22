clc
clear all



deployed_veh = dlmread('deployed_vehicles_box_test.dat');
covered_veh = sum(dlmread('Covered_vehicles_box_test.dat'));
deployed_veh_dacemad = dlmread('deployed_vehicles_N7_saturation_dacemad.dat');
covered_veh_dacemad = sum(dlmread('Covered_vehicles_N7_saturation_dacemad.dat'));
deployed_veh_damad = dlmread('deployed_vehicles_N7_saturation_damad.dat');
covered_veh_damad = sum(dlmread('Covered_vehicles_N7_saturation_damad.dat'));
deployed_veh_hi = dlmread('deployed_vehicles_box_test_h.dat');
covered_veh_hi = sum(dlmread('Covered_vehicles_box_test_h.dat'));

covered_veh_mad = sum(dlmread('Covered_vehicles_N7_Saturation_cmad.dat'));
deployed_veh_mad = dlmread('deployed_vehicles_N7_Saturation_cmad.dat');
covered_veh_cmad = sum(dlmread('Covered_vehicles_N7_Saturation_mad.dat'));
deployed_veh_cmad = dlmread('deployed_vehicles_N7_Saturation_mad.dat');
epi = 1:1:length(deployed_veh);
epi_lo = 1:1:length(deployed_veh_dacemad);
epi_m = 1:1:length(deployed_veh_damad);
epi_hi = 1:1:length(deployed_veh_hi);

plotCDR = 2;

if (plotCDR == 1)
    figure;
    a1 = axes();
    percentage_cov = covered_veh./deployed_veh;
    percentage_cov_dacemad = covered_veh_dacemad./deployed_veh_dacemad;
    percentage_cov_damad = covered_veh_damad./deployed_veh_damad;
    percentage_cov_mad = covered_veh_mad./deployed_veh_mad;
    percentage_cov_cmad = covered_veh_cmad./deployed_veh_cmad;
    percentage_cov_hi = covered_veh_hi./deployed_veh_hi;
    %plot(epi_m, percentage_cov_m, 'r-', epi_lo, percentage_cov_lo, 'b-', epi_hi, percentage_cov_hi, 'g-', 'Linewidth', 1)
    plot(epi_lo, percentage_cov_dacemad, 'r-', epi_m, percentage_cov_damad, 'b-', epi_m, percentage_cov_cmad, 'k-',  epi_m, percentage_cov_mad, 'g-', 'Linewidth', 1)
     
    %plot(epi_m, percentage_cov_m, 'b-')
    set(gca, 'FontSize', 16)  
    legend('DACEMAD-DDQN', 'DAMAD-DDQN', 'CMAD-DDQN', 'MAD-DDQN', 'location', 'best');
    %legend('Mixed Traffic','Lower Traffic', 'Higher Traffic', 'location', 'best');
    xlabel('Episodes','Fontsize',16);
    ylabel('CDR','Fontsize',16);    
    axis([1 length(deployed_veh_dacemad) 0.0 1.1])    
    grid on;
%     a2 = axes();
%     a2.Position = [0.420 0.200 0.25 0.2]; 
%     %a2.Position = [0.3200 0.6600 0.2 0.2]; % xlocation, ylocation, xsize, ysize
%     plot((220:250),percentage_cov_dacemad(220:250), 'r-', (220:250), percentage_cov_damad(220:250), 'b-', (220:250), percentage_cov_cmad(220:250), 'k-', (220:250), percentage_cov_mad(220:250), 'g-', 'Linewidth', 1); axis tight
%     set(gca, 'FontSize', 10)
else
    %plot(epi_m, deployed_veh_damad, 'b-', epi_m, covered_veh_damad, 'r-', 'Linewidth', 1)
    %plot(epi_lo, deployed_veh_damad, 'b-', epi_lo, covered_veh_damad, 'r-', 'Linewidth', 1)
    plot(epi_lo, deployed_veh_cmad, 'b-', epi_lo, covered_veh_cmad, 'r-', 'Linewidth', 1)
    
    %plot(epi,covered_veh, 'r-', 'Linewidth', 1)
    set(gca, 'FontSize', 16)
    xlabel('Episodes','Fontsize',16);    
    ylabel('Vehicles','Fontsize',16);
    %CDR_DACEMAD_M50_low_traffic
    legend('Deployed (CMAD-DDQN)','Covered (CMAD-DDQN)', 'location', 'best')
    %axis([000 500 200.0 700])    
    axis([1 length(deployed_veh) 0 120])
    grid on;    
end



 

