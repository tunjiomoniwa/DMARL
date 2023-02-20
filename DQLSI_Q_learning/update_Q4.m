function ansQ4 = update_Q4(Q4, current_state4, new_state4, action4, reward4, alpha, gamma)
    
    ansQ4 = Q4(current_state4,action4)+alpha.*(reward4+gamma.*max(Q4(new_state4,:))-Q4(current_state4,action4));
end

