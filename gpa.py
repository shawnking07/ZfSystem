def average(data_list):
    # 计算均分
    score_sum = 0
    weight_sum = 0
    weight_score_sum = 0
    for i in data_list:
        print(i['name'] + " " + i['score'] + " " + i['weight'])
        score = convert_score(i['score'])
        weight = float(i['weight'])
        score_sum += score
        weight_sum += weight
        weight_score_sum += score * weight
    w_avg = weight_score_sum / weight_sum
    avg = score_sum / len(data_list)

    print("加权平均： ")
    print(w_avg)
    print("算术平均: ")
    print(avg)


def convert_score(level):
    if level == "优秀":
        return 90
    elif level == '良好':
        return 80
    elif level == "中等":
        return 70
    elif level == "合格":
        return 60
    else:
        return int(level)


def convert_gpa(score):
    if score >= 90:
        return 4
    elif score >= 80:
        return 3
    elif score >= 70:
        return 2
    elif score >= 60:
        return 1
    else:
        return 0

