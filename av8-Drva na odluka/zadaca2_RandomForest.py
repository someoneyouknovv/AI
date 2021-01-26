import csv, math
from sklearn.preprocessing import  OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier

if __name__ == '__main__':
    with open("car.csv") as csv_file:
        file_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(file_reader)[1:]

        train_set = dataset[ 0 : int( 0.7* len(dataset))]
        test_set = dataset [ int( 0.7* len(dataset)) : ]

        train_x = [ x[:-1] for x in train_set]
        train_y = [x[-1] for x in train_set]
        test_x = [x[:-1] for x in test_set]
        test_y = [x[-1] for x in test_set]

        encoder = OrdinalEncoder()
        encoder.fit([dataset[i][:-1] for i in range(len(dataset))])

        train_x = encoder.transform(train_x)
        test_x = encoder.transform(test_x)

        classifier = RandomForestClassifier(n_estimators=100, criterion='entropy')
        classifier.fit(train_x, train_y)

        predictions = classifier.predict(test_x)
        acc = 0
        for pred, true in zip(predictions, test_y):
            if pred == true:
                acc +=1

        print(f'Tochnost so RandomForest {acc/len(test_y)}')

        feature_importances = list(classifier.feature_importances_)
        most_im = feature_importances.index(max(feature_importances))
        least_im = feature_importances.index(min(feature_importances))
        print(f'Most: {most_im}')
        print(f'Least: {least_im}')