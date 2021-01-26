import csv
from sklearn.preprocessing import  OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB

if __name__ == '__main__':
    with open("car.csv") as file:
        file_reader = csv.reader(file, delimiter = ',')
        dataset = list(file_reader)[1:]

        train_set = dataset[ 0 : int( 0.7* len(dataset))]
        test_set = dataset [ int( 0.7 * len(dataset)) : ]

        train_x = [ x[:-1] for x in train_set]
        train_y = [ x[-1] for x in train_set]
        test_x = [x[:-1] for x in test_set]
        test_y = [x[-1] for x in test_set]

        encoder = OrdinalEncoder()
        encoder.fit([dataset[i][:-1] for i in range(len(dataset))])

        train_x = encoder.transform(train_x)
        test_x = encoder.transform(test_x)

        print(train_x)
        print(test_x)


        cnb = CategoricalNB()
        cnb.fit(train_x, train_y)

        predict = cnb.predict(test_x)
        acc =0
        for pred, true in zip(predict, test_y):
            if pred == true:
                acc +=1

        print(f'Tochnost so CategoricalNB {acc/len(test_set)}')

        entry = [ elem for elem in input().split(' ')]
        entry = encoder.transform([entry])

        rez = cnb.predict(entry)
        print(f'Rez od vlez e {rez}')


