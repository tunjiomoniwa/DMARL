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

### step files
from RWP import RWP
from GMM import GMM
from RW import RW
from stepOverlap4nodes_static import stepOverlap4nodes_static
from stepBL1_static import stepBL1_static
from stepBL2_static import stepBL2_static
from stepBL3_static import stepBL3_static
from stepBL4_static import stepBL4_static

from neighbor_reward_factor import neighbor_reward_factor
from neighbor_reward_factor import neighbor_val
from neighbor_reward_factor import neighbor_rew_fxn
from neighbor_reward_factor import agent_i_rew_fxn
from neighbor_reward_factor import done_agent_i_rew
from throughput_calc import TP
from step_fairness import step_fairness ##
from CalcDistance import CalcDistance
import random
import matplotlib.pyplot as plt

###Reference
## https://github.com/jeffery1236/Atari_DoubleDeepQNetwork


if __name__ == '__main__':
    mode = "Double"
    best_score = -np.inf
    test_mode = False # False #True
    render = False #True
    n_games =  1000
    runs = 1
    Max_iterations = 1500    
    uavs = 4
    n_games_exp = 250    
    cov_tot = []
    ene_tot=  []
    fair_tot = []
    ee_tot = []
    for run in range(runs):
        epsilon = 1
        
        if mode == "Double":
            agent1 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                            obs_dims=14,
                            num_actions=7, 
                            mem_size=10000,
                            mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                            env_name='Multi_UAVBS_Deployment',
                            algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
            agent2 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                            obs_dims=14,
                            num_actions=7, 
                            mem_size=10000,
                            mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                            env_name='Multi_UAVBS_Deployment',
                            algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
            agent3 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                            obs_dims=14,
                            num_actions=7, 
                            mem_size=10000,
                            mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                            env_name='Multi_UAVBS_Deployment',
                            algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
            agent4 = DoubleDQAgent(lr=0.0001, gamma=0.95, 
                            obs_dims=14,
                            num_actions=7, 
                            mem_size=10000,
                            mini_batchsize=1024, epsilon_dec=(1/n_games_exp),
                            env_name='Multi_UAVBS_Deployment',
                            algo_name='DoubleDQAgent', epsilon=1, epsilon_min=0.1)
            
        
    
        
         
    
        if test_mode:
            agent1.load_models()
            agent2.load_models()
            agent3.load_models()
            agent4.load_models()
             

        n_steps = 0
        scores1, eps_history1, steps_arr1 = [], [], []
        scores2, eps_history2, steps_arr2 = [], [], []
        scores3, eps_history3, steps_arr3 = [], [], []
        scores4, eps_history4, steps_arr4 = [], [], []
         
         
        
        writer1 = SummaryWriter(os.path.join(agent1.checkpoint_dir, 'logs'))
        writer2 = SummaryWriter(os.path.join(agent2.checkpoint_dir, 'logs'))
        writer3 = SummaryWriter(os.path.join(agent3.checkpoint_dir, 'logs'))
        writer4 = SummaryWriter(os.path.join(agent4.checkpoint_dir, 'logs'))
          
        
        
        r_sums1 = []  # stores rewards of each epsiode
        r_sums2 = []
        r_sums3 = []
        r_sums4 = []
         

        devfairness = []
        truput = []
        fairfact = []
        fairness_dev =0.99
        efficiency = []
        dist_1 = []
        dist_2 = []
        dist_3 = []
        dist_4 = []
         
        

        rewcumsum1 = 0
        rewcumsum2 = 0
        rewcumsum3 = 0
        rewcumsum4 = 0
         
         
        

        UAV1cov = [] # stores coverage values
        UAV2cov = []
        UAV3cov = []
        UAV4cov = []

        covtot = []
        enetot=  []
        fairtot = []
         
         
        UAV1eng = [] # stores energy values
        UAV2eng = []
        UAV3eng = []
        UAV4eng = []
         

        iter_store = []

        x1 = 150
        y1 = 150
        z1 = 250
        e1 = 0
        old_cov1 = 40;
        old_cov2 = 40;
        old_cov3 = 40;
        old_cov4 = 40;

        noise =-130;
        beta = 1;
        P = -7;
        Bw =1000000;
         
            
        ##126 data points ...Drumcondra South A ITM grid

        bin_data_x = [1000,997.072214800000,984.948617500000,968.633702900000,964.125221200000,956.059447200000,928.648016900000,928.249333000000,888.622523100000,867.742960500000,861.542904600000,855.785721900000,851.846195100000,848.952267400000,847.336525200000,847.126728700000,846.811716100000,825.096330400000,816.985975300000,808.126770600000,804.605549000000,797.456432800000,785.420204200000,776.696869100000,769.980955000000,767.678347600000,766.915782700000,759.835608300000,756.049541000000,753.632662900000,745.878428600000,736.217639600000,719.658609900000,719.071987400000,704.276665700000,695.424363900000,689.327984100000,684.716734700000,683.748623000000,683.607361500000,683.580131300000,650.748082500000,630.352702400000,622.543501600000,609.747665300000,602.082525400000,602.082518600000,570.459320500000,567.018374200000,566.440428500000,562.280497800000,562.256017800000,551.749866100000,531.433256500000,530.158762100000,521.746454900000,515.133485700000,493.884553000000,492.313895500000,491.677973200000,491.656035500000,474.791411700000,473.231290000000,472.737635200000,470.656263800000,469.771710700000,453.141372200000,450.284718900000,447.988944800000,435.209393800000,433.272831800000,425.833810000000,424.465696600000,420.889748600000,419.393970000000,417.210188000000,412.895384200000,409.238572500000,398.531274000000,398.007674200000,391.810862400000,383.864834100000,381.839045500000,369.183443100000,356.348556000000,354.959546600000,346.420178700000,345.302137800000,325.985001100000,325.787646500000,313.899747000000,281.855623900000,279.781143100000,243.229671600000,204.572930200000,199.989874200000,193.494261800000,163.236364900000,161.693109700000,155.458120200000,154.743394000000,143.810289800000,138.712356400000,138.154289700000,136.678000900000,136.385108000000,136.084182800000,134.768326100000,114.864580500000,112.825183900000,89.6626356700000,88.6022148800000,77.4445585200000,74.7585542700000,69.1688215100000,65.0693127600000,63.0130482600000,54.8292877700000,53.2063741300000,49.4219996500000,48.3594727800000,44.5171850900000,27.3815095100000,9.69356873600000,8.34480656800000,0];
        bin_data_y = [838.398868100000,843.733994400000,946.673674600000,259.256249600000,455.263182200000,263.042977600000,395.489732800000,944.564006000000,514.217232800000,965.918810900000,313.200308500000,755.546562000000,817.002928200000,918.420802100000,863.150606500000,932.362588800000,948.164999300000,957.969224600000,295.935122500000,949.981906600000,283.762051600000,935.080509800000,249.530056500000,878.051621700000,855.755822700000,398.766938400000,581.404557100000,570.443970700000,411.115106300000,561.001765300000,423.127999700000,814.186888300000,161.322759100000,828.225447200000,768.995452500000,143.796157500000,739.710142800000,677.351349400000,961.460071700000,680.399967400000,958.121294300000,949.363117300000,489.510939900000,656.685584500000,498.905718500000,627.070506800000,627.070508500000,519.046665800000,491.407273900000,589.109847700000,467.723449500000,582.721194200000,66.0667508700000,525.400091000000,534.647011100000,501.146206500000,931.896009200000,940.049384800000,940.700756400000,437.372658300000,766.488012400000,416.139054400000,946.963998700000,55.9944530100000,381.753274000000,394.617806200000,769.463159300000,331.638592500000,818.291653200000,623.276709400000,623.283162800000,0,277.416850400000,639.178189000000,250.346103400000,640.591221400000,692.037540800000,226.136050200000,1000,651.091180800000,727.525674600000,175.332604100000,69.2575938800000,756.198581700000,134.771604200000,899.477666500000,106.474706100000,156.782706700000,174.192763300000,33.2932403600000,186.370249400000,716.554660000000,717.729082500000,244.511768000000,680.584535900000,277.188062900000,68.3115930500000,482.470721700000,163.578638300000,382.180183800000,265.378545000000,214.154550000000,806.202957300000,322.849284400000,387.509206100000,376.498882100000,808.605664600000,332.560862100000,230.156725600000,351.822346000000,274.170392800000,254.273308100000,779.628304000000,761.528459400000,535.630439300000,37.4594185200000,538.800679200000,530.744887200000,542.821760300000,541.853545600000,534.260882300000,982.283337100000,866.495864100000,876.241797800000,875.441684800000,551.001179000000];

        random.seed(1)
        syn_data_x = random.sample(range(40, 960), 200-126)
        syn_data_y = random.sample(range(40, 960), 200-126)
        



        ####
