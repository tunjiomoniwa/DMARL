
clc
clear all

%%Ref: https://uk.mathworks.com/matlabcentral/answers/22-how-do-i-display-different-boxplot-groups-on-the-same-figure-in-matlab
%%%%DDQN Communication
cmad_EE_ = dlmread('ee_M50_CMAD2.dat');
cmad_ene_ = sum(dlmread('Energy_M50_CMAD2.dat'));
cmad_Cov_ = sum(dlmread('Covered_vehicles_M50_CMAD2.dat'));
cmad_Dep_ = dlmread('deployed_vehicles_M50_CMAD2.dat');
cmad_Cov = cmad_Cov_(200:250)';
cmad_Dep = cmad_Dep_(200:250)';
cmad_CDR =  cmad_Cov./cmad_Dep;
mad_energy = cmad_ene_(200:250)';

%%%%%%%%
mad_EE_ = dlmread('ee_M50_MAD3.dat');
mad_ene_ = sum(dlmread('Energy_M50_MAD3.dat'));
mad_Cov_ = sum(dlmread('Covered_vehicles_M50_MAD3.dat'));
mad_Dep_ = dlmread('deployed_vehicles_M50_MAD3.dat');
mad_Cov = mad_Cov_(200:250)';
mad_Dep = mad_Dep_(200:250)';
mad_CDR =  mad_Cov./mad_Dep;
cmad_energy = mad_ene_(200:250)';

%%%%%%%%%%%
dace_EE_ = dlmread('ee_box_test_4.dat'); %%ee_DEMAD_2.dat
dace_ene_ = sum(dlmread('Energy_data_box_test_4.dat')); %%Energy_DEMAD_test_2.dat
dace_Cov_ = sum(dlmread('Covered_vehicles_box_test_4.dat')); %%Covered_vehicles_DEMAD_2.dat
dace_Dep_ = dlmread('deployed_vehicles_box_test_4.dat'); %%deployed_vehicles_DEMAD_2.dat
dace_Cov = dace_Cov_(200:250)';
dace_Dep = dace_Dep_(200:250)';
dace_CDR =  dace_Cov./dace_Dep;
damad_energy = dace_ene_(200:250)';

%%%%%%%%%
%%%%%%%%%%%
damad_EE_ = dlmread('ee_DEMAD_2.dat'); %%ee_DEMAD_2.dat
damad_ene_ = sum(dlmread('Energy_DEMAD_test_2.dat')); %%
damad_Cov_ = sum(dlmread('Covered_vehicles_DEMAD_2.dat')); %%
damad_Dep_ = dlmread('deployed_vehicles_DEMAD_2.dat'); %%
damad_Cov = damad_Cov_(200:250)';
damad_Dep = damad_Dep_(200:250)';
damad_CDR =  damad_Cov./damad_Dep;
dace_energy = damad_ene_(200:250)';

%%%


%%%%%%%%%
maddpg_EE_ = dlmread('ee_DDPG_M50.dat');
maddpg_ene_ = sum(dlmread('Energy_DDPG_N7_low.dat'));
maddpg_Cov_ = sum(dlmread('Covered_vehicles_box_test_4.dat'));
maddpg_Dep_ = dlmread('deployed_vehicles_box_test_4.dat');
maddpg_Cov = maddpg_Cov_(200:250)';
maddpg_Dep = maddpg_Dep_(200:250)';
maddpg_CDR =  maddpg_Cov./maddpg_Dep;
maddpg_energy = maddpg_ene_(50:100)';

%%%%%%%%%%%

f=figure;   

normVal = 1000;
CMAD_energy = [cmad_energy]/normVal;
MAD_energy = [mad_energy]/normVal;
DDPG_energy = [maddpg_energy]/normVal;
DACE_energy = [dace_energy]/normVal;
DAMAD_energy = [damad_energy]/normVal;
m1= max(DACE_energy(:));
m2=  max(DDPG_energy(:));
m3= max(MAD_energy(:));
m4 = max(CMAD_energy(:));
maxVal = max(m1, max(m2,max(m3,m4))); 



