import torch
from torch import Tensor


class ImageList:
    """
    The "ImageList" class is to handle batches of images that may be of varying sizes, so model can process images uniformly.

    This class is a slightly modified implementation of the PyTorch implementation.
    (https://github.com/pytorch/vision/blob/main/torchvision/models/detection/image_list.py)

    The original class requres image_sized 2 args:
    tensors (tensor): Tensor containing images.
    image_sizes (list[tuple[int, int]]): List of Tuples each containing size of images.
    
    We simplifies the initialization by not requiring the explicit list of image sizes. The MIMIC-CXR image dataset we use has a uniform size(256×256).
    """

    def __init__(self, images_tensor: Tensor) -> None:
        self.tensors = images_tensor

        # all tensors have the same shape ([batch_size, 1, image_width, image_height])
        batch_size = images_tensor.shape[0]
        image_sizes = images_tensor.shape[-2:]

        self.image_sizes = [tuple(image_sizes) for _ in range(batch_size)]

    def to(self, device: torch.device) -> "ImageList":
        cast_tensor = self.tensors.to(device)
        return ImageList(cast_tensor, self.image_sizes)

