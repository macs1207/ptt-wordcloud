from wordcloud.wordcloud import FONT_PATH
from PttWebCrawler.crawler import *
from wordcloud import WordCloud
import numpy as np
import jieba
import multidict
import json
import re


board = 'Stock'
article_id = 'M.1609135202.A.69E'


class PttWordCloud:
    FONT_PATH = "./fonts/NotoSansTC-Bold.otf"
    DICT_PATH = "./data/dict.txt.big"
    SYMBOLS = ['!', '?', ',', '~']

    def __init__(self, board, article_id):
        self.board = board
        self.article_id = article_id

        jieba.set_dictionary(self.DICT_PATH)

    def get_keywords(self):
        c = PttWebCrawler(as_lib=True)
        filename = c.parse_article(board=self.board,
                                   article_id=self.article_id)
        f = open(filename, encoding="utf-8")
        article = json.load(f)

        return self._parse(article)

    def _parse(self, article):
        comments_str = ' '.join([message['push_content'] for message in article['messages']])
        comments_str = re.sub(r'http\S+', '', comments_str)
        for filter in self.SYMBOLS:
            comments_str = comments_str.replace(filter, ' ')

        words = jieba.cut(comments_str)
        full_terms_dict = multidict.MultiDict()
        tmp_dict = {}

        for w in words:
            if len(w) >= 2:
                val = tmp_dict.get(w, 0)
                tmp_dict[w] = val + 1

        for key in tmp_dict:
            full_terms_dict.add(key, tmp_dict[key])

        return full_terms_dict

    def make_image(self, filename, text):
        wc = WordCloud(width=1920, height=1080, font_path=self.FONT_PATH, background_color="black", max_words=500)
        wc.generate_from_frequencies(text)
        wc.to_file(filename)



if __name__ == "__main__":
    p = PttWordCloud(board, article_id)
    p.make_image(f'{board}-{article_id}.png', p.get_keywords())
