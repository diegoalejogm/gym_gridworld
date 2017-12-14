import math
import gym
from gym import spaces


class SquareGridWorld(gym.Env):

    UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
    metadata = {'render.modes': ['human']}

    def __init__(self, l):
        self.l = l
        self.initial = 0
        self.transition_reward = -1
        self.state = self.initial
        self.finish = l**2 - 1
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Discrete(self.l**2)

    def _step(self, action):
        assert self.action_space.contains(action)
        self.state = self.__next_state__(action)
        observation = {'state': self.state}
        reward = self.transition_reward
        done = self.__is_finish_state__(self.state)
        info = None
        return observation, reward, done, info

    def _reset(self):
        self.state = self.initial

    def _render(self, mode='human', close=False):
        pass

    def _seed(self, seed=None):
        pass

    # Control methods

    def __is_finish_state__(self, state):
        return state == self.finish

    def __next_state__(self, action):
        agent_row = math.floor(self.state / self.l)
        agent_col = self.state % self.l

        # Handle Up
        if action == self.UP:
            return self.state if agent_row == 0 else self.state - self.l
        # Handle Right
        if action == self.RIGHT:
            return self.state if agent_col == self.l - 1 else self.state + 1
        # Handle Down
        if action == self.DOWN:
            return self.state if agent_row == self.l - 1 else self.state + self.l
        # Handle Left
        if action == self.LEFT:
            return self.state if agent_col == 0 else self.state - 1
