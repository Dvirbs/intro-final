#################################################################
# FILE : cartoonify.py
# WRITER : Dvir , Dvirbs , 204270243
# EXERCISE : intro2cs2 ex6 2020
# DESCRIPTION: search engine
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES:
#################################################################
import pickle
import typing
import requests
import bs4
import urllib.parse
import sys
from typing import List

Small_index = 'C:/Google One/University/Third year/Intro/week_6/ex6/ex6_project/small_index.txt'
Base_url = 'https://www.cs.huji.ac.il/~intro2cs1/ex6/wiki/Tom_Riddle.html'
Url = 'https://www.cs.huji.ac.il/~intro2cs1/ex6/wiki/Harry_Potter.html'


# section A


def collect_small_index_data(small_index) -> List:
    """
    collecting the data of small list txt file to a list of names
    :param small_index: the TXT file!!!!!
    :return: list of names in the small index
    """
    small_index_names = list()
    with open(small_index) as f:
        line = f.readline()
        small_index_names.append(line[:-1])
        while line:
            line = f.readline()
            if line.endswith('\n'):
                small_index_names.append(line[:-1])
            else:
                small_index_names.append(line[:])
                return small_index_names
    return small_index_names


def dic_page_name_url(base_url: str, index_file: List) -> typing.Dict:
    """
    collecting file names from index_file and base_url and connecting them together to dic
    :param base_url: the base url
    :param index_file: list!! of index file with the names ---->we get it from  collect_small_index_data   function
    :return: dic that the keys is names in index_file and values is full url
    """
    dic = dict()
    pickle = list()
    file_names_list = list()
    for file_name in index_file:
        full_url = urllib.parse.urljoin(base_url, file_name)
        dic[file_name] = full_url
    return dic


def lst_href_names(url):
    """
    getting from the url all the href value
    :param url: the url that we get from it all the href_names
    :return: href list in the url
    """
    href_list = list()
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for p in soup.find_all("p"):
        for link in p.find_all("a"):
            target = link.get("href")
            if target != '':
                href_list.append(target)
    return href_list


def traffic_dict(small_index, base_url) -> typing.Dict:
    """

    :return:
    """
    small_index_names = collect_small_index_data(small_index)
    dict_page_name_url = dic_page_name_url(base_url, small_index_names)
    traffic_dict = dict()
    count_dic = dict()
    for name in dict_page_name_url:
        href_links_in_name_url = lst_href_names(dict_page_name_url[name])
        for index_name in small_index_names:
            count = href_links_in_name_url.count(index_name)
            count_dic[index_name] = count
        traffic_dict[name] = count_dic
        count_dic = dict()
    return traffic_dict


# section B


def total_href(values: List):
    """
    getting list of keys names in dict and return the sum of all values
    :param values: dic with names and values(int)
    :return: sum of values
    """
    if len(values) == 1:
        return values[0]
    else:
        return values[-1] + total_href(values[:-1])


def tot_pop_calculation_to_add(last_iter_r_sec_name, sec_name, head_name, _traffic_dict_, sec_name_values):
    """

    :param last_iter_r_sec_name:
    :param sec_name:
    :param head_name:
    :param _traffic_dict_:
    :param sec_name_values:
    :return:
    """
    sec_name_pop = last_iter_r_sec_name
    sec_name_head_link = _traffic_dict_[sec_name][head_name]
    tot_href = total_href(sec_name_values)
    pop = sec_name_pop * (sec_name_head_link / tot_href)
    return pop


def tot_pop_calculation_to_subtract(last_iter_r_head_name, sec_name, head_name, _traffic_dict_, head_name_links) -> int:
    """

    :param last_iter_r_head_name:
    :param sec_name:
    :param head_name:
    :param _traffic_dict_:
    :param head_name_links:
    :return:
    """
    sec_name_pop = last_iter_r_head_name
    head_to_second_link = _traffic_dict_[head_name][sec_name]
    tot_href = total_href(head_name_links)
    pop_calculation = sec_name_pop * (head_to_second_link / tot_href)
    return pop_calculation


def pop_zero_iter(small_index_names: List) -> dict:
    r = dict()
    for name in small_index_names:
        r[name] = 0
    return r


