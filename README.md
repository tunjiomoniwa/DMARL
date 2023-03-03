# DMARL
This git repository is linked to the thesis research titled: "Using deep reinforcement learning to optimise energy efficiency of UAV small
cells in urban environments" It presents codes for the Decentralised Multi-Agent Reinforcement Learning (DMARL) for UAV-assisted networks. Here, each UAV in the network is equipped with an autonomous agent. Our DMARL solution 
Our DMARL solution comprises of 5 variants, namely: 
1. DQLSI variant coded using MATLAB, while
2. MAD-DDQN,
3. CMAD-DDQN,
4. DAMAD-DDQN and
5. DACEMAD-DDQN are coded in Python. The Double Deep Q-Network library used was adapted from: https://github.com/jeffery1236/Atari_DoubleDeepQNetwork

The Figure below shows our considered scenario:

<img src="https://user-images.githubusercontent.com/46023480/220615690-76feb823-975c-4d81-a5d8-12d3886c6749.jpg" width=40% height=40%>
Due to the difficulty in obtaining non-sparse and temporal mobility traces, several mathematical mobility models have been proposed in ad-hoc networks literature to depict the realistic mobility patterns of ground users. We call three widely used mobility models in our simulations: 
(i) Random Walk (RW),
(ii) Random WayPoint (RWP) and,
(iii) Gauss Markov Mobility (GMM). 

In our simulations, we also use some real world data, especially in the DAMAD-DDQN and DACEMAD-DDQN variants where we investigate different road traffic scenarios in the Republic of Ireland. Some of the data were gotten from SUMO via the link: https://github.com/maxime-gueriau/ITSC2020_CAV_impact.
The FCD script is included for reproducibility. Also since the FCD data is quite large, BaseX was used to query the data and filter out the GPS data of the vehicles and persons in the network.

You may cite using:

For DQLSI:
B. Omoniwa, B. Galkin and I. Dusparic, "Energy-aware optimization of UAV base stations placement via decentralized multi-agent Q-learning," 2022 IEEE 19th Annual Consumer Communications & Networking Conference (CCNC), Las Vegas, NV, USA, 2022, pp. 216-222, doi: 10.1109/CCNC49033.2022.9700536.

For MAD-DDQN: 
B. Omoniwa, B. Galkin and I. Dusparic, "Optimizing Energy Efficiency in UAV-Assisted Networks Using Deep Reinforcement Learning," in IEEE Wireless Communications Letters, vol. 11, no. 8, pp. 1590-1594, Aug. 2022, doi: 10.1109/LWC.2022.3167568.

For queries and advice on improvement, you may reach me on tunjiomoniwa at yahoo dot com.
