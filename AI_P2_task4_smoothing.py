import os
import re
import math

path = '/Users/Downloads/train'
files=os.listdir(path)
x_list = []
y_list = []

###### smooth 0.0
# num_files_spam_smooth = 0
# num_files_ham_smooth = 0
# count_ham_smooth = 0
# num_ham_smooth = 0
# count_spam_smooth = 0
# num_spam_smooth = 0
# count_word_dic = 0
# count_smooth = 1
# ham_prop_smooth = None
# spam_prop_smooth = None
# word_smooth = []
# word_set_smooth = []
# word_dict_smooth = {}
# word_dict_spam_smooth = {}
# word_dict_ham_smooth = {}
# model_dict_smooth = {}
# wordset_test_smooth = []
#
# def no_preprocess_smooth(files):
#     global num_files_ham_smooth
#     global num_files_spam_smooth
#     global word_set_smooth
#     global word_dict_smooth
#     global word_dict_ham_smooth
#     global word_dict_spam_smooth
#     for i in files:
#         if i[6] == "s":
#             num_files_spam_smooth += 1
#         elif i[6] == "h":
#             num_files_ham_smooth += 1
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
#                 if word not in word_dict_smooth:
#                     word_set_smooth.append(word)
#                     word_dict_smooth[word] = 1
#                 elif word in word_dict_smooth:
#                     word_dict_smooth[word] += 1
#                 if i[6] == "s":
#                     if word not in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] = 1
#                     elif word in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] += 1
#                 elif i[6] == "h":
#                     if word not in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] = 1
#                     elif word in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] += 1
#
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test = []
# spam_score = 1
# ham_score = 1
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# no_preprocess_smooth(files)
# for word_ham in word_dict_ham_smooth:
#     count_ham_smooth += word_dict_ham_smooth[word_ham]
#     num_ham_smooth += 1
#
# for word_spam in word_dict_spam_smooth:
#     count_spam_smooth += word_dict_spam_smooth[word_spam]
#     num_spam_smooth += 1
#
# for word in sorted(word_set_smooth):
#     if word_dict_ham_smooth.get(word) == None:
#         str2 = 0
#         smooth_ham_prop = float("-inf")
#         # continue
#     else:
#         str2 = word_dict_ham_smooth[word]
#         smooth_ham_prop = (word_dict_ham_smooth[word])/ (count_ham_smooth)
#
#     if word_dict_spam_smooth.get(word) == None:
#         str4 = 0
#         smooth_spam_prop = float("-inf")
#         # continue
#     else:
#         str4 = word_dict_spam_smooth[word]
#         smooth_spam_prop = (word_dict_spam_smooth.get(word))/ (count_spam_smooth)
#
#
#     output_task1 = str(count_smooth),str(word),str(str2),str(smooth_ham_prop),str(str4),str(smooth_spam_prop)
#     model_dict_smooth[word]=[str2,smooth_ham_prop,str4,smooth_spam_prop]
#     # outstr="  ".join(list(output_task1))
#     # output_file_.writelines(outstr+"\r\n")
#     # print(outstr)
#     # print(count,"  ",word,ham_prop,"  ",smooth_ham_prop,"  ",spam_prop,"  ",smooth_spam_prop)
#     count_smooth += 1
# # output_file_wlf.close()
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# p_spam_smooth = num_files_spam_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_ham_smooth = num_files_ham_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_spam_list_smooth = []
# p_ham_list_smooth = []
# word_model_set_smooth = []
# count_task2_smooth = 1
# # file_model = open("/Users/PycharmProjects/model.txt")
# # contents_model = file_model.readlines()
# # for i in contents_model:
# #     word_model = re.split("  ", i)
# #     # model li de wordset
# #     word_model_set.append(word_model[1])
# count_self = 0
# # print(model_dict)
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test_smooth = []
# spam_score_smooth = 1
# ham_score_smooth = 1
#
# #
# # dict_I = {}
# # for word in word_dict_smooth:
# #     if word_dict_smooth[word] <= 1:
# #         continue
# #     else:
# #         dict_I[word] = word_dict_smooth[word]
#
# output_file_task2_smooth = ""
# output_file_task2_smooth = open("./smooth0.0-result.txt","w")
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_smooth(file)
#     score_spam_smooth = math.log10(p_spam_smooth)
#     score_ham_smooth = math.log10(p_ham_smooth)
#     score_deno_smooth = 0
#     for word in sorted(wordset_test_smooth):
#         if not word in model_dict_smooth:
#             continue
#         elif model_dict_smooth[word][1] != float("-inf") and model_dict_smooth[word][3] != float("-inf"):
#             score_ham_smooth += math.log10(model_dict_smooth[word][1])
#             score_spam_smooth += math.log10(model_dict_smooth[word][3])
#         elif model_dict_smooth[word][1] == float("-inf"):
#             score_ham_smooth = float("-inf")
#         elif model_dict_smooth[word][3] == float("-inf"):
#             score_spam_smooth = float("-inf")
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_smooth > score_spam_smooth:
#         hamORspam_smooth = "ham"
#     elif score_ham_smooth < score_spam_smooth:
#         hamORspam_smooth = "spam"
#     else:
#         hamORspam_smooth = "draw"
#     if file.find("spam")>=0:
#         correct_classification_smooth = "spam"
#     else:
#         correct_classification_smooth = "ham"
#     if hamORspam_smooth == correct_classification_smooth:
#         result_smooth = "right"
#         if hamORspam_smooth == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_smooth = "wrong"
#         if hamORspam_smooth == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_smooth = str(count_task2_smooth), str(file), str(hamORspam_smooth), str(score_ham_smooth), str(score_spam_smooth), str(correct_classification_smooth), str(result_smooth)
#     outstr_task2_smooth = "  ".join(list(output_task2_smooth))
#     output_file_task2_smooth.writelines(outstr_task2_smooth + "\r\n")
#     count_task2_smooth += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append("smooth 0.0")
# output_file_task2_smooth.close()