##        ####City Centre Dublin 2 along the River Lifey -194 Bins Data Points
##        bin_data_x = [1000,979.476262000000,970.965143000000,969.334229000000,966.113047000000,963.529552000000,962.082031000000,961.819624000000,961.819584000000,961.316963000000,958.470642000000,951.736749000000,948.591041000000,943.578617000000,938.327370000000,936.347695000000,934.125671000000,896.588605000000,876.454699000000,871.825207000000,868.197151000000,866.932001000000,858.207666000000,857.984514000000,855.428259000000,847.327977000000,835.810655000000,828.106157000000,827.924618000000,827.924578000000,823.019890000000,821.760387000000,816.054852000000,810.571286000000,795.873889000000,794.326391000000,789.317340000000,787.821194000000,782.766196000000,780.873639000000,773.450759000000,752.940874000000,752.549577000000,740.436013000000,738.618268000000,737.077283000000,737.001389000000,728.387033000000,726.178472000000,724.284308000000,722.108631000000,720.362438000000,719.083862000000,688.798882000000,688.638907000000,684.302812000000,670.608033000000,666.185071000000,665.696636000000,665.091559000000,640.034932000000,637.851144000000,626.753098000000,624.604192000000,622.673283000000,614.769294000000,610.685119000000,603.718554000000,597.543876000000,586.676025000000,578.331598000000,578.298483000000,558.969537000000,558.888489000000,556.209272000000,555.000975000000,546.940809000000,544.655886000000,540.306971000000,536.393474000000,534.621676000000,529.997580000000,529.198663000000,526.966934000000,519.520867000000,514.026624000000,512.088640000000,508.148788000000,507.701587000000,500.216569000000,498.847896000000,484.528987000000,468.037101000000,456.545670000000,453.282288000000,451.010312000000,439.617043000000,438.671734000000,434.695963000000,433.635930000000,432.792752000000,429.165933000000,423.937312000000,423.404761000000,418.653668000000,406.386418000000,398.091555000000,397.072768000000,395.265792000000,391.901687000000,375.570879000000,374.059543000000,372.172952000000,364.815764000000,360.704351000000,359.922739000000,357.685420000000,342.417358000000,324.803361000000,321.667954000000,321.667117000000,320.556420000000,319.594089000000,316.391063000000,315.370126000000,311.669177000000,306.358986000000,306.139218000000,285.593890000000,281.554800000000,281.356491000000,278.227454000000,272.945363000000,271.651624000000,267.550750000000,266.903803000000,260.512111000000,258.392579000000,251.399078000000,243.136802000000,242.049736000000,234.582959000000,230.600204000000,223.099958000000,221.633754000000,215.002068000000,212.411662000000,208.821804000000,199.591989000000,192.741489000000,189.712930000000,185.800740000000,183.399860000000,182.064885000000,176.315596000000,157.453329000000,155.205256000000,152.718548000000,150.367726000000,147.286522000000,139.009190000000,136.348457000000,131.714433000000,130.731506000000,125.201183000000,116.552583000000,103.240069000000,98.7287850000000,93.2228980000000,85.7557440000000,82.2597720000000,80.8289840000000,78.7130390000000,63.1286030000000,55.8017890000000,55.3965080000000,52.5456810000000,50.5555710000000,49.4566530000000,49.0957030000000,45.8391930000000,45.7953240000000,41.1142680000000,38.5262060000000,36.2793250000000,29.9567380000000,24.9864180000000,19.8120260000000,19.7665850000000,14.4120330000000,12.3940510000000,4.65045800000000,3.56065700000000,0];
##        bin_data_y = [157.570364000000,288.489976000000,356.230040000000,312.141451000000,432.237646000000,154.661497000000,206.200560000000,388.181143000000,388.181146000000,555.281158000000,426.590781000000,60.0088550000000,380.621571000000,427.956856000000,386.470052000000,425.772126000000,686.394149000000,319.873543000000,216.330686000000,313.541443000000,416.145098000000,380.885527000000,156.266592000000,334.919760000000,296.070209000000,413.044839000000,0,406.686605000000,378.183181000000,378.183183000000,327.249313000000,300.294694000000,539.771934000000,154.966715000000,369.038302000000,67.3151090000000,358.119196000000,289.483530000000,374.486732000000,529.542064000000,214.961434000000,15.2439780000000,154.826706000000,377.893288000000,275.086465000000,398.143118000000,642.854161000000,370.896179000000,402.328277000000,390.318407000000,204.563032000000,287.941822000000,1000,308.656738000000,156.542457000000,417.726408000000,526.344998000000,287.585950000000,214.324830000000,358.177319000000,72.0748970000000,311.180321000000,355.331841000000,459.793734000000,361.824846000000,156.889504000000,349.906556000000,333.005872000000,361.292952000000,616.912630000000,347.947309000000,874.955669000000,233.827419000000,784.846924000000,813.092716000000,239.112969000000,202.739756000000,501.867137000000,819.174460000000,620.497158000000,513.059442000000,49.9859300000000,61.2719700000000,353.460432000000,502.963922000000,346.666076000000,602.205426000000,151.892432000000,803.112092000000,803.337844000000,233.532495000000,350.195493000000,263.699987000000,438.194455000000,31.8674550000000,157.443194000000,603.362567000000,810.823826000000,210.503261000000,390.036627000000,196.002384000000,340.072723000000,197.442730000000,247.960486000000,35.0142170000000,338.334717000000,343.344568000000,207.078703000000,498.544022000000,580.934039000000,154.388508000000,39.4640990000000,243.940486000000,335.750429000000,492.738742000000,251.872048000000,73.5972790000000,682.422046000000,333.519030000000,201.437008000000,498.757573000000,124.132506000000,483.360985000000,688.708294000000,73.0015130000000,699.584472000000,526.047484000000,563.648105000000,245.858462000000,574.518158000000,188.765581000000,333.471367000000,80.4725420000000,185.797261000000,148.789889000000,477.439914000000,196.714890000000,721.165667000000,677.538733000000,131.740805000000,665.648991000000,157.199392000000,325.275342000000,840.700106000000,181.370116000000,230.522998000000,553.775653000000,565.081283000000,323.038923000000,155.242418000000,142.262978000000,666.428945000000,178.494918000000,558.420576000000,71.0686500000000,48.7395080000000,466.341526000000,760.799935000000,324.373525000000,186.375888000000,137.449779000000,66.9928700000000,176.400927000000,96.9977580000000,470.945684000000,86.4252790000000,104.802864000000,181.735686000000,231.187679000000,321.359444000000,140.923013000000,459.279978000000,842.718760000000,464.826194000000,731.841167000000,64.6871430000000,219.188364000000,311.832386000000,337.502730000000,164.966169000000,167.607036000000,176.367613000000,136.617192000000,226.730536000000,532.370212000000,174.960974000000,139.661429000000,349.645312000000,308.516167000000,313.220168000000,859.293353000000,51.4173940000000,690.066285000000,171.713655000000];
##
##        random.seed(1)
##        syn_data_x = random.sample(range(40, 960), 200-194)
##        syn_data_y = random.sample(range(40, 960), 200-194)

        ###Static Scaling the distribution
        bin_data_x  = np.array(bin_data_x)*0.92 +40
        bin_data_y  = np.array(bin_data_y)*0.92 +40
        
        
        

        random.seed(1)
        xblock1 = random.sample(range(40, 460), 50)
        xblock2 = random.sample(range(540, 960), 50)
        xblock3 = random.sample(range(40, 460), 50)
        xblock4 = random.sample(range(540, 960), 50)

        random.seed(2)
        yblock1 = random.sample(range(40, 460), 50)
        yblock2 = random.sample(range(40, 460), 50)
        yblock3 = random.sample(range(540, 960), 50)
        yblock4 =  random.sample(range(540, 960), 50)

        

        xsef_mob = np.concatenate((bin_data_x, syn_data_x))
        ysef_mob = np.concatenate((bin_data_y, syn_data_y))

        #rwp_model = RWP(xsef_mob, ysef_mob)
        #rw_model = RW(xsef_mob, ysef_mob)
        #gmm_model = GMM(xsef_mob, ysef_mob)

        xsef = np.concatenate((xsef_mob, xblock1, xblock2, xblock3, xblock4))
        ysef = np.concatenate((ysef_mob, yblock1, yblock2, yblock3, yblock4))


        x1 =  random.randint(10, 470)
        y1 =  random.randint(10, 470)
        z1 = 150
        e1 = 0
        dist1 = 0 
        x2 = random.randint(5, 470)
        y2 = random.randint(5, 480)
        z2 = 150
        e2 = 0
        dist2 = 0 
        x3 =  random.randint(10, 480)
        y3 =  random.randint(10, 470)
        z3 = 150
        e3 = 0
        dist3 = 0 
        x4 =  random.randint(10, 970)
        y4 =  random.randint(10, 470)
        z4 = 150
        e4 = 0
        dist4 = 0


        MAX_Connected_users_allowed = 150
        ####
         
         
         
        
        #print(xsef)
        #print(ysef)

        random.shuffle



        for i in range(n_games):


            
            #rwp_model = RWP(xsef_mob, ysef_mob)
            #rw_model = RW(xsef_mob, ysef_mob)
            #gmm_model = GMM(xsef_mob, ysef_mob)
            #print(len(rwp_model))
            #print(len(rwp_modely))
            

            xsef = np.concatenate((xsef_mob, xblock1, xblock2, xblock3, xblock4))
            ysef = np.concatenate((ysef_mob, yblock1, yblock2, yblock3, yblock4))
            
            done = False
            done1 = False
            done2 = False
            done3 = False
            done4 = False
             
            
            
            
            score = 0

            
        
            #observation = env.reset()
            s1 = np.array([x1, y1, z1, 100, 100, 100, 5, 5, 5, 5, 0, 0, 0, 0])
            s2 = np.array([x2, y2, z2, 100, 100, 100, 5, 5, 5, 5, 0, 0, 0, 0])
            s3 = np.array([x3, y3, z3, 100, 100, 100, 5, 5, 5, 5, 0, 0, 0, 0])
            s4 = np.array([x4, y4, z4, 100, 100, 100, 5, 5, 5, 5, 0, 0, 0, 0])
             

            sprime1val = np.array([x1, y1, z1, 100, 100, 100, 5, 5, 5, 5, 0, 0, 0, 0])
            sprime2val = np.array([x2, y2, z2, 100, 100, 100, 5, 5, 5, 5, 0, 0, 0, 0])
            sprime3val = np.array([x3, y3, z3, 100, 100, 100, 5, 5, 5, 5, 0, 0, 0, 0])
            sprime4val = np.array([x4, y4, z4, 100, 100, 100, 5, 5, 5, 5, 0, 0, 0, 0])
             
            action1 = random.randint(0,6)
            action2 = random.randint(0,6)
            action3 = random.randint(0,6)
            action4 = random.randint(0,6)
              
            
            sprime1 = stepBL1_static(action1, x1, y1, z1, e1, dist1)
            sprime2 = stepBL2_static(action2, x2, y2, z2, e2, dist2)
            sprime3 = stepBL3_static(action3, x3, y3, z3, e3, dist3)
            sprime4 = stepBL4_static(action4, x4, y4, z4, e4, dist4)
             
            
            cov_obs = stepOverlap4nodes_static(sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], xsef, ysef)

            #cov_obs = stepOverlap_static(sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], xsef, ysef)

            old_cov1 = 50
            old_cov2 = 50
            old_cov3 = 50
            old_cov4 = 50
            
             
            
            old_ene1 = sprime1[3]
            old_ene2 = sprime2[3]
            old_ene3 = sprime3[3]
            old_ene4 = sprime4[3]
             
             
            max_cov_obs =0

            fair_sum = 0
            fairness = 0
            done1 = False
            done2 = False
            done3 = False
            done4 = False
             
             

            covd1 = 0
            covd2 = 0
            covd3 = 0
            covd4 = 0
             
             
            
            energy_UAV1 = sprime1[3]
            energy_UAV2 = sprime2[3]
            energy_UAV3 = sprime3[3]
            energy_UAV4 = sprime4[3]

            
            tp1 = 0
            tp2 = 0
            tp3 = 0
            tp4 = 0

            
            c1 = 0
            c2 = 0
            c3 = 0
            c4 = 0
             
             
            
            r_sum1 = 0
            r_sum2 = 0
            r_sum3 = 0
            r_sum4 = 0
             
             
            
            itern = 0
            #plt.scatter(xsef, ysef)
            #plt.show()

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

                #xsef = np.concatenate((xsef_mob, xblock1, xblock2, xblock3, xblock4))
                #ysef = np.concatenate((xsef_mob, yblock1, yblock2, yblock3, yblock4))
                
                #print(itern)
                
                if c1>=1:
                    action1 = 0
                else: #elif c1==0:
                    action1 =  agent1.get_action(s1, epsilon)
                    
                if c2>=1:
                    action2 = 0
                else: #elif c2==0:
                    action2 = agent2.get_action(s2, epsilon)
                    
                if c3>=1:
                    action3 = 0
                else: #elif c3==0:
                    action3 = agent3.get_action(s3, epsilon)
                    
                if c4>=1:
                    action4 = 0
                else: #elif c4==0:
                    action4 = agent4.get_action(s4, epsilon)

                            
                 
                

                #print([action1, action2, action3, action4])
                
                #new_observation, reward, done, _ = env.step(action1)
                sprime1 = stepBL1_static(action1, sprime1[0], sprime1[1], sprime1[2], sprime1[3], sprime1[5])
                sprime2 = stepBL2_static(action2, sprime2[0], sprime2[1], sprime2[2], sprime2[3], sprime2[5])
                sprime3 = stepBL3_static(action3, sprime3[0], sprime3[1], sprime3[2], sprime3[3], sprime3[5])
                sprime4 = stepBL4_static(action4, sprime4[0], sprime4[1], sprime4[2], sprime4[3], sprime4[5])
                
                cov_obs = stepOverlap4nodes_static(sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], xsef, ysef)

                
                ave_ene_old1 = old_ene1/(1+itern)
                present_ave_ene1 = sprime1[3]/(2+itern)
                ave_ene_old2 = old_ene2/(1+itern)
                present_ave_ene2 = sprime2[3]/(2+itern)
                ave_ene_old3 = old_ene3/(1+itern)
                present_ave_ene3 = sprime3[3]/(2+itern)
                ave_ene_old4 = old_ene4/(1+itern)
                present_ave_ene4 = sprime4[3]/(2+itern)
                 

                #####Get closest neighbour index fxn here

                cl_ne_1 = neighbor_reward_factor(sprime1[0], sprime1[1], sprime1[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2])
                cl_ne_2 = neighbor_reward_factor(sprime2[0], sprime2[1], sprime2[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2])
                cl_ne_3 = neighbor_reward_factor(sprime3[0], sprime3[1], sprime3[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2])
                cl_ne_4 = neighbor_reward_factor(sprime4[0], sprime4[1], sprime4[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2])
                

                #### distance value of UAVs nearest neighbours           
                N_1 = neighbor_val(sprime1[0], sprime1[1], sprime1[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2])
                N_2 = neighbor_val(sprime2[0], sprime2[1], sprime2[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2])
                N_3 = neighbor_val(sprime3[0], sprime3[1], sprime3[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2])
                N_4 = neighbor_val(sprime4[0], sprime4[1], sprime4[2], sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2])
                  


                #neighbour_list(cl_ne_1[1], cl_ne_1[2], cl_ne_1[3])

                ##cov_obs[neighbor_fact[1]]+cov_obs[neighbor_fact[2]]+cov_obs[neighbor_fact[2]]
                

                oldcc = [old_cov1,old_cov2,old_cov3,old_cov4]
                
                ####Neighbour coverage-based cooperative factor relative to each i{th} agent
                mu1 = neighbor_rew_fxn(cov_obs[cl_ne_1[1]],cov_obs[cl_ne_1[2]],cov_obs[cl_ne_1[3]], oldcc[cl_ne_1[1]], oldcc[cl_ne_1[2]], oldcc[cl_ne_1[3]])
                mu2 = neighbor_rew_fxn(cov_obs[cl_ne_2[1]],cov_obs[cl_ne_2[2]],cov_obs[cl_ne_2[3]], oldcc[cl_ne_2[1]], oldcc[cl_ne_2[2]], oldcc[cl_ne_2[3]])
                mu3 = neighbor_rew_fxn(cov_obs[cl_ne_3[1]],cov_obs[cl_ne_3[2]],cov_obs[cl_ne_3[3]], oldcc[cl_ne_3[1]], oldcc[cl_ne_3[2]], oldcc[cl_ne_3[3]])
                mu4 = neighbor_rew_fxn(cov_obs[cl_ne_4[1]],cov_obs[cl_ne_4[2]],cov_obs[cl_ne_4[3]], oldcc[cl_ne_4[1]], oldcc[cl_ne_4[2]], oldcc[cl_ne_4[3]])
                 

                ####This is the individual reward of each agent, and it has in it the neighbour reward factor for coperation
                r1  = agent_i_rew_fxn(mu1, cov_obs[0], old_cov1, present_ave_ene1, ave_ene_old1)
                r2  = agent_i_rew_fxn(mu2, cov_obs[1], old_cov2, present_ave_ene2, ave_ene_old2)
                r3  = agent_i_rew_fxn(mu3, cov_obs[2], old_cov3, present_ave_ene3, ave_ene_old3)
                r4  = agent_i_rew_fxn(mu4, cov_obs[3], old_cov4, present_ave_ene4, ave_ene_old4)
                 
                done1 = sprime1[4]
                done2 = sprime2[4]
                done3 = sprime3[4]
                done4 = sprime4[4]
                 

                if done1:
                    energy_UAV1 = sprime1[3]
                    c1=c1+1
                    r1 = done_agent_i_rew(c1, MAX_Connected_users_allowed) 
                if done2:
                    c2=c2+1
                    energy_UAV2 = sprime2[3]
                    r2 = done_agent_i_rew(c2, MAX_Connected_users_allowed) 
                if done3:
                    c3=c3+1
                    energy_UAV3 = sprime3[3]
                    r3 = done_agent_i_rew(c3, MAX_Connected_users_allowed) 
                if done4:
                    c4=c4+1
                    energy_UAV4 = sprime4[3]
                    r4 = done_agent_i_rew(c4, MAX_Connected_users_allowed)
                 
                
                en_ratio = [sprime1[3], sprime2[3], sprime3[3], sprime4[3]]

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

                

                #print(np.add(fair_sum, cov_obs[uavs]))

                fair_sum = np.add(fair_sum, cov_obs[uavs])
                ##print(fair_sum)
                fairness_dev = step_fairness(fair_sum)
                shannon_rate = fairness_dev
                Bw = 1000000  #

                

                shannon_rate = fairness_dev
                
                ##print(fairness_dev)

                ###################Energy Efficiency

                covdiff = (cov_obs[0]+cov_obs[1]+cov_obs[2]+cov_obs[3])-(old_cov1+old_cov2+old_cov3+old_cov4)
                cov_tp = (cov_obs[0]+cov_obs[1]+cov_obs[2]+cov_obs[3])

                usage = 1+(sprime1[3]-energy_UAV1) + (sprime2[3]-energy_UAV2)+ (sprime3[3]-energy_UAV3)+ (sprime4[3]-energy_UAV4)
                                
                


                devices_by_UAVs =  TP(sprime1[0], sprime1[1], sprime1[2], sprime2[0], sprime2[1], sprime2[2], sprime3[0], sprime3[1], sprime3[2], sprime4[0], sprime4[1], sprime4[2], xsef, ysef, noise, beta, P, Bw)


                tp1 = devices_by_UAVs[0]+tp1
                tp2 = devices_by_UAVs[1]+tp2
                tp3 = devices_by_UAVs[2]+tp3
                tp4 = devices_by_UAVs[3]+tp4
                
                
                #print([tp1, tp2, tp3, tp4])
                tp_sum = sum([tp1, tp2, tp3, tp4])
                energy_sum = sum([energy_UAV1, energy_UAV2, energy_UAV3, energy_UAV4])
                #eneeff = tp_sum/energy_sum
                #print(eneeff)

                reached_tp = devices_by_UAVs[0] + devices_by_UAVs[1] + devices_by_UAVs[2] + devices_by_UAVs[3] 

                tot_tp = tp_sum+(reached_tp*(1300-itern))
                eneeff = tot_tp/energy_sum

                
                sprime1val = np.array([sprime1[0], sprime1[1], sprime1[2], N_1a, N_1b, N_1c, cov_obs[0]-old_cov1, cd1a, cd1b, cd1c, sprime1[3]/(sprime1[3]+sprime1[3]), ed1a, ed1b, ed1c])
                sprime2val = np.array([sprime2[0], sprime2[1], sprime2[2], N_2a, N_2b, N_2c, cov_obs[1]-old_cov2, cd2a, cd2b, cd2c, sprime2[3]/(sprime2[3]+sprime2[3]), ed2a, ed2b, ed2c])
                sprime3val = np.array([sprime3[0], sprime3[1], sprime3[2], N_3a, N_3b, N_3c, cov_obs[2]-old_cov3, cd3a, cd3b, cd3c, sprime3[3]/(sprime3[3]+sprime3[3]), ed3a, ed3b, ed3c])
                sprime4val = np.array([sprime4[0], sprime4[1], sprime4[2], N_4a, N_4b, N_4c, cov_obs[3]-old_cov4, cd4a, cd4b, cd4c, sprime4[3]/(sprime4[3]+sprime4[3]), ed4a, ed4b, ed4c])
                 

                #sprime, r, done, info = [np.array([200,200,200,45.5]), 4, 0, 1] #env.step(a)
                r_sum1 += r1
                r_sum2 += r2
                r_sum3 += r3
                r_sum4 += r4
                
                
                if not test_mode:
                    agent1.store_memory(s1, action1, r1, sprime1val, done1)
                    agent2.store_memory(s2, action2, r2, sprime2val, done2)
                    agent3.store_memory(s3, action3, r3, sprime3val, done3)
                    agent4.store_memory(s4, action4, r4, sprime4val, done4)
                     
                    agent1.learn()
                    agent2.learn()
                    agent3.learn()
                    agent4.learn()
                     
                    
                agent1.log(i)  # log td_error and learing_target_diff on tensorboard
                agent2.log(i)
                agent3.log(i)
                agent4.log(i)
                 
                 
                #observation = new_observation

                energy_UAV1 = sprime1[3]
                energy_UAV2 = sprime2[3]
                energy_UAV3 = sprime3[3]
                energy_UAV4 = sprime4[3]

