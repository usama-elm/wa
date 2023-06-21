from transformers import BartForConditionalGeneration, BartTokenizer
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load pretrained model and tokenizer
model_path = "./model/ffmpeg-bart.bin"
model = BartForConditionalGeneration.from_pretrained(model_path).to(device)
tokenizer = BartTokenizer.from_pretrained(model_path)

# Set model to evaluation mode
model.eval()

while True:
    # Get user input
    request = input("Enter your request: ")

    if request.lower() == 'quit':
        break

    # Encode the request and generate command
    input_ids = tokenizer.encode(request, return_tensors="pt").to(device)
    output_ids = model.generate(input_ids)

    # Decode the output ids to get the command
    command = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    print("Generated FFmpeg command: ", command)