###### smooth 0.1
# num_files_spam_smooth = 0
# num_files_ham_smooth = 0
# count_ham_smooth = 0
# num_ham_smooth = 0
# count_spam_smooth = 0
# num_spam_smooth = 0
# count_word_dic = 0
# count_smooth = 1
# ham_prop_smooth = None
# spam_prop_smooth = None
# word_smooth = []
# word_set_smooth = []
# word_dict_smooth = {}
# word_dict_spam_smooth = {}
# word_dict_ham_smooth = {}
# model_dict_smooth = {}
# wordset_test_smooth = []
#
# def no_preprocess_smooth(files):
#     global num_files_ham_smooth
#     global num_files_spam_smooth
#     global word_set_smooth
#     global word_dict_smooth
#     global word_dict_ham_smooth
#     global word_dict_spam_smooth
#     for i in files:
#         if i[6] == "s":
#             num_files_spam_smooth += 1
#         elif i[6] == "h":
#             num_files_ham_smooth += 1
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
#                 if word not in word_dict_smooth:
#                     word_set_smooth.append(word)
#                     word_dict_smooth[word] = 1
#                 elif word in word_dict_smooth:
#                     word_dict_smooth[word] += 1
#                 if i[6] == "s":
#                     if word not in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] = 1
#                     elif word in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] += 1
#                 elif i[6] == "h":
#                     if word not in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] = 1
#                     elif word in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] += 1
#
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test = []
# spam_score = 1
# ham_score = 1
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# no_preprocess_smooth(files)
# for word_ham in word_dict_ham_smooth:
#     count_ham_smooth += word_dict_ham_smooth[word_ham]
#     num_ham_smooth += 1
#
# for word_spam in word_dict_spam_smooth:
#     count_spam_smooth += word_dict_spam_smooth[word_spam]
#     num_spam_smooth += 1
#
# for word in sorted(word_set_smooth):
#     if word_dict_ham_smooth.get(word) == None:
#         str2 = 0
#         smooth_ham_prop = (0.1) / (count_ham_smooth + (0.1 * len(word_set_smooth)))
#     else:
#         str2 = word_dict_ham_smooth[word]
#         smooth_ham_prop = (word_dict_ham_smooth[word] + 0.1)/ (count_ham_smooth + 0.1 * len(word_set_smooth))
#
#     if word_dict_spam_smooth.get(word) == None:
#         str4 = 0
#         smooth_spam_prop = (0.1) / (count_spam_smooth + 0.1 * len(word_set_smooth))
#     else:
#         str4 = word_dict_spam_smooth[word]
#         smooth_spam_prop = (word_dict_spam_smooth.get(word) + 0.1)/ (count_spam_smooth + 0.1*len(word_set_smooth))
#
#
#     output_task1 = str(count_smooth),str(word),str(str2),str(smooth_ham_prop),str(str4),str(smooth_spam_prop)
#     model_dict_smooth[word]=[str2,smooth_ham_prop,str4,smooth_spam_prop]
#     # outstr="  ".join(list(output_task1))
#     # output_file_.writelines(outstr+"\r\n")
#     # print(outstr)
#     # print(count,"  ",word,ham_prop,"  ",smooth_ham_prop,"  ",spam_prop,"  ",smooth_spam_prop)
#     count_smooth += 1
# # output_file_wlf.close()
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# p_spam_smooth = num_files_spam_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_ham_smooth = num_files_ham_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_spam_list_smooth = []
# p_ham_list_smooth = []
# word_model_set_smooth = []
# count_task2_smooth = 1
# # file_model = open("/Users/PycharmProjects/comp6721_with_YH.M/model.txt")
# # contents_model = file_model.readlines()
# # for i in contents_model:
# #     word_model = re.split("  ", i)
# #     # model li de wordset
# #     word_model_set.append(word_model[1])
# count_self = 0
# # print(model_dict)
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test_smooth = []
# spam_score_smooth = 1
# ham_score_smooth = 1
#
# #
# # dict_I = {}
# # for word in word_dict_smooth:
# #     if word_dict_smooth[word] <= 1:
# #         continue
# #     else:
# #         dict_I[word] = word_dict_smooth[word]
#
# output_file_task2_smooth = ""
# output_file_task2_smooth = open("./smooth-result.txt","w")
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_smooth(file)
#     score_spam_smooth = math.log10(p_spam_smooth)
#     score_ham_smooth = math.log10(p_ham_smooth)
#     score_deno_smooth = 0
#     for word in sorted(wordset_test_smooth):
#         if not word in model_dict_smooth:
#             continue
#         else:
#             score_ham_smooth += math.log10(model_dict_smooth[word][1])
#             score_spam_smooth += math.log10(model_dict_smooth[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_smooth > score_spam_smooth:
#         hamORspam_smooth = "ham"
#     else:
#         hamORspam_smooth = "spam"
#     if file.find("spam")>=0:
#         correct_classification_smooth = "spam"
#     else:
#         correct_classification_smooth = "ham"
#     if hamORspam_smooth == correct_classification_smooth:
#         result_smooth = "right"
#         if hamORspam_smooth == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_smooth = "wrong"
#         if hamORspam_smooth == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_smooth = str(count_task2_smooth), str(file), str(hamORspam_smooth), str(score_ham_smooth), str(score_spam_smooth), str(correct_classification_smooth), str(result_smooth)
#     outstr_task2_smooth = "  ".join(list(output_task2_smooth))
#     output_file_task2_smooth.writelines(outstr_task2_smooth + "\r\n")
#     count_task2_smooth += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append("smooth 0.1")
# output_file_task2_smooth.close()
# print("11111")
# print(tp)
# print(fp)
# print(fn)
# print(tn)


####### smooth 0.2
# num_files_spam_smooth = 0
# num_files_ham_smooth = 0
# count_ham_smooth = 0
# num_ham_smooth = 0
# count_spam_smooth = 0
# num_spam_smooth = 0
# count_word_dic = 0
# count_smooth = 1
# ham_prop_smooth = None
# spam_prop_smooth = None
# word_smooth = []
# word_set_smooth = []
# word_dict_smooth = {}
# word_dict_spam_smooth = {}
# word_dict_ham_smooth = {}
# model_dict_smooth = {}
# wordset_test_smooth = []
# def no_preprocess_smooth(files):
#     global num_files_ham_smooth
#     global num_files_spam_smooth
#     global word_set_smooth
#     global word_dict_smooth
#     global word_dict_ham_smooth
#     global word_dict_spam_smooth
#     for i in files:
#         if i[6] == "s":
#             num_files_spam_smooth += 1
#         elif i[6] == "h":
#             num_files_ham_smooth += 1
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
#                 if word not in word_dict_smooth:
#                     word_set_smooth.append(word)
#                     word_dict_smooth[word] = 1
#                 elif word in word_dict_smooth:
#                     word_dict_smooth[word] += 1
#                 if i[6] == "s":
#                     if word not in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] = 1
#                     elif word in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] += 1
#                 elif i[6] == "h":
#                     if word not in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] = 1
#                     elif word in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] += 1
#
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test = []
# spam_score = 1
# ham_score = 1
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# no_preprocess_smooth(files)
# for word_ham in word_dict_ham_smooth:
#     count_ham_smooth += word_dict_ham_smooth[word_ham]
#     num_ham_smooth += 1
#
# for word_spam in word_dict_spam_smooth:
#     count_spam_smooth += word_dict_spam_smooth[word_spam]
#     num_spam_smooth += 1
#
# for word in sorted(word_set_smooth):
#     if word_dict_ham_smooth.get(word) == None:
#         str2 = 0
#         smooth_ham_prop = (0.2) / (count_ham_smooth + (0.2 * len(word_set_smooth)))
#     else:
#         str2 = word_dict_ham_smooth[word]
#         smooth_ham_prop = (word_dict_ham_smooth[word] + 0.2)/ (count_ham_smooth + 0.2 * len(word_set_smooth))
#
#     if word_dict_spam_smooth.get(word) == None:
#         str4 = 0
#         smooth_spam_prop = (0.2) / (count_spam_smooth + 0.2 * len(word_set_smooth))
#     else:
#         str4 = word_dict_spam_smooth[word]
#         smooth_spam_prop = (word_dict_spam_smooth.get(word) + 0.2)/ (count_spam_smooth + 0.2*len(word_set_smooth))
#
#
#     output_task1 = str(count_smooth),str(word),str(str2),str(smooth_ham_prop),str(str4),str(smooth_spam_prop)
#     model_dict_smooth[word]=[str2,smooth_ham_prop,str4,smooth_spam_prop]
#     # outstr="  ".join(list(output_task1))
#     # output_file_.writelines(outstr+"\r\n")
#     # print(outstr)
#     # print(count,"  ",word,ham_prop,"  ",smooth_ham_prop,"  ",spam_prop,"  ",smooth_spam_prop)
#     count_smooth += 1
# # output_file_wlf.close()
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# p_spam_smooth = num_files_spam_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_ham_smooth = num_files_ham_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_spam_list_smooth = []
# p_ham_list_smooth = []
# word_model_set_smooth = []
# count_task2_smooth = 1
# # file_model = open("/Users/PycharmProjects/model.txt")
# # contents_model = file_model.readlines()
# # for i in contents_model:
# #     word_model = re.split("  ", i)
# #     # model li de wordset
# #     word_model_set.append(word_model[1])
# count_self = 0
# # print(model_dict)
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test_smooth = []
# spam_score_smooth = 1
# ham_score_smooth = 1
#
# #
# # dict_I = {}
# # for word in word_dict_smooth:
# #     if word_dict_smooth[word] <= 1:
# #         continue
# #     else:
# #         dict_I[word] = word_dict_smooth[word]
#
# output_file_task2_smooth = ""
# output_file_task2_smooth = open("./smooth0.2-result.txt","w")
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_smooth(file)
#     score_spam_smooth = math.log10(p_spam_smooth)
#     score_ham_smooth = math.log10(p_ham_smooth)
#     score_deno_smooth = 0
#     for word in sorted(wordset_test_smooth):
#         if not word in model_dict_smooth:
#             continue
#         else:
#             score_ham_smooth += math.log10(model_dict_smooth[word][1])
#             score_spam_smooth += math.log10(model_dict_smooth[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_smooth > score_spam_smooth:
#         hamORspam_smooth = "ham"
#     else:
#         hamORspam_smooth = "spam"
#     if file.find("spam")>=0:
#         correct_classification_smooth = "spam"
#     else:
#         correct_classification_smooth = "ham"
#     if hamORspam_smooth == correct_classification_smooth:
#         result_smooth = "right"
#         if hamORspam_smooth == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_smooth = "wrong"
#         if hamORspam_smooth == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_smooth = str(count_task2_smooth), str(file), str(hamORspam_smooth), str(score_ham_smooth), str(score_spam_smooth), str(correct_classification_smooth), str(result_smooth)
#     outstr_task2_smooth = "  ".join(list(output_task2_smooth))
#     output_file_task2_smooth.writelines(outstr_task2_smooth + "\r\n")
#     count_task2_smooth += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append("smooth 0.2")
# output_file_task2_smooth.close()
#
#
#
#
# ####### smooth 0.3
num_files_spam_smooth = 0
num_files_ham_smooth = 0
count_ham_smooth = 0
num_ham_smooth = 0
count_spam_smooth = 0
num_spam_smooth = 0
count_word_dic = 0
count_smooth = 1
ham_prop_smooth = None
spam_prop_smooth = None
word_smooth = []
word_set_smooth = []
word_dict_smooth = {}
word_dict_spam_smooth = {}
word_dict_ham_smooth = {}
model_dict_smooth = {}
wordset_test_smooth = []
def no_preprocess_smooth(files):
    global num_files_ham_smooth
    global num_files_spam_smooth
    global word_set_smooth
    global word_dict_smooth
    global word_dict_ham_smooth
    global word_dict_spam_smooth
    for i in files:
        if i[6] == "s":
            num_files_spam_smooth += 1
        elif i[6] == "h":
            num_files_ham_smooth += 1
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
                if word not in word_dict_smooth:
                    word_set_smooth.append(word)
                    word_dict_smooth[word] = 1
                elif word in word_dict_smooth:
                    word_dict_smooth[word] += 1
                if i[6] == "s":
                    if word not in word_dict_spam_smooth:
                        word_dict_spam_smooth[word] = 1
                    elif word in word_dict_spam_smooth:
                        word_dict_spam_smooth[word] += 1
                elif i[6] == "h":
                    if word not in word_dict_ham_smooth:
                        word_dict_ham_smooth[word] = 1
                    elif word in word_dict_ham_smooth:
                        word_dict_ham_smooth[word] += 1


