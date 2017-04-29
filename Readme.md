# Python-Sapporo Github pages

# How to generate

## Install
Pelicanを利用しています。

```sh
pip install -r requirements.txt
```

## ウェブページの更新
content以下がウェブページの元となるファイルなので、これらのファイルを編集します。

## HTMLの生成
```sh
make html
```

## HTMLの確認
```sh
make serve
```

http://localhost:8000/にアクセスして確認します。

## 公開
```sh
make github
```

## 参考
[Pelican + Markdown + GitHub Pagesで管理するブログの作り方 - blog@sotm.jp](http://blog.sotm.jp/2014/01/04/Pelican-Markdown-GithubPages-install-guide/)
