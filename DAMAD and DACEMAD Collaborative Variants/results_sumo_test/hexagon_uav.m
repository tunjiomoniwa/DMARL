close all; clear; clc;


% Generate hexagonal grid
Rad3Over2 = sqrt(3) / 2;
[X Y] = meshgrid(0:1:11);
n = size(X,1);
X = Rad3Over2 * X;
Y = Y + repmat([0 0.55],[n,n/2]);
hold on
% Plot the hexagonal mesh, including cell borders
[XV YV] = voronoi(X(:),Y(:)); plot(XV,YV,'b-')
set(gca,'visible','off')
axis equal, axis([0 4 0 4]), zoom on


% [X Y] = meshgrid(0:200:1000);
% voronoi(X(:),Y(:), 'b--')%, axis square
% 
% xMax = 1000; % x between 0 and xMax
% yMax = 1000; % y between 0 and yMax
% x1 =200;
% x2 =600;
% x3 =450;
% x4 =300;
% x5 =790;
% %%
% y1 =350;
% y2 =600;
% y3 =900;
% y4 =500;
% y5 =500;
% 
% z1 = 350;
% z2 = 350;
% z3 = 350;
% z4 = 350;
% z5 = 350;
% hold on;
% plot3(x1,y1,z1,'rV')%%, 'MarkerSize', 20);
% 
% %plot3(x1,y1,z1,'r-')   
% 
% plot3(x2,y2,z2,'rV');
% plot3(x3,y3,z3,'rV');
% plot3(x4,y4,z4,'rV');
% plot3(x5,y5,z5,'rV');
% xlabel('x (m)');
% ylabel('y (m)');
% zlabel('h (m)');
% %title('K-Cells Partitions MADDPG [Liu et al., 2020]');
% axis([0 xMax 0 yMax]);
% grid on;
% %%%
% hold on;
% 
% 
% h1 = circle(x1,y1,150)
% h2 = circle(x2,y2,150)
% h3 = circle(x3,y3,150)
% h4 = circle(x4,y4,150)
% h5 = circle(x5,y5,150)
% legend('Ground users', 'Partitions','UAVs')
% % th = 0:1:360;  %np.array(range(int(0), int(2*180), int(180/50)))
% % lenl = 0:50; %np.array(range(0,len(outysef)))
% 
% % powRange = 1.7;
% % 
% % r1_ = (powRange*z1).^2 - (z1).^2;
% % r1 = (r1_).^0.5;
% % tl = cos(th);
% % 
% %     
% % xunit1 = r1*cos(th) + x1
% % yunit1 = r1*sin(th) + y1
% %     
% plot(xunit1, xunit1, 'r-')