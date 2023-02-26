function action = action_selection(obs, obs_over, MAX_user_connections, epsilon, current_state, Q)

    if obs ||obs_over>=MAX_user_connections
        action = 7;
    else
        action = select_action(epsilon, current_state, Q);          
end