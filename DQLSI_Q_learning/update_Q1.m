function ansQ1 = update_Q1(Q1, current_state1, new_state1, action1, reward1, alpha, gamma)
    
    ansQ1 = Q1(current_state1,action1)+alpha.*(reward1+gamma.*max(Q1(new_state1,:))-Q1(current_state1,action1));
end

