import csv
from sklearn.preprocessing import  OrdinalEncoder
from sklearn.naive_bayes import GaussianNB

if __name__ == '__main__':
    with open("medical_data.csv") as file:
        file_reader = csv.reader(file, delimiter = ',')
        dataset = list(file_reader)[1:]

        train_set = dataset[ 0 : int( 0.7* len(dataset))]
        test_set = dataset [ int( 0.7 * len(dataset)) : ]

        train_x = [ x[:-1] for x in train_set]
        train_y = [ x[-1] for x in train_set]
        test_x = [x[:-1] for x in test_set]
        test_y = [x[-1] for x in test_set]

        gnb = GaussianNB()
        gnb.fit(train_x, train_y)

        predicted = gnb.predict(test_x)
        acc = 0
        for pred, true in zip(predicted, test_y):
            if pred == true:
                acc += 1

        print(f'Tochnost so GaussianNB {acc/len(test_y)}')

        entry = [elem for elem in input().split(' ')]

        rez = gnb.predict([entry])
        print(rez)


