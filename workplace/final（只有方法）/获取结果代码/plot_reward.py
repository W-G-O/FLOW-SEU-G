import pandas as pd
import matplotlib.pyplot as plt

def PlotbothRew_Inter(PATH):
    first_PATH = PATH
    FILE_PATH = first_PATH + "/" + "progress.csv"
    EXP_TAG = "fixed_time_ppo"
    df = pd.read_csv(FILE_PATH )
    max_r, min_r,r = df["episode_reward_max"], df["episode_reward_min"], df["episode_reward_mean"]
    iteration = df["training_iteration"]

    fig = plt.figure(figsize=(6, 4.8))
    plt.plot(iteration, r, c='b')
    # plt.plot(iteration, max_r, label="max-reward", c='y')
    # plt.plot(iteration, min_r, label="min-reward", c='r')
    # plt.fill_between(iteration, min_r, max_r, where=(max_r>min_r),color='y',alpha=0.3)

    plt.xlabel('number of iterations')
    plt.ylabel("reward")
    plt.grid(color='y',)
    plt.legend(loc="lower right")
    plt.show()
    fig.savefig(first_PATH + '/' +"all_"+ EXP_TAG + '.png')

def PlotCav_LigthtRew_Inter(PATH):
    first_PATH=PATH
    FILE_PATH = first_PATH+"/"+"progress.csv"
    EXP_TAG = "fixed_time_ppo"

    df = pd.read_csv(FILE_PATH)
    max_r, min_r,r = df["episode_reward_max"], df["episode_reward_min"], df["episode_reward_mean"]
    iteration = df["training_iteration"]

    fig = plt.figure(figsize=(6, 4.8))
    plt.plot(iteration, r, c='b')
    # plt.plot(iteration, max_r, label="max-reward", c='y')
    # plt.plot(iteration, min_r, label="min-reward", c='r')
    # plt.fill_between(iteration, min_r, max_r, where=(max_r>min_r),color='y',alpha=0.3)

    plt.xlabel('number of iterations')
    plt.ylabel("reward")
    plt.grid(color='y',)
    plt.legend(loc="lower right")
    plt.show()
    fig.savefig(first_PATH + '/' +"all_"+ EXP_TAG + '.png')

    max_r, min_r,r = df["policy_reward_max/cav"], df["policy_reward_min/cav"], df["policy_reward_mean/cav"]
    iteration = df["training_iteration"]

    fig = plt.figure(figsize=(6, 4.8))
    plt.plot(iteration, r, c='b')
    # plt.plot(iteration, max_r, label="max-reward", c='y')
    # plt.plot(iteration, min_r, label="min-reward", c='r')
    # plt.fill_between(iteration, min_r, max_r, where=(max_r>min_r),color='y',alpha=0.3)

    plt.xlabel('number of iterations')
    plt.ylabel("icv_reward")
    plt.grid(color='y',)
    plt.legend(loc="lower right")
    plt.show()
    fig.savefig(first_PATH + '/'+"icv_" + EXP_TAG + '.png')

    max_r, min_r,r = df["policy_reward_max/tl"], df["policy_reward_min/tl"], df["policy_reward_mean/tl"]
    iteration = df["training_iteration"]

    fig = plt.figure(figsize=(6, 4.8))
    plt.plot(iteration, r, c='b')
    # plt.plot(iteration, max_r, label="max-reward", c='y')
    # plt.plot(iteration, min_r, label="min-reward", c='r')
    # plt.fill_between(iteration, min_r, max_r, where=(max_r>min_r),color='y',alpha=0.3)

    plt.xlabel('number of iterations')
    plt.ylabel("tl_reward")
    plt.grid(color='y',)
    plt.legend(loc="lower right")
    plt.show()
    fig.savefig(first_PATH + '/' + "tl_"+EXP_TAG + '.png')

def PlotAll(PATH):
    import os
    import numpy as np
    import pandas as pd
    # 当前目录
    dataPath = "/home/g/software/pycharm/projects/flow-SEU/workplace/final/"+PATH

    if "PO" in dataPath:
        PlotbothRew_Inter(dataPath)
        PlotCav_LigthtRew_Inter(dataPath)
    else:
        PlotbothRew_Inter(dataPath)



PATHS=["1*1路网/Co_PPO","1*1路网/fixedtime_cav","1*1路网/In_PPO","1*1路网/RL_HV",
       "1*6路网/Co_PPO","1*6路网/fixedtime_cav","1*6路网/In_PPO","1*6路网/RL_HV",
       "3*4路网/Co_PPO","3*4路网/fixedtime_cav","3*4路网/In_PPO","3*4路网/RL_HV",]
for PATH in PATHS:
    PlotAll(PATH)

