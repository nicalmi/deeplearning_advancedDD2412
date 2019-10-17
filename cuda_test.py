# Additionally, to check if your GPU driver and CUDA is enabled and accessible by PyTorch,
# run the following commands to return whether or not the CUDA driver is enabled:

import torch
print(torch.cuda.is_available())
