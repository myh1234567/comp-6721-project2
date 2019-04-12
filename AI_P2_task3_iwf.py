import matplotlib.pyplot as plt
import os
import re
import math
path = '/Users/Downloads/train'
files=os.listdir(path)


frequent_list = [1,5,10,15,20, 0.05, 0.1, 0.15, 0.2, 0.25]

num_files_spam_iwf = 0
num_files_ham_iwf = 0
count_ham_iwf = 0
num_ham_iwf = 0
count_spam_iwf = 0
num_spam_iwf = 0
count_word_dic = 0
count_iwf = 1
ham_prop_iwf = None
spam_prop_iwf = None
word_iwf = []
word_set_iwf = []
word_dict_iwf = {}
word_dict_spam_iwf = {}
word_dict_ham_iwf = {}
model_dict_iwf = {}
wordset_test_iwf = []
x_list = []
y_list = []


def no_preprocess_iwf(files):
    global num_files_ham_iwf
    global num_files_spam_iwf
    global word_set_iwf
    global word_dict_iwf
    global word_dict_ham_iwf
    global word_dict_spam_iwf
    for i in files:
        if i[6] == "s":
            num_files_spam_iwf += 1
        elif i[6] == "h":
            num_files_ham_iwf += 1
        file = open(path + "/" + i, encoding="latin-1")
        contents = file.readlines()
        for line in contents:
            string = re.split('[^a-zA-Z]',line)
            a = list(filter(None, string))
            words_str = " ".join(a).lower()
            words = re.split(" ", words_str)
            for word in words:
                if word == " ":
                    continue
                if word == "":
                    continue
                if word not in word_dict_iwf:
                    word_set_iwf.append(word)
                    word_dict_iwf[word] = 1
                elif word in word_dict_iwf:
                    word_dict_iwf[word] += 1
                if i[6] == "s":
                    if word not in word_dict_spam_iwf:
                        word_dict_spam_iwf[word] = 1
                    elif word in word_dict_spam_iwf:
                        word_dict_spam_iwf[word] += 1
                elif i[6] == "h":
                    if word not in word_dict_ham_iwf:
                        word_dict_ham_iwf[word] = 1
                    elif word in word_dict_ham_iwf:
                        word_dict_ham_iwf[word] += 1


path_test = '/Users/Downloads/test'
files_test=os.listdir(path_test)
wordset_test = []
spam_score = 1
ham_score = 1

def task2_no_preprocess_iwf(file):
    global wordset_test_iwf
    wordset_test_iwf = []
    file_test = open(path_test + "/" + file, encoding = "latin-1")
    contents = file_test.readlines()
    for line in contents:
        # print(line)
        string = re.split('[^a-zA-Z]',line)
        a = list(filter(None,string))
        words_str = " ".join(a).lower()
        words = re.split(" ",words_str)
        for word in words:
            if word == " ":
                continue
            if word == "":
                continue
            if word not in wordset_test_iwf:
                # print(word_set)
                wordset_test_iwf.append(word)

no_preprocess_iwf(files)
for word_ham in word_dict_ham_iwf:
    count_ham_iwf += word_dict_ham_iwf[word_ham]
    num_ham_iwf += 1

for word_spam in word_dict_spam_iwf:
    count_spam_iwf += word_dict_spam_iwf[word_spam]
    num_spam_iwf += 1

