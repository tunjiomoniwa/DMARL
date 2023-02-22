r1 = [1:100]'.*rand(100,1);
figure;
a1 = axes();
plot(a1,r1);
a2 = axes();
a2.Position = [0.3200 0.6600 0.2 0.2]; % xlocation, ylocation, xsize, ysize
plot(a2,r1(50:70)); axis tight
%annotation('ellipse',[.2 .3 .2 .2])
%annotation('arrow',[.1 .2],[.1 .2])
legend(a1,'u')