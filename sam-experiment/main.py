import torch, cv2
torch.cuda.empty_cache()
from segment_anything import sam_model_registry,SamAutomaticMaskGenerator
import supervision as sv


DEVICE = torch.device('cpu' if torch.cuda.is_available() else 'cuda:0')
MODEL_TYPE = "vit_h"
CHECKPOINT_PATH="sam_vit_h_4b8939.pth"
IMAGE_PATH="/home/asmy/Downloads/IMG-20221016-WA0003.jpg"

sam = sam_model_registry[MODEL_TYPE](checkpoint=CHECKPOINT_PATH)
sam.to(device=DEVICE)

mask_generator = SamAutomaticMaskGenerator(sam)

image_bgr = cv2.imread(IMAGE_PATH)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
result = mask_generator.generate(image_rgb)

mask_annotator = sv.MaskAnnotator()
detections = sv.Detections.from_sam(result)
annotated_image = mask_annotator.annotate(image_bgr, detections)
