import os
import re
import math
path = '/Users/yuhaomao/Downloads/train'
files=os.listdir(path)
output_file=""
output_file=open("./baseline-model.txt","w")

output_file_task2 = ""
output_file_task2 = open("./baseline-result.txt","w")
word_set = []
word_dict_ham  = {}
word_dict_spam = {}
word_dict = {}
model_dict = {}
files= os.listdir(path)
count = 1
count_ham = 0
num_ham = 0
count_spam = 0
num_spam = 0
count_word_dic = 0
ham_prop = None
spam_prop = None
# print(files)
num_files_spam = 0
num_files_ham = 0
##########################################task 1
def file_content(files):
    global num_files_ham
    global num_files_spam
    global word_set
    global word_dict
    global word_dict_ham
    global word_dict_spam
    # preprocess with : plus \n
    # lower case
    # symbols
    for i in files:
        # print(i)
        # print(i[6])
        if i[6] == "s":
            num_files_spam += 1
        elif i[6] == "h":
            num_files_ham += 1
        file = open(path + "/" + i, encoding = "latin-1")
        contents = file.readlines()
        for j in range(2,len(contents),1):
            if contents[j-2].find(":") == -1:
                continue
            if not contents[j-1] == "\n":
                continue
            if contents[j].find(":") == -1 or contents[j][-2] == ":":
                contents = contents[j:]
                # print(contents)
                for line in contents:
                    # print(line)
                    string = re.split('[^a-zA-Z]',line)
                    a = list(filter(None,string))
                    words_str = " ".join(a).lower()
                    words = re.split(" ",words_str)
                    for word in words:
                        # print("xxxx")
                        # print(word)
                        if word == " ":
                            continue
                        if word == "":
                            continue
                        if word not in word_dict:
                            # print(word_set)
                            word_set.append(word)
                            word_dict[word] = 1
                        elif word in word_dict:
                            word_dict[word] += 1
                        if i[6] == "s":
                            if word not in word_dict_spam:
                                word_dict_spam[word] = 1
                            elif word in word_dict_spam:
                                word_dict_spam[word] += 1
                        elif i[6] == "h":
                            if word not in word_dict_ham:
                                word_dict_ham[word] = 1
                            elif word in word_dict_ham:
                                word_dict_ham[word] += 1
                break


def no_preprocess(files):
    global num_files_ham
    global num_files_spam
    global word_set
    global word_dict
    global word_dict_ham
    global word_dict_spam
    for i in files:
        if i[6] == "s":
            num_files_spam += 1
        elif i[6] == "h":
            num_files_ham += 1
        file = open(path + "/" + i, encoding="latin-1")
        contents = file.readlines()
        for line in contents:
            string = re.split('[^a-zA-Z]',line)
            a = list(filter(None, string))
            words_str = " ".join(a).lower()
            words = re.split(" ", words_str)
            # words = re.split('[^a-zA-Z]', line)
            for word in words:
                # word = word.lower()
                if word == " "  or word == "":
                    continue
                if word not in word_dict:
                    # print(word_set)
                    word_set.append(word)
                    word_dict[word] = 1
                elif word in word_dict:
                    word_dict[word] += 1
                if i[6] == "s":
                    if word not in word_dict_spam:
                        word_dict_spam[word] = 1
                    elif word in word_dict_spam:
                        word_dict_spam[word] += 1
                elif i[6] == "h":
                    if word not in word_dict_ham:
                        word_dict_ham[word] = 1
                    elif word in word_dict_ham:
                        word_dict_ham[word] += 1


# file_content(files)
no_preprocess(files)


for word_ham in word_dict_ham:
    count_ham += word_dict_ham[word_ham]
    num_ham += 1

for word_spam in word_dict_spam:
    count_spam += word_dict_spam[word_spam]
    num_spam += 1

for word in word_dict:
    count_word_dic += word_dict[word]


