import math


def euclidean_distance(point_one, point_two):
    sum_of_dis = 0
    for i in range(len(point_one) - 1):
        sum_of_dis += math.pow(float(point_one[i]) - float(point_two[i]), 2)
    return math.sqrt(sum_of_dis)


def transform(a):
    if a == 0:
        return "setosa"
    elif a == 1:
        return "versicolor"
    elif a == 2:
        return "virginica"


def knn(k, training_table, testing_table):
    res = 3
    acc = 0
    counter_correct = 0
    counter_incorrect = 0
    vector_results = []

    for j, testing_line in enumerate(testing_table):
        sorted_distances = []
        setosa, versicolor, virginica = 0, 0, 0

        for i, training_line in enumerate(training_table):
            distance = euclidean_distance(training_line, testing_line)
            sorted_distances.append([distance, training_line[-1]])
        sorted_distances.sort()
        sorted_distances = sorted_distances[:k]

        for x in sorted_distances:

            if x[1] == "0":
                setosa += 1
            if x[1] == "1":
                versicolor += 1
            if x[1] == "2":
                virginica += 1

        tmp = max(setosa, versicolor, virginica)
        if tmp == setosa:
            res = 0
        if tmp == versicolor:
            res = 1
        if tmp == virginica:
            res = 2

        if str(res) != testing_line[-1]:
            counter_incorrect += 1
        else:
            counter_correct += 1

        res = transform(res)
        vector_results.append(res)

        acc = math.ceil((counter_correct / (counter_incorrect + counter_correct) * 100))

    if len(vector_results) == 1:
        return f'classified as: {vector_results}'
    else:
        return f'correct: {counter_correct}\naccuracy: {acc}\nclassified as: {vector_results}'


def main():
    k = 0
    training_data = open("iris_training.txt", 'r')
    table_training_data = []
    for line in training_data:
        verse = []
        for column in line.split("\t"):
            column = column.replace(",", ".")
            column = column.replace("Iris-setosa", "0")
            column = column.replace("Iris-versicolor", "1")
            column = column.replace("Iris-virginica", "2")
            column = column.replace("\n", "").strip()
            verse.append(column)
        table_training_data.append(verse)

    testing_data = open("iris_test.txt", 'r')
    table_testing_data = []

    for line in testing_data:
        verse = []
        for column in line.split("\t"):
            column = column.replace(",", ".")
            column = column.replace("Iris-setosa", "0")
            column = column.replace("Iris-versicolor", "1")
            column = column.replace("Iris-virginica", "2")
            column = column.replace("\n", "").strip()
            verse.append(column)
        table_testing_data.append(verse)

    # from txt
    c = 0
    while c != 1:
        try:
            set_k = int(input("pass k: "))
            print(knn(set_k, table_training_data, table_testing_data))
            c = 1
        except:
            print("incorrect input")

    # manual
    c = 0
    while True:
        try:
            while c != 1:
                try:
                    k = int(input("pass k: "))
                    c = 1
                except:
                    print("incorrect input")
            inp_str = input("pass the attribute vector (numbers separated by spaces): \n")
            vec = [inp_str.split()]
            print(knn(k, table_training_data, vec))
            c = 0
        except:
            print("incorrect input")


if __name__ == "__main__":
    main()
