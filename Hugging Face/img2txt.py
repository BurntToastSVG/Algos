import transformers


# CREATE A PIPELINE
pipe = transformers.pipeline( "image-to-text" , model = "Salesforce/blip-image-captioning-base"  )


# CREATE AN INPUT
image_description = pipe("eveonline-min-700x394.jpeg")


# DISPLAY THE OUTPUT
print(image_description)











# TODO
# take image description to LLM GPT model to write us a story about this picture

# create a soundtrack of someone telling the story