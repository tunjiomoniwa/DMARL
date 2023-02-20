clc;
clear all;
cov_data_ = load('cov_dyn_data_uneven2.mat');
cov_u1 = cov_data_.UAV1CoverageScorecount/4;
cov_u2 = cov_data_.UAV2CoverageScorecount/4;
cov_u3 = cov_data_.UAV3CoverageScorecount/4;
cov_u4 = cov_data_.UAV4CoverageScorecount/4;


fair_data_ = load('fair_RW_data_uneven.mat');
fair_u1 = fair_data_.fairfactor;


%save('geo_sta_data_new1.mat', 'sum_geo_sta', 'UAV1GeoAreacount', 'UAV2GeoAreacount','UAV3GeoAreacount', 'UAV4GeoAreacount');

geo_data_ = load('geo_dyn_data_new_rwp.mat');
geo_u1 = geo_data_.sum_geo_dyn;


ene_data_ = load('eng_dyn_data_new_RWP.mat');
ene_u1 = ene_data_.UAV1Energycount*1/1000;
ene_u2 = ene_data_.UAV2Energycount*1/1000;
ene_u3 = ene_data_.UAV3Energycount*1/1000;
ene_u4 = ene_data_.UAV4Energycount*1/1000;


% ene_u1 = ene_data_.UAV1Energycount*35/1000;
% ene_u2 = ene_data_.UAV2Energycount*35/1000;
% ene_u3 = ene_data_.UAV3Energycount*35/1000;
% ene_u4 = ene_data_.UAV4Energycount*35/1000;
%save('eng_sta_data_new.mat', 'sum_eng_sta', 'UAV1Energycount', 'UAV2Energycount','UAV3Energycount', 'UAV4Energycount');

rew_data_ = load('rew_dyn_data_new_RWP.mat');
rew_u1 = rew_data_.rewardcount1_;
rew_u2 = rew_data_.rewardcount2_;
rew_u3 = rew_data_.rewardcount3_;
rew_u4 = rew_data_.rewardcount4_;
%Reward_data1
% rewa_data_ = load('Reward_data1.dat');
% rewa_u1 = rewa_data_(1,:);
% rewa_u2 = rewa_data_(2,:);
% rewa_u3 = rewa_data_(3,:);
% rewa_u4 = rewa_data_(4,:);
% 
% minVal = min(rewa_u1(:));
% maxVal = max(rewa_u1(:));
% minVal2 = min(rewa_u2(:));
% maxVal2 = max(rewa_u2(:));
% minVal3 = min(rewa_u3(:));
% maxVal3 = max(rewa_u3(:));
% minVal4 = min(rewa_u4(:));
% maxVal4 = max(rewa_u4(:));
% 
% rew_u1 = (rewa_u1 - minVal) / ( maxVal - minVal ) ; %normdata
% rew_u2 = (rewa_u2 - minVal2) / ( maxVal2 - minVal2 ) ; 
% rew_u3 = (rewa_u3 - minVal3) / ( maxVal3 - minVal3 ) ;
% rew_u4 = (rewa_u4 - minVal4) / ( maxVal4 - minVal4 ) ;
%  







bits =1;
ee_u1 = bits*cov_u1./ene_u1;
ee_u2 = bits* cov_u2./ene_u2;
ee_u3 = bits* cov_u3./ene_u3;
ee_u4 = bits* cov_u4./ene_u4;

%save('rew_sta_data_new.mat', 'sum_rew_sta', 'rewa_u1_', 'rewa_u2_','rewa_u3_', 'rewa_u4_');

len = length(rew_u1);

% %%COVERAGE
% plot(1:len, cov_u1, 'r-', 1:len, cov_u2, 'b-', 1:len, cov_u3, 'k-', 1:len, cov_u4, 'g-', 'Linewidth', 1)% 
% set(gca, 'FontSize', 16)
% xlabel('Episodes','Fontsize',16);    
% ylabel('Number of Connected Users (%)','Fontsize',16);
% legend('Agent-1','Agent-2', 'Agent-3', 'Agent-4', 'location', 'best')
% axis([0 100 0 45])    
% %axis([1 length(deployed_veh) 200.0 700])
% grid on;    

%%REWARD
% plot(1:len, rew_u1, 'r-', 1:len, rew_u2, 'b-', 1:len, rew_u3, 'k-', 1:len, rew_u4, 'g-', 'Linewidth', 1) 
% set(gca, 'FontSize', 16)
% xlabel('Episodes','Fontsize',16);    
% ylabel('Normalised Cummulative Reward','Fontsize',16);
% legend('Agent-1','Agent-2', 'Agent-3', 'Agent-4', 'location', 'best')
% %axis([0 100 0 110])    
% %axis([1 length(deployed_veh) 200.0 700])
% grid on;    


% % % %%%%ENERGY
% plot(1:len, ene_u1, 'r-', 1:len, ene_u2, 'b-', 1:len, ene_u3, 'k-', 1:len, ene_u4, 'g-', 'Linewidth', 1)
% set(gca, 'FontSize', 16)
% xlabel('Episodes','Fontsize',16);    
% ylabel('Total Energy Consumed (kJ)','Fontsize',16);
% legend('Agent-1','Agent-2', 'Agent-3', 'Agent-4', 'location', 'best')
% ax = gca;
% ax.YAxis.Scale ="log";
% %axis([0 12 130 2300])
% grid on;


% %%EE
% plot(1:len, ee_u1, 'r-', 1:len, ee_u2, 'b-', 1:len, ee_u3, 'k-', 1:len, ee_u4, 'g-', 'Linewidth', 1)
% set(gca, 'FontSize', 16)
% xlabel('Episodes','Fontsize',16);    
% ylabel('Energy Efficiency \eta','Fontsize',16);
% legend('Agent-1','Agent-2', 'Agent-3', 'Agent-4', 'location', 'best')
% ax = gca;
% ax.YAxis.Scale ="log";
% %axis([0 12 130 2300])
% grid on;    

%%%Fairness
plot(1:len, fair_u1, 'r-', 'Linewidth', 1)
set(gca, 'FontSize', 16)
xlabel('Episodes','Fontsize',16);    
ylabel('Fairness Index','Fontsize',16);
%legend('Agent-1','Agent-2', 'Agent-3', 'Agent-4', 'location', 'best')
ax = gca;
ax.YAxis.Scale ="log";
axis([0 100 0 1.02])
grid on;  


% %Geogra Area
% plot(1:len, geo_u1, 'r-', 'Linewidth', 1)
% set(gca, 'FontSize', 16)
% xlabel('Episodes','Fontsize',16);    
% ylabel('Area covered (km^2)','Fontsize',16);
% %legend('Agent-1','Agent-2', 'Agent-3', 'Agent-4', 'location', 'best')
% ax = gca;
% ax.YAxis.Scale ="log";
% axis([0 100 0 1.02])
% grid on; 

