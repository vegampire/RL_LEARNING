import gym  
env = gym.make('CartPole-v0')  
env.reset()  
for _ in range(1000):
    env.render()  
    action = env.action_space.sample() 
    observation, reward, done, info = env.step(action)
    print(observation)
env.close()

#[ 0.01653398  0.19114579  0.02013859 -0.28050058]