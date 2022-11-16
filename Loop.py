#When run, this file will simply play Street Fighter with completely random inputs, and output the rewards that it recieves
#Retro is the emulator used here
import retro
#Time is used to slowdown the emulation
import time

#The environment is first created using retro's list of games. Environment MUST be closed for it to be run again

def randomLoop(episodes): 
    total_steps = 0
    total_reward = 0
    #Output data
    r = open("RandomRewards.csv", 'w')
    r.write("Steps, Average Reward \n")
    l = open("RandomLengths.csv", 'w')
    l.write("Episodes, Average Episode Length \n")
    for i in range(episodes):
        env = retro.make(game='StreetFighterIISpecialChampionEdition-Genesis')
        obs = env.reset()
        # Set flag to flase
        done = False 

        episode_length = 0
        while not done: 
            if done: 
                obs = env.reset()
            
            #If rendering the game, uncomment the next two lines
            #env.render()
            #time.sleep(0.01)

            #Every step within our game emulation returns several results
            #Obs: This is the observation space
            #Reward: The rewards recieved for that frame. Typically it is 0.
            #Done: Returns a boolean to tell us if the game has ended or not
            #Info: Returns additional info abotu the scene
            obs, reward, done, info = env.step(env.action_space.sample())

            #This if for the outputs
            total_reward += reward
            total_steps += 1
            episode_length += 1
            avg_reward = total_reward / total_steps
            r.write(str(total_steps) +  "," + str(avg_reward) + "\n")    
        print(i)
        l.write(str(i+1) +  "," + str(episode_length) + "\n")   
        env.close()

randomLoop(5)