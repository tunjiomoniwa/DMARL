clc
clear all

figure;
a1 = axes();
epi = 1:1:250;

Energy_10Uavs_dacemad = sum(dlmread('Energy_N7_congested_dacemad.dat'))./1000;
Energy_10Uavs_damad = sum(dlmread('Energy_N7_congested_damad.dat'))./1000;
Energy_10Uavs_mad = sum(dlmread('Energy_N7_congested_mad.dat'))./1000; 
Energy_10Uavs_cmad = sum(dlmread('Energy_N7_congested_cmad.dat'))./1000; 

%plot(epi1, Energy_10Uavs_mad, 'b-')
 
semilogy(epi, Energy_10Uavs_dacemad, 'r-', epi, Energy_10Uavs_damad, 'b-',  epi, Energy_10Uavs_cmad, 'k-',  epi, Energy_10Uavs_mad, 'g-', 'Linewidth', 1)
hold on;

%semilogy(epi_ddpg, energy_ddpg_train, 'k:', 'Linewidth', 1)
set(gca, 'FontSize', 16)
legend('DACEMAD-DDQN','DAMAD-DDQN', 'CMAD-DDQN', 'MAD-DDQN', 'location', 'best');


xlabel('Episodes','Fontsize',16);
ylabel('Total Energy Consumed (kJ)','Fontsize',16);
axis([2 250 100 max(Energy_10Uavs_dacemad)+10e3])
grid on;

% a2 = axes();
% a2.Position = [0.580 0.4600 0.25 0.2]; 
% %a2.Position = [0.3200 0.6600 0.2 0.2]; % xlocation, ylocation, xsize, ysize
% plot((220:250),Energy_10Uavs_dacemad(220:250), 'r-', (220:250), Energy_10Uavs_damad(220:250), 'b-', (220:250), Energy_10Uavs_cmad(220:250), 'k-', (220:250), Energy_10Uavs_mad(220:250), 'g-', 'Linewidth', 1); axis tight
% set(gca, 'FontSize', 10)
% %xlabel('Episodes','Fontsize',12);
% %ylabel('Total Energy Consumed (J)','Fontsize',12)

