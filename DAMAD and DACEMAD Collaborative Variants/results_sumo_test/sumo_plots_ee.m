clc
clear all



ee_10Uavs_dacemad = dlmread('ee_box_test_4.dat');
ee_10Uavs_damad = dlmread('ee_DEMAD_2.dat');
ee_10Uavs_mad = dlmread('ee_M50_MAD3.dat');
ee_10Uavs_cmad = dlmread('ee_M50_CMAD2.dat');

figure;
a1 = axes();
epi = 1:1:length(ee_10Uavs_dacemad);

%plot(epi, percentage_cov, 'b-')
semilogy(epi, ee_10Uavs_dacemad, 'r-', epi, ee_10Uavs_damad, 'b-', epi, ee_10Uavs_cmad, 'k-', epi, ee_10Uavs_mad, 'g-', 'Linewidth', 1)
%semilogy(epi_ddpg, energy_ddpg_train, 'k:', 'Linewidth', 1)
set(gca, 'FontSize', 16)
legend('DACEMAD-DDQN', 'DAMAD-DDQN', 'CMAD-DDQN', 'MAD-DDQN', 'location', 'best');
%legend('Deployed Vehicles','Covered Vehicles', 'location', 'best');
xlabel('Episodes','Fontsize',16);
ylabel('Total Energy Efficiency \eta','Fontsize',16);
axis([2 length(ee_10Uavs_dacemad) 0.0 1.1])
grid on;

a2 = axes();
a2.Position = [0.630 0.3600 0.25 0.2]; 
%a2.Position = [0.3200 0.6600 0.2 0.2]; % xlocation, ylocation, xsize, ysize
plot((220:250), ee_10Uavs_dacemad(220:250), 'r-', (220:250), ee_10Uavs_damad(220:250), 'b-', (220:250), ee_10Uavs_cmad(220:250), 'k-', (220:250), ee_10Uavs_mad(220:250), 'g-', 'Linewidth', 1); axis tight
set(gca, 'FontSize', 10)
