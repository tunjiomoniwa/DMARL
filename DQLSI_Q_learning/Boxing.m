 
function newobsBL1 = Boxing(xtBL1, ytBL1, ztBL1, dis_x, dis_y) %mapping
    %obs1 = [xBL1, yBL1, zBL1];
%% xBL1: 0 - 500, yBL1: 0 - 500, zBL1: 0 - 400
 %clc;
 %clear all;
 str =[];
 str_iter = [];
 iiter = 0;
mobilityt = 100;
 for xt1 = mobilityt +dis_x : mobilityt :500 +dis_x
     x1_low = xt1-mobilityt;     
     for yt1 = mobilityt +dis_y : mobilityt : 500 +dis_y
         y1_low = yt1-mobilityt;
         for zt1 = mobilityt: mobilityt: 400
             z1_low = zt1-mobilityt;
             iiter = iiter +1;
             str = [str; [xt1 yt1 zt1 x1_low y1_low z1_low]];
             str_iter = [str_iter; iiter];
         end
     end
 end
Box_division = [str str_iter];
 
index1 = find(xtBL1 < (Box_division(:,1) +1) & xtBL1 > Box_division(:,4) &  ytBL1 < (Box_division(:,2)+1) & ytBL1 > Box_division(:,5) & ztBL1 < (Box_division(:,3) + 1) & ztBL1 > Box_division(:,6));

newobsBL1 = Box_division(index1,7);

end