for word in sorted(word_set_iwf):
    if word_dict_ham_iwf.get(word) == None:
        str2 = 0
        smooth_ham_prop = (0.5) / (count_ham_iwf + (0.5 * len(word_set_iwf)))
    else:
        str2 = word_dict_ham_iwf[word]
        smooth_ham_prop = (word_dict_ham_iwf[word] + 0.5)/ (count_ham_iwf + 0.5 * len(word_set_iwf))

    if word_dict_spam_iwf.get(word) == None:
        str4 = 0
        smooth_spam_prop = (0.5) / (count_spam_iwf + 0.5 * len(word_set_iwf))
    else:
        str4 = word_dict_spam_iwf[word]
        smooth_spam_prop = (word_dict_spam_iwf.get(word) + 0.5)/ (count_spam_iwf + 0.5*len(word_set_iwf))


    output_task1 = str(count_iwf),str(word),str(str2),str(smooth_ham_prop),str(str4),str(smooth_spam_prop)
    model_dict_iwf[word]=[str2,smooth_ham_prop,str4,smooth_spam_prop]
    # outstr="  ".join(list(output_task1))
    # output_file_.writelines(outstr+"\r\n")
    # print(outstr)
    # print(count,"  ",word,ham_prop,"  ",smooth_ham_prop,"  ",spam_prop,"  ",smooth_spam_prop)
    count_iwf += 1
# output_file_wlf.close()

def task2_no_preprocess_iwf(file):
    global wordset_test_iwf
    wordset_test_iwf = []
    file_test = open(path_test + "/" + file, encoding = "latin-1")
    contents = file_test.readlines()
    for line in contents:
        # print(line)
        string = re.split('[^a-zA-Z]',line)
        a = list(filter(None,string))
        words_str = " ".join(a).lower()
        words = re.split(" ",words_str)
        for word in words:
            if word == " ":
                continue
            if word == "":
                continue
            if word not in wordset_test_iwf:
                # print(word_set)
                wordset_test_iwf.append(word)

p_spam_iwf = num_files_spam_iwf/(num_files_spam_iwf + num_files_ham_iwf)
p_ham_iwf = num_files_ham_iwf/(num_files_spam_iwf + num_files_ham_iwf)
p_spam_list_iwf = []
p_ham_list_iwf = []
word_model_set_iwf = []
count_task2_iwf = 1
# file_model = open("/Users/PycharmProjects/model.txt")
# contents_model = file_model.readlines()
# for i in contents_model:
#     word_model = re.split("  ", i)
#     # model li de wordset
#     word_model_set.append(word_model[1])
count_self = 0
# print(model_dict)

path_test = '/Users/Downloads/test'
files_test=os.listdir(path_test)
wordset_test_iwf = []
spam_score_iwf = 1
ham_score_iwf = 1

######## frequency = 1
dict_I = {}
for word in word_dict_iwf:
    if word_dict_iwf[word] <= 10:
        continue
    else:
        dict_I[word] = word_dict_iwf[word]

output_file_task2_iwf1 = ""
output_file_task2_iwf1 = open("./iwf1-result.txt","w")
tp = 0
fp = 0
fn = 0
tn = 0
for file in files_test:
    print(file)
    # task2_preprocess(file)
    task2_no_preprocess_iwf(file)
    score_spam_iwf = math.log10(p_spam_iwf)
    score_ham_iwf = math.log10(p_ham_iwf)
    score_deno_iwf = 0
    for word in sorted(wordset_test_iwf):
        if not word in dict_I:
            continue
        else:
            score_ham_iwf += math.log10(model_dict_iwf[word][1])
            score_spam_iwf += math.log10(model_dict_iwf[word][3])
    # final_ham = score_ham/score_deno
    # final_spam = score_spam/score_deno
    if score_ham_iwf > score_spam_iwf:
        hamORspam_iwf = "ham"
    else:
        hamORspam_iwf = "spam"
    if file.find("spam")>=0:
        correct_classification_iwf = "spam"
    else:
        correct_classification_iwf = "ham"
    if hamORspam_iwf == correct_classification_iwf:
        result_iwf = "right"
        if hamORspam_iwf == "ham":
            tp += 1
        else:
            tn += 1
    else:
        result_iwf = "wrong"
        if hamORspam_iwf == "ham":
            fp += 1
        else:
            fn += 1
    output_task2_iwf = str(count_task2_iwf), str(file), str(hamORspam_iwf), str(score_ham_iwf), str(score_spam_iwf), str(correct_classification_iwf), str(result_iwf)
    outstr_task2_iwf = "  ".join(list(output_task2_iwf))
    output_file_task2_iwf1.writelines(outstr_task2_iwf + "\r\n")
    count_task2_iwf += 1
