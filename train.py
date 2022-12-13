"""
@author: Kumara Ritvik Oruganti, Adarsh Malapaka, Sai Sandeep Adapa
Templete from Segmentation Models Pytorch, modified to train our dataset.
"""
import os
import torch
import matplotlib.pyplot as plt
import pytorch_lightning as pl
import segmentation_models_pytorch as smp
import argparse

from pprint import pprint
from torch.utils.data import DataLoader
from segmentation_models_pytorch.datasets import SimpleOxfordPetDataset
from model import PathModel

# Flop counter
from flopth import flopth


parser = argparse.ArgumentParser()
# parser.add_argument('--fold', type=int, help='0 or 1 or 2 for the current 3-fold cross-validation')
# args = parser.parse_args()

root = '.'
train_dataset = SimpleOxfordPetDataset(root, "train")
test_dataset = SimpleOxfordPetDataset(root, "test")
valid_dataset = SimpleOxfordPetDataset(root, "valid")


assert set(test_dataset.filenames).isdisjoint(set(train_dataset.filenames))

print(f"Train size: {len(train_dataset)}")
print(f"Test size: {len(test_dataset)}")

n_cpu = os.cpu_count()
train_dataloader = DataLoader(train_dataset, batch_size=4, shuffle=True, num_workers=n_cpu)
test_dataloader = DataLoader(test_dataset, batch_size=4, shuffle=False, num_workers=n_cpu)
valid_dataloader = DataLoader(valid_dataset, batch_size=4, shuffle=False, num_workers=n_cpu)

# Show some samples
# sample = train_dataset[0]
# plt.subplot(1,2,1)
# plt.imshow(sample["image"].transpose(1, 2, 0)) # for visualization we have to transpose back to HWC
# plt.subplot(1,2,2)
# plt.imshow(sample["mask"].squeeze())  # for visualization we have to remove 3rd dimension of mask
# plt.show()

# sample = valid_dataset[0]
# plt.subplot(1,2,1)
# plt.imshow(sample["image"].transpose(1, 2, 0)) # for visualization we have to transpose back to HWC
# plt.subplot(1,2,2)
# plt.imshow(sample["mask"].squeeze())  # for visualization we have to remove 3rd dimension of mask
# plt.show()

# sample = test_dataset[0]
# plt.subplot(1,2,1)
# plt.imshow(sample["image"].transpose(1, 2, 0)) # for visualization we have to transpose back to HWC
# plt.subplot(1,2,2)
# plt.imshow(sample["mask"].squeeze())  # for visualization we have to remove 3rd dimension of mask
# plt.show()


# Create a model
model = PathModel("Unet", "mobilenet_v2", in_channels=3, out_classes=1)

# Flops counter for created model
# dummy_inputs = torch.rand(1, 3, 640, 352)
# flops, params = flopth(model, inputs=(dummy_inputs,), show_detail=True)
# print(flops, params)

# Train the model
trainer = pl.Trainer(gpus=1, max_epochs=1, accelerator="auto")
trainer.fit(model, train_dataloaders=train_dataloader, val_dataloaders=valid_dataloader)

# Print Metrics
# print(model.log_dict)
# valid_metrics = trainer.validate(model, dataloaders=valid_dataloader, verbose=True)
# pprint(valid_metrics)

# test_metrics = trainer.test(model, dataloaders=test_dataloader, verbose=True)
# print("Test Metrices:")
# pprint(test_metrics)


# Visualization

batch = next(iter(test_dataloader))
with torch.no_grad():
    model.eval()
    logits = model(batch["image"])
pr_masks = logits.sigmoid()

for image, gt_mask, pr_mask in zip(batch["image"], batch["mask"], pr_masks):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(image.numpy().transpose(1, 2, 0))  # convert CHW -> HWC
    plt.title("Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(gt_mask.numpy().squeeze()) # just squeeze classes dim, because we have only one class
    plt.title("Ground truth")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(pr_mask.numpy().squeeze()) # just squeeze classes dim, because we have only one class
    plt.title("Prediction")
    plt.axis("off")

    plt.show()
