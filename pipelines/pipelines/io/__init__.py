# SPDX-License-Identifier: Apache-2.0
"""IO assets for the pipeline package.

This module provides a central point for importing and re-exporting all IO-related assets
used in the pipeline system.

"""

from .image import image_dataset_config, image_list, load_pil_images_op

IMAGE_ASSETS = [image_list, image_dataset_config]
IMAGE_OPS = [load_pil_images_op]
ASSETS = [*IMAGE_ASSETS]
OPS = [*IMAGE_OPS]


__all__ = ["ASSETS", "OPS", "image_dataset_config"]
