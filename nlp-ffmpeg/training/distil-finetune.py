from transformers import BartForConditionalGeneration, BartTokenizer, Trainer, TrainingArguments
import torch
import json

# Make sure we're running on GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 1. Load and process data
with open('commands.json', 'r') as f:
    data = json.load(f)

requests = ["convert: " + item['request'] for item in data] 
commands = [item['command'] for item in data]

# 2. Tokenize
tokenizer = BartTokenizer.from_pretrained('facebook/bart-base')
train_encodings = tokenizer(requests, truncation=True, padding=True, max_length=512)
train_labels = tokenizer(commands, truncation=True, padding=True, max_length=512)

# Prepare dataset
class MyDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]).to(device) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels['input_ids'][idx]).to(device)  # We'll use input_ids as labels
        return item

    def __len__(self):
        return len(self.labels['input_ids'])

train_dataset = MyDataset(train_encodings, train_labels)

# 3. Prepare for training
model = BartForConditionalGeneration.from_pretrained('facebook/bart-base').to(device)

# Define your Trainer
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=4,
    per_device_train_batch_size=32,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    save_strategy='steps',  # Save the model every 'n' steps
    save_steps=1000,  # number of steps for model to be saved
    dataloader_pin_memory=False,  # Set pin_memory to False
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
)

# 4. Train model
trainer.train()

# 5. Save model
model_path = "./model/ffmpeg-bart.bin"
model.save_pretrained(model_path)
tokenizer.save_pretrained(model_path)

