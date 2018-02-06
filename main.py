from query_score import query_score
from gpa import average

uid = "学号"
password = "密码"
url = "http://***/"

if __name__ == '__main__':
    data_list = query_score(uid, password, url)
    average(data_list)
