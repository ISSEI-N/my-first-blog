# fromは〇〇のimportで〇〇をインポートする
# 下記の場合はdjango.dbからmodelsをインポート
from django.db import models
from django.utils import timezone

# Postモデルの作成（オブジェクト）
# models.ModelでDjangoがデータベースに保存するべきものとわかるようになっている
class Post(models.Model):
    # 他のモデルとの結びつけ
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    # titleの文字数の制限
    title = models.CharField(max_length = 200)
    # textの文字数の制限なし
    text = models.TextField()
    # Postを投稿した日付
    created_date = models.DateTimeField(default = timezone.now)
    # 公開された日付
    published_date = models.DateTimeField(blank = True,
                                          null = True)
    
    # Postを投稿するメソッド
    def publish(self):
        self.published_date = timezone.now()
        self.save
    # タイトルの文字をストリングに修正する
    def __str__(self):
        return self.title





