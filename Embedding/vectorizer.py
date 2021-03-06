import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfVectorizer
from scipy import sparse 

# change category value accordingly
category = 'cool'
print(f"currently running for {category}")

print("load train, val, test data")
train_path = 'data/train_processed.csv'
val_path = 'data/val_processed.csv'
test_path = 'data/test_processed.csv'
train = pd.read_csv(train_path)
if category == 'cool':
    train = train[train['cool_sampled_flag'] == 1]
else:
    train = train[train['funny_sampled_flag'] == 1]
val = pd.read_csv(val_path)
test = pd.read_csv(test_path)


print("check data shape, drop rows with na values")
print("before dropna")
for i in [train, val, test]:
    print(i.shape)
for i in [train, val, test]:
    i.dropna(inplace=True)
print("after dropna")
for i in [train, val, test]:
    print(i.shape)


data_dict = {
    'train': train,
    'eval': val,
    'test': test
}

print("------- current model: TF-IDF Vectorizer -------")
model = 'tfidf_1gram'
vect = TfidfVectorizer(ngram_range = (1, 1))
transformed_train_text = vect.fit_transform(train['cleaned_text'])
sparse.save_npz(f"text_processing/{category}_processed_text/{category}_{model}_train.npz", transformed_train_text)

for data in ['eval', 'test']:
    df = data_dict[data]
    transformed_text = vect.transform(df['cleaned_text'])
    sparse.save_npz(f"text_processing/{category}_processed_text/{category}_{model}_{data}.npz", transformed_text)

model = 'tfidf_2gram'
vect = TfidfVectorizer(ngram_range = (2, 2))
transformed_train_text = vect.fit_transform(train['cleaned_text'])
sparse.save_npz(f"text_processing/{category}_processed_text/{category}_{model}_train.npz", transformed_train_text)

for data in ['eval', 'test']:
    df = data_dict[data]
    transformed_text = vect.transform(df['cleaned_text'])
    sparse.save_npz(f"text_processing/{category}_processed_text/{category}_{model}_{data}.npz", transformed_text)


print("------- current model: Count Vectorizer -------")
model = 'count_1gram'
vect = CountVectorizer(ngram_range = (1, 1))
transformed_train_text = vect.fit_transform(train['cleaned_text'])
sparse.save_npz(f"text_processing/{category}_processed_text/{category}_{model}_train.npz", transformed_train_text)

for data in ['eval', 'test']:
    df = data_dict[data]
    transformed_text = vect.transform(df['cleaned_text'])
    sparse.save_npz(f"text_processing/{category}_processed_text/{category}_{model}_{data}.npz", transformed_text)

model = 'count_2gram'
vect = CountVectorizer(ngram_range = (2, 2))
transformed_train_text = vect.fit_transform(train['cleaned_text'])
sparse.save_npz(f"text_processing/{category}_processed_text/{category}_{model}_train.npz", transformed_train_text)

for data in ['eval', 'test']:
    df = data_dict[data]
    transformed_text = vect.transform(df['cleaned_text'])
    sparse.save_npz(f"text_processing/{category}_processed_text/{category}_{model}_{data}.npz", transformed_text)


print("------- current model: Hashing Vectorizer -------")
model = 'hashing_1gram'
vect = HashingVectorizer(ngram_range = (1, 1))
transformed_train_text = vect.fit_transform(train['cleaned_text'])
sparse.save_npz(f"text_processing/{category}_processed_text/{category}_{model}_train.npz", transformed_train_text)

for data in ['eval', 'test']:
    df = data_dict[data]
    transformed_text = vect.transform(df['cleaned_text'])
    sparse.save_npz(f"text_processing/{category}_processed_text/{category}_{model}_{data}.npz", transformed_text)


model = 'hashing_2gram'
vect = HashingVectorizer(ngram_range = (2, 2))
transformed_train_text = vect.fit_transform(train['cleaned_text'])
sparse.save_npz(f"text_processing/{category}_processed_text/{category}_{model}_train.npz", transformed_train_text)

for data in ['eval', 'test']:
    df = data_dict[data]
    transformed_text = vect.transform(df['cleaned_text'])
    sparse.save_npz(f"text_processing/{category}_processed_text/{category}_{model}_{data}.npz", transformed_text)
