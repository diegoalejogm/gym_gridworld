import math
from collections import defaultdict
import gym
from gym import spaces


class SquareGridWorld(gym.Env):

    UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
    metadata = {'render.modes': ['human']}

    def __init__(self, l):
        self.l = l
        self.transition_reward = -1
        self.reward_range = [self.transition_reward, self.transition_reward]
        self.state = 1
        self.finish = [0, l**2 - 1]
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Discrete(self.l**2)
        self._state_transition_prob = self.__generate_state_transition_prob__()

    def _step(self, action):
        assert self.action_space.contains(action)
        self.state = self.next_state(self.state, action)
        observation = {'state': self.state}
        reward = self.transition_reward
        done = self.__is_finish_state__(self.state)
        info = None
        return observation, reward, done, info

    def _reset(self):
        pass

    def _render(self, mode='human', close=False):
        pass

    def _seed(self, seed=None):
        pass

    # Control methods

    def __is_finish_state__(self, state):
        return state in self.finish

    def next_state(self, state, action):
        assert self.observation_space.contains(state)
        assert self.action_space.contains(action)
        agent_row = math.floor(state / self.l)
        agent_col = state % self.l

        # Handle Up
        if action == self.UP:
            return state if agent_row == 0 else state - self.l
        # Handle Right
        if action == self.RIGHT:
            return state if agent_col == self.l - 1 else state + 1
        # Handle Down
        if action == self.DOWN:
            return state if agent_row == self.l - 1 else state + self.l
        # Handle Left
        if action == self.LEFT:
            return state if agent_col == 0 else state - 1

    # Additional functionality

    def state_transition_prob(self, s1, r, s, a):
        return self._state_transition_prob.get((s1, r, s, a), 0)

    def __generate_state_transition_prob__(self):
        prob = defaultdict()

        for s in range(1, self.observation_space.n - 1):
            for a in range(self.action_space.n):
                s1 = self.next_state(s, a)
                prob[(s1, self.transition_reward, s, a)] = 1.0
        return prob
