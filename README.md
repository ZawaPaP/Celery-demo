## これは何？

Celery をローカルにて動かしてみた時のコード

### 手順

```
// .envファイルを用意
cp .env.template .env

// dockerを立ち上げ
docker compose up --build

// python実行コンテナに入る
docker exec -it [container ID] bash

// python実行コンテナでTaskを実行してみる
python create_first_task.py

python create_multi_task.py
```

#### Worker 確認方法

Flower という Celery オフィシャルの UI 確認ツールがあるため、そちらを導入しています。
`http://localhost:5555/` にて確認可能です。

#### ログの確認方法

Default では、Stdout と logs.log ファイルの両方に出力されます。
詳細な設定は、`logging_config.yaml` に記載しています。

#### その他

フォーマッターとして `black`, `flake8`, `isort` を追加しています。
