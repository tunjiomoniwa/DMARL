 
function newobsBL3 = Boxing3(xtBL3, ytBL3, ztBL3) %mapping
    %obs1 = [xBL1, yBL1, zBL1];
%% xBL1: 0 - 500, yBL1: 0 - 500, zBL1: 0 - 400
 %clc;
 %clear all;
 str =[];
 str_iter = [];
 iiter = 0;
mobilityt = 100;
 for xt3 = mobilityt  : mobilityt  :500
     x3_low = xt3-mobilityt;     
     for yt3 = mobilityt +500: mobilityt : 500 +500
         y3_low = yt3-mobilityt;
         for zt3 = mobilityt: mobilityt: 400
             z3_low = zt3-mobilityt;
             iiter = iiter +1;
             str = [str; [xt3 yt3 zt3 x3_low y3_low z3_low]];
             str_iter = [str_iter; iiter];
         end
     end
 end
Box_division = [str str_iter];
 
index3 = find(xtBL3 < (Box_division(:,1) +1) & xtBL3 > Box_division(:,4) &  ytBL3 < (Box_division(:,2)+1) & ytBL3 > Box_division(:,5) & ztBL3 < (Box_division(:,3) + 1) & ztBL3 > Box_division(:,6));

newobsBL3 = Box_division(index3,7);

end

