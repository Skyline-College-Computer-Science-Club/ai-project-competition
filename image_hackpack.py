import openai

# For more assistance, and the rest of the OpenAI documentation go to:
# https://platform.openai.com/docs/overview

# [REQUIRED] This is where the API key goes
# You can find it in the overview Google doc (go back into our announcements and scroll up)
# Make sure that the API key is still a string
openai.api_key = 'Replace this text with the API key'

# DIFFERENT MODELS, PRICING, AND RESOLUTIONS 
#
# DALL-E 3:
#              Size          Price
#   Standard:  1024x1024  -  $0.04/image
#              1792x1024  -  $0.08/image
#           or 1024x1792 
#   HD:        1024x1024  -  $0.08/image
#              1792x1024  -  $0.12/image
#           or 1024x1792
#
# HD == more detail
#
#
# DALL-E 2:
#   Standard:  1024x1024  -  $0.02/image
#              512x512    -  $0.018/image
#              256x256    -  $0.016/image
#
# DALL-E 2 can use edits/inpainting as well as variations


# This is the basic template for generating an image
image_response = openai.images.generate (
    model='dall-e-3',
    # Set to either dall-e-3 or dall-e-2
    # DALL-E 3 will generate more artistic and creative images, 
    # while DALL-E 2 has other capabilities listed below
    prompt='',
    # Prompt for image generation
    size=''
    # See resolution sizes above
)

image_url = image_response.data[0].url



# DALL-E 2 ONLY: Variations

# DALL-E 2 can create image variations. These allow you to create AI
# variations/alterations of an already existing image

# First line is generally the same, but instead of 'generate', use 'create_variation'
image_response = openai.images.create_variation (
    # Put the file name of the original image here
    # The image file should be in the same folder as this hackpack
    # The image must be square, less than 4MB in size
    image=open('original_image.png','rb'),

    # With DALL-E 2, you can create multiple images in a single
    # function call. However, this does still charge you per
    # image, so be careful and mindful of your usage with this
    n=1,

    # See chart above for sizes and pricing
    size='1024x1024'
)

image_url = image_response.data[0].url