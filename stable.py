import os
import requests
import config
import base64



api_host = 'https://api.stability.ai/'
api_key = config.api_key
url = f"{api_host}/v1/engines/list"
engine_id = 'stable-diffusion-xl-beta-v2-2-2'



def getModelList():
    url = f"{api_host}/v1/engines/list"
    response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})

    if response.status_code == 200:
        payload = response.json()
        print(payload)





def generateStableDiffusionImage(prompt, height, width, steps):
    url = f"{api_host}v1/generation/{engine_id}/text-to-image"
    headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
    }
    
    payload = {}
    payload["text_prompts"] = [{"text": f"{prompt}"}]
    payload["cfg_scale"] = 7
    payload["clip_guidance_present"] = "FAST_BLUE"
    payload["height"] = height
    payload["width"] = width
    payload["samples"] = 1
    payload["steps"] = steps
    # payload["style_present"] = "anime"



    response = requests.post(url, headers=headers, json=payload)

    #Processing the response
    if response.status_code == 200:
        data = response.json()
        for i, image in enumerate(data["artifacts"]):
            with open(f"v1_txt2img_{i}.png", "wb") as f:
                f.write(base64.b64decode(image["base64"]))







# url = f"{api_host}v1/generation/{engine_id}/text-to-image"
# headers = {
#         "Content-Type": "application/json",
#         "Accept": "application/json",
#         "Authorization": f"Bearer {api_key}"
# }
    
# payload = {}
# payload["text_prompts"] = [{"text": f"{prompt}"}]
# payload["cfg_scale"] = 7
# payload["clip_guidance_present"] = "FAST_BLUE"
# payload["height"] = height
# payload["width"] = width
# payload["samples"] = 1
# payload["steps"] = steps
# payload["style_present"] = "anime"








generateStableDiffusionImage(
    prompt='Create a high resolution picture image of a luxury car in a studio setting, showcasing its sleek lines and high-end features. Perfect lighting with highlights',
    height=512,
    width=512,
    steps=50
)



# 'Create a high resolution picture image of a luxury car in a studio setting, showcasing its sleek lines and high-end features. Perfect lighting with highlights'



