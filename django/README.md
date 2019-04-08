
# Django

ここにシンプルなサンプルがあったので使ってみる(Django 2ではそのままでは動かなかったが)
https://qiita.com/podhmo/items/b6385fde9e32bbb8d57b

```
execute_from_command_line(sys.argv)
```

はCloud Functionsでは使えないので書き換える。

```
management.call_command
```