for word in sorted(word_set):
    if word_dict_ham.get(word) == None:
        str2 = 0
        smooth_ham_prop = (0.5) / (count_ham + (0.5 * len(word_set)))
    else:
        str2 = word_dict_ham[word]
        smooth_ham_prop = (word_dict_ham[word] + 0.5)/ (count_ham + (0.5 * len(word_set)))

    if word_dict_spam.get(word) == None:
        str4 = 0
        smooth_spam_prop = (0.5) / (count_spam + (0.5 * len(word_set)))
    else:
        str4 = word_dict_spam[word]
        smooth_spam_prop = (word_dict_spam.get(word) + 0.5)/ (count_spam + (0.5 * len(word_set)))


    output_task1 = str(count),str(word),str(str2),str(smooth_ham_prop),str(str4),str(smooth_spam_prop)
    model_dict[word]=[str2,smooth_ham_prop,str4,smooth_spam_prop]
    outstr="  ".join(list(output_task1))
    output_file.writelines(outstr+"\r\n")

    count += 1
output_file.close()




################## task 2
path_test = '/Users/yuhaomao/Downloads/test'
files_test=os.listdir(path_test)
wordset_test = []
spam_score = 1
ham_score = 1

def task2_preprocess(file):
    global wordset_test
    wordset_test = []
    file_test = open(path_test + "/" + file, encoding = "latin-1")
    contents = file_test.readlines()
    for j in range(2,len(contents),1):
        if contents[j-2].find(":") == -1:
            continue
        if not contents[j-1] == "\n":
            continue
        if contents[j].find(":") == -1 or contents[j][-2] == ":":
            contents = contents[j:]
            # print(contents)
            for line in contents:
                # print(line)
                string = re.split('[^a-zA-Z]',line)
                a = list(filter(None,string))
                words_str = " ".join(a).lower()
                words = re.split(" ",words_str)
                for word in words:
                    if word == " ":
                        pass
                    if word == "":
                        pass
                    if word not in wordset_test:
                        # print(word_set)
                        wordset_test.append(word)
            break

def task2_no_preprocess(file):
    global wordset_test
    wordset_test = []
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
            if word not in wordset_test:
                # print(word_set)
                wordset_test.append(word)


p_spam = num_files_spam/(num_files_spam + num_files_ham)
p_ham = num_files_ham/(num_files_spam + num_files_ham)
p_spam_list = []
p_ham_list = []
word_model_set = []
count_task2 = 1
tp = 0
fp = 0
fn = 0
tn = 0
# file_model = open("/Users/yuhaomao/PycharmProjects/comp6721_with_YH.M/model.txt")
# contents_model = file_model.readlines()
# for i in contents_model:
#     word_model = re.split("  ", i)
#     # model li de wordset
#     word_model_set.append(word_model[1])
count_self = 0
# print(model_dict)
for file in files_test:
    print(file)
    # task2_preprocess(file)
    task2_no_preprocess(file)
    score_spam = math.log10(p_spam)
    score_ham = math.log10(p_ham)
    score_deno = 0
    for word in sorted(wordset_test):
        # if not word in word_dict:
        #     continue
        # else:
        #     score_deno += math.log10(word_dict[word]/count_word_dic)
        #     # print(score_deno)
        if not word in model_dict:
            continue
        else:
            score_ham += math.log10(model_dict[word][1])
            score_spam += math.log10(model_dict[word][3])
    # final_ham = score_ham/score_deno
    # final_spam = score_spam/score_deno
    if score_ham > score_spam:
        hamORspam = "ham"
    else:
        hamORspam = "spam"
    if file.find("spam")>=0:
        correct_classification = "spam"
    else:
        correct_classification = "ham"
    if hamORspam == correct_classification:
        result = "right"
        if hamORspam == "ham":
            tp += 1
        else:
            tn += 1
    else:
        result = "wrong"
        if hamORspam == "ham":
            fp += 1
        else:
            fn += 1

    output_task2 = str(count_task2), str(file), str(hamORspam), str(score_ham), str(score_spam), str(correct_classification), str(result)
    outstr_task2 = "  ".join(list(output_task2))
    output_file_task2.writelines(outstr_task2 + "\r\n")
    count_task2 += 1
