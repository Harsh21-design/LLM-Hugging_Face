# image generation using stable diffussion

from diffusers import StableDiffusionPipeline
import torch

model_id = "stabilityai/sd-turbo"

pipe = StableDiffusionPipeline.from_pretrained(model_id,
                                              torch_dtype=torch.float32)

pipe = pipe.to("cpu")

prompt = "picture of a cute panda sitting"
# prompt = "a cat playing with ball"

image = pipe(prompt,
            num_inference_steps=25).images[0]

image.show()
image.save("panda.png")
# image.save("cat.png")
