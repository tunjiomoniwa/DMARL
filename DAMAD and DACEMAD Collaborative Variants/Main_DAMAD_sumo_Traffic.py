import os
import gym
import torch
import numpy as np
#from Env_wrappers import make_env
#from utils import plot_learning_curve
from torch.utils.tensorboard import SummaryWriter
from DDQAgent import DoubleDQAgent
from DuelingDQAgent import DuelingDQAgent
#from MeanTeacherAgent import MeanTeacherAgent
######
from sumo_position_data import update_low
from sumo_position_data import update_high
from sumo_position_data import update_M50
from sumo_position_data import update_DCC_Ped
### step files
from RWP import RWP
from GMM import GMM
from RW import RW
from stepOverlap10nodes_static import stepOverlap10nodes_static
from stepBL_static import stepBL_static
from neighbor_reward_factor import neighbor_reward_factor
from neighbor_reward_factor import neighbor_val
from neighbor_reward_factor import neighbor_rew_fxn
from neighbor_reward_factor import agent_i_rew_fxn
from neighbor_reward_factor import done_agent_i_rew
from step_fairness import step_fairness ##
from CalcDistance import CalcDistance
import random
import matplotlib.pyplot as plt
from throughput_calc import TP

###Reference


if __name__ == '__main__':
    mode = "Double"
    best_score = -np.inf
    test_mode = False 
    render = False 
    n_games = 250
    Max_iterations = 10# 1400
    epsilon = 1
    uavs = 10
    n_games_exp = 250
    #disp_period = 249  ##epi to display
    
    
    if mode == "Double":
        agent1 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent2 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent3 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent4 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent5 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent6 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent7 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent8 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent9 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent10 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
         
        
    else:
        agent1 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent2 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent3 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent4 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent5 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent6 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=7, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent7 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent8 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent9 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        agent10 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                        obs_dims=8,
                        num_actions=5, 
                        mem_size=10000,
                        mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                        env_name='Multi_UAVBS_Deployment',
                        algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
        


    if test_mode:
        agent1.load_models()
        agent2.load_models()
        agent3.load_models()
        agent4.load_models()
        agent5.load_models()
        agent6.load_models()
        agent7.load_models()
        agent8.load_models()
        agent9.load_models()
        agent10.load_models()
         

    n_steps = 0
    scores1, eps_history1, steps_arr1 = [], [], []
    scores2, eps_history2, steps_arr2 = [], [], []
    scores3, eps_history3, steps_arr3 = [], [], []
    scores4, eps_history4, steps_arr4 = [], [], []
    scores5, eps_history5, steps_arr5 = [], [], []
    scores6, eps_history6, steps_arr6 = [], [], []
    scores7, eps_history7, steps_arr7 = [], [], []
    scores8, eps_history8, steps_arr8 = [], [], []
    scores9, eps_history9, steps_arr9 = [], [], []
    scores10, eps_history10, steps_arr10 = [], [], []
     
    
    writer1 = SummaryWriter(os.path.join(agent1.checkpoint_dir, 'logs'))
    writer2 = SummaryWriter(os.path.join(agent2.checkpoint_dir, 'logs'))
    writer3 = SummaryWriter(os.path.join(agent3.checkpoint_dir, 'logs'))
    writer4 = SummaryWriter(os.path.join(agent4.checkpoint_dir, 'logs'))
    writer5 = SummaryWriter(os.path.join(agent5.checkpoint_dir, 'logs'))
    writer6 = SummaryWriter(os.path.join(agent6.checkpoint_dir, 'logs'))
    writer7 = SummaryWriter(os.path.join(agent7.checkpoint_dir, 'logs'))
    writer8 = SummaryWriter(os.path.join(agent8.checkpoint_dir, 'logs'))
    writer9 = SummaryWriter(os.path.join(agent9.checkpoint_dir, 'logs'))
    writer10 = SummaryWriter(os.path.join(agent10.checkpoint_dir, 'logs'))
     
    
    
    r_sums1 = []  # stores rewards of each epsiode
    r_sums2 = []
    r_sums3 = []
    r_sums4 = []
    r_sums5 = []
    r_sums6 = []
    r_sums7 = []
    r_sums8 = []
    r_sums9 = []
    r_sums10 = []
     

    devfairness = []
    fairfact = []
    fairness_dev =0.99
    efficiency = []
    throughput = []
    vehicles_deployed = []

    MAX_USER_CONNECT_ALLOWED = 150
    

        
    dist_1 = []
    dist_2 = []
    dist_3 = []
    dist_4 = []
    dist_5 = []
    dist_6 = []
    dist_7 = []
    dist_8 = []
    dist_9 = []
    dist_10 = []
     
    

    rewcumsum1 = 0
    rewcumsum2 = 0
    rewcumsum3 = 0
    rewcumsum4 = 0
    rewcumsum5 = 0
    rewcumsum6 = 0
    rewcumsum7 = 0
    rewcumsum8 = 0
    rewcumsum9 = 0
    rewcumsum10 = 0

    noise =-130;
    beta = 1;
    P = -7;  #UAVs transmit power in dB
    Bw =1000000; #Bandwidth
    

    UAV1cov = [] # stores coverage values
    UAV2cov = []
    UAV3cov = []
    UAV4cov = []
    UAV5cov = []
    UAV6cov = []
    UAV7cov = []
    UAV8cov = []
    UAV9cov = []
    UAV10cov = []
     
    UAV1eng = [] # stores energy values
    UAV2eng = []
    UAV3eng = []
    UAV4eng = []
    UAV5eng = []
    UAV6eng = []
    UAV7eng = []
    UAV8eng = []
    UAV9eng = []
    UAV10eng = []

    x1_ = []
    y1_ = []
    z1_ = []
    x2_ = []
    y2_ = []
    z2_ = []
    x3_ = []
    y3_ = []
    z3_ = []
    x4_ = []
    y4_ = []
    z4_ = []
    x5_ = []
    y5_ = []
    z5_ = []
    x6_ = []
    y6_ = []
    z6_ = []
    x7_ = []
    y7_ = []
    z7_ = []
    x8_ = []
    y8_ = []
    z8_ = []
    x9_ = []
    y9_ = []
    z9_ = []
    x10_ = []
    y10_ = []
    z10_ = []



    #SUMO TRAFFIC LOADED BASED ON DEPLOYMENT TIMESTEP
    data_bank_low = []
    for i in range(93, Max_iterations+94):
        data_bank_low.append(np.array(update_M50(i)))
        print('Loading sumo M50 traffic data at time',i)

        
    #sumo_veh_at_t_high = data_bank_high[0]
    sumo_veh_at_t_low = data_bank_low[0]


    

    iter_store = []

    x1 = 450
    y1 = 750
    z1 = 120
    e1 = 0
    old_cov1 = 40;
    old_cov2 = 40;
    old_cov3 = 40;
    old_cov4 = 40;
    old_cov5 = 40;
    old_cov6 = 40;
    old_cov7 = 40;
    old_cov8 = 40;
    old_cov9 = 40;
    old_cov10 = 40;
     
        
    ##126 data points ...Drumcondra South A ITM grid

    bin_data_x = [1000,997.072214800000,984.948617500000,968.633702900000,964.125221200000,956.059447200000,928.648016900000,928.249333000000,888.622523100000,867.742960500000,861.542904600000,855.785721900000,851.846195100000,848.952267400000,847.336525200000,847.126728700000,846.811716100000,825.096330400000,816.985975300000,808.126770600000,804.605549000000,797.456432800000,785.420204200000,776.696869100000,769.980955000000,767.678347600000,766.915782700000,759.835608300000,756.049541000000,753.632662900000,745.878428600000,736.217639600000,719.658609900000,719.071987400000,704.276665700000,695.424363900000,689.327984100000,684.716734700000,683.748623000000,683.607361500000,683.580131300000,650.748082500000,630.352702400000,622.543501600000,609.747665300000,602.082525400000,602.082518600000,570.459320500000,567.018374200000,566.440428500000,562.280497800000,562.256017800000,551.749866100000,531.433256500000,530.158762100000,521.746454900000,515.133485700000,493.884553000000,492.313895500000,491.677973200000,491.656035500000,474.791411700000,473.231290000000,472.737635200000,470.656263800000,469.771710700000,453.141372200000,450.284718900000,447.988944800000,435.209393800000,433.272831800000,425.833810000000,424.465696600000,420.889748600000,419.393970000000,417.210188000000,412.895384200000,409.238572500000,398.531274000000,398.007674200000,391.810862400000,383.864834100000,381.839045500000,369.183443100000,356.348556000000,354.959546600000,346.420178700000,345.302137800000,325.985001100000,325.787646500000,313.899747000000,281.855623900000,279.781143100000,243.229671600000,204.572930200000,199.989874200000,193.494261800000,163.236364900000,161.693109700000,155.458120200000,154.743394000000,143.810289800000,138.712356400000,138.154289700000,136.678000900000,136.385108000000,136.084182800000,134.768326100000,114.864580500000,112.825183900000,89.6626356700000,88.6022148800000,77.4445585200000,74.7585542700000,69.1688215100000,65.0693127600000,63.0130482600000,54.8292877700000,53.2063741300000,49.4219996500000,48.3594727800000,44.5171850900000,27.3815095100000,9.69356873600000,8.34480656800000,0];
    bin_data_y = [838.398868100000,843.733994400000,946.673674600000,259.256249600000,455.263182200000,263.042977600000,395.489732800000,944.564006000000,514.217232800000,965.918810900000,313.200308500000,755.546562000000,817.002928200000,918.420802100000,863.150606500000,932.362588800000,948.164999300000,957.969224600000,295.935122500000,949.981906600000,283.762051600000,935.080509800000,249.530056500000,878.051621700000,855.755822700000,398.766938400000,581.404557100000,570.443970700000,411.115106300000,561.001765300000,423.127999700000,814.186888300000,161.322759100000,828.225447200000,768.995452500000,143.796157500000,739.710142800000,677.351349400000,961.460071700000,680.399967400000,958.121294300000,949.363117300000,489.510939900000,656.685584500000,498.905718500000,627.070506800000,627.070508500000,519.046665800000,491.407273900000,589.109847700000,467.723449500000,582.721194200000,66.0667508700000,525.400091000000,534.647011100000,501.146206500000,931.896009200000,940.049384800000,940.700756400000,437.372658300000,766.488012400000,416.139054400000,946.963998700000,55.9944530100000,381.753274000000,394.617806200000,769.463159300000,331.638592500000,818.291653200000,623.276709400000,623.283162800000,0,277.416850400000,639.178189000000,250.346103400000,640.591221400000,692.037540800000,226.136050200000,1000,651.091180800000,727.525674600000,175.332604100000,69.2575938800000,756.198581700000,134.771604200000,899.477666500000,106.474706100000,156.782706700000,174.192763300000,33.2932403600000,186.370249400000,716.554660000000,717.729082500000,244.511768000000,680.584535900000,277.188062900000,68.3115930500000,482.470721700000,163.578638300000,382.180183800000,265.378545000000,214.154550000000,806.202957300000,322.849284400000,387.509206100000,376.498882100000,808.605664600000,332.560862100000,230.156725600000,351.822346000000,274.170392800000,254.273308100000,779.628304000000,761.528459400000,535.630439300000,37.4594185200000,538.800679200000,530.744887200000,542.821760300000,541.853545600000,534.260882300000,982.283337100000,866.495864100000,876.241797800000,875.441684800000,551.001179000000];

    random.seed(1)
    syn_data_x = random.sample(range(40, 960), 200-126)
    syn_data_y = random.sample(range(40, 960), 200-126)
    
     

    cc= update_low(0)
    xsef = cc[0]
    ysef = cc[1] 

    
    
    x1 =  random.randint(250, 400)
    y1 =  random.randint(250, 500)
    z1 = 120
    e1 = 0
    dist1 = 0 
    x2 = random.randint(200, 450)
    y2 = random.randint(200, 600)
    z2 = 120
    e2 = 0
    dist2 = 0 
    x3 =  random.randint(200, 350)
    y3 =  random.randint(300, 550)
    z3 = 120
    e3 = 0
    dist3 = 0 
    x4 =  random.randint(200, 300)
    y4 =  random.randint(500, 850)
    z4 = 120
    e4 = 0
    dist4 = 0

    ####
    x5 =  random.randint(200, 400)
    y5 =  random.randint(600, 800)
    z5 = 120
    e5 = 0
    dist5 = 0
    ##
    x6 =  random.randint(600, 800)
    y6 =  random.randint(200, 400)
    z6 = 120
    e6 = 0
    dist6 = 0
    ##
    x7 =  random.randint(500, 850)
    y7 =  random.randint(200, 400)
    z7 = 120
    e7 = 0
    dist7 = 0
    ##
    x8 =  random.randint(500, 800)
    y8 =  random.randint(300, 600)
    z8 = 120
    e8 = 0
    dist8 = 0

    x9 =  random.randint(500, 800)
    y9 =  random.randint(650, 850)
    z9 = 120
    e9 = 0
    dist9 = 0

    x10 =  random.randint(600, 800)
    y10 =  random.randint(550, 850)
    z10 = 120
    e10 = 0
    dist10 = 0

     


    x1_target  = x1
    y1_target  = y1
    x2_target  = x2
    y2_target  = y2
    x3_target  = x3
    y3_target  = y3
    x4_target  = x4
    y4_target  = y4
    x5_target  = x5
    y5_target  = y5
    x6_target  = x6
    y6_target  = y6
    x7_target  = x7
    y7_target  = y7
    x8_target  = x8
    y8_target  = y8
    x9_target  = x9
    y9_target  = y9
    x10_target  = x10
    y10_target  = y10


    past_cov1 =0
    past_cov2 =0
    past_cov3 =0
    past_cov4 =0
    past_cov5 =0
    past_cov6 =0
    past_cov7 =0
    past_cov8 =0
    past_cov9 =0
    past_cov10 =0

    thresh=40

    dense_goal1 = (x1> x1_target-thresh) and (x1<x1_target+thresh) and (y1>y1_target-thresh) and (y1<y1_target+thresh)
    dense_goal2 = (x2> x2_target-thresh) and (x2<x2_target+thresh) and (y2>y2_target-thresh) and (y2<y2_target+thresh)
    dense_goal3 = (x3> x3_target-thresh) and (x3<x3_target+thresh) and (y3>y3_target-thresh) and (y3<y3_target+thresh)
    dense_goal4 = (x4> x4_target-thresh) and (x4<x4_target+thresh) and (y4>y4_target-thresh) and (y4<y4_target+thresh)
    dense_goal5 = (x5> x5_target-thresh) and (x5<x5_target+thresh) and (y5>y5_target-thresh) and (y5<y5_target+thresh)
    dense_goal6 = (x6> x6_target-thresh) and (x6<x6_target+thresh) and (y6>y6_target-thresh) and (y6<y6_target+thresh)
    dense_goal7 = (x7> x7_target-thresh) and (x7<x7_target+thresh) and (y7>y7_target-thresh) and (y7<y7_target+thresh)
    dense_goal8 = (x8> x8_target-thresh) and (x8<x8_target+thresh) and (y8>y8_target-thresh) and (y8<y8_target+thresh)
    dense_goal9 = (x9> x9_target-thresh) and (x9<x9_target+thresh) and (y9>y9_target-thresh) and (y9<y9_target+thresh)
    dense_goal10 = (x10>x10_target-thresh) and (x10<x10_target+thresh) and (y10>y10_target-thresh) and (y10<y10_target+thresh) 
    
    #print(xsef)
    #print(ysef)

    random.shuffle



    for i in range(n_games):      
         
        
        #SUMO TRAFFIC LOADED BASED ON DEPLOYMENT TIMESTEP
        sumo_veh_at_t = data_bank_low[0]           
           
        xsef = sumo_veh_at_t[0] #np.concatenate((xsef_mob, xblock1, xblock2, xblock3, xblock4))
          
        ysef = sumo_veh_at_t[1] #np.concatenate((ysef_mob, yblock1, yblock2, yblock3, yblock4))
        
        done = False
        done1 = False
        done2 = False
        done3 = False
        done4 = False
        done5 = False
        done6 = False
        done7 = False
        done8 = False
        done9 = False
        done10 = False

        x1_ = []
        y1_ = []
        z1_ = []
        x2_ = []
        y2_ = []
        z2_ = []
        x3_ = []
        y3_ = []
        z3_ = []
        x4_ = []
        y4_ = []
        z4_ = []
        x5_ = []
        y5_ = []
        z5_ = []
        x6_ = []
        y6_ = []
        z6_ = []
        x7_ = []
        y7_ = []
        z7_ = []
        x8_ = []
        y8_ = []
        z8_ = []
        x9_ = []
        y9_ = []
        z9_ = []
        x10_ = []
        y10_ = []
        z10_ = []
        
        score = 0
        
    
        #observation = env.reset()
        s1 = np.array([x1, y1, z1, 5, 0, x1_target, y1_target, ((0+1)/(past_cov1+1))])
        s2 = np.array([x2, y2, z2, 5, 0, x2_target, y2_target, ((0+1)/(past_cov2+1))])
        s3 = np.array([x3, y3, z3, 5, 0, x3_target, y3_target, ((0+1)/(past_cov3+1))])
        s4 = np.array([x4, y4, z4, 5, 0, x4_target, y4_target, ((0+1)/(past_cov4+1))])
        s5 = np.array([x5, y5, z5, 5, 0, x5_target, y5_target, ((0+1)/(past_cov5+1))])
        s6 = np.array([x6, y6, z6, 5, 0, x6_target, y6_target, ((0+1)/(past_cov6+1))])
        s7 = np.array([x7, y7, z7, 5, 0, x7_target, y7_target, ((0+1)/(past_cov7+1))])
        s8 = np.array([x8, y8, z8, 5, 0, x8_target, y8_target, ((0+1)/(past_cov8+1))])
        s9 = np.array([x9, y9, z9, 5, 0, x9_target, y9_target, ((0+1)/(past_cov9+1))])
        s10 = np.array([x10, y10, z10, 5, 0, x10_target, y10_target, ((0+1)/(past_cov10+1))])


        sprime1val = np.array([x1, y1, z1, 5, 0, 0, 0, 0])
        sprime2val = np.array([x2, y2, z2, 5, 0, 0, 0, 0])
        sprime3val = np.array([x3, y3, z3, 5, 0, 0, 0, 0])
        sprime4val = np.array([x4, y4, z4, 5, 0, 0, 0, 0])
        sprime5val = np.array([x5, y5, z5, 5, 0, 0, 0, 0])
        sprime6val = np.array([x6, y6, z6, 5, 0, 0, 0, 0])
        sprime7val = np.array([x7, y7, z7, 5, 0, 0, 0, 0])
        sprime8val = np.array([x8, y8, z8, 5, 0, 0, 0, 0])
        sprime9val = np.array([x9, y9, z9, 5, 0, 0, 0, 0])
        sprime10val = np.array([x10, y10, z10, 5, 0, 0, 0, 0])
         
       
        dense_goal1 = (x1> x1_target-thresh) and (x1<x1_target+thresh) and (y1>y1_target-thresh) and (y1<y1_target+thresh)
        dense_goal2 = (x2> x2_target-thresh) and (x2<x2_target+thresh) and (y2>y2_target-thresh) and (y2<y2_target+thresh)
        dense_goal3 = (x3> x3_target-thresh) and (x3<x3_target+thresh) and (y3>y3_target-thresh) and (y3<y3_target+thresh)
        dense_goal4 = (x4> x4_target-thresh) and (x4<x4_target+thresh) and (y4>y4_target-thresh) and (y4<y4_target+thresh)
        dense_goal5 = (x5> x5_target-thresh) and (x5<x5_target+thresh) and (y5>y5_target-thresh) and (y5<y5_target+thresh)
        dense_goal6 = (x6> x6_target-thresh) and (x6<x6_target+thresh) and (y6>y6_target-thresh) and (y6<y6_target+thresh)
        dense_goal7 = (x7> x7_target-thresh) and (x7<x7_target+thresh) and (y7>y7_target-thresh) and (y7<y7_target+thresh)
        dense_goal8 = (x8> x8_target-thresh) and (x8<x8_target+thresh) and (y8>y8_target-thresh) and (y8<y8_target+thresh)
        dense_goal9 = (x9> x9_target-thresh) and (x9<x9_target+thresh) and (y9>y9_target-thresh) and (y9<y9_target+thresh)
        dense_goal10 = (x10>x10_target-thresh) and (x10<x10_target+thresh) and (y10>y10_target-thresh) and (y10<y10_target+thresh) 
