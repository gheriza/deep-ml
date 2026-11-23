from collections import Counter

def confusion_matrix(data):
    counts = Counter()

    for y_true, y_pred in data:
        counts[(y_true, y_pred)] += 1

    tp = counts[(1, 1)]
    fn = counts[(1, 0)]
    fp = counts[(0, 1)]
    tn = counts[(0, 0)]

    return [
        [tp, fn],
        [fp, tn]
    ]