from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image
import torch
import requests
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Load the pre-trained DETR model and the image processor
processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

# Load an image of a floor plan with visible paths
image_url = "https://example.com/path_to_floor_plan_image.jpg"  # Replace with your image URL
image = Image.open(requests.get(image_url, stream=True).raw)

# Preprocess the image and make predictions
inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)

# Post-process and filter the predictions
target_classes = [42]  # Replace 42 with class id(s) related to "paths" if fine-tuned
target_scores = 0.9    # Adjust this threshold as needed

# Convert the output logits to predicted boxes and classes
results = processor.post_process_object_detection(outputs, threshold=target_scores, target_sizes=[image.size])[0]

# Plot the image with bounding boxes for paths
plt.figure(figsize=(10, 10))
plt.imshow(image)
ax = plt.gca()

for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    if label in target_classes and score > target_scores:
        xmin, ymin, xmax, ymax = box
        rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, linewidth=2, edgecolor="r", facecolor="none")
        ax.add_patch(rect)
        ax.text(xmin, ymin, f"{label}: {score:.2f}", color="white", bbox=dict(facecolor="red", alpha=0.5))

plt.axis("off")
plt.show()
