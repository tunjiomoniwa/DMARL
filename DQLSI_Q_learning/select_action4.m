function action4 = select_action4(epsilon, state4, Q4)

if rand() < epsilon
    len_action = 7;
    action4 = randi(len_action,1); %Explore action space
else
    [maxval4 argmax4] = max(Q4(state4,:)); %Exploit learned values
    action4 = argmax4;
end
