function reward = self_Reward(obs_over, oldConn_count)
    if obs_over < oldConn_count % && obs3(7) == 0
        reward = -1;
    elseif obs_over == oldConn_count %&& obs3(7) == 0
        reward = 0;
    else
        reward = 1;         
            
end
