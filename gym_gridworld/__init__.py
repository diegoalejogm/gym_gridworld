from gym.envs.registration import register

register(
    id='square-gridworld-v0',
    entry_point='gym_gridworld.envs:SquareGridWorld',
    kwargs={'l': 4}
)
