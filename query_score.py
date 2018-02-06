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
    payload = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': view_state,
        'hidLanguage': '',
        'btn_zcj': '%C0%FA%C4%EA%B3%C9%BC%A8',
        'ddlXN': '',
        'ddlXQ': '',
        'ddl_kcxz': ''
    }
    r = session.post(new_url, headers=headers, data=payload)
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
    return data_list
