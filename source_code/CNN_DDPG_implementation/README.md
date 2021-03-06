# Convolutional Neural Network DDPG Implementation (TBM)
The first step towards the objective of the Master Thesis was the implementation of the algorithm in **[1]**.

This first version is not capable to elaborate images but only continuous environments of OpenAI Gym such as **MountainCarContinuous-v0**. 

The next step will be the implementation of the same algorithm using images as input, which is a similar context to the one of the Anki Cozmo environment.

## Data and Hyper-Parameter Used
### Neural Network
### Critic (Value) Neural Network
```python
CriticNN(
  (linear1): Linear(in_features=3, out_features=256, bias=True)
  (linear2): Linear(in_features=256, out_features=256, bias=True)
  (linear3): Linear(in_features=256, out_features=1, bias=True)
)
```
### Actor (Policy) Neural Network
```python
ActorNN(
  (linear1): Linear(in_features=2, out_features=256, bias=True)
  (linear2): Linear(in_features=256, out_features=256, bias=True)
  (linear3): Linear(in_features=256, out_features=1, bias=True)
)
```
### Ornstein Uhlenbeck process noise
```python
mu=0.0
sigma=0.3
theta=0.15
```
### DDPG
```python
# Decay of OUNoise
eps_start=0.9
eps_end=0.2
eps_decay=1000

# ReplayBuffer
batch_size=32
replay_min_size=10000
replay_max_size=1000000

# Simulation
n_episode=1000
episode_max_len=1000

# Update
discount=0.99
critic_weight_decay=0.
critic_update_method='adam'
critic_lr=1e-3
actor_weight_decay=0
actor_update_method='adam'
actor_lr=1e-4
soft_target_tau=0.001
n_updates_per_sample=1

# Test
eval_samples=10000
```

## Plots
These plots refers to one run of the DDPG algorithm using the **MountainCarContinuous-v0** environment provided by OpenAI Gym
## Comments about the results
As reported in OpenAI Gym Leaderboards the problem is considered solved if the mean of the last 100 episode is greater than 90. This code reaches this threshold after about 130 episode ([plot](https://github.com/pieromacaluso/A-Study-Of-Reinforcement-Learning/blob/master/source_code/NN_DDPG_implementation/README.md#reward-mean-over-last-100)). Taking into account that we are using a simple NN this is an accettable result, therefore it can be used as a good baseline to start the evolution of our project.

### Hyperparameters
#### Epsilon Decay
![hp_decay_epsilon](./svg_plots/hp_decay_epsilon.svg)
### Test
#### Steps mean
![test_steps_mean](./svg_plots/test_steps_mean.svg)
#### Reward mean
![test_reward_mean](./svg_plots/test_reward_mean.svg)\
### Train
#### Reward Mean
![reward_running_mean](./svg_plots/reward_running_mean.svg)
#### Reward Mean over last 100
![reward_running_mean_last_100](./svg_plots/reward_running_mean_last_100.svg)

### Loss
#### Critic (Value) Loss
![losses_critic_value](./svg_plots/losses_critic_value.svg)
#### Actor (Policy) Loss 
![losses_actor_policy](./svg_plots/losses_actor_policy.svg)

## References
**[1]** [Learning to Drive in a Day](https://arxiv.org/pdf/1807.00412.pdf) (Sep 2018) by Alex Kendall, Jeffrey Hawke, David Janz, Przemyslaw Mazur, Daniele Reda, John-Mark Allen, Vinh-Dieu Lam, Alex Bewley & Amar Shah

**[2]** [Continuous Control with Deep Reinforcement Learning](https://arxiv.org/pdf/1509.02971.pdf) (Feb 2016) by Timothy P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver & Daan Wierstra
