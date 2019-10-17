# To ensure that PyTorch was installed correctly, we can verify the installation by running sample PyTorch code.
# Here we will construct a randomly initialized tensor.

from __future__ import print_function
import torch
x = torch.rand(5, 3)
print(x)

'''Output example
tensor([[0.3380, 0.3845, 0.3217],
        [0.8337, 0.9050, 0.2650],
        [0.2979, 0.7141, 0.9069],
        [0.1449, 0.1132, 0.1375],
        [0.4675, 0.3947, 0.1426]])'''
