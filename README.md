# FastHub
FastHub is a collection of utilities for [Hub](https://github.com/activeloopai/hub).

## Quickstart
### Moving bytes back and forth on Hub
```python
from FastHub import fasthub_up

my_dataset = fasthub_up(directory="images", tag='mynameisvinn/samples')
```
We can retrieve dataset:
```python
# retrieve images from dataset
tag = "mynameisvinn/samples"
retrieved_dataset = hub.Dataset(tag)
```