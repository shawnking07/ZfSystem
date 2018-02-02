import urllib.parse
from pyquery import PyQuery as pq

from login import s_login


def query_score(uid, password, url):
    name, session = s_login(uid, password, url, 10)
    new_url = url + "xscjcx.aspx?xh=" + uid + "&xm=" + urllib.parse.quote(
        str(name).encode('gb2312')) + "&gnmkdm=N121605"
    headers = {
        'Referer': url + "xs_main.aspx?xh=" + uid
    }

    r = session.get(new_url, headers=headers)
    d = pq(r.text)
    view_state = d("input[name='__VIEWSTATE']").val()
    headers['Referer'] = new_url
    params = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': view_state,
        'hidLanguage': '',
        'btn_zcj': '%C0%FA%C4%EA%B3%C9%BC%A8',
        'ddlXN': '',
        'ddlXQ': '',
        'ddl_kcxz': ''
    }
    r = session.post(new_url, headers=headers, data=params)
    r.encoding = "gb2312"
    d = pq(r.text)
    # print(r.text)
    data_list = []
    lines = d("table.datelist tr")
    for i in lines.items():
        subject_data = {'name': pq(i)("td:eq(3)").text(), 'weight': pq(i)("td:eq(6)").text(),
                        'score': pq(i)("td:eq(8)").text()}
        data_list.append(subject_data)
    del data_list[0]
    # print(data_list)

    # 计算均分
    score_sum = 0
    weight_sum = 0
    weight_score_sum = 0
    for i in data_list:
        print(i['name']+" "+i['score']+" "+i['weight'])
        if i['score'] == "优秀":
            score = 90
        elif i['score'] == '良好':
            score = 80
        elif i['score'] == "中等":
            score = 70
        elif i['score'] == "合格":
            score = 60
        else:
            score = int(i['score'])
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
