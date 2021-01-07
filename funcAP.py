def printToAP():
    file = open("avaragePrediction.txt", "w")
    file.write("image_id      True_Positive       Precision                    Recall\n")
    file.close()

def appendToAP(name,true,precision,recall):
    file = open("avaragePrediction.txt", "a")
    file.write(name + "             ")
    file.write(str(true) + "          ")
    file.write(str(precision) + "                           ")
    file.write(str(recall) + "\n")
    file.close()

def printToAPB():
    file = open("avaragePredictionBlurred.txt", "w")
    file.write("image_id      True_Positive       Precision                    Recall\n")
    file.close()

def appendToAPB(name,true,precision,recall):
    file = open("avaragePredictionBlurred.txt", "a")
    file.write(name + "             ")
    file.write(str(true) + "          ")
    file.write(str(precision) + "                           ")
    file.write(str(recall) + "\n")
    file.close()

def calcPrecisionRecall(photo_name,true_pos,false_pos,false_neg,value):
    # vypocita precision a recall
    try:
        precision = true_pos / (true_pos + false_pos)
    except ZeroDivisionError:
        precision = 0.0

    try:
        recall = true_pos / ( true_pos + false_neg)
    except ZeroDivisionError:
        precision = 0.0

    if (value == 1):
        appendToAP(photo_name, true_pos, precision, recall)
    elif (value == 0):
        appendToAPB(photo_name,true_pos,precision,recall)

