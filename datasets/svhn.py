"""Dataset setting and data loader for SVHN."""


import torch
from torchvision import datasets, transforms
from misc import config as cfg


# def get_svhn(train, get_dataset=False, batch_size=cfg.batch_size):
#     """Get SVHN dataset loader."""
#     # image pre-processing
#     pre_process = transforms.Compose([transforms.Scale(cfg.image_size),
#                                       transforms.ToTensor(),
#                                       transforms.Normalize(
#                                           mean=cfg.dataset_mean,
#                                           std=cfg.dataset_std)])

#     # dataset and data loader
#     svhn_dataset = datasets.SVHN(root=cfg.data_root,
#                                  split='train' if train else 'test',
#                                  transform=pre_process,
#                                  download=False)

#     if get_dataset:
#         return svhn_dataset
#     else:
#         svhn_data_loader = torch.utils.data.DataLoader(
#             dataset=svhn_dataset,
#             batch_size=batch_size,
#             shuffle=True)
#         return svhn_data_loader

def get_svhn(train, get_dataset=False, batch_size=cfg.batch_size):
    """Get SVHN dataset loader."""
    #image pre-processing

    # pre_process = transforms.Compose([transforms.Resize(cfg.image_size),
    #                               transforms.Grayscale(num_output_channels=1),
    #                               transforms.ToTensor()])


    # pre_process = transforms.Compose([transforms.Resize(cfg.image_size),
    #                                   transforms.ToTensor(),
    #                                   transforms.Normalize(
    #                                       mean=(0.5, 0.5, 0.5),
    #                                       std=(0.5, 0.5, 0.5))])     
    
    convert_to_gray = transforms.Lambda(
    lambda x: (x[0, ...] * 0.299 + x[1, ...] * 0.587 + x[2, ...] * 0.114).unsqueeze(0))
    pre_process = transforms.Compose([transforms.Resize(cfg.image_size),
                                      transforms.ToTensor(),
                                      transforms.Normalize(
                                          mean=(0.5, 0.5, 0.5),
                                          std=(0.5, 0.5, 0.5)),                                      
                                      convert_to_gray]) 


    # pre_process = transforms.Compose([transforms.Resize(cfg.image_size),
    #                                   transforms.Grayscale(num_output_channels=1),
    #                                   transforms.ToTensor(),
    #                                   transforms.Normalize(
    #                                       mean=cfg.dataset_mean,
    #                                       std=cfg.dataset_std)])

    # dataset and data loader
    svhn_dataset = datasets.SVHN(root=cfg.data_root,
                                 split='train' if train else 'test',
                                 transform=pre_process,
                                 download=False)

    if get_dataset:
        return svhn_dataset
    else:
        svhn_data_loader = torch.utils.data.DataLoader(
            dataset=svhn_dataset,
            batch_size=batch_size,
            shuffle=True)
        return svhn_data_loader



