import torch
from torch import autocast
from diffusers import StableDiffusionPipeline, LMSDiscreteScheduler

device = "cpu"

# CUDA or CPU inference
if torch.cuda.is_available():
    print('CUDA inference started.')
    device = 'cuda'
    # RTX3070ti 8gb is low vram gpu...
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4",
                                                   revision="fp16",
                                                   torch_dtype=torch.float16,
                                                   use_auth_token=True).to('cuda')
else:
    print('CPU inference started.')
    # Optimization for cpu inference
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float32, low_cpu_mem_usage=True, use_auth_token=True).to('cpu')

# CUSTOM PROMPT -- YOU CAN ENTER WHATEVER YOU WANT IN THIS VARIABLE(str type)
prompt = "A digital Illustration of the Babel tower, 4k, detailed, trending in artstation, fantasy vivid colors"

with torch.autocast(device):
    image = pipe(prompt, guidance_scale=7.5)['sample'][0]

# SAVE RESULT -- check the name of file
image.save("test.png")
