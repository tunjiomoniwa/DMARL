% This script uses the k-means function on an example with randomly created
% data points in 2D and visualaizes its result.

close all; clear; clc;


%% Input args (and print them)

k = 5;     % number of clusters
numP = 400; % number of points
xMax = 1000; % x between 0 and xMax
yMax = 1000; % y between 0 and yMax
fprintf('k-Means will run with %d clusters and %d data points.\n',k,numP);


%% Create random data points

% create a random matrix of size 2-by-numP 
% with row 1/2 (x/y coordiante) ranging in [minX,maxX]/[minY,maxY]
xP = xMax * rand(1,numP);
yP = yMax * rand(1,numP);
points = [xP; yP];


%% run kMeans.m and measure/print performance

tic;
[cluster, centr] = kMeans(k, points); % my k-means
myPerform = toc;
fprintf('Computation time for kMeans.m: %d seconds.\n', myPerform);


%% run MATLAB's function kmeans(P,k) and measure/print performance

tic;
[cluster_mT, centr_m] = kmeans(points',k); % MATLAB's k-means
matlabsPerform = toc;
cluster_m = cluster_mT';
fprintf('Computation time for MATLABs kmeans: %d seconds.\n', matlabsPerform);


%% Compare performances

frac = matlabsPerform/myPerform;
fprintf('MATLAB uses %d of the time kMeans.m uses.\n' ,frac);
hold on;

%% All visualizations

%figure('Name','Visualizations','units','normalized','outerposition',[0 0 1 1]);

% visualize the clustering
% subplot(2,2,1);

%plot3(centr(1,:),centr(2,:), 3)

x1 =centr(1,1);
x2 =centr(1,2);
x3 =centr(1,3);
x4 =centr(1,4);
x5 =centr(1,5);
%%
y1 =centr(2,1);
y2 =centr(2,2);
y3 =centr(2,3);
y4 =centr(2,4);
y5 =centr(2,5);

z1 = 300;
z2 = 350;
z3 = 380;
z4 = 320;
z5 = 210;

plot3(x1,y1,z1,'r<');

%plot3(x1,y1,z1,'r-')   


hold on
scatter(xP,yP,200,cluster,'.');
plot3(x2,y2,z2,'r<');
plot3(x3,y3,z3,'r<');
plot3(x4,y4,z4,'r<');
plot3(x5,y5,z5,'r<');

hold on;
scatter(centr(1,:),centr(2,:),'xk','LineWidth',1.5);
axis([0 xMax 0 yMax]);
daspect([1 1 1]);
xlabel('x (m)');
ylabel('y (m)');
zlabel('h (m)');
legend('UAVs', 'Ground users')
%title('K-Means Clustering-based RL [Liu et al., 2019]');
grid on;

% % number of points in each cluster
% subplot(2,2,2);
% histogram(cluster);
% axis tight;
% [num,~] = histcounts(cluster);
% yticks(round(linspace(0,max(num),k)));
% xlabel('Clusters');
% ylabel('Number of data points');
% title('Histogram of the cluster points (own implementation)');

% % visualize MATLAB's clustering
% subplot(2,2,3);
% scatter(xP,yP,200,cluster_m,'.');
% hold on;
% scatter(centr_m(:,1),centr_m(:,2),'xk','LineWidth',1.5);
% axis([0 xMax 0 yMax]);
% daspect([1 1 1]);
% xlabel('x');
% ylabel('y');
% title('Random data points clustered (MATLABs implementation)');
% grid on;
% 
% % number of points in each MATLAB cluster
% subplot(2,2,4);
% histogram(cluster_m);
% axis tight;
% [num_m,~] = histcounts(cluster_m);
% yticks(round(linspace(0,max(num_m),k)));
% xlabel('Clusters');
% ylabel('Number of data points');
% title('Histogram of the cluster points (MATLABs implementation)');