##        
        action1 = random.randint(0,4)
        action2 = random.randint(0,4)
        action3 = random.randint(0,4)
        action4 = random.randint(0,4)
        action5 = random.randint(0,4)
        action6 = random.randint(0,4)
        action7 = random.randint(0,4)
        action8 = random.randint(0,4)
        action9 = random.randint(0,4)
        action10 = random.randint(0,4)
         
        
        sprime1 = stepBL_static(action1, x1, y1, z1, e1, dist1)
        sprime2 = stepBL_static(action2, x2, y2, z2, e2, dist2)
        sprime3 = stepBL_static(action3, x3, y3, z3, e3, dist3)
        sprime4 = stepBL_static(action4, x4, y4, z4, e4, dist4)
        sprime5 = stepBL_static(action5, x5, y5, z5, e5, dist5)
        sprime6 = stepBL_static(action6, x6, y6, z6, e6, dist6)
        sprime7 = stepBL_static(action7, x7, y7, z7, e7, dist7)
        sprime8 = stepBL_static(action8, x8, y8, z8, e8, dist8)
        sprime9 = stepBL_static(action9, x9, y9, z9, e9, dist9)
        sprime10 = stepBL_static(action10, x10, y10, z10, e10, dist10)

        
         
        
        cov_obs = stepOverlap10nodes_static(sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2],  sprime6[0], sprime6[1], sprime6[2],  sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2], xsef, ysef)

       
        old_cov1 = 50
        old_cov2 = 50
        old_cov3 = 50
        old_cov4 = 50
        old_cov5 = 50
        old_cov6 = 50
        old_cov7 = 50
        old_cov8 = 50
        old_cov9 = 50
        old_cov10 = 50
         
        
        old_ene1 = sprime1[3]
        old_ene2 = sprime2[3]
        old_ene3 = sprime3[3]
        old_ene4 = sprime4[3]
        old_ene5 = sprime5[3]
        old_ene6 = sprime6[3]
        old_ene7 = sprime7[3]
        old_ene8 = sprime8[3]
        old_ene9 = sprime9[3]
        old_ene10 = sprime10[3]
        

        tp1 = 0
        tp2 = 0
        tp3 = 0
        tp4 = 0
        tp5 = 0
        tp6 = 0
        tp7 = 0
        tp8 = 0
        tp9 = 0
        tp10 = 0
        

        max_cov_obs =0

        fair_sum = 0
        fairness = 0
        done1 = False
        done2 = False
        done3 = False
        done4 = False
        done5 = False
        done6 = False
        done7 = False
        done8 = False
        done9 = False
        done10 = False
         

        covd1 = 0
        covd2 = 0
        covd3 = 0
        covd4 = 0
        covd5 = 0
        covd6 = 0
        covd7 = 0
        covd8 = 0
        covd9 = 0
        covd10 = 0
         
        
        energy_UAV1 = sprime1[3]
        energy_UAV2 = sprime2[3]
        energy_UAV3 = sprime3[3]
        energy_UAV4 = sprime4[3]
        energy_UAV5 = sprime5[3]
        energy_UAV6 = sprime6[3]
        energy_UAV7 = sprime7[3]
        energy_UAV8 = sprime8[3]
        energy_UAV9 = sprime9[3]
        energy_UAV10 = sprime10[3]
         

        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        c5 = 0
        c6 = 0
        c7 = 0
        c8 = 0
        c9 = 0
        c10 = 0
         
        
        r_sum1 = 0
        r_sum2 = 0
        r_sum3 = 0
        r_sum4 = 0
        r_sum5 = 0
        r_sum6 = 0
        r_sum7 = 0
        r_sum8 = 0
        r_sum9 = 0
        r_sum10 = 0
         
        
        itern = 0
        

        while itern<Max_iterations:

           

            ###
            #rwp_model = RWP(rwp_model[0], rwp_model[1])
            #rw_model = RW(rw_model[0], rw_model[1])
            #gmm_model = GMM(gmm_model[0], gmm_model[1])
            #print(rwp_model[0])
            #print(rwp_model[1])

            #xsef = np.concatenate((rwp_model[0], xblock1, xblock2, xblock3, xblock4))
            #ysef = np.concatenate((rwp_model[1], yblock1, yblock2, yblock3, yblock4))

            #xsef = np.concatenate((rw_model[0], xblock1, xblock2, xblock3, xblock4))
            #ysef = np.concatenate((rw_model[1], yblock1, yblock2, yblock3, yblock4))

            #xsef = np.concatenate((gmm_model[0], xblock1, xblock2, xblock3, xblock4))
            #ysef = np.concatenate((gmm_model[1], yblock1, yblock2, yblock3, yblock4))


            #SUMO TRAFFIC LOADED BASED ON DEPLOYMENT TIMESTEP
            sumo_veh_at_t = data_bank_low[itern]            
            xsef = sumo_veh_at_t[0]           
            ysef = sumo_veh_at_t[1] 
            

            run_done = 7  # deactivate UAV
            
            if c1>=run_done:
                action1 = 0
            else: 
                action1 =  agent1.get_action(s1, epsilon)
                
            if c2>=run_done:
                action2 = 0
            else: 
                action2 = agent2.get_action(s2, epsilon)
                
            if c3>=run_done:
                action3 = 0
            else: 
                action3 = agent3.get_action(s3, epsilon)
                
            if c4>=run_done:
                action4 = 0
            else: 
                action4 = agent4.get_action(s4, epsilon)

            if c5>=run_done:
                action5 = 0
            else: 
                action5 = agent5.get_action(s5, epsilon)

            if c6>=run_done:
                action6 = 0
            else: 
                action6 = agent6.get_action(s6, epsilon)

            if c7>=run_done:
                action7 = 0
            else: 
                action7 = agent7.get_action(s7, epsilon)

            if c8>=run_done:
                action8 = 0
            else: 
                action8 = agent8.get_action(s8, epsilon)

            if c9>=run_done:
                action9 = 0
            else: 
                action9 = agent9.get_action(s9, epsilon)

            if c10>=run_done:
                action10 = 0
            else: 
                action10 = agent10.get_action(s10, epsilon)

            
            #new_observation, reward, done, _ = env.step(action1)
            sprime1 = stepBL_static(action1, sprime1[0], sprime1[1], sprime1[2], sprime1[3], sprime1[5])
            sprime2 = stepBL_static(action2, sprime2[0], sprime2[1], sprime2[2], sprime2[3], sprime2[5])
            sprime3 = stepBL_static(action3, sprime3[0], sprime3[1], sprime3[2], sprime3[3], sprime3[5])
            sprime4 = stepBL_static(action4, sprime4[0], sprime4[1], sprime4[2], sprime4[3], sprime4[5])
            sprime5 = stepBL_static(action5, sprime5[0], sprime5[1], sprime5[2], sprime5[3], sprime5[5])
            sprime6 = stepBL_static(action6, sprime6[0], sprime6[1], sprime6[2], sprime6[3], sprime6[5])
            sprime7 = stepBL_static(action7, sprime7[0], sprime7[1], sprime7[2], sprime7[3], sprime7[5])
            sprime8 = stepBL_static(action8, sprime8[0], sprime8[1], sprime8[2], sprime8[3], sprime8[5])
            sprime9 = stepBL_static(action9, sprime9[0], sprime9[1], sprime9[2], sprime9[3], sprime9[5])
            sprime10 = stepBL_static(action10, sprime10[0], sprime10[1], sprime10[2], sprime10[3], sprime10[5])
             

            
            cov_obs = stepOverlap10nodes_static(sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2], xsef, ysef)

            
            ave_ene_old1 = old_ene1/(1+itern)
            present_ave_ene1 = sprime1[3]/(2+itern)
            ave_ene_old2 = old_ene2/(1+itern)
            present_ave_ene2 = sprime2[3]/(2+itern)
            ave_ene_old3 = old_ene3/(1+itern)
            present_ave_ene3 = sprime3[3]/(2+itern)
            ave_ene_old4 = old_ene4/(1+itern)
            present_ave_ene4 = sprime4[3]/(2+itern)
            ave_ene_old5 = old_ene5/(1+itern)
            present_ave_ene5 = sprime5[3]/(2+itern)
            ave_ene_old6 = old_ene6/(1+itern)
            present_ave_ene6 = sprime6[3]/(2+itern)
            ave_ene_old7 = old_ene7/(1+itern)
            present_ave_ene7 = sprime7[3]/(2+itern)
            ave_ene_old8 = old_ene8/(1+itern)
            present_ave_ene8 = sprime8[3]/(2+itern)
            ave_ene_old9 = old_ene9/(1+itern)
            present_ave_ene9 = sprime9[3]/(2+itern)            
            ave_ene_old10 = old_ene10/(1+itern)
            present_ave_ene10 = sprime10[3]/(2+itern)            
                  

            #####Get closest neighbour index fxn here

            cl_ne_1 = neighbor_reward_factor(sprime1[0], sprime1[1], sprime1[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            cl_ne_2 = neighbor_reward_factor(sprime2[0], sprime2[1], sprime2[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            cl_ne_3 = neighbor_reward_factor(sprime3[0], sprime3[1], sprime3[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            cl_ne_4 = neighbor_reward_factor(sprime4[0], sprime4[1], sprime4[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            cl_ne_5 = neighbor_reward_factor(sprime5[0], sprime5[1], sprime5[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            cl_ne_6 = neighbor_reward_factor(sprime6[0], sprime6[1], sprime6[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            cl_ne_7 = neighbor_reward_factor(sprime7[0], sprime7[1], sprime7[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            cl_ne_8 = neighbor_reward_factor(sprime8[0], sprime8[1], sprime8[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            cl_ne_9 = neighbor_reward_factor(sprime9[0], sprime9[1], sprime9[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            cl_ne_10 = neighbor_reward_factor(sprime10[0], sprime10[1], sprime10[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
             

            #### distance value of UAVs nearest neighbours           
            N_1 = neighbor_val(sprime1[0], sprime1[1], sprime1[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            N_2 = neighbor_val(sprime2[0], sprime2[1], sprime2[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            N_3 = neighbor_val(sprime3[0], sprime3[1], sprime3[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            N_4 = neighbor_val(sprime4[0], sprime4[1], sprime4[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            N_5 = neighbor_val(sprime5[0], sprime5[1], sprime5[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            N_6 = neighbor_val(sprime6[0], sprime6[1], sprime6[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            N_7 = neighbor_val(sprime7[0], sprime7[1], sprime7[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            N_8 = neighbor_val(sprime8[0], sprime8[1], sprime8[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            N_9 = neighbor_val(sprime9[0], sprime9[1], sprime9[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
            N_10 = neighbor_val(sprime10[0], sprime10[1], sprime10[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2])
                        
            past_cov1 = max(cov_obs[0],past_cov1)
           
            if cov_obs[0]>=past_cov1:                
                x1_target = sprime1[0]
                y1_target = sprime1[1]
            else:
                x1_target = x1_target
                y1_target = y1_target                
            
            if cov_obs[1]>=past_cov2:                
                x2_target = sprime2[0]
                y2_target = sprime2[1]
            else:
                x2_target = x2_target
                y2_target = y2_target
            #######
            if cov_obs[2]>=past_cov3:                
                x3_target = sprime3[0]
                y3_target = sprime3[1]
            else:
                x3_target = x3_target
                y3_target = y3_target
            ######
            if cov_obs[3]>=past_cov4:                
                x4_target = sprime4[0]
                y4_target = sprime4[1]
            else:
                x4_target = x4_target
                y4_target = y4_target
            #######
            if cov_obs[4]>=past_cov5:                
                x5_target = sprime5[0]
                y5_target = sprime5[1]
            else:
                x5_target = x5_target
                y5_target = y5_target
            #######
            if cov_obs[5]>=past_cov6:                
                x6_target = sprime6[0]
                y6_target = sprime6[1]
            else:
                x6_target = x6_target
                y6_target = y6_target
            #######
            if cov_obs[6]>=past_cov7:                
                x7_target = sprime7[0]
                y7_target = sprime7[1]
            else:
                x7_target = x7_target
                y7_target = y7_target
            #######
            if cov_obs[7]>=past_cov8:                
                x8_target = sprime8[0]
                y8_target = sprime8[1]
            else:
                x8_target = x8_target
                y8_target = y8_target
            #######
            if cov_obs[8]>=past_cov9:                
                x9_target = sprime9[0]
                y9_target = sprime9[1]
            else:
                x9_target = x9_target
                y9_target = y9_target
            #######
            if cov_obs[9]>=past_cov10:                
                x10_target = sprime10[0]
                y10_target = sprime10[1]
            else:
                x10_target = x10_target
                y10_target = y10_target

            oldcc = [old_cov1,old_cov2,old_cov3,old_cov4,old_cov5, old_cov6, old_cov7, old_cov8, old_cov9, old_cov10]


            ####Neighbour coverage-based cooperative factor relative to each i{th} agent
            mu1 = neighbor_rew_fxn(cov_obs[cl_ne_1[1]],cov_obs[cl_ne_1[2]],cov_obs[cl_ne_1[3]], cov_obs[cl_ne_1[4]],cov_obs[cl_ne_1[5]] ,cov_obs[cl_ne_1[6]], oldcc[cl_ne_1[1]], oldcc[cl_ne_1[2]], oldcc[cl_ne_1[3]], oldcc[cl_ne_1[4]], oldcc[cl_ne_1[5]], oldcc[cl_ne_1[6]], cov_obs[0], past_cov1)
            mu2 = neighbor_rew_fxn(cov_obs[cl_ne_2[1]],cov_obs[cl_ne_2[2]],cov_obs[cl_ne_2[3]], cov_obs[cl_ne_2[4]],cov_obs[cl_ne_2[5]],cov_obs[cl_ne_2[6]], oldcc[cl_ne_2[1]], oldcc[cl_ne_2[2]], oldcc[cl_ne_2[3]], oldcc[cl_ne_2[4]], oldcc[cl_ne_2[5]], oldcc[cl_ne_2[6]], cov_obs[1], past_cov2)
            mu3 = neighbor_rew_fxn(cov_obs[cl_ne_3[1]],cov_obs[cl_ne_3[2]],cov_obs[cl_ne_3[3]], cov_obs[cl_ne_3[4]],cov_obs[cl_ne_3[5]],cov_obs[cl_ne_3[6]], oldcc[cl_ne_3[1]], oldcc[cl_ne_3[2]], oldcc[cl_ne_3[3]], oldcc[cl_ne_3[4]], oldcc[cl_ne_3[5]], oldcc[cl_ne_3[6]], cov_obs[2], past_cov3)
            mu4 = neighbor_rew_fxn(cov_obs[cl_ne_4[1]],cov_obs[cl_ne_4[2]],cov_obs[cl_ne_4[3]], cov_obs[cl_ne_4[4]],cov_obs[cl_ne_4[5]],cov_obs[cl_ne_4[6]], oldcc[cl_ne_4[1]], oldcc[cl_ne_4[2]], oldcc[cl_ne_4[3]], oldcc[cl_ne_4[4]], oldcc[cl_ne_4[5]], oldcc[cl_ne_4[6]], cov_obs[3], past_cov4)
            mu5 = neighbor_rew_fxn(cov_obs[cl_ne_5[1]],cov_obs[cl_ne_5[2]],cov_obs[cl_ne_5[3]], cov_obs[cl_ne_5[4]],cov_obs[cl_ne_5[5]],cov_obs[cl_ne_5[6]], oldcc[cl_ne_5[1]], oldcc[cl_ne_5[2]], oldcc[cl_ne_5[3]], oldcc[cl_ne_5[4]], oldcc[cl_ne_5[5]], oldcc[cl_ne_5[6]], cov_obs[4], past_cov5)
            mu6 = neighbor_rew_fxn(cov_obs[cl_ne_6[1]],cov_obs[cl_ne_6[2]],cov_obs[cl_ne_6[3]], cov_obs[cl_ne_6[4]],cov_obs[cl_ne_6[5]],cov_obs[cl_ne_6[6]], oldcc[cl_ne_6[1]], oldcc[cl_ne_6[2]], oldcc[cl_ne_6[3]], oldcc[cl_ne_6[4]], oldcc[cl_ne_6[5]], oldcc[cl_ne_6[6]], cov_obs[5], past_cov6)
            mu7 = neighbor_rew_fxn(cov_obs[cl_ne_7[1]],cov_obs[cl_ne_7[2]],cov_obs[cl_ne_7[3]], cov_obs[cl_ne_7[4]],cov_obs[cl_ne_7[5]],cov_obs[cl_ne_7[6]], oldcc[cl_ne_7[1]], oldcc[cl_ne_7[2]], oldcc[cl_ne_7[3]], oldcc[cl_ne_7[4]], oldcc[cl_ne_7[5]], oldcc[cl_ne_7[6]], cov_obs[6], past_cov7)
            mu8 = neighbor_rew_fxn(cov_obs[cl_ne_8[1]],cov_obs[cl_ne_8[2]],cov_obs[cl_ne_8[3]], cov_obs[cl_ne_8[4]],cov_obs[cl_ne_8[5]],cov_obs[cl_ne_8[6]], oldcc[cl_ne_8[1]], oldcc[cl_ne_8[2]], oldcc[cl_ne_8[3]], oldcc[cl_ne_8[4]], oldcc[cl_ne_8[5]], oldcc[cl_ne_8[6]], cov_obs[7], past_cov8)
            mu9 = neighbor_rew_fxn(cov_obs[cl_ne_9[1]],cov_obs[cl_ne_9[2]],cov_obs[cl_ne_9[3]], cov_obs[cl_ne_9[4]],cov_obs[cl_ne_9[5]],cov_obs[cl_ne_9[6]], oldcc[cl_ne_9[1]], oldcc[cl_ne_9[2]], oldcc[cl_ne_9[3]], oldcc[cl_ne_9[4]], oldcc[cl_ne_9[5]], oldcc[cl_ne_9[6]], cov_obs[8], past_cov9)
            mu10 = neighbor_rew_fxn(cov_obs[cl_ne_10[1]],cov_obs[cl_ne_10[2]],cov_obs[cl_ne_10[3]], cov_obs[cl_ne_10[4]],cov_obs[cl_ne_10[5]],cov_obs[cl_ne_10[6]], oldcc[cl_ne_10[1]], oldcc[cl_ne_10[2]], oldcc[cl_ne_10[3]], oldcc[cl_ne_10[4]], oldcc[cl_ne_10[5]], oldcc[cl_ne_10[6]], cov_obs[9], past_cov10)
            #print([mu1, mu2, mu3, mu4, mu5, mu6, mu7, mu8, mu9, mu10])

            ####This is the individual reward of each agent, and it has in it the neighbour reward factor for coperation
            r1  = agent_i_rew_fxn(mu1, cov_obs[0], old_cov1, present_ave_ene1, ave_ene_old1)
            r2  = agent_i_rew_fxn(mu2, cov_obs[1], old_cov2, present_ave_ene2, ave_ene_old2)
            r3  = agent_i_rew_fxn(mu3, cov_obs[2], old_cov3, present_ave_ene3, ave_ene_old3)
            r4  = agent_i_rew_fxn(mu4, cov_obs[3], old_cov4, present_ave_ene4, ave_ene_old4)
            r5  = agent_i_rew_fxn(mu5, cov_obs[4], old_cov5, present_ave_ene5, ave_ene_old5)
            r6  = agent_i_rew_fxn(mu6, cov_obs[5], old_cov6, present_ave_ene6, ave_ene_old6)
            r7  = agent_i_rew_fxn(mu7, cov_obs[6], old_cov7, present_ave_ene7, ave_ene_old7)
            r8  = agent_i_rew_fxn(mu8, cov_obs[7], old_cov8, present_ave_ene8, ave_ene_old8)
            r9  = agent_i_rew_fxn(mu9, cov_obs[8], old_cov9, present_ave_ene9, ave_ene_old9)
            r10  = agent_i_rew_fxn(mu10, cov_obs[9], old_cov10, present_ave_ene10, ave_ene_old10)

            ####Dense-Awareness
            dense_goal1 = (sprime1[0]> x1_target-thresh) and (sprime1[0]<x1_target+thresh) and (sprime1[1]>y1_target-thresh) and (sprime1[1]<y1_target+thresh)
            dense_goal2 = (sprime2[0]> x2_target-thresh) and (sprime2[0]<x2_target+thresh) and (sprime2[1]>y2_target-thresh) and (sprime2[1]<y2_target+thresh)
            dense_goal3 = (sprime3[0]> x3_target-thresh) and (sprime3[0]<x3_target+thresh) and (sprime3[1]>y3_target-thresh) and (sprime3[1]<y3_target+thresh)
            dense_goal4 = (sprime4[0]> x4_target-thresh) and (sprime4[0]<x4_target+thresh) and (sprime4[1]>y4_target-thresh) and (sprime4[1]<y4_target+thresh)
            dense_goal5 = (sprime5[0]> x5_target-thresh) and (sprime5[0]<x5_target+thresh) and (sprime5[1]>y5_target-thresh) and (sprime5[1]<y5_target+thresh)
            dense_goal6 = (sprime6[0]> x6_target-thresh) and (sprime6[0]<x6_target+thresh) and (sprime6[1]>y6_target-thresh) and (sprime6[1]<y6_target+thresh)
            dense_goal7 = (sprime7[0]> x7_target-thresh) and (sprime7[0]<x7_target+thresh) and (sprime7[1]>y7_target-thresh) and (sprime7[1]<y7_target+thresh)
            dense_goal8 = (sprime8[0]> x8_target-thresh) and (sprime8[0]<x8_target+thresh) and (sprime8[1]>y8_target-thresh) and (sprime8[1]<y8_target+thresh)
            dense_goal9 = (sprime9[0]> x9_target-thresh) and (sprime9[0]<x9_target+thresh) and (sprime9[1]>y9_target-thresh) and (sprime9[1]<y9_target+thresh)
            dense_goal10 = (sprime10[0]>x10_target-thresh) and (sprime10[0]<x10_target+thresh) and (sprime10[1]>y10_target-thresh) and (sprime10[1]<y10_target+thresh) 
             
            ###if battery dead or new location/region with highest experienced agent coverage
            done1 = sprime1[4] and dense_goal1
            done2 = sprime2[4] and dense_goal2
            done3 = sprime3[4] and dense_goal3
            done4 = sprime4[4] and dense_goal4
            done5 = sprime5[4] and dense_goal5
            done6 = sprime6[4] and dense_goal6
            done7 = sprime7[4] and dense_goal7
            done8 = sprime8[4] and dense_goal8
            done9 = sprime9[4] and dense_goal9
            done10 = sprime10[4] and dense_goal10
             

            if done1:
                energy_UAV1 = sprime1[3]
                c1=c1+1
                r1 = done_agent_i_rew(c1, MAX_USER_CONNECT_ALLOWED) 
            if done2:
                c2=c2+1
                energy_UAV2 = sprime2[3]
                r2 = done_agent_i_rew(c2, MAX_USER_CONNECT_ALLOWED) 
            if done3:
                c3=c3+1
                energy_UAV3 = sprime3[3]
                r3 = done_agent_i_rew(c3, MAX_USER_CONNECT_ALLOWED) 
            if done4:
                c4=c4+1
                energy_UAV4 = sprime4[3]
                r4 = done_agent_i_rew(c4, MAX_USER_CONNECT_ALLOWED) 
            if done5:
                c5=c5+1
                energy_UAV5 = sprime5[3]
                r5 = done_agent_i_rew(c5, MAX_USER_CONNECT_ALLOWED) 
            if done6:
                c6=c6+1
                energy_UAV6 = sprime6[3]
                r6 = done_agent_i_rew(c6, MAX_USER_CONNECT_ALLOWED) 
            if done7:
                c7=c7+1
                energy_UAV7 = sprime7[3]
                r7 = done_agent_i_rew(c7, MAX_USER_CONNECT_ALLOWED)
            if done8:
                c8=c8+1
                energy_UAV8 = sprime8[3]
                r8 = done_agent_i_rew(c8, MAX_USER_CONNECT_ALLOWED)
            if done9:
                c9=c9+1
                energy_UAV9 = sprime9[3]
                r9 = done_agent_i_rew(c9, MAX_USER_CONNECT_ALLOWED)
            if done10:
                c10=c10+1
                energy_UAV10 = sprime10[3]
                r10 = done_agent_i_rew(c10, MAX_USER_CONNECT_ALLOWED)
             
            
            en_ratio = [sprime1[3], sprime2[3], sprime3[3], sprime4[3], sprime5[3], sprime6[3], sprime7[3], sprime8[3], sprime9[3], sprime10[3]]

            ed1a = en_ratio[cl_ne_1[1]]/(sprime1[3]+en_ratio[cl_ne_1[1]])
            ed1b = en_ratio[cl_ne_1[2]]/(sprime1[3]+en_ratio[cl_ne_1[2]])
            ed1c = en_ratio[cl_ne_1[3]]/(sprime1[3]+en_ratio[cl_ne_1[3]])

            ed2a = en_ratio[cl_ne_2[1]]/(sprime2[3]+en_ratio[cl_ne_2[1]])
            ed2b = en_ratio[cl_ne_2[2]]/(sprime2[3]+en_ratio[cl_ne_2[2]])
            ed2c = en_ratio[cl_ne_2[3]]/(sprime2[3]+en_ratio[cl_ne_2[3]])

            ed3a = en_ratio[cl_ne_3[1]]/(sprime3[3]+en_ratio[cl_ne_3[1]])
            ed3b = en_ratio[cl_ne_3[2]]/(sprime3[3]+en_ratio[cl_ne_3[2]])
            ed3c = en_ratio[cl_ne_3[3]]/(sprime3[3]+en_ratio[cl_ne_3[3]])

            ed4a = en_ratio[cl_ne_4[1]]/(sprime4[3]+en_ratio[cl_ne_4[1]])
            ed4b = en_ratio[cl_ne_4[2]]/(sprime4[3]+en_ratio[cl_ne_4[2]])
            ed4c = en_ratio[cl_ne_4[3]]/(sprime4[3]+en_ratio[cl_ne_4[3]])

            ed5a = en_ratio[cl_ne_5[1]]/(sprime5[3]+en_ratio[cl_ne_5[1]])
            ed5b = en_ratio[cl_ne_5[2]]/(sprime5[3]+en_ratio[cl_ne_5[2]])
            ed5c = en_ratio[cl_ne_5[3]]/(sprime5[3]+en_ratio[cl_ne_5[3]])

            ed6a = en_ratio[cl_ne_6[1]]/(sprime6[3]+en_ratio[cl_ne_6[1]])
            ed6b = en_ratio[cl_ne_6[2]]/(sprime6[3]+en_ratio[cl_ne_6[2]])
            ed6c = en_ratio[cl_ne_6[3]]/(sprime6[3]+en_ratio[cl_ne_6[3]])

            ed7a = en_ratio[cl_ne_7[1]]/(sprime7[3]+en_ratio[cl_ne_7[1]])
            ed7b = en_ratio[cl_ne_7[2]]/(sprime7[3]+en_ratio[cl_ne_7[2]])
            ed7c = en_ratio[cl_ne_7[3]]/(sprime7[3]+en_ratio[cl_ne_7[3]])

            ed8a = en_ratio[cl_ne_8[1]]/(sprime8[3]+en_ratio[cl_ne_8[1]])
            ed8b = en_ratio[cl_ne_8[2]]/(sprime8[3]+en_ratio[cl_ne_8[2]])
            ed8c = en_ratio[cl_ne_8[3]]/(sprime8[3]+en_ratio[cl_ne_8[3]])

            ed9a = en_ratio[cl_ne_9[1]]/(sprime9[3]+en_ratio[cl_ne_9[1]])
            ed9b = en_ratio[cl_ne_9[2]]/(sprime9[3]+en_ratio[cl_ne_9[2]])
            ed9c = en_ratio[cl_ne_9[3]]/(sprime9[3]+en_ratio[cl_ne_9[3]])

            ed10a = en_ratio[cl_ne_10[1]]/(sprime10[3]+en_ratio[cl_ne_10[1]])
            ed10b = en_ratio[cl_ne_10[2]]/(sprime10[3]+en_ratio[cl_ne_10[2]])
            ed10c = en_ratio[cl_ne_10[3]]/(sprime10[3]+en_ratio[cl_ne_10[3]])

             

            
           ############### 
            cd1a = cov_obs[cl_ne_1[1]] - oldcc[cl_ne_1[1]]
            cd1b = cov_obs[cl_ne_1[2]] - oldcc[cl_ne_1[2]]
            cd1c = cov_obs[cl_ne_1[3]] - oldcc[cl_ne_1[3]]

            cd2a = cov_obs[cl_ne_2[1]] - oldcc[cl_ne_2[1]]
            cd2b = cov_obs[cl_ne_2[2]] - oldcc[cl_ne_2[2]]
            cd2c = cov_obs[cl_ne_2[3]] - oldcc[cl_ne_2[3]]

            cd3a = cov_obs[cl_ne_3[1]] - oldcc[cl_ne_3[1]]
            cd3b = cov_obs[cl_ne_3[2]] - oldcc[cl_ne_3[2]]
            cd3c = cov_obs[cl_ne_3[3]] - oldcc[cl_ne_3[3]]

            cd4a = cov_obs[cl_ne_4[1]] - oldcc[cl_ne_4[1]]
            cd4b = cov_obs[cl_ne_4[2]] - oldcc[cl_ne_4[2]]
            cd4c = cov_obs[cl_ne_4[3]] - oldcc[cl_ne_4[3]]

            cd5a = cov_obs[cl_ne_5[1]] - oldcc[cl_ne_5[1]]
            cd5b = cov_obs[cl_ne_5[2]] - oldcc[cl_ne_5[2]]
            cd5c = cov_obs[cl_ne_5[3]] - oldcc[cl_ne_5[3]]

            cd6a = cov_obs[cl_ne_6[1]] - oldcc[cl_ne_6[1]]
            cd6b = cov_obs[cl_ne_6[2]] - oldcc[cl_ne_6[2]]
            cd6c = cov_obs[cl_ne_6[3]] - oldcc[cl_ne_6[3]]

            cd7a = cov_obs[cl_ne_7[1]] - oldcc[cl_ne_7[1]]
            cd7b = cov_obs[cl_ne_7[2]] - oldcc[cl_ne_7[2]]
            cd7c = cov_obs[cl_ne_7[3]] - oldcc[cl_ne_7[3]]

            cd8a = cov_obs[cl_ne_8[1]] - oldcc[cl_ne_8[1]]
            cd8b = cov_obs[cl_ne_8[2]] - oldcc[cl_ne_8[2]]
            cd8c = cov_obs[cl_ne_8[3]] - oldcc[cl_ne_8[3]]

            cd9a = cov_obs[cl_ne_9[1]] - oldcc[cl_ne_9[1]]
            cd9b = cov_obs[cl_ne_9[2]] - oldcc[cl_ne_9[2]]
            cd9c = cov_obs[cl_ne_9[3]] - oldcc[cl_ne_9[3]]

            cd10a = cov_obs[cl_ne_10[1]] - oldcc[cl_ne_10[1]]
            cd10b = cov_obs[cl_ne_10[2]] - oldcc[cl_ne_10[2]]
            cd10c = cov_obs[cl_ne_10[3]] - oldcc[cl_ne_10[3]]

             
            

            ###we get this from the closest neighbor UAVs
            N_1a = N_1[1]
            N_1b = N_1[2]
            N_1c = N_1[3]

            N_2a = N_2[1]
            N_2b = N_2[2]
            N_2c = N_2[3]

            N_3a = N_3[1]
            N_3b = N_3[2]
            N_3c = N_3[3]

            N_4a = N_4[1]
            N_4b = N_4[2]
            N_4c = N_4[3]

            N_5a = N_5[1]
            N_5b = N_5[2]
            N_5c = N_5[3]

            N_6a = N_6[1]
            N_6b = N_6[2]
            N_6c = N_6[3]

            N_7a = N_7[1]
            N_7b = N_7[2]
            N_7c = N_7[3]

            N_8a = N_8[1]
            N_8b = N_8[2]
            N_8c = N_8[3]

            N_9a = N_9[1]
            N_9b = N_9[2]
            N_9c = N_9[3]

            N_10a = N_10[1]
            N_10b = N_10[2]
            N_10c = N_10[3]

            
            covdiff = (cov_obs[0]+cov_obs[1]+cov_obs[2]+cov_obs[3]+cov_obs[4]+cov_obs[5]+cov_obs[6]+cov_obs[7]+cov_obs[8]+cov_obs[9])-(old_cov1+old_cov2+old_cov3+old_cov4+old_cov5+old_cov6+old_cov7+old_cov8+old_cov9+old_cov10)

            usage = 1+(sprime1[3]-energy_UAV1) + (sprime2[3]-energy_UAV2)+ (sprime3[3]-energy_UAV3)+ (sprime4[3]-energy_UAV4)+ (sprime5[3]-energy_UAV5) + (sprime6[3]-energy_UAV6) + (sprime7[3]-energy_UAV7) + (sprime8[3]-energy_UAV8) + (sprime9[3]-energy_UAV9) + (sprime10[3]-energy_UAV10)
            
            devices_by_UAVs =  TP(sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], sprime5[0], sprime5[1], sprime5[2], sprime6[0], sprime6[1], sprime6[2], sprime7[0], sprime7[1], sprime7[2], sprime8[0], sprime8[1], sprime8[2], sprime9[0], sprime9[1], sprime9[2], sprime10[0], sprime10[1], sprime10[2], xsef, ysef, noise, beta, P, Bw)


            tp1 = devices_by_UAVs[0]+tp1
            tp2 = devices_by_UAVs[1]+tp2
            tp3 = devices_by_UAVs[2]+tp3
            tp4 = devices_by_UAVs[3]+tp4
            tp5 = devices_by_UAVs[4]+tp5
            tp6 = devices_by_UAVs[5]+tp6
            tp7 = devices_by_UAVs[6]+tp7
            tp8 = devices_by_UAVs[7]+tp8
            tp9 = devices_by_UAVs[8]+tp9
            tp10 = devices_by_UAVs[9]+tp10
                
                
                
            tp_sum = sum([tp1, tp2, tp3, tp4, tp5, tp6, tp7, tp8, tp9, tp10])
            energy_sum = sum([energy_UAV1, energy_UAV2, energy_UAV3, energy_UAV4, energy_UAV5, energy_UAV6, energy_UAV7, energy_UAV8, energy_UAV9, energy_UAV10])
                
            reached_tp = devices_by_UAVs[0] + devices_by_UAVs[1] + devices_by_UAVs[2] + devices_by_UAVs[3] + devices_by_UAVs[4] + devices_by_UAVs[5] + devices_by_UAVs[6] + devices_by_UAVs[7] + devices_by_UAVs[8] + devices_by_UAVs[9] 

            tot_tp = tp_sum+(reached_tp*(1400-itern))
            eneeff = tot_tp/energy_sum

            
            sprime1val = np.array([sprime1[0], sprime1[1], sprime1[2], cov_obs[0]-old_cov1, sprime1[3]/(sprime1[3]+sprime1[3]), x1_target, y1_target, ((cov_obs[0]+1)/(past_cov1+1))])
            sprime2val = np.array([sprime2[0], sprime2[1], sprime2[2], cov_obs[1]-old_cov2, sprime2[3]/(sprime2[3]+sprime2[3]), x2_target, y2_target, ((cov_obs[1]+1)/(past_cov2+1))])
            sprime3val = np.array([sprime3[0], sprime3[1], sprime3[2], cov_obs[2]-old_cov3, sprime3[3]/(sprime3[3]+sprime3[3]), x3_target, y3_target, ((cov_obs[2]+1)/(past_cov3+1))])
            sprime4val = np.array([sprime4[0], sprime4[1], sprime4[2], cov_obs[3]-old_cov4, sprime4[3]/(sprime4[3]+sprime4[3]), x4_target, y4_target, ((cov_obs[3]+1)/(past_cov4+1))])
            sprime5val = np.array([sprime5[0], sprime5[1], sprime5[2], cov_obs[4]-old_cov5, sprime5[3]/(sprime5[3]+sprime5[3]), x5_target, y5_target, ((cov_obs[4]+1)/(past_cov5+1))])
            sprime6val = np.array([sprime6[0], sprime6[1], sprime6[2], cov_obs[5]-old_cov6, sprime6[3]/(sprime6[3]+sprime6[3]), x6_target, y6_target, ((cov_obs[5]+1)/(past_cov6+1))])
            sprime7val = np.array([sprime7[0], sprime7[1], sprime7[2], cov_obs[6]-old_cov7, sprime7[3]/(sprime7[3]+sprime7[3]), x7_target, y7_target, ((cov_obs[6]+1)/(past_cov7+1))])
            sprime8val = np.array([sprime8[0], sprime8[1], sprime8[2], cov_obs[7]-old_cov8, sprime8[3]/(sprime8[3]+sprime8[3]), x8_target, y8_target, ((cov_obs[7]+1)/(past_cov8+1))])
            sprime9val = np.array([sprime9[0], sprime9[1], sprime9[2], cov_obs[8]-old_cov9, sprime9[3]/(sprime9[3]+sprime9[3]), x9_target, y9_target, ((cov_obs[8]+1)/(past_cov9+1))])
            sprime10val = np.array([sprime10[0], sprime10[1], sprime10[2], cov_obs[9]-old_cov10, sprime10[3]/(sprime10[3]+sprime10[3]), x10_target, y10_target, ((cov_obs[9]+1)/(past_cov10+1))])
             

            #sprime, r, done, info = [np.array([200,200,200,45.5]), 4, 0, 1] #env.step(a)
            r_sum1 += r1
            r_sum2 += r2
            r_sum3 += r3
            r_sum4 += r4
            r_sum5 += r5
            r_sum6 += r6
            r_sum7 += r7
            r_sum8 += r8
            r_sum9 += r9
            r_sum10 += r10
             
            
            if not test_mode:
                agent1.store_memory(s1, action1, r1, sprime1val, done1)
                agent2.store_memory(s2, action2, r2, sprime2val, done2)
                agent3.store_memory(s3, action3, r3, sprime3val, done3)
                agent4.store_memory(s4, action4, r4, sprime4val, done4)
                agent5.store_memory(s5, action5, r5, sprime5val, done5)
                agent6.store_memory(s6, action6, r6, sprime6val, done6)
                agent7.store_memory(s7, action7, r7, sprime7val, done7)
                agent8.store_memory(s8, action8, r8, sprime8val, done8)
                agent9.store_memory(s9, action9, r9, sprime9val, done9)
                agent10.store_memory(s10, action10, r10, sprime10val, done10)
                 
                agent1.learn()
                agent2.learn()
                agent3.learn()
                agent4.learn()
                agent5.learn()
                agent6.learn()
                agent7.learn()
                agent8.learn()
                agent9.learn()
                agent10.learn()
                 
                
            agent1.log(i)  # log td_error and learing_target_diff on tensorboard
            agent2.log(i)
            agent3.log(i)
            agent4.log(i)
            agent5.log(i)
            agent6.log(i)
            agent7.log(i)
            agent8.log(i)
            agent9.log(i)
            agent10.log(i)
             
            #observation = new_observation

            energy_UAV1 = sprime1[3]
            energy_UAV2 = sprime2[3]
            energy_UAV3 = sprime3[3]
            energy_UAV4 = sprime4[3]
            energy_UAV5 = sprime5[3]
            energy_UAV6 = sprime6[3]
            energy_UAV7 = sprime7[3]
            energy_UAV8 = sprime8[3]
            energy_UAV9 = sprime9[3]
            energy_UAV10 = sprime10[3]

            
            past_cov1 = max(cov_obs[0],past_cov1)
            past_cov2 = max(cov_obs[1],past_cov2)
            past_cov3 = max(cov_obs[2],past_cov3)
            past_cov4 = max(cov_obs[3],past_cov4)
            past_cov5 = max(cov_obs[4],past_cov5)
            past_cov6 = max(cov_obs[5],past_cov6)
            past_cov7 = max(cov_obs[6],past_cov7)
            past_cov8 = max(cov_obs[7],past_cov8)
            past_cov9 = max(cov_obs[8],past_cov9)
            past_cov10 = max(cov_obs[9],past_cov10)

            old_cov1 = cov_obs[0];
            old_cov2 = cov_obs[1];
            old_cov3 = cov_obs[2];
            old_cov4 = cov_obs[3];
            old_cov5 = cov_obs[4];
            old_cov6 = cov_obs[5];
            old_cov7 = cov_obs[6];
            old_cov8 = cov_obs[7];
            old_cov9 = cov_obs[8];
            old_cov10 = cov_obs[9];
             
            # Update state
            s1=sprime1val
            s2=sprime2val
            s3=sprime3val
            s4=sprime4val
            s5=sprime5val
            s6=sprime6val
            s7=sprime7val
            s8=sprime8val
            s9=sprime9val
            s10=sprime10val
            
            #print(observation)
            itern += 1

            if c1>=1 and c2>=1 and c3>=1 and c4>=1 and c5>=1 and c6>=1 and c7>=1 and c8>=1 and c9>=1 and c10>=1: 
                
                break

        
        if epsilon > 0.01:
            epsilon -= 1/(n_games+1) #0.001

        fairness = pow((cov_obs[0] + cov_obs[1] + cov_obs[2] + cov_obs[3] + cov_obs[4] + cov_obs[5] + cov_obs[6] + cov_obs[7] + cov_obs[8] +cov_obs[9] + 0.000001),2)/(10*(pow(cov_obs[0],2) + pow(cov_obs[1],2) + pow(cov_obs[2],2) + pow(cov_obs[3],2) + pow(cov_obs[4],2) + pow(cov_obs[5],2) + pow(cov_obs[6],2) + pow(cov_obs[7],2) + pow(cov_obs[8],2) + 0.000001+ pow(cov_obs[9],2)))
        
        
        writer1.add_scalar("Episode scores", r_sum1, i) # 
        writer2.add_scalar("Episode scores", r_sum2, i) 
        writer3.add_scalar("Episode scores", r_sum3, i) 
        writer4.add_scalar("Episode scores", r_sum4, i)
        writer5.add_scalar("Episode scores", r_sum5, i)
        writer6.add_scalar("Episode scores", r_sum6, i)
        writer7.add_scalar("Episode scores", r_sum7, i)
        writer8.add_scalar("Episode scores", r_sum8, i)
        writer9.add_scalar("Episode scores", r_sum9, i)
        writer10.add_scalar("Episode scores", r_sum10, i)
         
        
        scores1.append(r_sum1)  
        eps_history1.append(epsilon)
        steps_arr1.append(itern)

        scores2.append(r_sum2)  
        eps_history2.append(epsilon)
        steps_arr2.append(itern)

        scores3.append(r_sum3)  
        eps_history3.append(epsilon)
        steps_arr3.append(itern)

        scores4.append(r_sum4)  
        eps_history4.append(epsilon)
        steps_arr4.append(itern)

        scores5.append(r_sum5)  
        eps_history5.append(epsilon)
        steps_arr5.append(itern)

        scores6.append(r_sum6)  
        eps_history6.append(epsilon)
        steps_arr6.append(itern)

        scores7.append(r_sum7)  
        eps_history7.append(epsilon)
        steps_arr7.append(itern)

        scores8.append(r_sum8)  
        eps_history8.append(epsilon)
        steps_arr8.append(itern)

        scores9.append(r_sum9)  
        eps_history9.append(epsilon)
        steps_arr9.append(itern)

        scores10.append(r_sum10)  
        eps_history10.append(epsilon)
        steps_arr10.append(itern)

               
        



        sample_len = min(10000, len(scores1))
        avg_score = np.mean(scores1[-(sample_len):])
        if avg_score > best_score:
            best_score = avg_score
            if not test_mode:
                agent1.save_models()
                agent2.save_models()
                agent3.save_models()
                agent4.save_models()
                agent5.save_models()
                agent6.save_models()
                agent7.save_models()
                agent8.save_models()
                agent9.save_models()
                agent10.save_models()                 
                

        print(epsilon)
        print("Episode: ", i, "Iteration: ", itern)
        
        print("Energy Efficiency: ", eneeff)
        print("Total reward:", [r_sum1,r_sum2,r_sum3,r_sum4,r_sum5, r_sum6, r_sum7, r_sum8, r_sum9, r_sum10])
        print("UAV reached? ", [done1, done2, done3, done4, done5, done6, done7, done8, done9, done10])
        print("Connected devices:", [cov_obs[0], cov_obs[1], cov_obs[2], cov_obs[3], cov_obs[4], cov_obs[5], cov_obs[6], cov_obs[7], cov_obs[8], cov_obs[9]])
        print("Total deployed vehicles :", len(xsef))
        print("Total Connected vehicles :", cov_obs[0]+cov_obs[1]+cov_obs[2]+cov_obs[3]+cov_obs[4]+cov_obs[5]+cov_obs[6]+cov_obs[7]+cov_obs[8]+cov_obs[9])
        print("Energy Consumed:", [sprime1[3], sprime2[3], sprime3[3], sprime4[3], sprime5[3], sprime6[3], sprime7[3], sprime8[3], sprime9[3], sprime10[3]])
        #print("Distance Covered:", [sprime1[5], sprime2[5], sprime3[5], sprime4[5], sprime5[5], sprime6[5], sprime7[5], sprime8[5], sprime9[5], sprime10[5]])
        print("*******************************End of Epidode********************************")

        
        rewcumsum1 = rewcumsum1 + r_sum1
        rewcumsum2 = rewcumsum2 + r_sum2
        rewcumsum3 = rewcumsum3 + r_sum3
        rewcumsum4 = rewcumsum4 + r_sum4
        rewcumsum5 = rewcumsum5 + r_sum5
        rewcumsum6 = rewcumsum6 + r_sum6
        rewcumsum7 = rewcumsum7 + r_sum7
        rewcumsum8 = rewcumsum8 + r_sum8
        rewcumsum9 = rewcumsum9 + r_sum9
        rewcumsum10 = rewcumsum10 + r_sum10
             

        #devfairness.append(fairness_dev)
        efficiency.append(eneeff)
        throughput.append(tot_tp)
        vehicles_deployed.append(len(xsef))
        
        dist_1.append(sprime1[5])
        dist_2.append(sprime2[5])
        dist_3.append(sprime3[5])
        dist_4.append(sprime4[5])
        dist_5.append(sprime5[5])
        dist_6.append(sprime6[5])
        dist_7.append(sprime7[5])
        dist_8.append(sprime8[5])
        dist_9.append(sprime9[5])
        dist_10.append(sprime10[5])
             
            
        r_sums1.append(rewcumsum1)
        r_sums2.append(rewcumsum2)
        r_sums3.append(rewcumsum3)
        r_sums4.append(rewcumsum4)
        r_sums5.append(rewcumsum5)
        r_sums6.append(rewcumsum6)
        r_sums7.append(rewcumsum7)
        r_sums8.append(rewcumsum8)
        r_sums9.append(rewcumsum9)
        r_sums10.append(rewcumsum10)
            
        UAV1cov.append(cov_obs[0])
        UAV2cov.append(cov_obs[1])
        UAV3cov.append(cov_obs[2])
        UAV4cov.append(cov_obs[3])
        UAV5cov.append(cov_obs[4])
        UAV6cov.append(cov_obs[5])
        UAV7cov.append(cov_obs[6])
        UAV8cov.append(cov_obs[7])
        UAV9cov.append(cov_obs[8])
        UAV10cov.append(cov_obs[9])
             
            
        UAV1eng.append(sprime1[3])
        UAV2eng.append(sprime2[3])
        UAV3eng.append(sprime3[3])
        UAV4eng.append(sprime4[3])
        UAV5eng.append(sprime5[3])
        UAV6eng.append(sprime6[3])
        UAV7eng.append(sprime7[3])
        UAV8eng.append(sprime8[3])
        UAV9eng.append(sprime9[3])
        UAV10eng.append(sprime10[3])
             
             
            
        iter_store.append(itern)

            
        np.savetxt('results_sumo_test/Energy_DAMAD.dat', [UAV1eng, UAV2eng, UAV3eng, UAV4eng, UAV5eng, UAV6eng, UAV7eng, UAV8eng, UAV9eng, UAV10eng])
        np.savetxt('results_sumo_test/Covered_vehicles_DAMAD.dat', [UAV1cov, UAV2cov, UAV3cov, UAV4cov, UAV5cov, UAV6cov, UAV7cov, UAV8cov, UAV9cov, UAV10cov])
        np.savetxt('results_sumo_test/deployed_vehicles_DAMAD.dat', [vehicles_deployed])
        np.savetxt('results_sumo_test/ee_DAMAD.dat', [efficiency])
        z1 = 120
        z2 = 120
        z3 = 120
        z4 = 120
        z5 = 120
        z6 = 120
        z7 = 120
        z8 = 120
        z9 = 120
        z10 = 120
        
                
