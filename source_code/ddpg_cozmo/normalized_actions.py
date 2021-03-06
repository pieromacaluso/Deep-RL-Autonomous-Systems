import gym


class NormalizedActions(gym.ActionWrapper):
    def __init__(self, env):
        """
        Args:
            env:
        """
        super().__init__(env)
    
    def action(self, action):
        """Transform the action normalized between [-1, 1] to the correct
        action-space bound of the environment. mod -> range of the actions tra
        -> center of the actions

        Args:
            action: action normalized in [-1, 1]

        Returns:
            action de-normalized in the environment space
        """
        mod = (self.action_space.high - self.action_space.low) / 2
        tra = (self.action_space.high + self.action_space.low) / 2
        action = action * mod + tra
        # action = action * (self.action_space.high - self.action_space.low) + self.action_space.low
        return action
    
    def _reverse_action(self, action):
        """Normalize the action between [-1, 1]

        Args:
            action: action in the action-space range

        Returns:
            action normalized in [-1, 1]
        """
        mod = (self.action_space.high - self.action_space.low) / 2
        tra = (self.action_space.high + self.action_space.low) / 2
        action = (action - tra) / mod
        return action
