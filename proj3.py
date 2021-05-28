import time
from sklearn.ensemble import GradientBoostingClassifier, VotingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.naive_bayes import GaussianNB
import json
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import sklearn.naive_bayes as sk_bayes
from sklearn.model_selection import GridSearchCV
import sys
import argparse
warnings.filterwarnings("ignore")
import random

if __name__ == '__main__':
    '''
    从命令行读参数示例
    '''
    t = time.time()
    # print("从命令行读参数示例")
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--train', type=str, default='train.json')
    parser.add_argument('-i', '--test', type=str, default='test.txt')

    args = parser.parse_args()
    train = args.train
    test = args.test


    with open(train, 'r') as load_f:
        load_dict = json.load(load_f)
        # print(load_dict)
    with open(test, 'r') as f:
        x = f.read()
    one = x.strip('[')
    two = one.strip(']')
    three = two.replace('"', '')
    test_list = three.split(',')


    test_sentence = []
    train_sentence = []
    test_label = []
    label = []
    count = 0
    for i in load_dict:
        count += 1

        train_sentence.append(i['data'])
        label.append(i['label'])
    test_sentence=test_list

    # print(len(test_sentence))
    # print(len(train_sentence))
    tf = TfidfVectorizer(
        analyzer='word',
        ngram_range=(1, 5),
        max_df=0.6,
        max_features=600000
    )

    # temp=train_sentence.copy()
    # temp.extend(test_sentence)
    tf.fit(train_sentence)
    x_train = tf.transform(train_sentence)
    y_train=label
    X_test = tf.transform(test_sentence)

    from sklearn.svm import LinearSVC
    linsvm=LinearSVC()
    linsvm.fit(x_train,y_train)

    X_train = x_train



    predictions = linsvm.predict(X_test)

    with open('output.txt','w')as f:
        cnt=0
        for res in range(len(predictions)):
            f.write(str(predictions[res]))
            f.write('\n')

    sys.stdout.flush()