output_file_task2.close()
# print(tp)
# print(fp)
# print(fn)
# print(tn)


##################### task 3


# path_stopword = '/Users/yuhaomao/PycharmProjects/comp6721_with_YH.M/stop_word.txt'
# files_stopword=open(path_stopword)
#
# output_file_stopW=""
# output_file_stopW=open("./stopword-model.txt","w")
#
# num_files_spam_stopword = 0
# num_files_ham_stopword = 0
# count_ham_stopword = 0
# num_ham_stopword = 0
# count_spam_stopword = 0
# num_spam_stopword = 0
# count_word_dic = 0
# count_stopword = 1
# ham_prop_stopword = None
# spam_prop_stopword = None
# word_stop = []
# word_set_stopword = []
# word_dict_stopword = {}
# word_dict_spam_stopword = {}
# word_dict_ham_stopword = {}
# model_dict_stopword = {}
# tp = 0
# tn = 0
# fn = 0
# fp = 0
# word = files_stopword.readlines()
#
# for i in word:
#     a = i.replace("\n","")
#     word_stop.append(a)
#
# # stopword_dict = {}
# # for word in sorted(word_dict)[1:]:
# #     if word in word_stop:
# #         pass
# #     else:
# #         stopword_dict[word] = word_dict[word]
# print("adasdsadadasdad")
# print(word_stop)
#
#
# def no_preprocess_stopword(files):
#     global num_files_ham_stopword
#     global num_files_spam_stopword
#     global word_set_stopword
#     global word_dict_stopword
#     global word_dict_ham_stopword
#     global word_dict_spam_stopword
#     for i in files:
#         if i[6] == "s":
#             num_files_spam_stopword += 1
#         elif i[6] == "h":
#             num_files_ham_stopword += 1
#         file = open(path + "/" + i, encoding="latin-1")
#         contents = file.readlines()
#         for line in contents:
#             string = re.split('[^a-zA-Z]',line)
#             a = list(filter(None, string))
#             words_str = " ".join(a).lower()
#             words = re.split(" ", words_str)
#             for word in words:
#                 if word == " ":
#                     continue
#                 if word == "":
#                     continue
#                 if word in word_stop:
#                     continue
#                 if word not in word_dict_stopword:
#                     # print(word_set)
#                     word_set_stopword.append(word)
#                     word_dict_stopword[word] = 1
#                 elif word in word_dict_stopword:
#                     word_dict_stopword[word] += 1
#                 if i[6] == "s":
#                     if word not in word_dict_spam_stopword:
#                         word_dict_spam_stopword[word] = 1
#                     elif word in word_dict_spam_stopword:
#                         word_dict_spam_stopword[word] += 1
#                 elif i[6] == "h":
#                     if word not in word_dict_ham_stopword:
#                         word_dict_ham_stopword[word] = 1
#                     elif word in word_dict_ham_stopword:
#                         word_dict_ham_stopword[word] += 1
#
#
# # file_content(files)
# no_preprocess_stopword(files)
# print("111111111111")
# print(word_dict_stopword)
#
# for word_ham in word_dict_ham_stopword:
#     count_ham_stopword += word_dict_ham_stopword[word_ham]
#     num_ham_stopword += 1
#
# for word_spam in word_dict_spam_stopword:
#     count_spam_stopword += word_dict_spam_stopword[word_spam]
#     num_spam_stopword += 1
# #
# # for word in word_dict_stopword:
# #     count_word_dic += word_dict_stopword[word]
# # print("word_dic spam")
# # print(word_dict_spam)
# # print(num_files_spam)
# # print("2222222222222")
# # print(count_spam + 0.5 * num_spam * num_spam)
# for word in sorted(word_set_stopword):
#     if word in word_stop:
#         print("1asfdbfgndf")
#         continue
#     if word_dict_ham_stopword.get(word) == None:
#         str2 = 0
#         smooth_ham_prop = (0.5) / (count_ham_stopword + (0.5 * num_ham_stopword))
#         # if word_dict_spam.get(word) == None:
#         #     p_ham_word_smooth = (0.5) / (0.5 + 0.5)
#         #     p_word = 1 / ((count_ham + (0.5 * num_ham)) + (count_spam + (0.5 * num_spam)))
#         #     p_ham = num_files_ham / (num_files_spam + num_files_ham)
#         #     smooth_ham_prop = (p_ham_word_smooth * p_word) / p_ham
#         # else:
#         #     p_ham_word_smooth = (0.5) / (1 + word_dict_spam[word])
#         #     p_word =  (1 + word_dict_spam[word]) / ((count_ham + (0.5 * num_ham)) + (count_spam + (0.5 * num_spam)))
#         #     p_ham = num_files_ham / (num_files_spam + num_files_ham)
#         #     smooth_ham_prop = (p_ham_word_smooth * p_word) / p_ham
#     else:
#         str2 = word_dict_ham_stopword[word]
#         smooth_ham_prop = (word_dict_ham_stopword[word] + 0.5)/ (count_ham_stopword + 0.5 * num_ham_stopword)
#
#     if word_dict_spam_stopword.get(word) == None:
#         str4 = 0
#         smooth_spam_prop = (0.5) / (count_spam_stopword + 0.5 * num_spam_stopword)
#     else:
#         str4 = word_dict_spam_stopword[word]
#         smooth_spam_prop = (word_dict_spam_stopword.get(word) + 0.5)/ (count_spam_stopword + 0.5*num_spam_stopword)
#
#
#     output_task1 = str(count_stopword),str(word),str(str2),str(smooth_ham_prop),str(str4),str(smooth_spam_prop)
#     model_dict_stopword[word]=[str2,smooth_ham_prop,str4,smooth_spam_prop]
#     outstr="  ".join(list(output_task1))
#     output_file_stopW.writelines(outstr+"\r\n")
#     # print(outstr)
#     # print(count,"  ",word,ham_prop,"  ",smooth_ham_prop,"  ",spam_prop,"  ",smooth_spam_prop)
#     count_stopword += 1
# output_file_stopW.close()
#
# def task2_no_preprocess_stopword(file):
#     global wordset_test_stopword
#     wordset_test_stopword = []
#     file_test = open(path_test + "/" + file, encoding = "latin-1")
#     contents = file_test.readlines()
#     for line in contents:
#         # print(line)
#         string = re.split('[^a-zA-Z]',line)
#         a = list(filter(None,string))
#         words_str = " ".join(a).lower()
#         words = re.split(" ",words_str)
#         for word in words:
#             if word == " ":
#                 pass
#             if word == "":
#                 pass
#             if word not in wordset_test_stopword:
#                 # print(word_set)
#                 wordset_test_stopword.append(word)
#
# def task2_preprocess(file):
#     global wordset_test_stopword
#     wordset_test_stopword = []
#     file_test = open(path_test + "/" + file, encoding = "latin-1")
#     contents = file_test.readlines()
#     for j in range(2,len(contents),1):
#         if contents[j-2].find(":") == -1:
#             continue
#         if not contents[j-1] == "\n":
#             continue
#         if contents[j].find(":") == -1 or contents[j][-2] == ":":
#             contents = contents[j:]
#             # print(contents)
#             for line in contents:
#                 # print(line)
#                 string = re.split('[^a-zA-Z]',line)
#                 a = list(filter(None,string))
#                 words_str = " ".join(a).lower()
#                 words = re.split(" ",words_str)
#                 for word in words:
#                     if word == " ":
#                         pass
#                     if word == "":
#                         pass
#                     if word not in wordset_test_stopword:
#                         # print(word_set)
#                         wordset_test_stopword.append(word)
#             break
#
# output_file_task2_stopword = ""
# output_file_task2_stopword = open("./stopword-result.txt","w")
# p_spam_stopword = num_files_spam_stopword/(num_files_spam_stopword + num_files_ham_stopword)
# p_ham_stopword = num_files_ham_stopword/(num_files_spam_stopword + num_files_ham_stopword)
# p_spam_list_stopword = []
# p_ham_list_stopword = []
# word_model_set_stopword = []
# count_task2_stopword = 1
# # file_model = open("/Users/yuhaomao/PycharmProjects/comp6721_with_YH.M/model.txt")
# # contents_model = file_model.readlines()
# # for i in contents_model:
# #     word_model = re.split("  ", i)
# #     # model li de wordset
# #     word_model_set.append(word_model[1])
# count_self = 0
# # print(model_dict)
#
# path_test = '/Users/yuhaomao/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test_stopword = []
# spam_score_stopword = 1
# ham_score_stopword = 1
#
# for file in files_test:
#     print(file)
#     task2_preprocess(file)
#     # task2_no_preprocess_stopword(file)
#     score_spam_stopword = math.log10(p_spam_stopword)
#     score_ham_stopword = math.log10(p_ham_stopword)
#     score_deno_stopword = 0
#     for word in sorted(wordset_test_stopword):
#         # if not word in word_dict_stopword:
#         #     pass
#         # else:
#         #     score_deno_stopword += math.log10(word_dict_stopword[word])
#         if not word in model_dict_stopword:
#             continue
#         else:
#             score_ham_stopword += math.log10(model_dict_stopword[word][1])
#             score_spam_stopword += math.log10(model_dict_stopword[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_stopword > score_spam_stopword:
#         hamORspam_stopword = "ham"
#     else:
#         hamORspam_stopword = "spam"
#     if file.find("spam")>=0:
#         correct_classification_stopword = "spam"
#     else:
#         correct_classification_stopword = "ham"
#     if hamORspam_stopword == correct_classification_stopword:
#         result_stopword = "right"
#         if hamORspam_stopword == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_stopword = "wrong"
#         if hamORspam_stopword == "spam":
#             fp += 1
#         else:
#             fn += 1
#
#
#     output_task2_stopword = str(count_task2_stopword), str(file), str(hamORspam_stopword), str(score_ham_stopword), str(score_spam_stopword), str(correct_classification_stopword), str(result_stopword)
#     outstr_task2_stopword = "  ".join(list(output_task2_stopword))
#     output_file_task2_stopword.writelines(outstr_task2_stopword + "\r\n")
#     count_task2_stopword += 1
# output_file_task2_stopword.close()
# print("121121121")
# print(tp)
# print(fp)
# print(fn)
# print(tn)


