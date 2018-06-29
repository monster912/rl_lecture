# coding=utf8
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from agents.agent import AbstractAgent
from agents.common.input import observation_dim
import logging
import config

logger = logging.getLogger('rl.agent')
FLAGS = config.flags.FLAGS


class Agent(AbstractAgent):

    def __init__(self, env):
        super(Agent, self).__init__(env)
        logger.info("Random Agent")

        self.action_dim = env.action_space.n
        self.obs_dim = observation_dim(env.observation_space)
        self.train_step = FLAGS.train_step
        self.test_step = FLAGS.test_step

    def learn(self):
        logger.debug("No Learning")

    def test(self, global_step=0):
        logger.debug("Test step: {}".format(global_step))

        global_step = 0
        total_reward = 0
        episode_num = 0

        while global_step < self.test_step:

            episode_num += 1

            self.env.reset()  # Reset environment
            done = False

            while not done:
                global_step += 1
                action = self.get_action()

                _, reward, done, _ = self.env.step(action)

                if FLAGS.gui:
                    self.env.render()

                total_reward += reward

        print("[ train_ep: {}, total reward: {} ]".format(episode_num, total_reward))

    def get_action(self):
        # 키보드 인풋 받을 것
        return self.env.action_space.sample()
