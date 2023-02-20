function [finx, finy] = RWP4(mob_x, mob_y);
%%[newx, newy] = RWP(mob_x, mob_y);
    matxMax = [980];
    matxMin = [520];
    matyMax = [980];
    matyMin = [520];
    
    %%%
    num_devices = length(mob_x);
    inc_xs =[];
    inc_ys =[];
    finx = [];
    finy = [];
    for i = 1: num_devices
        [inc_x, inc_y] = circle(randi([-5 5]), randi([-2 2]), randi([0 10]), randi([0 180]), rand); 
        %[inc_x, inc_y] = circle(random.randrange(-5, 5), random.randrange(-2, 2), random.randrange(0, 10), random.randrange(0, 360), random.uniform(0, 1));   
        inc_xs = [inc_xs , inc_x];
        inc_ys = [inc_ys , inc_y];
    end
    
    newx = mob_x + inc_xs;
    newy = mob_y + inc_ys;
    
    for i = 1: num_devices
        if (newx(i) > matxMax)
            %%% It's past the right edge
            distancemBeyond = abs(newx(i) - matxMax);
            %% Walk in the x direction.
            newx(i) = matxMax - distancemBeyond;
        elseif (newx(i) < matxMin)
            %% It's past the left edge
            distancemBeyond = abs(matxMin - newx(i));
            %%% Walk in the x direction.
            newx(i) = matxMin + distancemBeyond;
        else
            newx(i) = newx(i);
            
        end
            %%%%%%%%%%%
        if (newy(i) > matyMax)
            % It's past the right edge
            distancemBeyond = abs(newy(i) - matyMax);
            % Walk in the x direction.
            newy(i) = matyMax - distancemBeyond;
        elseif (newy(i) <matyMin)
            % It's past the left edge
            distancemBeyond = abs(matyMin - newy(i));
            % Walk in the y direction.
            newy(i) = matyMin + distancemBeyond;
        else
            newy(i) = newy(i);            
        end 
        finx = [finx, newx(i)]; 
        finy = [finy, newy(i)]; 
    end
   %[[finx], [finy]]    
end




% def circle(a,b,r,t, pause_prob):
%     if pause_prob>0.5:
%         cosinus = r*math.cos(t)
%         sinus = r*math.sin(t) 
%         x = a + cosinus
%         y = b + sinus
%     else:
%         x = 0
%         y = 0
%     return x,y
function [x, y] = circle(a,b,r,t, pause_prob)
    %t = randi([0 2*pi]);%(0:0.01:2*pi)';
    if pause_prob>0.5
        cosinus = r*cos(t);
        sinus = r*sin(t); 
        
        x = a + cosinus;
        y = b+ sinus;
%         n = length(t)
%         m = length(a)
%         x = repmat(a,n,1) + repmat(cosinus,m,1);
%         y = repmat(b,n,1) + repmat(sinus,m,1);
    else
        x = 0;
        y = 0;
    end
end


