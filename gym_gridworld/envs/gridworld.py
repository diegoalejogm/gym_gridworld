import math
import gym
from gym import spaces


class SquareGridWorld(gym.Env):

    metadata = {'render.modes': ['human']}

    def __init__(self, l):
        self.l = l
        self.initial = 0
        self.transition_reward = -1
        self.agent_state = self.initial
        self.finish = l**2 - 1
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Discrete(self.l**2)

    def _step(self, action):
        assert self.action_space.contains(action)
        next_state = self.__next_agent_state__(action)
        observation = {'state': next_state}
        reward = self.transition_reward
        done = self.__is_finish_state__(next_state)
        info = None
        return observation, reward, done, info

    def _reset(self):
        self.agent_state = self.initial

    def _render(self, mode='human', close=False):
        pass

    def _seed(self, seed=None):
        pass

    # Control methods

    def __is_finish_state__(self, state):
        return state == self.finish

    def __next_agent_state__(self, action):
        agent_row = math.floor(self.agent_state / self.l)
        agent_col = self.agent_state % self.l

        # Handle Up
        if action == 0:
            return self.agent_state if agent_row == 0 else self.agent_state - self.l
        # Handle Right
        if action == 1:
            return self.agent_state if agent_col == self.l - 1 else self.agent_state + 1
        # Handle Down
        if action == 2:
            return self.agent_state if agent_row == self.l - 1 else self.agent_state + self.l
        # Handle Left
        if action == 3:
            return self.agent_state if agent_col == 0 else self.agent_state - 1