################ word length filter

# output_file_wlf=""
# output_file_wlf=open("./wordlength-model.txt","w")
#
# num_files_spam_wlf = 0
# num_files_ham_wlf = 0
# count_ham_wlf = 0
# num_ham_wlf = 0
# count_spam_wlf = 0
# num_spam_wlf = 0
# count_word_dic = 0
# count_wlf = 1
# ham_prop_wlf = None
# spam_prop_wlf = None
# word_wlf = []
# word_set_wlf = []
# word_dict_wlf = {}
# word_dict_spam_wlf = {}
# word_dict_ham_wlf = {}
# model_dict_wlf = {}
# tp = 0
# tn = 0
# fn = 0
# fp = 0
#
# # stopword_dict = {}
# # for word in sorted(word_dict)[1:]:
# #     if word in word_stop:
# #         pass
# #     else:
# #         stopword_dict[word] = word_dict[word]
#
#
# def no_preprocess_wlf(files):
#     global num_files_ham_wlf
#     global num_files_spam_wlf
#     global word_set_wlf
#     global word_dict_wlf
#     global word_dict_ham_wlf
#     global word_dict_spam_wlf
#     for i in files:
#         if i[6] == "s":
#             num_files_spam_wlf += 1
#         elif i[6] == "h":
#             num_files_ham_wlf += 1
#         file = open(path + "/" + i, encoding="latin-1")
#         contents = file.readlines()
#         for line in contents:
#             string = re.split('[^a-zA-Z]',line)
#             a = list(filter(None, string))
#             words_str = " ".join(a).lower()
#             words = re.split(" ", words_str)
#             for word in words:
#                 if word == " ":
#                     continue
#                 if word == "":
#                     continue
#                 if len(word) <= 2 or len(word) >= 9:
#                     continue
#                 if word not in word_dict_wlf:
#                     # print(word_set)
#                     word_set_wlf.append(word)
#                     word_dict_wlf[word] = 1
#                 elif word in word_dict_wlf:
#                     word_dict_wlf[word] += 1
#                 if i[6] == "s":
#                     if word not in word_dict_spam_wlf:
#                         word_dict_spam_wlf[word] = 1
#                     elif word in word_dict_spam_wlf:
#                         word_dict_spam_wlf[word] += 1
#                 elif i[6] == "h":
#                     if word not in word_dict_ham_wlf:
#                         word_dict_ham_wlf[word] = 1
#                     elif word in word_dict_ham_wlf:
#                         word_dict_ham_wlf[word] += 1
#
#
# # file_content(files)
# no_preprocess_wlf(files)
#
# for word_ham in word_dict_ham_wlf:
#     count_ham_wlf += word_dict_ham_wlf[word_ham]
#     num_ham_wlf += 1
#
# for word_spam in word_dict_spam_wlf:
#     count_spam_wlf += word_dict_spam_wlf[word_spam]
#     num_spam_wlf += 1
# #
# # for word in word_dict_stopword:
# #     count_word_dic += word_dict_stopword[word]
# # print("word_dic spam")
# # print(word_dict_spam)
# # print(num_files_spam)
# # print("2222222222222")
# # print(count_spam + 0.5 * num_spam * num_spam)
# for word in sorted(word_set_wlf):
#     if len(word) >= 9 or len(word) <= 2:
#         continue
#     if word_dict_ham_wlf.get(word) == None:
#         str2 = 0
#         smooth_ham_prop = (0.5) / (count_ham_wlf + (0.5 * len(word_set_wlf)))
#         # if word_dict_spam.get(word) == None:
#         #     p_ham_word_smooth = (0.5) / (0.5 + 0.5)
#         #     p_word = 1 / ((count_ham + (0.5 * num_ham)) + (count_spam + (0.5 * num_spam)))
#         #     p_ham = num_files_ham / (num_files_spam + num_files_ham)
#         #     smooth_ham_prop = (p_ham_word_smooth * p_word) / p_ham
#         # else:
#         #     p_ham_word_smooth = (0.5) / (1 + word_dict_spam[word])
#         #     p_word =  (1 + word_dict_spam[word]) / ((count_ham + (0.5 * num_ham)) + (count_spam + (0.5 * num_spam)))
#         #     p_ham = num_files_ham / (num_files_spam + num_files_ham)
#         #     smooth_ham_prop = (p_ham_word_smooth * p_word) / p_ham
#     else:
#         str2 = word_dict_ham_wlf[word]
#         smooth_ham_prop = (word_dict_ham_wlf[word] + 0.5)/ (count_ham_wlf + 0.5 * len(word_set_wlf))
#
#     if word_dict_spam_wlf.get(word) == None:
#         str4 = 0
#         smooth_spam_prop = (0.5) / (count_spam_wlf + 0.5 * len(word_set_wlf))
#     else:
#         str4 = word_dict_spam_wlf[word]
#         smooth_spam_prop = (word_dict_spam_wlf.get(word) + 0.5)/ (count_spam_wlf + 0.5*len(word_set_wlf))
#
#
#     output_task1 = str(count_wlf),str(word),str(str2),str(smooth_ham_prop),str(str4),str(smooth_spam_prop)
#     model_dict_wlf[word]=[str2,smooth_ham_prop,str4,smooth_spam_prop]
#     outstr="  ".join(list(output_task1))
#     output_file_wlf.writelines(outstr+"\r\n")
#     # print(outstr)
#     # print(count,"  ",word,ham_prop,"  ",smooth_ham_prop,"  ",spam_prop,"  ",smooth_spam_prop)
#     count_wlf += 1
# output_file_wlf.close()
#
# def task2_no_preprocess_wlf(file):
#     global wordset_test_wlf
#     wordset_test_wlf = []
#     file_test = open(path_test + "/" + file, encoding = "latin-1")
#     contents = file_test.readlines()
#     for line in contents:
#         # print(line)
#         string = re.split('[^a-zA-Z]',line)
#         a = list(filter(None,string))
#         words_str = " ".join(a).lower()
#         words = re.split(" ",words_str)
#         for word in words:
#             if word == " ":
#                 continue
#             if word == "":
#                 continue
#             if len(word) <= 2 or len(word) >= 9:
#                 continue
#             if word not in wordset_test_wlf:
#                 # print(word_set)
#                 wordset_test_wlf.append(word)
#
#
#
# output_file_task2_wlf = ""
# output_file_task2_wlf = open("./wordlength-result.txt","w")
# p_spam_wlf = num_files_spam_wlf/(num_files_spam_wlf + num_files_ham_wlf)
# p_ham_wlf = num_files_ham_wlf/(num_files_spam_wlf + num_files_ham_wlf)
# p_spam_list_wlf = []
# p_ham_list_wlf = []
# word_model_set_wlf = []
# count_task2_wlf = 1
# # file_model = open("/Users/yuhaomao/PycharmProjects/comp6721_with_YH.M/model.txt")
# # contents_model = file_model.readlines()
# # for i in contents_model:
# #     word_model = re.split("  ", i)
# #     # model li de wordset
# #     word_model_set.append(word_model[1])
# count_self = 0
# # print(model_dict)
#
# path_test = '/Users/yuhaomao/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test_wlf = []
# spam_score_wlf = 1
# ham_score_wlf = 1
#
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_wlf(file)
#     score_spam_wlf = math.log10(p_spam_wlf)
#     score_ham_wlf = math.log10(p_ham_wlf)
#     score_deno_wlf = 0
#     for word in sorted(wordset_test_wlf):
#         # if not word in word_dict_stopword:
#         #     pass
#         # else:
#         #     score_deno_stopword += math.log10(word_dict_stopword[word])
#         if not word in model_dict_wlf:
#             continue
#         else:
#             score_ham_wlf += math.log10(model_dict_wlf[word][1])
#             score_spam_wlf += math.log10(model_dict_wlf[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_wlf > score_spam_wlf:
#         hamORspam_wlf = "ham"
#     else:
#         hamORspam_wlf = "spam"
#     if file.find("spam")>=0:
#         correct_classification_wlf = "spam"
#     else:
#         correct_classification_wlf = "ham"
#     if hamORspam_wlf == correct_classification_wlf:
#         result_wlf = "right"
#         if hamORspam_wlf == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_wlf = "wrong"
#         if hamORspam_wlf =="spam":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_wlf = str(count_task2_wlf), str(file), str(hamORspam_wlf), str(score_ham_wlf), str(score_spam_wlf), str(correct_classification_wlf), str(result_wlf)
#     outstr_task2_wlf = "  ".join(list(output_task2_wlf))
#     output_file_task2_wlf.writelines(outstr_task2_wlf + "\r\n")
#     count_task2_wlf += 1
# output_file_task2_wlf.close()
#
# print("1111")
# print(tp)
# print(fp)
# print(fn)
# print(tn)