import os
from glob import glob

from skimage.io import imread

import hub
from hub.schema import Image
from hub import transform


def fasthub_up(directory, tag) -> hub.api.dataset.Dataset:
    """Upload images to Hub.
    """
    paths = glob(directory + '/*')

    if len(paths) == 0:
        raise ValueError("Empty folder")

    size, max_size = _infer_shapes(paths)
    schema = _generate_schema(size=size, max_size=max_size)

    @transform(schema=schema)
    def load_transform(p):
        image = imread(p)
        return {
            "data": image
        }

    ds = load_transform(paths)  # returns a transform object
    return ds.store(tag)


def _infer_shapes(paths: str):
    """Infer shapes and max shapes from data.
    """
    heights = []
    widths = []
    channels = []

    for path in paths:
        img = imread(path)

        height = img.shape[0]
        width = img.shape[1]
        channel = img.shape[2]

        if height not in heights:
            heights.append(height)

        if width not in widths:
            widths.append(width)

        if channel not in channels:
            channels.append(channel)

    size = [None, None, None]
    max_size = [None, None, None]
    
    if len(heights) > 1:
        max_size[0] = sorted(heights)[-1]
    else:
        size[0] = heights[0]

    if len(widths) > 1:
        max_size[1] = sorted(widths)[-1]
    else:
        size[1] = widths[0]

    if len(channels) > 1:
        max_size[2] = sorted(channels)[-1]
    else:
        size[2] = channels[0]
        
    return tuple(size), tuple(max_size)


def _generate_schema(size, max_size):
    """Generate a hub.Schema.
    """
    if all(x is None for x in max_size):
        d = Image(shape=size, dtype="uint8")
    else:
        max_size = list(max_size)
        for i, (a, b) in enumerate(zip(size, max_size)):
            if a != None and b == None:
                max_size[i] = a
        max_size = tuple(max_size)
        
        d = Image(shape=size, max_shape=max_size, dtype="uint8")        
    return {"data": d}