function ansQ1 = update_Q(Q, current_state, new_state, action, reward, alpha, gamma)
    
    ansQ1 = Q(current_state,action)+alpha.*(reward+gamma.*max(Q(new_state,:))-Q(current_state,action));
end

