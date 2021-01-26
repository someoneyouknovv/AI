import csv, math
from sklearn.preprocessing import  OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

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
        encoder.fit([dataset[i][:-1]for i in range(len(dataset))])

        train_x = encoder.transform(train_x)
        test_x = encoder.transform(test_x)

        classifier = DecisionTreeClassifier()
        classifier.fit(train_x, train_y)
        predictions = classifier.predict(test_x)
        acc = 0
        for pred, true in zip(predictions, test_y):
            if pred == true:
                acc +=1

        print(f'Tochnost so DecisionTreeClassifier {acc/len(test_y)}')

        feature_importances = list(classifier.feature_importances_)
        most_im = feature_importances.index(max(feature_importances))
        least_im = feature_importances.index(min(feature_importances))

        print(f'Najvazhna karakteristika { most_im}')
        print(f'Najnevazhna karakteristika { least_im}')

        new_train_x = list()
        for row in train_x:
            sample = [ row[tmp] for tmp in range(len(row)) if  tmp!= least_im]
            new_train_x.append(sample)

        new_test_x = list()
        for row in test_x:
            sample = [row[tmp] for tmp in range(len(row)) if tmp != least_im]
            new_test_x.append(sample)

        new_classifier = DecisionTreeClassifier()
        new_classifier.fit(new_train_x, train_y)

        new_predictions = new_classifier.predict(new_test_x)
        acc = 0
        for pred, true in zip(new_predictions, test_y):
            if pred == true:
                acc +=1

        print(f'Tochnost so novoto drvo {acc/len(test_y)}')

        depth = classifier.get_depth()
        leaves = classifier.get_n_leaves()
        print(f'Depth: {depth}')
        print(f'Leaves: {leaves}')

