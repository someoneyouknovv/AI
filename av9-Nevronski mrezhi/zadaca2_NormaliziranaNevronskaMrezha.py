from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def read_dataset():
    data = []
    with open('winequality.csv') as f:
        _ = f.readline()
        while True:
            line = f.readline().strip()
            if line == '':
                break
            parts = line.split(';')
            data.append(list(map(float, parts[:-1])) + parts[-1:])

    return data

def divide_data(dataset):
    #ako ne pishe OD SEKOJA OD KLASITE
    #slednite dve linii kod ne gi pisis
    bad_class = [i for i in dataset if i[-1] == 'bad']
    good_class = [i for i in dataset if i[-1] == 'good']

    train_set = bad_class[0 : int( 0.7* len(bad_class))] + good_class[ 0 : int( 0.7*len(good_class))]
    val_set = bad_class[int( 0.7* len(bad_class)) : int( 0.8* len(bad_class))]  \
            + good_class[int( 0.7* len(good_class)) : int( 0.8* len(good_class))]
    test_set = bad_class[ int( 0.8* len(bad_class)) : ] + good_class[int( 0.8* len(good_class)) : ]

    return train_set, val_set, test_set

if __name__ == '__main__':
    dataset = read_dataset()

    train_set, val_set, test_set = divide_data(dataset)

    train_x = [ x[:-1] for x in train_set]
    train_y = [ x[-1] for x in train_set]
    val_x = [ x[:-1] for x in val_set]
    val_y = [ x[-1] for x in val_set]
    test_x = [ x[:-1] for x in test_set]
    test_y = [ x[-1] for x in test_set]

    scaler1 = StandardScaler()
    scaler1.fit(train_x)
    scaler2 = MinMaxScaler()
    scaler2.fit(train_x)


    classifier1 = MLPClassifier(100, activation='relu', learning_rate_init=0.001, random_state=0)
    classifier2 = MLPClassifier(100, activation='relu', learning_rate_init=0.001, random_state=0)
    classifier3 = MLPClassifier(100, activation='relu', learning_rate_init=0.001, random_state=0)

    classifier1.fit(train_x, train_y)
    classifier2.fit(scaler1.transform(train_x), train_y)
    classifier3.fit(scaler2.transform(train_x), train_y)

    acc = 0
    predictions = classifier1.predict(val_x)
    for pred, true in zip(predictions, val_y):
        if pred == true:
            acc +=1
    print(f'Bez normalizacija: {acc/len(val_y)}')

    acc = 0
    predictions = classifier2.predict(val_x)
    for pred, true in zip(predictions, val_y):
        if pred == true:
            acc += 1
    print(f'So Standard Scaler: {acc / len(val_y)}')

    acc = 0
    predictions = classifier3.predict(val_x)
    for pred, true in zip(predictions, val_y):
        if pred == true:
            acc += 1
    print(f'So MinMax Scaler: {acc / len(val_y)}')

    #najdobar e prviot klasifikator, pa:
    final_pred = classifier1.predict(test_x)
    tp, fp, tn, fn = 0,0,0,0
    for pred, true in zip(final_pred, test_y):
        if true == 'good':
            if pred == true:
                tp +=1
            else:
                fp +=1

        else:
            if pred == true:
                tn +=1
            else:
                fp +=1

    tochnost =  (tp + tn ) / ( tp + fp + tn + fn)
    preciznost = tp / (tp + fp)
    odziv = tp / (tp + fn)
    print(f'Evaluacija:')
    print(f'Tochnost: {tochnost}')
    print(f'Preciznost: {preciznost}')
    print(f'Odziv: {odziv}')




