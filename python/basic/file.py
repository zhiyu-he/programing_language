# -*- coding:utf-8 -*-


FILE_PATH = 'sample.txt'


if __name__ == '__main__':
    mock_ads = [];
    with open(FILE_PATH) as f:
        for line in f:
            if len(line) < 10:
                continue
            t = eval(line)
            mock_ads.append(t)


    for ad in mock_ads:
        data = ad[11]
        import json
        d = json.loads(data)
        print type(d)
        print d