def pop_ones_iter(small_index_names: List) -> dict:
    r = dict()
    for name in small_index_names:
        r[name] = 1
    return r


def pop_first_iter(small_index: List, _traffic_dict_) -> dict:
    last_iter_r = pop_zero_iter(small_index)
    current_iter_r = dict()
    for head_name in _traffic_dict_.keys():
        head_name_links = list(_traffic_dict_[head_name].values())
        popularity = 0
        for sec_name in _traffic_dict_[head_name].keys():
            if sec_name != head_name:
                sec_name_links = list(_traffic_dict_[sec_name].values())
                popularity += tot_pop_calculation_to_add(last_iter_r[sec_name], sec_name, head_name,
                                                         _traffic_dict_, sec_name_links)
                popularity -= tot_pop_calculation_to_subtract(last_iter_r[head_name], sec_name, head_name,
                                                              _traffic_dict_, head_name_links)
                if popularity < 0:
                    print('\nsomething want wrong, pop value is minus.')
                    print('pop value', popularity)
                current_iter_r[head_name] = popularity
    return current_iter_r


def pop_first_iteration(small_index: List, _traffic_dict_) -> dict:
    current_r = dict()
    for head_name in _traffic_dict_:
        total_links_of_head_name = list(_traffic_dict_[head_name].values())
        popularity = 0
        for sec_name in _traffic_dict_[head_name].keys():
            if sec_name != head_name:
                total_links_of_sec_name = list(_traffic_dict_[sec_name].values())
                popularity += 1 * (_traffic_dict_[sec_name][head_name] / total_href(total_links_of_sec_name))
                popularity -= 1 * (_traffic_dict_[head_name][sec_name] / total_href(total_links_of_head_name))
        if popularity < 0:
            print('\nsomething want wrong, pop value is minus.')
            print('pop value', popularity)
        current_r[head_name] = popularity
    return current_r


def another_iteration(small_index: List, _traffic_dict_, last_iter_r: dict) -> dict:
    """
    doing another iteration for page rank that in this iteration we get the trafic dic from the last iteration
    and update the current r dict
    :param last_iter_r: last iteration dict
    :param _traffic_dict_: the traffic dic from the last iteration
    :return: current iteration r dict
    """
    current_iter_r = pop_zero_iter(small_index)
    for head_name in _traffic_dict_.keys():
        head_name_links = list(_traffic_dict_[head_name].values())
        popularity = last_iter_r[head_name]
        for sec_name in _traffic_dict_[head_name].keys():
            if sec_name != head_name:
                sec_name_links = list(_traffic_dict_[sec_name].values())
                popularity += tot_pop_calculation_to_add(last_iter_r[sec_name], sec_name, head_name,
                                                         _traffic_dict_, sec_name_links)
                popularity -= tot_pop_calculation_to_subtract(last_iter_r[head_name], sec_name, head_name,
                                                              _traffic_dict_, head_name_links)
        if popularity < 0:
            print('\nsomething want wrong, pop value is minus.')
            print('pop value', popularity)
        current_iter_r[head_name] += popularity
    return current_iter_r


def page_rank(N: int, _traffic_dict_: typing.Dict) -> typing.Dict:
    """
    creating page rank of the pages in the small index
    :param N:
    :param _traffic_dict_:
    :return:
    """
    small_index_names = list(_traffic_dict_.keys())
    r = pop_ones_iter(small_index_names)
    for iteration in range(2, N+1):
        r = another_iteration(small_index_names, _traffic_dict_, r)
    return r


# section C


def page_content(url):
    """
    getting from the url all the words
    :param url: the url that we get from it all the href_names
    :return: return list of all the words in the url page
    """
    word_list = list()
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for p in soup.find_all("p"):
        content = p.text
        content_word_list = content.split(' ')
        word_list += content_word_list
    return word_list


