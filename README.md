# PTT 詞雲產生器

## Intro

![demo](demo.png)

補眠睡醒看到股板這篇文章 - [[其他] 推薦忙碌人看股板的方法](https://www.ptt.cc/bbs/Stock/M.1609164072.A.C2A.html)
參考 PTT allmwh 大大的一部分 [code](https://gist.github.com/allmwh/0a1842350874c9733ac21f2fe2aacb57)

想想也不只能放在股板使用，乾脆做成詞雲產生器

## Usage

### Python 3.7

Use `pipenv`

```
pipenv install
```

Download and import [ptt-web-crawler](https://github.com/jwlin/ptt-web-crawler)

修改 `src/run.py` 中的 `board` 和 `article_id` 變數，如

```python
board = 'Stock'
article_id = 'M.1609135202.A.69E'
```

執行
```
python src/run.py
```

# Ref
- [victorgau
/
wordcloud](https://github.com/victorgau/wordcloud)
