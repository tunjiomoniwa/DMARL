function action = select_action(epsilon, statex, Qval)

if rand() < epsilon
    len_action = 7;
    action = randi(len_action,1); %Explore action space
else
    [maxval1 argmax1] = max(Qval(statex,:)); %Exploit learned values
    action = argmax1;
end
