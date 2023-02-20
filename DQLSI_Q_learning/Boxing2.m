 
function newobsBL2 = Boxing2(xtBL2, ytBL2, ztBL2) %mapping
    %obs1 = [xBL1, yBL1, zBL1];
%% xBL1: 0 - 500, yBL1: 0 - 500, zBL1: 0 - 400
 %clc;
 %clear all;
 str =[];
 str_iter = [];
 iiter = 0;
mobilityt = 100;
 for xt2 = mobilityt +500 : mobilityt  :500 +500
     x2_low = xt2-mobilityt;     
     for yt2 = mobilityt : mobilityt : 500
         y2_low = yt2-mobilityt;
         for zt2 = mobilityt: mobilityt: 400
             z2_low = zt2-mobilityt;
             iiter = iiter +1;
             str = [str; [xt2 yt2 zt2 x2_low y2_low z2_low]];
             str_iter = [str_iter; iiter];
         end
     end
 end
Box_division = [str str_iter];
 
index2 = find(xtBL2 < (Box_division(:,1) +1) & xtBL2 > Box_division(:,4) &  ytBL2 < (Box_division(:,2)+1) & ytBL2 > Box_division(:,5) & ztBL2 < (Box_division(:,3) + 1) & ztBL2 > Box_division(:,6));

newobsBL2 = Box_division(index2,7);

end

