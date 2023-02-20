 
function newobsBL4 = Boxing4(xtBL4, ytBL4, ztBL4) %mapping
    %obs1 = [xBL1, yBL1, zBL1];
%% xBL1: 0 - 500, yBL1: 0 - 500, zBL1: 0 - 400
 %clc;
 %clear all;
 str =[];
 str_iter = [];
 iiter = 0;
mobilityt = 100;
 for xt4 = mobilityt +500  : mobilityt  :500 +500
     x4_low = xt4-mobilityt;     
     for yt4 = mobilityt +500: mobilityt : 500 +500
         y4_low = yt4-mobilityt;
         for zt4 = mobilityt: mobilityt: 400
             z4_low = zt4-mobilityt;
             iiter = iiter +1;
             str = [str; [xt4 yt4 zt4 x4_low y4_low z4_low]];
             str_iter = [str_iter; iiter];
         end
     end
 end
Box_division = [str str_iter];
 
index4 = find(xtBL4 < (Box_division(:,1) +1) & xtBL4 > Box_division(:,4) &  ytBL4 < (Box_division(:,2)+1) & ytBL4 > Box_division(:,5) & ztBL4 < (Box_division(:,3) + 1) & ztBL4 > Box_division(:,6));

newobsBL4 = Box_division(index4,7);

end

