
clc
clear all

%%Ref: https://uk.mathworks.com/matlabcentral/answers/22-how-do-i-display-different-boxplot-groups-on-the-same-figure-in-matlab
%%%%DDQN Communication
cmad_EE_ = dlmread('ee_M50_congested_cmad.dat');
cmad_ene_ = sum(dlmread('Energy_M50_CMAD2.dat'));
cmad_Cov_ = sum(dlmread('Covered_vehicles_M50_CMAD2.dat'));
cmad_Dep_ = dlmread('deployed_vehicles_M50_CMAD2.dat');
cmad_Cov = cmad_Cov_(200:250)';
cmad_Dep = cmad_Dep_(200:250)';
cmad_CDR =  cmad_Cov./cmad_Dep;
cmad_ee = cmad_EE_(200:250)';

%%%%%%%%
mad_EE_ = dlmread('ee_M50_congested_mad.dat');
mad_ene_ = sum(dlmread('Energy_M50_MAD3.dat'));
mad_Cov_ = sum(dlmread('Covered_vehicles_M50_MAD3.dat'));
mad_Dep_ = dlmread('deployed_vehicles_M50_MAD3.dat');
mad_Cov = mad_Cov_(200:250)';
mad_Dep = mad_Dep_(200:250)';
mad_CDR =  mad_Cov./mad_Dep;
mad_ee = mad_EE_(200:250)';

%%%%%%%%%%%
dace_EE_ = dlmread('ee_m50_congested_dacemad.dat'); %%ee_DEMAD_2.dat
dace_ene_ = sum(dlmread('Energy_data_box_test_4.dat')); %%Energy_DEMAD_test_2.dat
dace_Cov_ = sum(dlmread('Covered_vehicles_box_test_4.dat')); %%Covered_vehicles_DEMAD_2.dat
dace_Dep_ = dlmread('deployed_vehicles_box_test_4.dat'); %%deployed_vehicles_DEMAD_2.dat
dace_Cov = dace_Cov_(200:250)';
dace_Dep = dace_Dep_(200:250)';
dace_CDR =  dace_Cov./dace_Dep;
dace_ee = dace_EE_(200:250)';

%%%%%%%%%
%%%%%%%%%%%
damad_EE_ = dlmread('ee_m50_congested_damad.dat'); %%ee_DEMAD_2.dat


damad_ee = damad_EE_(200:250)';

%%%


%%%%%%%%%
maddpg_EE_ = dlmread('ee_DDPG_M50_con.dat');
maddpg_ene_ = sum(dlmread('Energy_data_box_test_4.dat'));
maddpg_Cov_ = sum(dlmread('Covered_vehicles_DDPG_M50.dat'));
maddpg_Dep_ = dlmread('deployed_vehicles_box_test_4.dat');
maddpg_Cov = maddpg_Cov_(200:250)';
maddpg_Dep = maddpg_Dep_(200:250)';
maddpg_CDR =  maddpg_Cov./maddpg_Dep;
maddpg_ee = maddpg_EE_(50:100)';

%%%%%%%%%%%

f=figure;   

normVal = mean(dace_ee);
CMAD_ee = [cmad_ee]./normVal;
MAD_ee = [mad_ee]./normVal;
DDPG_ee = [maddpg_ee]./normVal;
DACE_ee = [dace_ee]./normVal;
DAMAD_ee = [damad_ee]./normVal;
m1= max(DACE_ee(:));
m2=  max(DDPG_ee(:));
m3= max(MAD_ee(:));
m4 = max(CMAD_ee(:));
maxVal = max(m1, max(m2,max(m3,m4))); 



xx_mad_over_cmad = mean(DACE_ee) - mean(CMAD_ee)
damad_imp = mean(DACE_ee) - mean(DAMAD_ee)
mad_imp = mean(DACE_ee) - mean(MAD_ee)
cmad_imp = mean(DACE_ee) - mean(CMAD_ee)
DDPG_imp = mean(DACE_ee) - mean(DDPG_ee)


position_dace_ee = 2;  % Define position 
box_dace_ee = boxplot(DACE_ee,'colors','r','positions',position_dace_ee,'width',1, 'BoxStyle',"filled");
set(gca,'XTickLabel',{' '})  % Erase xlabels   
hold on

position_damad = 4;  
box_DAMAD_ee = boxplot(DAMAD_ee,'colors','b','positions',position_damad,'width',1, 'BoxStyle',"filled"); 
set(gca,'XTickLabel',{' '})  % Erase xlabels   
hold on  % Keep the Month_O boxplots on figure overlap the Month_S boxplots 

position_cmad = 6;  
box_CMAD_ee = boxplot(CMAD_ee,'colors','k','positions',position_cmad,'width',1, 'BoxStyle',"filled"); 
set(gca,'XTickLabel',{' '})  % Erase xlabels   
hold on  % Keep the Month_O boxplots on figure overlap the Month_S boxplots   

position_mad = 8;  
box_MAD_ee = boxplot(max(0.018,MAD_ee),'colors','g','positions',position_mad,'width',1, 'BoxStyle',"filled"); 
set(gca,'XTickLabel',{' '})  % Erase xlabels   
hold on  % Keep the Month_O boxplots on figure overlap the Month_S boxplots   

 

%DDPG_ee = normalize(DDPG_ee, 2, 'range', [0, 1]);
position_DDPG_ee = 10;  % Define position for 12 Month_S boxplots  
box_DDPG_ee = boxplot(max(0.0016, DDPG_ee),'colors','c','positions',position_DDPG_ee,'width',1, 'BoxStyle',"filled"); 

%%%
hold on  


%rand_ee = normalize(rand_ee, 2, 'range', [0, 1]);


%c = get(gca, 'Children');
legend(findobj(gca,'Tag','Box'), 'MADDPG', 'MAD-DDQN', 'CMAD-DDQN', 'DAMAD-DDQN', 'DACEMAD-DDQN', 'Location', 'best')
%hleg1 = legend([c(4) c(3) c(2) c(1)], 'CMAD-DDQN', 'MAD-DDQN', 'MADDPG [3]', 'DACEMAD-DDQN');

%grid on;
grid minor;
hold off;   
ylabel('Normalised Energy Efficiency \eta','Fontsize',16);
xlabel('Approaches') 
 
set(gca, 'FontSize', 14, 'XTickLabelRotation', 30, 'XTickLabel',{})
ax = gca;
ax.YAxis.Scale ="log";
axis([0.8 11.8 0.00026 1.7])

%set(gca,'XTickLabel',{'2-Agents', '4-Agents', '6-Agents', '8-Agents', '10-Agents', '12-Agents'});   
%%% To hide outliers 
out_O = box_MAD_ee(end,~isnan(box_MAD_ee(end,:)));  
delete(out_O)  
out_S = box_DDPG_ee(end,~isnan(box_DDPG_ee(end,:)));  
delete(out_S)
out_K = box_dace_ee(end,~isnan(box_dace_ee(end,:)));  
delete(out_K)
out_D = box_CMAD_ee(end,~isnan(box_CMAD_ee(end,:)));  
delete(out_D)
out_A = box_DAMAD_ee(end,~isnan(box_DAMAD_ee(end,:)));  
delete(out_A)  
  











%%ylabel('Normalised Energy Efficiency \eta','Fontsize',16);
