# FastHub
FastHub is an experimental high level api for [Hub](https://github.com/activeloopai/hub).

Note: This is a proof of concept.

## Quickstart
### Moving bytes back and forth
We can push data to Hub with a `fasthub_up`. Once uploaded, data can be visualized or transformed as usual.
```python
my_dataset = fasthub_up(directory="images", tag='mynameisvinn/samples')
```
We can easily retrieve our dataset with the correct tag:
```python
tag = "mynameisvinn/samples"
retrieved_dataset = hub.Dataset(tag)
```