acc = (tp + tn) / (tp + tn + fn + fp)
precision = tp / (tp + fp)
recall = tp / (tp + fn)
y_list.append([acc,precision,recall])
x_list.append(len(dict_I))
output_file_task2_iwf1.close()


######## frequency = 5
# dict_V = {}
# for word in word_dict_iwf:
#     if word_dict_iwf[word] <= 5:
#         continue
#     else:
#         dict_V[word] = word_dict_iwf[word]
#
# output_file_task2_iwf2 = ""
# output_file_task2_iwf2 = open("./iwf2-result.txt","w")
# count_task2_iwf = 1
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_iwf(file)
#     score_spam_iwf = math.log10(p_spam_iwf)
#     score_ham_iwf = math.log10(p_ham_iwf)
#     score_deno_iwf = 0
#     for word in sorted(wordset_test_iwf):
#         if not word in dict_V:
#             continue
#         else:
#             score_ham_iwf += math.log10(model_dict_iwf[word][1])
#             score_spam_iwf += math.log10(model_dict_iwf[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_iwf > score_spam_iwf:
#         hamORspam_iwf = "ham"
#     else:
#         hamORspam_iwf = "spam"
#     if file.find("spam")>=0:
#         correct_classification_iwf = "spam"
#     else:
#         correct_classification_iwf = "ham"
#     if hamORspam_iwf == correct_classification_iwf:
#         result_iwf = "right"
#         if hamORspam_iwf == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_iwf = "wrong"
#         if hamORspam_iwf == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_iwf = str(count_task2_iwf), str(file), str(hamORspam_iwf), str(score_ham_iwf), str(score_spam_iwf), str(correct_classification_iwf), str(result_iwf)
#     outstr_task2_iwf = "  ".join(list(output_task2_iwf))
#     output_file_task2_iwf2.writelines(outstr_task2_iwf + "\r\n")
#     count_task2_iwf += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append(len(dict_V))
# output_file_task2_iwf2.close()
#
# ######## frequency = 10
# dict_X = {}
# for word in word_dict_iwf:
#     if word_dict_iwf[word] <= 10:
#         continue
#     else:
#         dict_X[word] = word_dict_iwf[word]
#
# output_file_task2_iwf3 = ""
# output_file_task2_iwf3 = open("./iwf3-result.txt","w")
# count_task2_iwf = 1
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_iwf(file)
#     score_spam_iwf = math.log10(p_spam_iwf)
#     score_ham_iwf = math.log10(p_ham_iwf)
#     score_deno_iwf = 0
#     for word in sorted(wordset_test_iwf):
#         if not word in dict_X:
#             continue
#         else:
#             score_ham_iwf += math.log10(model_dict_iwf[word][1])
#             score_spam_iwf += math.log10(model_dict_iwf[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_iwf > score_spam_iwf:
#         hamORspam_iwf = "ham"
#     else:
#         hamORspam_iwf = "spam"
#     if file.find("spam")>=0:
#         correct_classification_iwf = "spam"
#     else:
#         correct_classification_iwf = "ham"
#     if hamORspam_iwf == correct_classification_iwf:
#         result_iwf = "right"
#         if hamORspam_iwf == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_iwf = "wrong"
#         if hamORspam_iwf == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_iwf = str(count_task2_iwf), str(file), str(hamORspam_iwf), str(score_ham_iwf), str(score_spam_iwf), str(correct_classification_iwf), str(result_iwf)
#     outstr_task2_iwf = "  ".join(list(output_task2_iwf))
#     output_file_task2_iwf3.writelines(outstr_task2_iwf + "\r\n")
#     count_task2_iwf += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append(len(dict_X))
# output_file_task2_iwf3.close()
#
# ######## frequency = 15
# dict_XV = {}
# for word in word_dict_iwf:
#     if word_dict_iwf[word] <= 15:
#         continue
#     else:
#         dict_XV[word] = word_dict_iwf[word]
#
# output_file_task2_iwf4 = ""
# output_file_task2_iwf4 = open("./iwf4-result.txt","w")
# count_task2_iwf = 1
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_iwf(file)
#     score_spam_iwf = math.log10(p_spam_iwf)
#     score_ham_iwf = math.log10(p_ham_iwf)
#     score_deno_iwf = 0
#     for word in sorted(wordset_test_iwf):
#         if not word in dict_XV:
#             continue
#         else:
#             score_ham_iwf += math.log10(model_dict_iwf[word][1])
#             score_spam_iwf += math.log10(model_dict_iwf[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_iwf > score_spam_iwf:
#         hamORspam_iwf = "ham"
#     else:
#         hamORspam_iwf = "spam"
#     if file.find("spam")>=0:
#         correct_classification_iwf = "spam"
#     else:
#         correct_classification_iwf = "ham"
#     if hamORspam_iwf == correct_classification_iwf:
#         result_iwf = "right"
#         if hamORspam_iwf == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_iwf = "wrong"
#         if hamORspam_iwf == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_iwf = str(count_task2_iwf), str(file), str(hamORspam_iwf), str(score_ham_iwf), str(score_spam_iwf), str(correct_classification_iwf), str(result_iwf)
#     outstr_task2_iwf = "  ".join(list(output_task2_iwf))
#     output_file_task2_iwf4.writelines(outstr_task2_iwf + "\r\n")
#     count_task2_iwf += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append(len(dict_XV))
# output_file_task2_iwf4.close()
#
# ######## frequency = 20
# dict_XX = {}
# for word in word_dict_iwf:
#     if word_dict_iwf[word] <= 20:
#         continue
#     else:
#         dict_XX[word] = word_dict_iwf[word]
#
# output_file_task2_iwf5 = ""
# output_file_task2_iwf5 = open("./iwf5-result.txt","w")
# count_task2_iwf = 1
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_iwf(file)
#     score_spam_iwf = math.log10(p_spam_iwf)
#     score_ham_iwf = math.log10(p_ham_iwf)
#     score_deno_iwf = 0
#     for word in sorted(wordset_test_iwf):
#         if not word in dict_XX:
#             continue
#         else:
#             score_ham_iwf += math.log10(model_dict_iwf[word][1])
#             score_spam_iwf += math.log10(model_dict_iwf[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_iwf > score_spam_iwf:
#         hamORspam_iwf = "ham"
#     else:
#         hamORspam_iwf = "spam"
#     if file.find("spam")>=0:
#         correct_classification_iwf = "spam"
#     else:
#         correct_classification_iwf = "ham"
#     if hamORspam_iwf == correct_classification_iwf:
#         result_iwf = "right"
#         if hamORspam_iwf == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_iwf = "wrong"
#         if hamORspam_iwf == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_iwf = str(count_task2_iwf), str(file), str(hamORspam_iwf), str(score_ham_iwf), str(score_spam_iwf), str(correct_classification_iwf), str(result_iwf)
#     outstr_task2_iwf = "  ".join(list(output_task2_iwf))
#     output_file_task2_iwf5.writelines(outstr_task2_iwf + "\r\n")
#     count_task2_iwf += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append(len(dict_XX))
# output_file_task2_iwf5.close()
# #
# #
# # print(len(dict_I))
# # print(len(dict_V))
# # print(len(dict_X))
# # print(len(dict_XV))
#
#
# ######## frequency = 5%
# dic_topV = []
# dict_topV = {}
# final_topV = []
# for word in word_dict_iwf:
#     dic_topV.append(word_dict_iwf[word])
#
# dic_topV_sorted = sorted(dic_topV)
# value_95 = dic_topV_sorted[int(len(dic_topV_sorted)* 0.99)-1]
# value_05 = dic_topV_sorted[int(len(dic_topV_sorted)* 0.03)-1]
# for i in dic_topV_sorted:
#     if i < value_95:
#         final_topV.append(i)
#     else:
#         break
# word_stop = []
# path_stopword = '/Users/ycharmProjects/stop_word.txt'
# files_stopword=open(path_stopword)
# word = files_stopword.readlines()
#
# for i in word:
#     a = i.replace("\n","")
#     word_stop.append(a)
#
# for word in word_dict_iwf:
#     if word_dict_iwf[word] >= value_95:
#         continue
#     # if word_dict_iwf[word] <= value_05:
#     #     continue
#     if word_dict_iwf[word] <= 6:
#         continue
#     if word in word_stop:
#         continue
#     else:
#         dict_topV[word] = word_dict_iwf[word]
#
# print("111111")
# print(dict_topV)
# output_file_task2_iwf6 = ""
# output_file_task2_iwf6 = open("./iwf6-result.txt","w")
# count_task2_iwf = 1
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_iwf(file)
#     score_spam_iwf = math.log10(p_spam_iwf)
#     score_ham_iwf = math.log10(p_ham_iwf)
#     score_deno_iwf = 0
#     for word in sorted(wordset_test_iwf):
#         if not word in dict_topV:
#             continue
#         else:
#             score_ham_iwf += math.log10(model_dict_iwf[word][1])
#             score_spam_iwf += math.log10(model_dict_iwf[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_iwf > score_spam_iwf:
#         hamORspam_iwf = "ham"
#     else:
#         hamORspam_iwf = "spam"
#     if file.find("spam")>=0:
#         correct_classification_iwf = "spam"
#     else:
#         correct_classification_iwf = "ham"
#     if hamORspam_iwf == correct_classification_iwf:
#         result_iwf = "right"
#         if hamORspam_iwf == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_iwf = "wrong"
#         if hamORspam_iwf == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_iwf = str(count_task2_iwf), str(file), str(hamORspam_iwf), str(score_ham_iwf), str(score_spam_iwf), str(correct_classification_iwf), str(result_iwf)
#     outstr_task2_iwf = "  ".join(list(output_task2_iwf))
#     output_file_task2_iwf6.writelines(outstr_task2_iwf + "\r\n")
#     count_task2_iwf += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append(len(dict_topV))
# output_file_task2_iwf6.close()
#
# print("11111")
# print(tp)
# print(fp)
# print(fn)
# print(tn)


