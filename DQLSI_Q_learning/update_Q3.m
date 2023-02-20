function ansQ3 = update_Q3(Q3, current_state3, new_state3, action3, reward3, alpha, gamma)
    
    ansQ3 = Q3(current_state3,action3)+alpha.*(reward3+gamma.*max(Q3(new_state3,:))-Q3(current_state3,action3));
end

