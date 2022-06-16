from collections import defaultdict


def solution(word, pages):
    answer = 0
    scores = []
    tag_lists = []
    for i, page in enumerate(pages):
        tag_list, basic_score = parse_page(word, page)
        scores.append([basic_score])
        tag_lists.append(tag_list)
    url_to_i = defaultdict(int)
    i_to_url = defaultdict(str)
    pointed_to_pointing_idx = defaultdict(list)
    pointing_num = defaultdict(int)
    for i, tag_list in enumerate(tag_lists):
        # print(tag_list)
        for tag in tag_list:
            if tag[:5] == '<meta' or tag[:2] == '<a':
                start_i = tag.find("https://")
                if start_i == -1:
                    continue
                url = ""
                while tag[start_i] != '"':
                    url += tag[start_i]
                    start_i += 1
                if tag[:5] == '<meta':
                    url_to_i[url] = i
                    i_to_url[i] = url
                else:
                    pointed_to_pointing_idx[url].append(i)
                    pointing_num[i] += 1
    # print(url_to_i)
    # print(i_to_url)
    # print(pointed_to_pointing_idx)
    # print(pointing_num)
    for i in range(len(scores)):
        i_url = i_to_url[i]
        pointing_idx_list = pointed_to_pointing_idx[i_url]
        total_link_socre = 0
        for pointing_idx in pointing_idx_list:
            total_link_socre += scores[pointing_idx][0] / pointing_num[pointing_idx]
        scores[i].append(total_link_socre)
        scores[i].append(i)
    scores = sorted(scores, key=lambda x: (-(x[0] + x[1]), x[2]))
    return scores[0][2]


def parse_page(word: str, page: str):
    page_len = len(page)
    i = 0
    tag_list = []
    check_word = ""
    basic_score = 0
    while i < page_len:
        if page[i] == '<':
            tag = page[i]
            i += 1
            while page[i] != '>':
                tag += page[i]
                i += 1
            tag += '>'
            tag_list.append(tag)
        else:
            if page[i].isalpha():
                check_word += page[i]
            else:
                if check_word.lower() == word.lower():
                    basic_score += 1
                check_word = ""
            i += 1
    return tag_list, basic_score


print(solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
