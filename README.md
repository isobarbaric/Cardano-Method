
# CardanoMethod

[![release](https://img.shields.io/badge/dynamic/json.svg?label=release&url=https://pypi.org/pypi/cardanomethod/json&query=%24.info.version&colorB=blue)](https://pypi.org/project/CardanoMethod/)

A fast, reliable Python library to solve cubic equations of all kinds. You can test out `cardano-method` [in your browser](https://replit.com/@Vndom/cardano-method-playground?v=1#main.py).

## How It Works

`cardano-method` implements Gerolamo Cardano's famous method of solving cubic equations - 'Cardano Method'. Separated amongst various stages, this library **mirrors the steps described as Cardano's Method**.

## Why Use Cardano's Method

### Fast Results

Many profanity detection libraries use a hard-coded list of bad words to detect and filter profanity. For example, [profanity](https://pypi.org/project/profanity/) uses [this wordlist](https://github.com/ben174/profanity/blob/master/profanity/data/wordlist.txt), and even [better-profanity](https://pypi.org/project/better-profanity/) still uses [a wordlist](https://github.com/snguyenthanh/better_profanity/blob/master/better_profanity/profanity_wordlist.txt). There are obviously glaring issues with this approach, and, while they might be performant, **these libraries are not accurate at all**.

A simple example for which `profanity-check` is better is the phrase *"You cocksucker"* - `profanity` thinks this is clean because it doesn't have *"cocksucker"* in its wordlist.

### Fast Results

Other libraries like [profanity-filter](https://github.com/rominf/profanity-filter) use more sophisticated methods that are much more accurate but at the cost of performance. A benchmark (performed December 2018 on a new 2018 Macbook Pro) using [a Kaggle dataset of Wikipedia comments](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data) yielded roughly the following results:

| Package | 1 Prediction (ms) | 10 Predictions (ms) | 100 Predictions (ms)
| --------|-------------------|---------------------|-----------------------
| profanity-check | 0.2 | 0.5 | 3.5
| profanity-filter | 60 | 1200 | 13000
| profanity | 0.3 | 1.2 | 24

`profanity-check` is anywhere from **300 - 4000 times faster** than `profanity-filter` in this benchmark!

### Accuracy

This table speaks for itself:

| Package | Test Accuracy | Balanced Test Accuracy | Precision | Recall | F1 Score
| ------- | ------------- | ---------------------- | --------- | ------ | --------
| profanity-check | 95.0% | 93.0% | 86.1% | 89.6% | 0.88
| profanity-filter | 91.8% | 83.6% | 85.4% | 70.2% | 0.77
| profanity | 85.6% | 65.1% | 91.7% | 30.8% | 0.46

See the How section below for more details on the dataset used for these results.

## Installation

```
$ pip install cardano-method
```

## Usage

```python
from profanity_check import CubicEquation

predict(['predict() takes an array and returns a 1 for each string if it is offensive, else 0.'])
# [0]

from cardano_method import CubicEquation

a = CubicEquation([1, 3, 4, 4])
sol = a.solve()

print(sol)
# [-2.0, -0.5+1.322875i, -0.5-1.322875i]
```

Note that both `solve()` return [`complex`](https://docs.python.org/3/library/cmath.html#module-cmath) objects.

## More on How/Why It Works

### How

Special thanks to the authors of the datasets used in this project. `profanity-check` was trained on a combined dataset from 2 sources:
- [t-davidson/hate-speech-and-offensive-language](https://github.com/t-davidson/hate-speech-and-offensive-language/tree/master/data), used in their paper *Automated Hate Speech Detection and the Problem of Offensive Language*
- the [Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data) on Kaggle.

`profanity-check` relies heavily on the excellent [`scikit-learn`](https://scikit-learn.org/) library. It's mostly powered by `scikit-learn` classes [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html), [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html), and [`CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html). It uses a [Bag-of-words model](https://en.wikipedia.org/wiki/Bag-of-words_model) to vectorize input strings before feeding them to a linear classifier.

### Why

One simplified way you could think about why `profanity-check` works is this: during the training process, the model learns which words are "bad" and how "bad" they are because those words will appear more often in offensive texts. Thus, it's as if the training process is picking out the "bad" words out of all possible words and using those to make future predictions. This is better than just relying on arbitrary word blacklists chosen by humans!

## Caveats

This library is far from perfect. For example, it has a hard time picking up on less common variants of swear words like *"f4ck you"* or *"you b1tch"* because they don't appear often enough in the training corpus. **Never treat any prediction from this library as unquestionable truth, because it does and will make mistakes.** Instead, use this library as a heuristic.