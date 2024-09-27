import random 
import os

correct_file_path = "./syntax_checking_correct"
correct_file_names = [
    "syntax_checking_FMA_correct.txt",
    "syntax_checking_GO_correct.txt",
    "syntax_checking_MarineTLO_correct.txt",
    "syntax_checking_Music_correct.txt",
    "syntax_checking_OBI_correct.txt"
] 

wrong_file_path = "./syntax_checking_wrong"
wrong_file_names = [
    "syntax_checking_FMA_wrong.txt",
    "syntax_checking_GO_wrong.txt",
    "syntax_checking_MarineTLO_wrong.txt",
    "syntax_checking_Music_wrong.txt",
    "syntax_checking_OBI_wrong.txt"
] 

test_path = "./test"
test_file_names = [
    "test_FMA.txt",
    "test_checking_GO.txt",
    "test_checking_MarineTLO.txt",
    "test_checking_Music.txt",
    "test_checking_OBI.txt"
] 

test_truth_file_names = [
    "test_truth_FMA.txt",
    "test_truth_checking_GO.txt",
    "test_truth_checking_MarineTLO.txt",
    "test_truth_checking_Music.txt",
    "test_truth_checking_OBI.txt"
] 


for i in range(5):
    correct_axioms, wrong_axioms = [], []
    with open(os.path.join(correct_file_path, correct_file_names[i]), 'r', encoding="UTF-8") as f1:
        axiom_lines = f1.readlines()
        for axiom in axiom_lines:
            correct_axioms.append(axiom.strip("\n"))
    with open(os.path.join(wrong_file_path, wrong_file_names[i]), 'r', encoding="UTF-8") as f2:
        axiom_lines = f2.readlines()
        for axiom in axiom_lines:
            axiom = (axiom.split("\t"))[0]
            wrong_axioms.append(axiom.strip("\n"))

    len_cor = len(correct_axioms)
    len_wro = len(wrong_axioms)
    #print(len_cor, len_wro)

    random.shuffle(correct_axioms)
    random.shuffle(wrong_axioms)

    p_cor, p_wro = 0, 0
    test_list, test_list_truth = [], []

    while p_cor < len_cor and p_wro < len_wro:
            a = random.random()
            if a < 0.5:  # input correct axiom
                test_list.append(correct_axioms[p_cor])
                test_list_truth.append(True)
                p_cor = p_cor + 1
            else:        # input wrong axiom
                test_list.append(wrong_axioms[p_wro])
                test_list_truth.append(False)
                p_wro = p_wro + 1

    while p_cor < len_cor:
        test_list.append(correct_axioms[p_cor])
        test_list_truth.append(True)
        p_cor = p_cor + 1

    while p_wro < len_wro:
        test_list.append(wrong_axioms[p_wro])
        test_list_truth.append(False)
        p_wro = p_wro + 1


    with open(os.path.join(test_path, test_file_names[i]), "w", encoding="UTF-8") as f1:
        with open(os.path.join(test_path, test_truth_file_names[i]), "w", encoding="UTF-8") as f2:
            for i in range(len_cor+len_wro):
                axiom = test_list[i]
                syntax_truth = test_list_truth[i]
                f1.write(axiom)
                f1.write("\n")
                f2.write(str(syntax_truth)) 
                f2.write("\n")