def words_dictionary(small_index, base_url):
    """
    getting html and creating dic of word keys and dictionary values of page and count of word in page
    :param small_index: txt file that have list of names of the different internet pages
    :return: dictionary values of page and count of word in page
    """
    word_dic = dict()
    small_index_name_lst = collect_small_index_data(small_index)
    names_and_full_url_dic = dic_page_name_url(base_url, small_index_name_lst)
    for page_name in names_and_full_url_dic.keys():
        the_world_list = page_content(names_and_full_url_dic[page_name])
        for word in the_world_list:
            word = word.strip()
            if word not in word_dic.keys():
                word_dic[word] = dict()
                word_dic[word][page_name] = 1
            elif word in word_dic.keys():
                if page_name not in word_dic[word].keys():
                    word_dic[word][page_name] = 1
                if page_name in word_dic[word].keys():
                    word_dic[word][page_name] += 1
    return word_dic


# section D

# stage 1 - getting filter pages
# pre_processing:
def all_search_words(query: str) -> List:
    """
    collecting all the search words from query
    :param query: String that include all the search words separate by spacing
    :return: List of all the separate search words
    """
    search_word = query.split(' ')
    return search_word


def relevant_search_words(query: str, word_dict: typing.Dict) -> List:
    """
    collecting all the relevant search words from query
    :param query: String that include all the search words separate by spacing
    :param word_dict: the dictionary of the words
    :return: List of all the relevant separate search words
    """
    all_search_word = all_search_words(query)
    relevant = [word for word in all_search_word if word in word_dict.keys()]
    return relevant


# filter pages:
def all_filter_pages(query: str, word_dict: typing.Dict, page_rank_dic: typing.Dict) -> set:
    """
    collecting al the pages from both dics and filter them
    :param query: String that include all the search words separate by spacing
    :param word_dict: the dictionary of the words
    :param page_rank_dic: the page rank dic
    :return: set of all the pages names
    """
    rank_pages = set(page_rank_dic.keys())
    relevant_search_word = relevant_search_words(query, word_dict)
    words_pages = set()
    for word in relevant_search_word:
        words_pages = words_pages | set(word_dict[word].keys())
    all_pages = rank_pages.intersection(words_pages)
    return all_pages


# stage 2 - getting sorted pages list
# pre_processing
def filtered_pages_ranks_dic(query: str, word_dict: typing.Dict, page_rank_dic: typing.Dict) -> typing.Dict:
    """
    creating filters pages names with rank values
    :param query: String that include all the search words separate by spacing
    :param word_dict: the dictionary of the words
    :param page_rank_dic: the page rank dic
    :return: dictionary
    """
    filtered_dic = dict()
    all_pages_f = all_filter_pages(query, word_dict, page_rank_dic)
    for page_name in all_pages_f:
        filtered_dic[page_name] = page_rank_dic[page_name]
    return filtered_dic


def sorted_list(query: str, word_dict: typing.Dict, page_rank_dic: typing.Dict) -> List:
    """
    creating sorted page name link by ranks
    :param query: String that include all the search words separate by spacing
    :param word_dict: the dictionary of the words
    :param page_rank_dic: the page rank dic
    :return: List
    """
    filtered_pages_dic = filtered_pages_ranks_dic(query, word_dict, page_rank_dic)
    sorted_page_list = [k for k, v in sorted(filtered_pages_dic.items(), key=lambda v: v[1], reverse=True)]
#    sorted_page_dic = {k: v for k, v in sorted(filtered_pages_dic.items(), key=lambda v: v[1], reverse=True)}
#    print(sorted_page_dic)
    return sorted_page_list


def max_pages(query: str, word_dict: typing.Dict, page_rank_dic: typing.Dict, max_results: int) -> List:
    """
    taking the sorted list and setting it to the maximum value
    :param query: String that include all the search words separate by spacing
    :param word_dict: the dictionary of the words
    :param page_rank_dic: the page rank dic
    :param max_results: max pages results
    :return: List with correct len
    """
    sort_list = sorted_list(query, word_dict, page_rank_dic)
    if len(sort_list) <= max_results:
        return sort_list
    else:
        return sort_list[:max_results]


# stage 3 - new score pages list

#pre_prossisng
def sorted_dict(new_score_dic: typing.Dict) -> typing.Dict:
    """
    creating sorted page name link by ranks
    :param new_score_dic: the page new score rank dic
    :return: List
    """
