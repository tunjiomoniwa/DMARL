clc
clear all

 

%%Ref: https://uk.mathworks.com/matlabcentral/answers/22-how-do-i-display-different-boxplot-groups-on-the-same-figure-in-matlab
%%%%DDQN Communication

cmad_Cov_ = sum(dlmread('Covered_vehicles_N7_congested_cmad.dat'));
cmad_Dep_ = dlmread('deployed_vehicles_N7_congested_cmad.dat');
cmad_Cov = cmad_Cov_(200:250)';
cmad_Dep = cmad_Dep_(200:250)';
cmad_CDR =  cmad_Cov./cmad_Dep;

%%%%%%%%

mad_Cov_ = sum(dlmread('Covered_vehicles_N7_congested_mad.dat'));
mad_Dep_ = dlmread('deployed_vehicles_N7_congested_mad.dat');
mad_Cov = mad_Cov_(200:250)';
mad_Dep = mad_Dep_(200:250)';
mad_CDR =  mad_Cov./mad_Dep;

%%%%%%%%%%%

dace_Cov_ = sum(dlmread('Covered_vehicles_N7_congested_dacemad.dat')); %%Covered_vehicles_DEMAD_2.dat
dace_Dep_ = dlmread('deployed_vehicles_N7_congested_dacemad.dat'); %%deployed_vehicles_DEMAD_2.dat
dace_Cov = dace_Cov_(200:250)';
dace_Dep = dace_Dep_(200:250)';
dace_CDR =  dace_Cov./dace_Dep;

%%%%%%%%%
%%%%%%%%%%%

damad_Cov_ = sum(dlmread('Covered_vehicles_N7_congested_damad.dat')); %%
damad_Dep_ = dlmread('deployed_vehicles_N7_congested_damad.dat'); %%
damad_Cov = damad_Cov_(200:250)';
damad_Dep = damad_Dep_(200:250)';
damad_CDR =  damad_Cov./damad_Dep;

%%%


%%%%%%%%%
maddpg_EE_ = dlmread('ee_M50_MAD2.dat');
maddpg_ene_ = sum(dlmread('Energy_data_box_test_4.dat'));
maddpg_Cov_ = sum(dlmread('Covered_vehicles_DDPG_N7_con.dat'));
maddpg_Dep_ = dlmread('deployed_vehicles_DDPG_N7_con.dat');
maddpg_Cov = maddpg_Cov_(50:100)';
maddpg_Dep = maddpg_Dep_(50:100)';
maddpg_CDR =  maddpg_Cov./maddpg_Dep;

%%%%%%%%%%%

f=figure;   

normVal = 1;
CMAD_CDR = [cmad_CDR]/normVal;
MAD_CDR = [mad_CDR]/normVal;
DDPG_CDR = [maddpg_CDR]/normVal;
DACE_CDR = [dace_CDR]/normVal;
DAMAD_CDR = [damad_CDR]/normVal;
m1= max(DACE_CDR(:));
m2=  max(DDPG_CDR(:));
m3= max(MAD_CDR(:));
m4 = max(CMAD_CDR(:));
maxVal = max(m1, max(m2,max(m3,m4))); 



xx_mad_over_cmad = mean(DACE_CDR) - mean(CMAD_CDR)
damad_imp = mean(DACE_CDR) - mean(DAMAD_CDR)
mad_imp = mean(DACE_CDR) - mean(MAD_CDR)
cmad_imp = mean(DACE_CDR) - mean(CMAD_CDR)
DDPG_imp = mean(DACE_CDR) - mean(DDPG_CDR)


position_dace_CDR = 2;  % Define position 
box_dace_CDR = boxplot(DACE_CDR,'colors','r','positions',position_dace_CDR,'width',1, 'BoxStyle',"filled");
set(gca,'XTickLabel',{' '})  % Erase xlabels   
hold on

position_damad = 4;  
box_DAMAD_CDR = boxplot(DAMAD_CDR,'colors','b','positions',position_damad,'width',1, 'BoxStyle',"filled"); 
set(gca,'XTickLabel',{' '})  % Erase xlabels   
hold on  % KCDRp the Month_O boxplots on figure overlap the Month_S boxplots 

position_cmad = 6;  
box_CMAD_CDR = boxplot(CMAD_CDR,'colors','k','positions',position_cmad,'width',1, 'BoxStyle',"filled"); 
set(gca,'XTickLabel',{' '})  % Erase xlabels   
hold on  % KCDRp the Month_O boxplots on figure overlap the Month_S boxplots   

position_mad = 8;  
box_MAD_CDR = boxplot(MAD_CDR,'colors','g','positions',position_mad,'width',1, 'BoxStyle',"filled"); 
set(gca,'XTickLabel',{' '})  % Erase xlabels   
hold on  % KCDRp the Month_O boxplots on figure overlap the Month_S boxplots   

 

%DDPG_CDR = normalize(DDPG_CDR, 2, 'range', [0, 1]);
position_DDPG_CDR = 10;  % Define position for 12 Month_S boxplots  
box_DDPG_CDR = boxplot(DDPG_CDR,'colors','c','positions',position_DDPG_CDR,'width',1, 'BoxStyle',"filled"); 

%%%
hold on  


%rand_CDR = normalize(rand_CDR, 2, 'range', [0, 1]);


%c = get(gca, 'Children');
legend(findobj(gca,'Tag','Box'), 'MADDPG', 'MAD-DDQN', 'CMAD-DDQN', 'DAMAD-DDQN', 'DACEMAD-DDQN', 'Location', 'best')
%hleg1 = legend([c(4) c(3) c(2) c(1)], 'CMAD-DDQN', 'MAD-DDQN', 'MADDPG [3]', 'DACEMAD-DDQN');

%grid on;
grid minor;
hold off;   
ylabel('CDR','Fontsize',16);
xlabel('Approaches') 
 
set(gca, 'FontSize', 14, 'XTickLabelRotation', 30, 'XTickLabel',{})
%ax = gca;
%ax.YAxis.Scale ="log";

axis([0 12 0 1])
%set(gca,'XTickLabel',{'2-Agents', '4-Agents', '6-Agents', '8-Agents', '10-Agents', '12-Agents'});   
%%% To hide outliers 
out_O = box_MAD_CDR(end,~isnan(box_MAD_CDR(end,:)));  
delete(out_O)  
out_S = box_DDPG_CDR(end,~isnan(box_DDPG_CDR(end,:)));  
delete(out_S)
out_K = box_dace_CDR(end,~isnan(box_dace_CDR(end,:)));  
delete(out_K)
out_D = box_CMAD_CDR(end,~isnan(box_CMAD_CDR(end,:)));  
delete(out_D)
out_A = box_DAMAD_CDR(end,~isnan(box_DAMAD_CDR(end,:)));  
delete(out_A)  
  