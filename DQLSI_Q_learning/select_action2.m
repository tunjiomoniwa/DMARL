function act2 = select_action2(epsilon, state2, Q2)
% linear
% epsilon =1-(epi/1000)
% 
% exp decay
% epsilon =float(np.exp(-0.0015*epi))
%%to be used in the episode
if rand() < epsilon
    len_action = 7;
    act2 = randi(len_action,1); %Explore action space
else
    [maxval2 argmax2] = max(Q2(state2,:)); %Exploit learned values
    act2 = argmax2;
end
