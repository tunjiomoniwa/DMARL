clc
clear all

episodes =100;
% %%%%%%%%%%energy data dynamic
% energy = matfile('eng_dyn_data_uneven2.mat');
% eUAV1 = energy.UAV1Energycount;
% eUAV2 = energy.UAV2Energycount;
% eUAV3 = energy.UAV3Energycount;
% eUAV4 = energy.UAV4Energycount;
% 
% semilogy(1:episodes, eUAV1, 'b-', 1:episodes, eUAV2, 'r-', 1:episodes, eUAV3, 'k--', 1:episodes, eUAV4, 'r--')
% %%%set(gca, 'XTick', 0:20:100, 'YTick', 0:20:100);
% set(gca, 'FontSize', 18)
% %ax = gca;
% %ax.YAxis.Scale ="log";
% legend('Agent-1', 'Agent-2','Agent-3', 'Agent-4', 'location', 'best');
% xlabel('Episodes','Fontsize',20);
% ylabel('Energy consumed (Joules)','Fontsize',20);
% grid on;


%%%%%%%%%%%%%%%%%Coverage dynamic
%%%%%%%%%%
cov = matfile('cov_dyn_data_uneven2.mat');
cUAV1 = cov.UAV1CoverageScorecount;
cUAV2 = cov.UAV2CoverageScorecount;
cUAV3 = cov.UAV3CoverageScorecount;
cUAV4 = cov.UAV4CoverageScorecount;
cUAVtot = cov.sum_cov_dyn;

%%%%%%%
plot(1:episodes, (cUAVtot), 'k-')
%%plot(1:episodes, min(100,cUAV1), 'b-', 1:episodes, min(100,cUAV2), 'r-', 1:episodes, min(100,cUAV3), 'k--', 1:episodes, min(100,cUAV4), 'r--')%, 1:episodes, 84*ones(1,episodes), 'r-')
% plot(1:episodes, cUAV1, 'b-', 1:episodes, cUAV2, 'r-', 1:episodes, cUAV3, 'k--', 1:episodes, cUAV4, 'r--')%, 1:episodes, 84*ones(1,episodes), 'r-')
% 
set(gca, 'FontSize', 18)
set(gca, 'XTick', 0:10:100, 'YTick', 0:50:400);
  %axis(gca,'square');
ylabel('Connected ground devices','Fontsize',20)
xlabel('Episodes','Fontsize',20)
%legend('Agent-1', 'Agent-2','Agent-3', 'Agent-4', 'location', 'southeast')
% axis([0 100 0 140])
grid on;

% % %%%%%%%%%%%%%%%%%Geog dynamic
% %%%%%%%%%%
% geo = matfile('geo_dyn_data_uneven2.mat');
% gUAV1 = geo.UAV1GeoAreacount;
% gUAV2 = geo.UAV2GeoAreacount;
% gUAV3 = geo.UAV3GeoAreacount;
% gUAV4 = geo.UAV4GeoAreacount;
% gUAVtot = geo.sum_geo_dyn;
% 
% %plot(1:episodes, gUAV1, 'b-', 1:episodes, gUAV2, 'r-', 1:episodes, gUAV3, 'k--', 1:episodes, gUAV4, 'r--')%, 1:episodes, 84*ones(1,episodes), 'r-')
% plot(1:episodes, gUAVtot, 'r-') 
% set(gca, 'FontSize', 18)
% %%set(gca, 'XTick', 0:10:100, 'YTick', 0:10:100);
%   %axis(gca,'square');
% ylabel('Area covered (sq. km)','Fontsize',20)
% xlabel('Episodes','Fontsize',20)
% %legend('Agent-1', 'Agent-2','Agent-3', 'Agent-4', 'location', 'southeast')
% %% axis([0 100 0 105])
% grid on;
% 

% %%%%%%%%%%%%%%%%%Iter dynamic
% %%%%%%%%%%
% rew = matfile('rew_dyn_data_uneven2.mat');
% rUAV1 = rew.rewardcount1_;
% rUAV2 = rew.rewardcount2_;
% rUAV3 = rew.rewardcount3_;
% rUAV4 = rew.rewardcount4_;
% rUAVtot = rew.sum_rew_dyn;
% 
% plot(1:episodes, rUAV1, 'b-', 1:episodes, rUAV2, 'r-', 1:episodes, rUAV3, 'k--', 1:episodes, rUAV4, 'r--')%, 1:episodes, 84*ones(1,episodes), 'r-')
%  set(gca, 'FontSize', 18)
% %%set(gca, 'XTick', 0:10:100, 'YTick', 0:10:100);
%   %axis(gca,'square');
% xlabel('Episodes','Fontsize',20)
% ylabel('Norm. Accum. Reward','Fontsize',20)
% legend('Agent-1', 'Agent-2','Agent-3', 'Agent-4', 'location', 'best')
% grid on;
