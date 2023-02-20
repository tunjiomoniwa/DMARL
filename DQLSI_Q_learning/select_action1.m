function action1 = select_action1(epsilon, state1, Q1)
% linear
% epsilon =1-(epi/1000)
% 
% exp decay
% epsilon =float(np.exp(-0.0015*epi))
%%to be used in the episode
if rand() < epsilon
    len_action = 7;
    action1 = randi(len_action,1); %Explore action space
else
    [maxval1 argmax1] = max(Q1(state1,:)); %Exploit learned values
    action1 = argmax1;
end
