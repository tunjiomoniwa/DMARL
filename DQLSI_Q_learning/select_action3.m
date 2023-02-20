function action3 = select_action3(epsilon, state3, Q3)
% linear
% epsilon =1-(epi/1000)
% 
% exp decay
% epsilon =float(np.exp(-0.0015*epi))
%%to be used in the episode
if rand() < epsilon
    len_action = 7;
    action3 = randi(len_action,1); %Explore action space
else
    [maxval3 argmax3] = max(Q3(state3,:)); %Exploit learned values
    action3 = argmax3;
end