xx_mad_over_cmad = mean(DDPG_energy) - mean(CMAD_energy)
damad_imp = mean(DACE_energy) - mean(DAMAD_energy)
mad_imp = mean(DACE_energy) - mean(MAD_energy)
cmad_imp = mean(DACE_energy) - mean(CMAD_energy)
DDPG_imp = mean(DACE_energy) - mean(DDPG_energy)


position_dace_energy = 2;  % Define position 
box_dace_energy = boxplot(DACE_energy,'colors','r','positions',position_dace_energy,'width',1, 'BoxStyle',"filled");
set(gca,'XTickLabel',{' '})  % Erase xlabels   
hold on

position_damad = 4;  
box_DAMAD_energy = boxplot(DAMAD_energy,'colors','b','positions',position_damad,'width',1, 'BoxStyle',"filled"); 
set(gca,'XTickLabel',{' '})  % Erase xlabels   
hold on  % Kenergyp the Month_O boxplots on figure overlap the Month_S boxplots 

position_cmad = 6;  
box_CMAD_energy = boxplot(CMAD_energy,'colors','k','positions',position_cmad,'width',1, 'BoxStyle',"filled"); 
set(gca,'XTickLabel',{' '})  % Erase xlabels   
hold on  % Kenergyp the Month_O boxplots on figure overlap the Month_S boxplots   

position_mad = 8;  
box_MAD_energy = boxplot(MAD_energy,'colors','g','positions',position_mad,'width',1, 'BoxStyle',"filled"); 
set(gca,'XTickLabel',{' '})  % Erase xlabels   
hold on  % Kenergyp the Month_O boxplots on figure overlap the Month_S boxplots   

 

%DDPG_energy = normalize(DDPG_energy, 2, 'range', [0, 1]);
position_DDPG_energy = 10;  % Define position for 12 Month_S boxplots  
box_DDPG_energy = boxplot(max(468,DDPG_energy),'colors','c','positions',position_DDPG_energy,'width',1, 'BoxStyle',"filled"); 

%%%
hold on  


%rand_energy = normalize(rand_energy, 2, 'range', [0, 1]);


%c = get(gca, 'Children');
legend(findobj(gca,'Tag','Box'), 'MADDPG', 'MAD-DDQN', 'CMAD-DDQN', 'DAMAD-DDQN', 'DACEMAD-DDQN', 'Location', 'best')
%hleg1 = legend([c(4) c(3) c(2) c(1)], 'CMAD-DDQN', 'MAD-DDQN', 'MADDPG [3]', 'DACEMAD-DDQN');

grid on;
grid minor;
hold off;   
ylabel('Total Energy Consumed (kJ)','Fontsize',16);
xlabel('Approaches') 
 
set(gca, 'FontSize', 14, 'XTickLabelRotation', 30, 'XTickLabel',{})
ax = gca;
ax.YAxis.Scale ="log";
axis([0 12 400 3000])

%set(gca,'XTickLabel',{'2-Agents', '4-Agents', '6-Agents', '8-Agents', '10-Agents', '12-Agents'});   
%%% To hide outliers 
out_O = box_MAD_energy(end,~isnan(box_MAD_energy(end,:)));  
delete(out_O)  
out_S = box_DDPG_energy(end,~isnan(box_DDPG_energy(end,:)));  
delete(out_S)
out_K = box_dace_energy(end,~isnan(box_dace_energy(end,:)));  
delete(out_K)
out_D = box_CMAD_energy(end,~isnan(box_CMAD_energy(end,:)));  
delete(out_D)
out_A = box_DAMAD_energy(end,~isnan(box_DAMAD_energy(end,:)));  
delete(out_A)  
  



 