######## frequency = 10%
# dic_topX = []
# dict_topX = {}
# final_topX = []
# for word in word_dict_iwf:
#     dic_topX.append(word_dict_iwf[word])
#
# dic_topX_sorted = sorted(dic_topX)
# value_90 = dic_topX_sorted[int(len(dic_topX_sorted)* 0.9)-1]
# for i in dic_topX_sorted:
#     if i < value_90:
#         final_topX.append(i)
#     else:
#         break
#
# for word in word_dict_iwf:
#     if word_dict_iwf[word] >= value_90:
#         continue
#     else:
#         dict_topX[word] = word_dict_iwf[word]
#
#
# output_file_task2_iwf7 = ""
# output_file_task2_iwf7 = open("./iwf7-result.txt","w")
# count_task2_iwf = 1
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_iwf(file)
#     score_spam_iwf = math.log10(p_spam_iwf)
#     score_ham_iwf = math.log10(p_ham_iwf)
#     score_deno_iwf = 0
#     for word in sorted(wordset_test_iwf):
#         if not word in dict_topX:
#             continue
#         else:
#             score_ham_iwf += math.log10(model_dict_iwf[word][1])
#             score_spam_iwf += math.log10(model_dict_iwf[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_iwf > score_spam_iwf:
#         hamORspam_iwf = "ham"
#     else:
#         hamORspam_iwf = "spam"
#     if file.find("spam")>=0:
#         correct_classification_iwf = "spam"
#     else:
#         correct_classification_iwf = "ham"
#     if hamORspam_iwf == correct_classification_iwf:
#         result_iwf = "right"
#         if hamORspam_iwf == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_iwf = "wrong"
#         if hamORspam_iwf == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_iwf = str(count_task2_iwf), str(file), str(hamORspam_iwf), str(score_ham_iwf), str(score_spam_iwf), str(correct_classification_iwf), str(result_iwf)
#     outstr_task2_iwf = "  ".join(list(output_task2_iwf))
#     output_file_task2_iwf7.writelines(outstr_task2_iwf + "\r\n")
#     count_task2_iwf += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append(len(dict_topX))
# output_file_task2_iwf7.close()
#
#
# ######## frequency = 15%
# dic_topXV = []
# dict_topXV = {}
# final_topXV = []
# for word in word_dict_iwf:
#     dic_topXV.append(word_dict_iwf[word])
#
# dic_topXV_sorted = sorted(dic_topXV)
# value_85 = dic_topXV_sorted[int(len(dic_topXV_sorted)* 0.85)-1]
# for i in dic_topXV_sorted:
#     if i < value_85:
#         final_topXV.append(i)
#     else:
#         break
#
# for word in word_dict_iwf:
#     if word_dict_iwf[word] >= value_85:
#         continue
#     else:
#         dict_topXV[word] = word_dict_iwf[word]
#
#
# output_file_task2_iwf8 = ""
# output_file_task2_iwf8 = open("./iwf8-result.txt","w")
# count_task2_iwf = 1
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_iwf(file)
#     score_spam_iwf = math.log10(p_spam_iwf)
#     score_ham_iwf = math.log10(p_ham_iwf)
#     score_deno_iwf = 0
#     for word in sorted(wordset_test_iwf):
#         if not word in dict_topXV:
#             continue
#         else:
#             score_ham_iwf += math.log10(model_dict_iwf[word][1])
#             score_spam_iwf += math.log10(model_dict_iwf[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_iwf > score_spam_iwf:
#         hamORspam_iwf = "ham"
#     else:
#         hamORspam_iwf = "spam"
#     if file.find("spam")>=0:
#         correct_classification_iwf = "spam"
#     else:
#         correct_classification_iwf = "ham"
#     if hamORspam_iwf == correct_classification_iwf:
#         result_iwf = "right"
#         if hamORspam_iwf == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_iwf = "wrong"
#         if hamORspam_iwf == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_iwf = str(count_task2_iwf), str(file), str(hamORspam_iwf), str(score_ham_iwf), str(score_spam_iwf), str(correct_classification_iwf), str(result_iwf)
#     outstr_task2_iwf = "  ".join(list(output_task2_iwf))
#     output_file_task2_iwf8.writelines(outstr_task2_iwf + "\r\n")
#     count_task2_iwf += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append(len(dict_topXV))
# output_file_task2_iwf8.close()
#
# ######## frequency = 20%
# dic_topXX = []
# dict_topXX = {}
# final_topXX = []
# for word in word_dict_iwf:
#     dic_topXX.append(word_dict_iwf[word])
#
# dic_topXX_sorted = sorted(dic_topXX)
# value_80 = dic_topXX_sorted[int(len(dic_topXX_sorted)* 0.8)-1]
# for i in dic_topXX_sorted:
#     if i < value_80:
#         final_topXX.append(i)
#     else:
#         break
#
# for word in word_dict_iwf:
#     if word_dict_iwf[word] >= value_80:
#         continue
#     else:
#         dict_topXX[word] = word_dict_iwf[word]
#
#
# output_file_task2_iwf9 = ""
# output_file_task2_iwf9 = open("./iwf9-result.txt","w")
# count_task2_iwf = 1
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_iwf(file)
#     score_spam_iwf = math.log10(p_spam_iwf)
#     score_ham_iwf = math.log10(p_ham_iwf)
#     score_deno_iwf = 0
#     for word in sorted(wordset_test_iwf):
#         if not word in dict_topXX:
#             continue
#         else:
#             score_ham_iwf += math.log10(model_dict_iwf[word][1])
#             score_spam_iwf += math.log10(model_dict_iwf[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_iwf > score_spam_iwf:
#         hamORspam_iwf = "ham"
#     else:
#         hamORspam_iwf = "spam"
#     if file.find("spam")>=0:
#         correct_classification_iwf = "spam"
#     else:
#         correct_classification_iwf = "ham"
#     if hamORspam_iwf == correct_classification_iwf:
#         result_iwf = "right"
#         if hamORspam_iwf == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_iwf = "wrong"
#         if hamORspam_iwf == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_iwf = str(count_task2_iwf), str(file), str(hamORspam_iwf), str(score_ham_iwf), str(score_spam_iwf), str(correct_classification_iwf), str(result_iwf)
#     outstr_task2_iwf = "  ".join(list(output_task2_iwf))
#     output_file_task2_iwf9.writelines(outstr_task2_iwf + "\r\n")
#     count_task2_iwf += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append(len(dict_topXX))
# output_file_task2_iwf9.close()
#
#
# ######## frequency = 25%
# dic_topXXV = []
# dict_topXXV = {}
# final_topXXV = []
# for word in word_dict_iwf:
#     dic_topXXV.append(word_dict_iwf[word])
#
# dic_topXXV_sorted = sorted(dic_topXXV)
# value_75 = dic_topXXV_sorted[int(len(dic_topXXV_sorted)* 0.75)-1]
# for i in dic_topXXV_sorted:
#     if i < value_75:
#         final_topXXV.append(i)
#     else:
#         break
#
# for word in word_dict_iwf:
#     if word_dict_iwf[word] >= value_75:
#         continue
#     else:
#         dict_topXXV[word] = word_dict_iwf[word]
#
#
# output_file_task2_iwf10 = ""
# output_file_task2_iwf10 = open("./iwf10-result.txt","w")
# count_task2_iwf = 1
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_iwf(file)
#     score_spam_iwf = math.log10(p_spam_iwf)
#     score_ham_iwf = math.log10(p_ham_iwf)
#     score_deno_iwf = 0
#     for word in sorted(wordset_test_iwf):
#         if not word in dict_topXXV:
#             continue
#         else:
#             score_ham_iwf += math.log10(model_dict_iwf[word][1])
#             score_spam_iwf += math.log10(model_dict_iwf[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_iwf > score_spam_iwf:
#         hamORspam_iwf = "ham"
#     else:
#         hamORspam_iwf = "spam"
#     if file.find("spam")>=0:
#         correct_classification_iwf = "spam"
#     else:
#         correct_classification_iwf = "ham"
#     if hamORspam_iwf == correct_classification_iwf:
#         result_iwf = "right"
#         if hamORspam_iwf == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_iwf = "wrong"
#         if hamORspam_iwf == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_iwf = str(count_task2_iwf), str(file), str(hamORspam_iwf), str(score_ham_iwf), str(score_spam_iwf), str(correct_classification_iwf), str(result_iwf)
#     outstr_task2_iwf = "  ".join(list(output_task2_iwf))
#     output_file_task2_iwf10.writelines(outstr_task2_iwf + "\r\n")
#     count_task2_iwf += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append(len(dict_topXXV))
# output_file_task2_iwf10.close()
#
# ######## plot
#
# import matplotlib.pyplot as mplot
#
# x = []
# y0 = []
# y1 = []
# y2 = []
#
# for i in x_list:
#     x.append(i)
#
# for i in y_list:
#     y0.append(i[0])
#     y1.append(i[1])
#     y2.append(i[2])
#
# x_tick = list(range(len(x)))
# width = 0.2
# mplot.bar(x_tick, y0, width=width, label='accurcy', fc="blue")
# for i in range(len(x)):
#     x_tick[i] = x_tick[i] + width
# mplot.bar(x_tick, y1, width=width, label='precision', tick_label=x, fc="red")
# for i in range(len(x)):
#     x_tick[i] = x_tick[i] + width
# mplot.bar(x_tick, y2, width=width, label='recall', fc="green")
# mplot.legend()
# mplot.show()