#    sorted_page_list = [k for k, v in sorted(new_score_dic.items(), key=lambda v: v[1], reverse=True)]
    sorted_page_dic = {k: v for k, v in sorted(new_score_dic.items(), key=lambda v: v[1], reverse=True)}
    return sorted_page_dic


# re_calculate_score

def re_calculate_score(query: str, word_dict: typing.Dict, page_rank_dic: typing.Dict, max_results: int) -> List:
    """
    creating sorted page name list by new score calculate
    :param query: String that include all the search words separate by spacing
    :param word_dict: the dictionary of the words
    :param page_rank_dic: the page rank dic
    :return: List
    """
    word_list = relevant_search_words(query, word_dict)
    page_list = max_pages(query, word_dict, page_rank_dic, max_results)
    new_score_dic = dict()
    for page in page_list:
        min_appearances = -1
        for word in word_list:
            if min_appearances == -1:
                min_appearances = word_dict[word][page]
            else:
                min_appearances = min(min_appearances, word_dict[word][page])
        new_score_dic[page] = min_appearances * page_rank_dic[page]
    sorted_dic = sorted_dict(new_score_dic)
    for page in sorted_dic:
        print(page, sorted_dic[page])


# main
# if __name__ == '__main__':
#     args = sys.argv
#     if len(args) == 5:
#         if args[1] == 'crawl':                                   # section A
#             _traffic_dict_ = traffic_dict(args[3], args[2])
#             with open(args[4], 'wb') as f:
#                 pickle.dump(_traffic_dict_, f)
#         elif args[1] == 'page_rank':                               # section B
#             with open(args[4], 'rb') as f:                                     # getting _traffic_dict_ from pickle name
#                 _traffic_dict_ = pickle.load(f)
#             page_rank_dict = page_rank(int(args[2]), _traffic_dict_)
#             with open(args[4], 'wb') as f:
#                 pickle.dump(page_rank_dict, f)
#         elif args[1] == 'words_dict':                              # section C
#             word_dic = words_dictionary(args[3], args[2])
#             with open(args[4], 'wb') as f:
#                 pickle.dump(word_dic, f)
#         else:
#             sys.exit("args[1] is not correct")
#     elif len(args) == 6:                                           # section D
#         if args[1] == 'search':
#             with open(args[4], 'rb') as f:                           # pre_presses- word and page dict from pickle name
#                 word_dict = pickle.load(f)
#             with open(args[3], 'rb') as f:                           # pre_presses- word and page dict from pickle name
#                 page_rank_dic = pickle.load(f)
#             re_calculate_score(args[2], word_dict, page_rank_dic, int(args[5]))
#         else:
#             sys.exit("args[1] is not correct")
#     else:
#         sys.exit("number of arguments is not correct")


# section A - traffic dic


# Tests
# _traffic_dict_ = traffic_dict(Small_index, Base_url)
# print(_traffic_dict_)

# section B - page rank
# to = page_rank(100, traffic_dict(Small_index, Base_url))
# print(to)
# print(sum(to.values()))

# section B - pop_first_iteration
# small_index = collect_small_index_data(Small_index)
# to = pop_first_iteration(small_index, _traffic_dict_)
# print(to)
# print(sum(to.values()))


# section C - words_dictionary
# world_dic = words_dictionary(Small_index, Base_url)
# print(world_dic)


# section D - putting all together
query = 'broom wand cape'
word_dict = words_dictionary(Small_index, Base_url)
page_rank = page_rank(100, traffic_dict(Small_index, Base_url))

# stage 1
# all_the_pages = all_filter_pages(query, word_dict, page_rank)
# print(all_the_pages)
# print(len(all_the_pages))
# stage 2
# pre_prossing
# filtered_dic = filtered_names_values_dic(query, word_dict, page_rank)
# sorted_list
# sort_the_dic = sorted_list(query, word_dict, page_rank)
# print(sort_the_dic)
# # correct len list
# max_page = max_pages(query, word_dict, page_rank, 4)
# print(max_page)
# # stage 3
new_score_list = re_calculate_score(query, word_dict, page_rank, 4)
print(new_score_list)