##                tp1 = devices_by_UAVs[0]
##                tp2 = devices_by_UAVs[1]
##                tp3 = devices_by_UAVs[2]
##                tp4 = devices_by_UAVs[3]
##                 

                old_cov1 = cov_obs[0];
                old_cov2 = cov_obs[1];
                old_cov3 = cov_obs[2];
                old_cov4 = cov_obs[3];
                 
                 
                # Update state
                s1=sprime1val
                s2=sprime2val
                s3=sprime3val
                s4=sprime4val
                 
                
                
                #print(observation)
                itern += 1

                if c1>=1 and c2>=1 and c3>=1 and c4>=1: 
                    
                    break

               
            #plt.plot(xsef, ysef, '.')
            #plt.pause(0.5)            
            #plt.show()
                 
            if epsilon > 0.01:
                epsilon -= 1/(n_games_exp+1) #0.001

            fairness = pow((cov_obs[0] + cov_obs[1] + cov_obs[2] + cov_obs[3]),2)/(4*(pow(cov_obs[0],2) + pow(cov_obs[1],2) + pow(cov_obs[2],2) + pow(cov_obs[3],2)))
            
            
            writer1.add_scalar("Episode scores", r_sum1, i) ####from 1 to 2
            writer2.add_scalar("Episode scores", r_sum2, i) 
            writer3.add_scalar("Episode scores", r_sum3, i) 
            writer4.add_scalar("Episode scores", r_sum4, i)
             
            
            scores1.append(r_sum1) ###from 1 to 2
            eps_history1.append(epsilon)
            steps_arr1.append(itern)

            scores2.append(r_sum2) ###from 1 to 2
            eps_history2.append(epsilon)
            steps_arr2.append(itern)

            scores3.append(r_sum3) ###from 1 to 2
            eps_history3.append(epsilon)
            steps_arr3.append(itern)

            scores4.append(r_sum4) ###from 1 to 2
            eps_history4.append(epsilon)
            steps_arr4.append(itern)                

                   
            



            sample_len = min(10000, len(scores1))
            avg_score = np.mean(scores1[-(sample_len):])
            if avg_score > best_score:
                best_score = avg_score
                if not test_mode:
                    agent1.save_models()
                    agent2.save_models()
                    agent3.save_models()
                    agent4.save_models()
                     
                    

            #print(f'Episode {i}: score={score}, average score={avg_score}, epsilon={epsilon}, steps={itern}')
            
            
            print(epsilon)
            print("Episode: ", i, "Iteration: ", itern)
            print("Device Fairness: ", fairness_dev)
            #print("UAV Load Fairness: ", fairness)
            print("Energy Efficiency: ", eneeff)
            print("Throughput: ", tot_tp)            
            print("Total reward:", [r_sum1,r_sum2,r_sum3,r_sum4])
            print("UAV reached? ", [done1, done2, done3, done4])
            print("Connected devices:", [cov_obs[0], cov_obs[1], cov_obs[2], cov_obs[3]])
            print("Total Connected devices (/400):", cov_obs[0]+cov_obs[1]+cov_obs[2]+cov_obs[3])
            print("Energy Consumed:", [sprime1[3], sprime2[3], sprime3[3], sprime4[3]])
            print("Distance Covered:", [sprime1[5], sprime2[5], sprime3[5], sprime4[5]])
            print("*******************************End of Epidode********************************")


        
            rewcumsum1 = rewcumsum1 + r_sum1
            rewcumsum2 = rewcumsum2 + r_sum2
            rewcumsum3 = rewcumsum3 + r_sum3
            rewcumsum4 = rewcumsum4 + r_sum4
             
             

            devfairness.append(fairness_dev)
            fairfact.append(fairness)
            
            truput.append(tot_tp)
            dist_1.append(sprime1[5])
            dist_2.append(sprime2[5])
            dist_3.append(sprime3[5])
            dist_4.append(sprime4[5])
             
            
            r_sums1.append(rewcumsum1)
            r_sums2.append(rewcumsum2)
            r_sums3.append(rewcumsum3)
            r_sums4.append(rewcumsum4)
             
            UAV1cov.append(cov_obs[0])
            UAV2cov.append(cov_obs[1])
            UAV3cov.append(cov_obs[2])
            UAV4cov.append(cov_obs[3])
             
            
            UAV1eng.append(sprime1[3])
            UAV2eng.append(sprime2[3])
            UAV3eng.append(sprime3[3])
            UAV4eng.append(sprime4[3])
            
            iter_store.append(itern)

            covtot.append(cov_obs[0]+cov_obs[1]+cov_obs[2]+cov_obs[3])
            enetot.append(sprime1[3]+sprime2[3]+sprime3[3]+sprime4[3])
            fairtot.append(fairness_dev)
            efficiency.append(eneeff)
            
        
            np.savetxt('results_test/Energy.dat', enetot)
            #np.savetxt('results_test/Reward.dat', r_sum1, r_sum2, r_sum3, r_sum4)    
            np.savetxt('results_test/Coverage.dat', covtot)
            np.savetxt('results_test/Fair.dat', fairtot)
            np.savetxt('results_test/ee.dat', efficiency)
                
