from datasets import load_dataset

def load_hate_dataset(return_type=None):
    train_dataset = load_dataset("hatexplain", split="train")
    test_dataset = load_dataset("hatexplain", split="test")
    val_dataset = load_dataset("hatexplain", split="validation")

    train_dataset = train_dataset.map(lambda e: {"label" : int(np.median(e["annotators"]["label"]))})
    test_dataset = test_dataset.map(lambda e: {"label" : int(np.median(e["annotators"]["label"]))})
    val_dataset = val_dataset.map(lambda e: {"label" : int(np.median(e["annotators"]["label"]))})

    
    train_dataset = train_dataset.set_format(type=return_type, columns="post_tokens")
    test_dataset = test_dataset.set_format(type=return_type, columns="post_tokens")
    val_dataset = val_dataset.set_format(type=return_type, columns="post_tokens")

    return train_dataset, test_dataset, val_dataset