path_test = '/Users/Downloads/test'
files_test=os.listdir(path_test)
wordset_test = []
spam_score = 1
ham_score = 1

def task2_no_preprocess_smooth(file):
    global wordset_test_smooth
    wordset_test_smooth = []
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
            if word not in wordset_test_smooth:
                # print(word_set)
                wordset_test_smooth.append(word)

no_preprocess_smooth(files)
for word_ham in word_dict_ham_smooth:
    count_ham_smooth += word_dict_ham_smooth[word_ham]
    num_ham_smooth += 1

for word_spam in word_dict_spam_smooth:
    count_spam_smooth += word_dict_spam_smooth[word_spam]
    num_spam_smooth += 1

for word in sorted(word_set_smooth):
    if word_dict_ham_smooth.get(word) == None:
        str2 = 0
        smooth_ham_prop = (0.3) / (count_ham_smooth + (0.3 * len(word_set_smooth)))
    else:
        str2 = word_dict_ham_smooth[word]
        smooth_ham_prop = (word_dict_ham_smooth[word] + 0.3)/ (count_ham_smooth + 0.3 * len(word_set_smooth))

    if word_dict_spam_smooth.get(word) == None:
        str4 = 0
        smooth_spam_prop = (0.3) / (count_spam_smooth + 0.3 * len(word_set_smooth))
    else:
        str4 = word_dict_spam_smooth[word]
        smooth_spam_prop = (word_dict_spam_smooth.get(word) + 0.3)/ (count_spam_smooth + 0.3*len(word_set_smooth))


    output_task1 = str(count_smooth),str(word),str(str2),str(smooth_ham_prop),str(str4),str(smooth_spam_prop)
    model_dict_smooth[word]=[str2,smooth_ham_prop,str4,smooth_spam_prop]
    # outstr="  ".join(list(output_task1))
    # output_file_.writelines(outstr+"\r\n")
    # print(outstr)
    # print(count,"  ",word,ham_prop,"  ",smooth_ham_prop,"  ",spam_prop,"  ",smooth_spam_prop)
    count_smooth += 1
# output_file_wlf.close()

def task2_no_preprocess_smooth(file):
    global wordset_test_smooth
    wordset_test_smooth = []
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
            if word not in wordset_test_smooth:
                # print(word_set)
                wordset_test_smooth.append(word)

p_spam_smooth = num_files_spam_smooth/(num_files_spam_smooth + num_files_ham_smooth)
p_ham_smooth = num_files_ham_smooth/(num_files_spam_smooth + num_files_ham_smooth)
p_spam_list_smooth = []
p_ham_list_smooth = []
word_model_set_smooth = []
count_task2_smooth = 1
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
wordset_test_smooth = []
spam_score_smooth = 1
ham_score_smooth = 1

#
# dict_I = {}
# for word in word_dict_smooth:
#     if word_dict_smooth[word] <= 1:
#         continue
#     else:
#         dict_I[word] = word_dict_smooth[word]

output_file_task2_smooth = ""
output_file_task2_smooth = open("./smooth0.3-result.txt","w")
tp = 0
fp = 0
fn = 0
tn = 0
for file in files_test:
    print(file)
    # task2_preprocess(file)
    task2_no_preprocess_smooth(file)
    score_spam_smooth = math.log10(p_spam_smooth)
    score_ham_smooth = math.log10(p_ham_smooth)
    score_deno_smooth = 0
    for word in sorted(wordset_test_smooth):
        if not word in model_dict_smooth:
            continue
        else:
            score_ham_smooth += math.log10(model_dict_smooth[word][1])
            score_spam_smooth += math.log10(model_dict_smooth[word][3])
    # final_ham = score_ham/score_deno
    # final_spam = score_spam/score_deno
    if score_ham_smooth > score_spam_smooth:
        hamORspam_smooth = "ham"
    else:
        hamORspam_smooth = "spam"
    if file.find("spam")>=0:
        correct_classification_smooth = "spam"
    else:
        correct_classification_smooth = "ham"
    if hamORspam_smooth == correct_classification_smooth:
        result_smooth = "right"
        if hamORspam_smooth == "ham":
            tp += 1
        else:
            tn += 1
    else:
        result_smooth = "wrong"
        if hamORspam_smooth == "ham":
            fp += 1
        else:
            fn += 1
    output_task2_smooth = str(count_task2_smooth), str(file), str(hamORspam_smooth), str(score_ham_smooth), str(score_spam_smooth), str(correct_classification_smooth), str(result_smooth)
    outstr_task2_smooth = "  ".join(list(output_task2_smooth))
    output_file_task2_smooth.writelines(outstr_task2_smooth + "\r\n")
    count_task2_smooth += 1
acc = (tp + tn) / (tp + tn + fn + fp)
precision = tp / (tp + fp)
recall = tp / (tp + fn)
y_list.append([acc,precision,recall])
x_list.append("smooth 0.3")
output_file_task2_smooth.close()

