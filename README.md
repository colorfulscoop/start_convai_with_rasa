# 「自分だけの会話AIを作ろう！Rasaで始めるチャットボット開発」サポートページ

本リポジトリは
[Colorful Scoop](https://colorfulscoop.com)
による書籍
「自分だけの会話AIを作ろう！Rasaで始めるチャットボット開発」
のサポートサイトです。

## 内容

### src/{directory}

[src](src)下のディレクトリには、書籍の対応する章まで読み進めるとできるRasaプロジェクトを格納しています。
実装のチェックに使ってください。

| ディレクトリ | 対応する章 |
| --- | --- |
| [src/ch03](src/ch03) | 3章 |
| [src/ch04](src/ch04) | 4章 |
| [src/ch05](src/ch05) | 5章 |
| [src/ch06](src/ch06) | 6章 |

### src/index.html

[src/index.html](src/index.html)は、
Botfrontにより開発されている
[Rasa Webchat](https://github.com/botfront/rasa-webchat)
用のHTMLファイルです。

このHTMLファイルはRasa Webchatの
[Usage](https://github.com/botfront/rasa-webchat/tree/0119e94e6df7b84c3edf1db6f3be3aee7fa3db43#usage)
にしたがって作成しています。

### project_ja

[project_ja](project_ja)ディレクトリには、日本語のRasaプロジェクトのテンプレートを格納しています。

## 動作確認環境

本リポジトリは、macOS上で次のコマンドでDockerコンテナを準備して動作確認しています。

```sh
$ docker container run -v $(pwd):/work -w /work -p5005:5005 --rm -it python:3.8.13-slim-buster bash
```
