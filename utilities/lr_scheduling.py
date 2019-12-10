#Library Imports
import math

#Using Adam optimizer with
#Beta_1=0.9, Beta_2=0.98, and Epsilon=10^-9

#Learning rate varies over course of training
#lrate = sqrt(d_model)*min((1/sqrt(step_num)), step_num*(1/warmup_steps*sqrt(warmup_steps)))

# LrStepTracker
class LrStepTracker:
    def __init__(self, model_dim=512, warmup_steps=4000):
        # Store Values
        self.warmup_steps = warmup_steps
        self.model_dim = model_dim

        # Begin Calculations
        self.invsqrt_dim = (1 / math.sqrt(model_dim))
        self.invsqrt_warmup = (1 / (warmup_steps * math.sqrt(warmup_steps)))

    # step
    def step(self, step):
        if(step <= self.warmup_steps):
            return self.invsqrt_dim * self.invsqrt_warmup * step
        else:
            invsqrt_step = (1 / math.sqrt(step))
            return self.invsqrt_dim * invsqrt_step

# get_lr
def get_lr(optimizer):
    for param_group in optimizer.param_groups:
        return param_group['lr']