#
# ###### smooth 0.4
# num_files_spam_smooth = 0
# num_files_ham_smooth = 0
# count_ham_smooth = 0
# num_ham_smooth = 0
# count_spam_smooth = 0
# num_spam_smooth = 0
# count_word_dic = 0
# count_smooth = 1
# ham_prop_smooth = None
# spam_prop_smooth = None
# word_smooth = []
# word_set_smooth = []
# word_dict_smooth = {}
# word_dict_spam_smooth = {}
# word_dict_ham_smooth = {}
# model_dict_smooth = {}
# wordset_test_smooth = []
# def no_preprocess_smooth(files):
#     global num_files_ham_smooth
#     global num_files_spam_smooth
#     global word_set_smooth
#     global word_dict_smooth
#     global word_dict_ham_smooth
#     global word_dict_spam_smooth
#     for i in files:
#         if i[6] == "s":
#             num_files_spam_smooth += 1
#         elif i[6] == "h":
#             num_files_ham_smooth += 1
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
#                 if word not in word_dict_smooth:
#                     word_set_smooth.append(word)
#                     word_dict_smooth[word] = 1
#                 elif word in word_dict_smooth:
#                     word_dict_smooth[word] += 1
#                 if i[6] == "s":
#                     if word not in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] = 1
#                     elif word in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] += 1
#                 elif i[6] == "h":
#                     if word not in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] = 1
#                     elif word in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] += 1
#
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test = []
# spam_score = 1
# ham_score = 1
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# no_preprocess_smooth(files)
# for word_ham in word_dict_ham_smooth:
#     count_ham_smooth += word_dict_ham_smooth[word_ham]
#     num_ham_smooth += 1
#
# for word_spam in word_dict_spam_smooth:
#     count_spam_smooth += word_dict_spam_smooth[word_spam]
#     num_spam_smooth += 1
#
# for word in sorted(word_set_smooth):
#     if word_dict_ham_smooth.get(word) == None:
#         str2 = 0
#         smooth_ham_prop = (0.4) / (count_ham_smooth + (0.4 * len(word_set_smooth)))
#     else:
#         str2 = word_dict_ham_smooth[word]
#         smooth_ham_prop = (word_dict_ham_smooth[word] + 0.4)/ (count_ham_smooth + 0.4 * len(word_set_smooth))
#
#     if word_dict_spam_smooth.get(word) == None:
#         str4 = 0
#         smooth_spam_prop = (0.4) / (count_spam_smooth + 0.4 * len(word_set_smooth))
#     else:
#         str4 = word_dict_spam_smooth[word]
#         smooth_spam_prop = (word_dict_spam_smooth.get(word) + 0.4)/ (count_spam_smooth + 0.4*len(word_set_smooth))
#
#
#     output_task1 = str(count_smooth),str(word),str(str2),str(smooth_ham_prop),str(str4),str(smooth_spam_prop)
#     model_dict_smooth[word]=[str2,smooth_ham_prop,str4,smooth_spam_prop]
#     # outstr="  ".join(list(output_task1))
#     # output_file_.writelines(outstr+"\r\n")
#     # print(outstr)
#     # print(count,"  ",word,ham_prop,"  ",smooth_ham_prop,"  ",spam_prop,"  ",smooth_spam_prop)
#     count_smooth += 1
# # output_file_wlf.close()
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# p_spam_smooth = num_files_spam_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_ham_smooth = num_files_ham_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_spam_list_smooth = []
# p_ham_list_smooth = []
# word_model_set_smooth = []
# count_task2_smooth = 1
# # file_model = open("/Users/PycharmProjects/model.txt")
# # contents_model = file_model.readlines()
# # for i in contents_model:
# #     word_model = re.split("  ", i)
# #     # model li de wordset
# #     word_model_set.append(word_model[1])
# count_self = 0
# # print(model_dict)
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test_smooth = []
# spam_score_smooth = 1
# ham_score_smooth = 1
#
# #
# # dict_I = {}
# # for word in word_dict_smooth:
# #     if word_dict_smooth[word] <= 1:
# #         continue
# #     else:
# #         dict_I[word] = word_dict_smooth[word]
#
# output_file_task2_smooth = ""
# output_file_task2_smooth = open("./smooth0.4-result.txt","w")
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_smooth(file)
#     score_spam_smooth = math.log10(p_spam_smooth)
#     score_ham_smooth = math.log10(p_ham_smooth)
#     score_deno_smooth = 0
#     for word in sorted(wordset_test_smooth):
#         if not word in model_dict_smooth:
#             continue
#         else:
#             score_ham_smooth += math.log10(model_dict_smooth[word][1])
#             score_spam_smooth += math.log10(model_dict_smooth[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_smooth > score_spam_smooth:
#         hamORspam_smooth = "ham"
#     else:
#         hamORspam_smooth = "spam"
#     if file.find("spam")>=0:
#         correct_classification_smooth = "spam"
#     else:
#         correct_classification_smooth = "ham"
#     if hamORspam_smooth == correct_classification_smooth:
#         result_smooth = "right"
#         if hamORspam_smooth == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_smooth = "wrong"
#         if hamORspam_smooth == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_smooth = str(count_task2_smooth), str(file), str(hamORspam_smooth), str(score_ham_smooth), str(score_spam_smooth), str(correct_classification_smooth), str(result_smooth)
#     outstr_task2_smooth = "  ".join(list(output_task2_smooth))
#     output_file_task2_smooth.writelines(outstr_task2_smooth + "\r\n")
#     count_task2_smooth += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append("smooth 0.4")
# output_file_task2_smooth.close()
#
#
# ####### smooth 0.5
# num_files_spam_smooth = 0
# num_files_ham_smooth = 0
# count_ham_smooth = 0
# num_ham_smooth = 0
# count_spam_smooth = 0
# num_spam_smooth = 0
# count_word_dic = 0
# count_smooth = 1
# ham_prop_smooth = None
# spam_prop_smooth = None
# word_smooth = []
# word_set_smooth = []
# word_dict_smooth = {}
# word_dict_spam_smooth = {}
# word_dict_ham_smooth = {}
# model_dict_smooth = {}
# wordset_test_smooth = []
# def no_preprocess_smooth(files):
#     global num_files_ham_smooth
#     global num_files_spam_smooth
#     global word_set_smooth
#     global word_dict_smooth
#     global word_dict_ham_smooth
#     global word_dict_spam_smooth
#     for i in files:
#         if i[6] == "s":
#             num_files_spam_smooth += 1
#         elif i[6] == "h":
#             num_files_ham_smooth += 1
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
#                 if word not in word_dict_smooth:
#                     word_set_smooth.append(word)
#                     word_dict_smooth[word] = 1
#                 elif word in word_dict_smooth:
#                     word_dict_smooth[word] += 1
#                 if i[6] == "s":
#                     if word not in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] = 1
#                     elif word in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] += 1
#                 elif i[6] == "h":
#                     if word not in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] = 1
#                     elif word in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] += 1
#
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test = []
# spam_score = 1
# ham_score = 1
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# no_preprocess_smooth(files)
# for word_ham in word_dict_ham_smooth:
#     count_ham_smooth += word_dict_ham_smooth[word_ham]
#     num_ham_smooth += 1
#
# for word_spam in word_dict_spam_smooth:
#     count_spam_smooth += word_dict_spam_smooth[word_spam]
#     num_spam_smooth += 1
#
# for word in sorted(word_set_smooth):
#     if word_dict_ham_smooth.get(word) == None:
#         str2 = 0
#         smooth_ham_prop = (0.5) / (count_ham_smooth + (0.5 * len(word_set_smooth)))
#     else:
#         str2 = word_dict_ham_smooth[word]
#         smooth_ham_prop = (word_dict_ham_smooth[word] + 0.5)/ (count_ham_smooth + 0.5 * len(word_set_smooth))
#
#     if word_dict_spam_smooth.get(word) == None:
#         str4 = 0
#         smooth_spam_prop = (0.5) / (count_spam_smooth + 0.5 * len(word_set_smooth))
#     else:
#         str4 = word_dict_spam_smooth[word]
#         smooth_spam_prop = (word_dict_spam_smooth.get(word) + 0.5)/ (count_spam_smooth + 0.5*len(word_set_smooth))
#
#
#     output_task1 = str(count_smooth),str(word),str(str2),str(smooth_ham_prop),str(str4),str(smooth_spam_prop)
#     model_dict_smooth[word]=[str2,smooth_ham_prop,str4,smooth_spam_prop]
#     # outstr="  ".join(list(output_task1))
#     # output_file_.writelines(outstr+"\r\n")
#     # print(outstr)
#     # print(count,"  ",word,ham_prop,"  ",smooth_ham_prop,"  ",spam_prop,"  ",smooth_spam_prop)
#     count_smooth += 1
# # output_file_wlf.close()
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# p_spam_smooth = num_files_spam_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_ham_smooth = num_files_ham_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_spam_list_smooth = []
# p_ham_list_smooth = []
# word_model_set_smooth = []
# count_task2_smooth = 1
# # file_model = open("/Users/PycharmProjects/model.txt")
# # contents_model = file_model.readlines()
# # for i in contents_model:
# #     word_model = re.split("  ", i)
# #     # model li de wordset
# #     word_model_set.append(word_model[1])
# count_self = 0
# # print(model_dict)
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test_smooth = []
# spam_score_smooth = 1
# ham_score_smooth = 1
#
# #
# # dict_I = {}
# # for word in word_dict_smooth:
# #     if word_dict_smooth[word] <= 1:
# #         continue
# #     else:
# #         dict_I[word] = word_dict_smooth[word]
#
# output_file_task2_smooth = ""
# output_file_task2_smooth = open("./smooth0.5-result.txt","w")
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_smooth(file)
#     score_spam_smooth = math.log10(p_spam_smooth)
#     score_ham_smooth = math.log10(p_ham_smooth)
#     score_deno_smooth = 0
#     for word in sorted(wordset_test_smooth):
#         if not word in model_dict_smooth:
#             continue
#         else:
#             score_ham_smooth += math.log10(model_dict_smooth[word][1])
#             score_spam_smooth += math.log10(model_dict_smooth[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_smooth > score_spam_smooth:
#         hamORspam_smooth = "ham"
#     else:
#         hamORspam_smooth = "spam"
#     if file.find("spam")>=0:
#         correct_classification_smooth = "spam"
#     else:
#         correct_classification_smooth = "ham"
#     if hamORspam_smooth == correct_classification_smooth:
#         result_smooth = "right"
#         if hamORspam_smooth == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_smooth = "wrong"
#         if hamORspam_smooth == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_smooth = str(count_task2_smooth), str(file), str(hamORspam_smooth), str(score_ham_smooth), str(score_spam_smooth), str(correct_classification_smooth), str(result_smooth)
#     outstr_task2_smooth = "  ".join(list(output_task2_smooth))
#     output_file_task2_smooth.writelines(outstr_task2_smooth + "\r\n")
#     count_task2_smooth += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append("smooth 0.5")
# output_file_task2_smooth.close()
#
# ###### smooth 0.6
# num_files_spam_smooth = 0
# num_files_ham_smooth = 0
# count_ham_smooth = 0
# num_ham_smooth = 0
# count_spam_smooth = 0
# num_spam_smooth = 0
# count_word_dic = 0
# count_smooth = 1
# ham_prop_smooth = None
# spam_prop_smooth = None
# word_smooth = []
# word_set_smooth = []
# word_dict_smooth = {}
# word_dict_spam_smooth = {}
# word_dict_ham_smooth = {}
# model_dict_smooth = {}
# wordset_test_smooth = []
# def no_preprocess_smooth(files):
#     global num_files_ham_smooth
#     global num_files_spam_smooth
#     global word_set_smooth
#     global word_dict_smooth
#     global word_dict_ham_smooth
#     global word_dict_spam_smooth
#     for i in files:
#         if i[6] == "s":
#             num_files_spam_smooth += 1
#         elif i[6] == "h":
#             num_files_ham_smooth += 1
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
#                 if word not in word_dict_smooth:
#                     word_set_smooth.append(word)
#                     word_dict_smooth[word] = 1
#                 elif word in word_dict_smooth:
#                     word_dict_smooth[word] += 1
#                 if i[6] == "s":
#                     if word not in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] = 1
#                     elif word in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] += 1
#                 elif i[6] == "h":
#                     if word not in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] = 1
#                     elif word in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] += 1
#
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test = []
# spam_score = 1
# ham_score = 1
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# no_preprocess_smooth(files)
# for word_ham in word_dict_ham_smooth:
#     count_ham_smooth += word_dict_ham_smooth[word_ham]
#     num_ham_smooth += 1
#
# for word_spam in word_dict_spam_smooth:
#     count_spam_smooth += word_dict_spam_smooth[word_spam]
#     num_spam_smooth += 1
#
# for word in sorted(word_set_smooth):
#     if word_dict_ham_smooth.get(word) == None:
#         str2 = 0
#         smooth_ham_prop = (0.6) / (count_ham_smooth + (0.6 * len(word_set_smooth)))
#     else:
#         str2 = word_dict_ham_smooth[word]
#         smooth_ham_prop = (word_dict_ham_smooth[word] + 0.6)/ (count_ham_smooth + 0.6 * len(word_set_smooth))
#
#     if word_dict_spam_smooth.get(word) == None:
#         str4 = 0
#         smooth_spam_prop = (0.6) / (count_spam_smooth + 0.6 * len(word_set_smooth))
#     else:
#         str4 = word_dict_spam_smooth[word]
#         smooth_spam_prop = (word_dict_spam_smooth.get(word) + 0.6)/ (count_spam_smooth + 0.6*len(word_set_smooth))
#
#
#     output_task1 = str(count_smooth),str(word),str(str2),str(smooth_ham_prop),str(str4),str(smooth_spam_prop)
#     model_dict_smooth[word]=[str2,smooth_ham_prop,str4,smooth_spam_prop]
#     # outstr="  ".join(list(output_task1))
#     # output_file_.writelines(outstr+"\r\n")
#     # print(outstr)
#     # print(count,"  ",word,ham_prop,"  ",smooth_ham_prop,"  ",spam_prop,"  ",smooth_spam_prop)
#     count_smooth += 1
# # output_file_wlf.close()
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# p_spam_smooth = num_files_spam_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_ham_smooth = num_files_ham_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_spam_list_smooth = []
# p_ham_list_smooth = []
# word_model_set_smooth = []
# count_task2_smooth = 1
# # file_model = open("/Users/PycharmProjects/model.txt")
# # contents_model = file_model.readlines()
# # for i in contents_model:
# #     word_model = re.split("  ", i)
# #     # model li de wordset
# #     word_model_set.append(word_model[1])
# count_self = 0
# # print(model_dict)
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test_smooth = []
# spam_score_smooth = 1
# ham_score_smooth = 1
#
# #
# # dict_I = {}
# # for word in word_dict_smooth:
# #     if word_dict_smooth[word] <= 1:
# #         continue
# #     else:
# #         dict_I[word] = word_dict_smooth[word]
#
# output_file_task2_smooth = ""
# output_file_task2_smooth = open("./smooth0.6-result.txt","w")
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_smooth(file)
#     score_spam_smooth = math.log10(p_spam_smooth)
#     score_ham_smooth = math.log10(p_ham_smooth)
#     score_deno_smooth = 0
#     for word in sorted(wordset_test_smooth):
#         if not word in model_dict_smooth:
#             continue
#         else:
#             score_ham_smooth += math.log10(model_dict_smooth[word][1])
#             score_spam_smooth += math.log10(model_dict_smooth[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_smooth > score_spam_smooth:
#         hamORspam_smooth = "ham"
#     else:
#         hamORspam_smooth = "spam"
#     if file.find("spam")>=0:
#         correct_classification_smooth = "spam"
#     else:
#         correct_classification_smooth = "ham"
#     if hamORspam_smooth == correct_classification_smooth:
#         result_smooth = "right"
#         if hamORspam_smooth == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_smooth = "wrong"
#         if hamORspam_smooth == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_smooth = str(count_task2_smooth), str(file), str(hamORspam_smooth), str(score_ham_smooth), str(score_spam_smooth), str(correct_classification_smooth), str(result_smooth)
#     outstr_task2_smooth = "  ".join(list(output_task2_smooth))
#     output_file_task2_smooth.writelines(outstr_task2_smooth + "\r\n")
#     count_task2_smooth += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append("smooth 0.6")
# output_file_task2_smooth.close()
#
#
#
# ####### smooth 0.7
# num_files_spam_smooth = 0
# num_files_ham_smooth = 0
# count_ham_smooth = 0
# num_ham_smooth = 0
# count_spam_smooth = 0
# num_spam_smooth = 0
# count_word_dic = 0
# count_smooth = 1
# ham_prop_smooth = None
# spam_prop_smooth = None
# word_smooth = []
# word_set_smooth = []
# word_dict_smooth = {}
# word_dict_spam_smooth = {}
# word_dict_ham_smooth = {}
# model_dict_smooth = {}
# wordset_test_smooth = []
# def no_preprocess_smooth(files):
#     global num_files_ham_smooth
#     global num_files_spam_smooth
#     global word_set_smooth
#     global word_dict_smooth
#     global word_dict_ham_smooth
#     global word_dict_spam_smooth
#     for i in files:
#         if i[6] == "s":
#             num_files_spam_smooth += 1
#         elif i[6] == "h":
#             num_files_ham_smooth += 1
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
#                 if word not in word_dict_smooth:
#                     word_set_smooth.append(word)
#                     word_dict_smooth[word] = 1
#                 elif word in word_dict_smooth:
#                     word_dict_smooth[word] += 1
#                 if i[6] == "s":
#                     if word not in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] = 1
#                     elif word in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] += 1
#                 elif i[6] == "h":
#                     if word not in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] = 1
#                     elif word in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] += 1
#
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test = []
# spam_score = 1
# ham_score = 1
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# no_preprocess_smooth(files)
# for word_ham in word_dict_ham_smooth:
#     count_ham_smooth += word_dict_ham_smooth[word_ham]
#     num_ham_smooth += 1
#
# for word_spam in word_dict_spam_smooth:
#     count_spam_smooth += word_dict_spam_smooth[word_spam]
#     num_spam_smooth += 1
#
# for word in sorted(word_set_smooth):
#     if word_dict_ham_smooth.get(word) == None:
#         str2 = 0
#         smooth_ham_prop = (0.7) / (count_ham_smooth + (0.7 * len(word_set_smooth)))
#     else:
#         str2 = word_dict_ham_smooth[word]
#         smooth_ham_prop = (word_dict_ham_smooth[word] + 0.7)/ (count_ham_smooth + 0.7 * len(word_set_smooth))
#
#     if word_dict_spam_smooth.get(word) == None:
#         str4 = 0
#         smooth_spam_prop = (0.7) / (count_spam_smooth + 0.7 * len(word_set_smooth))
#     else:
#         str4 = word_dict_spam_smooth[word]
#         smooth_spam_prop = (word_dict_spam_smooth.get(word) + 0.7)/ (count_spam_smooth + 0.7*len(word_set_smooth))
#
#
#     output_task1 = str(count_smooth),str(word),str(str2),str(smooth_ham_prop),str(str4),str(smooth_spam_prop)
#     model_dict_smooth[word]=[str2,smooth_ham_prop,str4,smooth_spam_prop]
#     # outstr="  ".join(list(output_task1))
#     # output_file_.writelines(outstr+"\r\n")
#     # print(outstr)
#     # print(count,"  ",word,ham_prop,"  ",smooth_ham_prop,"  ",spam_prop,"  ",smooth_spam_prop)
#     count_smooth += 1
# # output_file_wlf.close()
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# p_spam_smooth = num_files_spam_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_ham_smooth = num_files_ham_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_spam_list_smooth = []
# p_ham_list_smooth = []
# word_model_set_smooth = []
# count_task2_smooth = 1
# # file_model = open("/Users/PycharmProjects/model.txt")
# # contents_model = file_model.readlines()
# # for i in contents_model:
# #     word_model = re.split("  ", i)
# #     # model li de wordset
# #     word_model_set.append(word_model[1])
# count_self = 0
# # print(model_dict)
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test_smooth = []
# spam_score_smooth = 1
# ham_score_smooth = 1
#
# #
# # dict_I = {}
# # for word in word_dict_smooth:
# #     if word_dict_smooth[word] <= 1:
# #         continue
# #     else:
# #         dict_I[word] = word_dict_smooth[word]
#
# output_file_task2_smooth = ""
# output_file_task2_smooth = open("./smooth0.7-result.txt","w")
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_smooth(file)
#     score_spam_smooth = math.log10(p_spam_smooth)
#     score_ham_smooth = math.log10(p_ham_smooth)
#     score_deno_smooth = 0
#     for word in sorted(wordset_test_smooth):
#         if not word in model_dict_smooth:
#             continue
#         else:
#             score_ham_smooth += math.log10(model_dict_smooth[word][1])
#             score_spam_smooth += math.log10(model_dict_smooth[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_smooth > score_spam_smooth:
#         hamORspam_smooth = "ham"
#     else:
#         hamORspam_smooth = "spam"
#     if file.find("spam")>=0:
#         correct_classification_smooth = "spam"
#     else:
#         correct_classification_smooth = "ham"
#     if hamORspam_smooth == correct_classification_smooth:
#         result_smooth = "right"
#         if hamORspam_smooth == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_smooth = "wrong"
#         if hamORspam_smooth == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_smooth = str(count_task2_smooth), str(file), str(hamORspam_smooth), str(score_ham_smooth), str(score_spam_smooth), str(correct_classification_smooth), str(result_smooth)
#     outstr_task2_smooth = "  ".join(list(output_task2_smooth))
#     output_file_task2_smooth.writelines(outstr_task2_smooth + "\r\n")
#     count_task2_smooth += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append("smooth 0.7")
# output_file_task2_smooth.close()
#
# ####### smooth 0.8
# num_files_spam_smooth = 0
# num_files_ham_smooth = 0
# count_ham_smooth = 0
# num_ham_smooth = 0
# count_spam_smooth = 0
# num_spam_smooth = 0
# count_word_dic = 0
# count_smooth = 1
# ham_prop_smooth = None
# spam_prop_smooth = None
# word_smooth = []
# word_set_smooth = []
# word_dict_smooth = {}
# word_dict_spam_smooth = {}
# word_dict_ham_smooth = {}
# model_dict_smooth = {}
# wordset_test_smooth = []
# def no_preprocess_smooth(files):
#     global num_files_ham_smooth
#     global num_files_spam_smooth
#     global word_set_smooth
#     global word_dict_smooth
#     global word_dict_ham_smooth
#     global word_dict_spam_smooth
#     for i in files:
#         if i[6] == "s":
#             num_files_spam_smooth += 1
#         elif i[6] == "h":
#             num_files_ham_smooth += 1
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
#                 if word not in word_dict_smooth:
#                     word_set_smooth.append(word)
#                     word_dict_smooth[word] = 1
#                 elif word in word_dict_smooth:
#                     word_dict_smooth[word] += 1
#                 if i[6] == "s":
#                     if word not in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] = 1
#                     elif word in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] += 1
#                 elif i[6] == "h":
#                     if word not in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] = 1
#                     elif word in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] += 1
#
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test = []
# spam_score = 1
# ham_score = 1
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# no_preprocess_smooth(files)
# for word_ham in word_dict_ham_smooth:
#     count_ham_smooth += word_dict_ham_smooth[word_ham]
#     num_ham_smooth += 1
#
# for word_spam in word_dict_spam_smooth:
#     count_spam_smooth += word_dict_spam_smooth[word_spam]
#     num_spam_smooth += 1
#
# for word in sorted(word_set_smooth):
#     if word_dict_ham_smooth.get(word) == None:
#         str2 = 0
#         smooth_ham_prop = (0.8) / (count_ham_smooth + (0.8 * len(word_set_smooth)))
#     else:
#         str2 = word_dict_ham_smooth[word]
#         smooth_ham_prop = (word_dict_ham_smooth[word] + 0.8)/ (count_ham_smooth + 0.8 * len(word_set_smooth))
#
#     if word_dict_spam_smooth.get(word) == None:
#         str4 = 0
#         smooth_spam_prop = (0.8) / (count_spam_smooth + 0.8 * len(word_set_smooth))
#     else:
#         str4 = word_dict_spam_smooth[word]
#         smooth_spam_prop = (word_dict_spam_smooth.get(word) + 0.8)/ (count_spam_smooth + 0.8*len(word_set_smooth))
#
#
#     output_task1 = str(count_smooth),str(word),str(str2),str(smooth_ham_prop),str(str4),str(smooth_spam_prop)
#     model_dict_smooth[word]=[str2,smooth_ham_prop,str4,smooth_spam_prop]
#     # outstr="  ".join(list(output_task1))
#     # output_file_.writelines(outstr+"\r\n")
#     # print(outstr)
#     # print(count,"  ",word,ham_prop,"  ",smooth_ham_prop,"  ",spam_prop,"  ",smooth_spam_prop)
#     count_smooth += 1
# # output_file_wlf.close()
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# p_spam_smooth = num_files_spam_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_ham_smooth = num_files_ham_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_spam_list_smooth = []
# p_ham_list_smooth = []
# word_model_set_smooth = []
# count_task2_smooth = 1
# # file_model = open("/Users/PycharmProjects/model.txt")
# # contents_model = file_model.readlines()
# # for i in contents_model:
# #     word_model = re.split("  ", i)
# #     # model li de wordset
# #     word_model_set.append(word_model[1])
# count_self = 0
# # print(model_dict)
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test_smooth = []
# spam_score_smooth = 1
# ham_score_smooth = 1
#
# #
# # dict_I = {}
# # for word in word_dict_smooth:
# #     if word_dict_smooth[word] <= 1:
# #         continue
# #     else:
# #         dict_I[word] = word_dict_smooth[word]
#
# output_file_task2_smooth = ""
# output_file_task2_smooth = open("./smooth0.8-result.txt","w")
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_smooth(file)
#     score_spam_smooth = math.log10(p_spam_smooth)
#     score_ham_smooth = math.log10(p_ham_smooth)
#     score_deno_smooth = 0
#     for word in sorted(wordset_test_smooth):
#         if not word in model_dict_smooth:
#             continue
#         else:
#             score_ham_smooth += math.log10(model_dict_smooth[word][1])
#             score_spam_smooth += math.log10(model_dict_smooth[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_smooth > score_spam_smooth:
#         hamORspam_smooth = "ham"
#     else:
#         hamORspam_smooth = "spam"
#     if file.find("spam")>=0:
#         correct_classification_smooth = "spam"
#     else:
#         correct_classification_smooth = "ham"
#     if hamORspam_smooth == correct_classification_smooth:
#         result_smooth = "right"
#         if hamORspam_smooth == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_smooth = "wrong"
#         if hamORspam_smooth == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_smooth = str(count_task2_smooth), str(file), str(hamORspam_smooth), str(score_ham_smooth), str(score_spam_smooth), str(correct_classification_smooth), str(result_smooth)
#     outstr_task2_smooth = "  ".join(list(output_task2_smooth))
#     output_file_task2_smooth.writelines(outstr_task2_smooth + "\r\n")
#     count_task2_smooth += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append("smooth 0.8")
# output_file_task2_smooth.close()
#
# ####### smooth 0.9
# num_files_spam_smooth = 0
# num_files_ham_smooth = 0
# count_ham_smooth = 0
# num_ham_smooth = 0
# count_spam_smooth = 0
# num_spam_smooth = 0
# count_word_dic = 0
# count_smooth = 1
# ham_prop_smooth = None
# spam_prop_smooth = None
# word_smooth = []
# word_set_smooth = []
# word_dict_smooth = {}
# word_dict_spam_smooth = {}
# word_dict_ham_smooth = {}
# model_dict_smooth = {}
# wordset_test_smooth = []
# def no_preprocess_smooth(files):
#     global num_files_ham_smooth
#     global num_files_spam_smooth
#     global word_set_smooth
#     global word_dict_smooth
#     global word_dict_ham_smooth
#     global word_dict_spam_smooth
#     for i in files:
#         if i[6] == "s":
#             num_files_spam_smooth += 1
#         elif i[6] == "h":
#             num_files_ham_smooth += 1
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
#                 if word not in word_dict_smooth:
#                     word_set_smooth.append(word)
#                     word_dict_smooth[word] = 1
#                 elif word in word_dict_smooth:
#                     word_dict_smooth[word] += 1
#                 if i[6] == "s":
#                     if word not in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] = 1
#                     elif word in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] += 1
#                 elif i[6] == "h":
#                     if word not in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] = 1
#                     elif word in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] += 1
#
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test = []
# spam_score = 1
# ham_score = 1
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# no_preprocess_smooth(files)
# for word_ham in word_dict_ham_smooth:
#     count_ham_smooth += word_dict_ham_smooth[word_ham]
#     num_ham_smooth += 1
#
# for word_spam in word_dict_spam_smooth:
#     count_spam_smooth += word_dict_spam_smooth[word_spam]
#     num_spam_smooth += 1
#
# for word in sorted(word_set_smooth):
#     if word_dict_ham_smooth.get(word) == None:
#         str2 = 0
#         smooth_ham_prop = (0.9) / (count_ham_smooth + (0.9 * len(word_set_smooth)))
#     else:
#         str2 = word_dict_ham_smooth[word]
#         smooth_ham_prop = (word_dict_ham_smooth[word] + 0.9)/ (count_ham_smooth + 0.9 * len(word_set_smooth))
#
#     if word_dict_spam_smooth.get(word) == None:
#         str4 = 0
#         smooth_spam_prop = (0.9) / (count_spam_smooth + 0.9 * len(word_set_smooth))
#     else:
#         str4 = word_dict_spam_smooth[word]
#         smooth_spam_prop = (word_dict_spam_smooth.get(word) + 0.9)/ (count_spam_smooth + 0.9*len(word_set_smooth))
#
#
#     output_task1 = str(count_smooth),str(word),str(str2),str(smooth_ham_prop),str(str4),str(smooth_spam_prop)
#     model_dict_smooth[word]=[str2,smooth_ham_prop,str4,smooth_spam_prop]
#     # outstr="  ".join(list(output_task1))
#     # output_file_.writelines(outstr+"\r\n")
#     # print(outstr)
#     # print(count,"  ",word,ham_prop,"  ",smooth_ham_prop,"  ",spam_prop,"  ",smooth_spam_prop)
#     count_smooth += 1
# # output_file_wlf.close()
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# p_spam_smooth = num_files_spam_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_ham_smooth = num_files_ham_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_spam_list_smooth = []
# p_ham_list_smooth = []
# word_model_set_smooth = []
# count_task2_smooth = 1
# # file_model = open("/Users/PycharmProjectsmodel.txt")
# # contents_model = file_model.readlines()
# # for i in contents_model:
# #     word_model = re.split("  ", i)
# #     # model li de wordset
# #     word_model_set.append(word_model[1])
# count_self = 0
# # print(model_dict)
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test_smooth = []
# spam_score_smooth = 1
# ham_score_smooth = 1
#
# #
# # dict_I = {}
# # for word in word_dict_smooth:
# #     if word_dict_smooth[word] <= 1:
# #         continue
# #     else:
# #         dict_I[word] = word_dict_smooth[word]
#
# output_file_task2_smooth = ""
# output_file_task2_smooth = open("./smooth0.9-result.txt","w")
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_smooth(file)
#     score_spam_smooth = math.log10(p_spam_smooth)
#     score_ham_smooth = math.log10(p_ham_smooth)
#     score_deno_smooth = 0
#     for word in sorted(wordset_test_smooth):
#         if not word in model_dict_smooth:
#             continue
#         else:
#             score_ham_smooth += math.log10(model_dict_smooth[word][1])
#             score_spam_smooth += math.log10(model_dict_smooth[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_smooth > score_spam_smooth:
#         hamORspam_smooth = "ham"
#     else:
#         hamORspam_smooth = "spam"
#     if file.find("spam")>=0:
#         correct_classification_smooth = "spam"
#     else:
#         correct_classification_smooth = "ham"
#     if hamORspam_smooth == correct_classification_smooth:
#         result_smooth = "right"
#         if hamORspam_smooth == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_smooth = "wrong"
#         if hamORspam_smooth == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_smooth = str(count_task2_smooth), str(file), str(hamORspam_smooth), str(score_ham_smooth), str(score_spam_smooth), str(correct_classification_smooth), str(result_smooth)
#     outstr_task2_smooth = "  ".join(list(output_task2_smooth))
#     output_file_task2_smooth.writelines(outstr_task2_smooth + "\r\n")
#     count_task2_smooth += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append("smooth 0.9")
# output_file_task2_smooth.close()
#
#
# ####### smooth 1
# num_files_spam_smooth = 0
# num_files_ham_smooth = 0
# count_ham_smooth = 0
# num_ham_smooth = 0
# count_spam_smooth = 0
# num_spam_smooth = 0
# count_word_dic = 0
# count_smooth = 1
# ham_prop_smooth = None
# spam_prop_smooth = None
# word_smooth = []
# word_set_smooth = []
# word_dict_smooth = {}
# word_dict_spam_smooth = {}
# word_dict_ham_smooth = {}
# model_dict_smooth = {}
# wordset_test_smooth = []
# def no_preprocess_smooth(files):
#     global num_files_ham_smooth
#     global num_files_spam_smooth
#     global word_set_smooth
#     global word_dict_smooth
#     global word_dict_ham_smooth
#     global word_dict_spam_smooth
#     for i in files:
#         if i[6] == "s":
#             num_files_spam_smooth += 1
#         elif i[6] == "h":
#             num_files_ham_smooth += 1
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
#                 if word not in word_dict_smooth:
#                     word_set_smooth.append(word)
#                     word_dict_smooth[word] = 1
#                 elif word in word_dict_smooth:
#                     word_dict_smooth[word] += 1
#                 if i[6] == "s":
#                     if word not in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] = 1
#                     elif word in word_dict_spam_smooth:
#                         word_dict_spam_smooth[word] += 1
#                 elif i[6] == "h":
#                     if word not in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] = 1
#                     elif word in word_dict_ham_smooth:
#                         word_dict_ham_smooth[word] += 1
#
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test = []
# spam_score = 1
# ham_score = 1
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# no_preprocess_smooth(files)
# for word_ham in word_dict_ham_smooth:
#     count_ham_smooth += word_dict_ham_smooth[word_ham]
#     num_ham_smooth += 1
#
# for word_spam in word_dict_spam_smooth:
#     count_spam_smooth += word_dict_spam_smooth[word_spam]
#     num_spam_smooth += 1
#
# for word in sorted(word_set_smooth):
#     if word_dict_ham_smooth.get(word) == None:
#         str2 = 0
#         smooth_ham_prop = (1) / (count_ham_smooth + (1 * len(word_set_smooth)))
#     else:
#         str2 = word_dict_ham_smooth[word]
#         smooth_ham_prop = (word_dict_ham_smooth[word] + 1)/ (count_ham_smooth + 1 * len(word_set_smooth))
#
#     if word_dict_spam_smooth.get(word) == None:
#         str4 = 0
#         smooth_spam_prop = (1) / (count_spam_smooth + 1 * len(word_set_smooth))
#     else:
#         str4 = word_dict_spam_smooth[word]
#         smooth_spam_prop = (word_dict_spam_smooth.get(word) + 1)/ (count_spam_smooth + 1*len(word_set_smooth))
#
#
#     output_task1 = str(count_smooth),str(word),str(str2),str(smooth_ham_prop),str(str4),str(smooth_spam_prop)
#     model_dict_smooth[word]=[str2,smooth_ham_prop,str4,smooth_spam_prop]
#     # outstr="  ".join(list(output_task1))
#     # output_file_.writelines(outstr+"\r\n")
#     # print(outstr)
#     # print(count,"  ",word,ham_prop,"  ",smooth_ham_prop,"  ",spam_prop,"  ",smooth_spam_prop)
#     count_smooth += 1
# # output_file_wlf.close()
#
# def task2_no_preprocess_smooth(file):
#     global wordset_test_smooth
#     wordset_test_smooth = []
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
#             if word not in wordset_test_smooth:
#                 # print(word_set)
#                 wordset_test_smooth.append(word)
#
# p_spam_smooth = num_files_spam_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_ham_smooth = num_files_ham_smooth/(num_files_spam_smooth + num_files_ham_smooth)
# p_spam_list_smooth = []
# p_ham_list_smooth = []
# word_model_set_smooth = []
# count_task2_smooth = 1
# # file_model = open("/Users/PycharmProjects/model.txt")
# # contents_model = file_model.readlines()
# # for i in contents_model:
# #     word_model = re.split("  ", i)
# #     # model li de wordset
# #     word_model_set.append(word_model[1])
# count_self = 0
# # print(model_dict)
#
# path_test = '/Users/Downloads/test'
# files_test=os.listdir(path_test)
# wordset_test_smooth = []
# spam_score_smooth = 1
# ham_score_smooth = 1
#
# #
# # dict_I = {}
# # for word in word_dict_smooth:
# #     if word_dict_smooth[word] <= 1:
# #         continue
# #     else:
# #         dict_I[word] = word_dict_smooth[word]
#
# output_file_task2_smooth = ""
# output_file_task2_smooth = open("./smooth1.0-result.txt","w")
# tp = 0
# fp = 0
# fn = 0
# tn = 0
# for file in files_test:
#     print(file)
#     # task2_preprocess(file)
#     task2_no_preprocess_smooth(file)
#     score_spam_smooth = math.log10(p_spam_smooth)
#     score_ham_smooth = math.log10(p_ham_smooth)
#     score_deno_smooth = 0
#     for word in sorted(wordset_test_smooth):
#         if not word in model_dict_smooth:
#             continue
#         else:
#             score_ham_smooth += math.log10(model_dict_smooth[word][1])
#             score_spam_smooth += math.log10(model_dict_smooth[word][3])
#     # final_ham = score_ham/score_deno
#     # final_spam = score_spam/score_deno
#     if score_ham_smooth > score_spam_smooth:
#         hamORspam_smooth = "ham"
#     else:
#         hamORspam_smooth = "spam"
#     if file.find("spam")>=0:
#         correct_classification_smooth = "spam"
#     else:
#         correct_classification_smooth = "ham"
#     if hamORspam_smooth == correct_classification_smooth:
#         result_smooth = "right"
#         if hamORspam_smooth == "ham":
#             tp += 1
#         else:
#             tn += 1
#     else:
#         result_smooth = "wrong"
#         if hamORspam_smooth == "ham":
#             fp += 1
#         else:
#             fn += 1
#     output_task2_smooth = str(count_task2_smooth), str(file), str(hamORspam_smooth), str(score_ham_smooth), str(score_spam_smooth), str(correct_classification_smooth), str(result_smooth)
#     outstr_task2_smooth = "  ".join(list(output_task2_smooth))
#     output_file_task2_smooth.writelines(outstr_task2_smooth + "\r\n")
#     count_task2_smooth += 1
# acc = (tp + tn) / (tp + tn + fn + fp)
# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# y_list.append([acc,precision,recall])
# x_list.append("smooth 1.0")
# output_file_task2_smooth.close()
#
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
