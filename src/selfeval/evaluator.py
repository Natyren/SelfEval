import torch


class Evaluator:
    def __init__(self, scheduler, model, num_timesteps):
        self.scheduler = scheduler
        self.model = model
        self.num_timesteps = num_timesteps

    def reverse_diffusion(self, img, text):
        pass

    def evaluate_on_step(self, timestep):
        pass

    def evaluate(self, image: torch.Tensor):
        """
        1. Noise Image step by step, saving the residiuals
        2. Denoising collected noise step by step with text prior, comparing with saved noised residiuals
        3. On every step compute conditionals
        4. Compute final probability and likelyhood
        5. Compute final text prior probability
        """
        pass
