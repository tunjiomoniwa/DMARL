function ansQ2 = update_Q2(Q2, current_state1, new_state1, action1, reward1, alpha, gamma)
    
    ansQ2 = Q2(current_state1,action1)+alpha.*(reward1+gamma.*max(Q2(new_state1,:))-Q2(current_state1,action1));
end

