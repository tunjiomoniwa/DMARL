function Team_factor = neighbourhood_Reward(tot_obs_over_, tot_oldConn_count_)
    if tot_obs_over_ > tot_oldConn_count_ 
        Team_factor = 1;            
    else 
        Team_factor = -1;           

end