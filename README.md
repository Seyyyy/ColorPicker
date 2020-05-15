# Color Picker
このAPIはbase64形式のイメージから画像の特徴を取得するAPIです。

## Getting Started
- production環境の場合

    Dockerfileで作成したコンテナをデプロイしてください。

- development環境の場合
    ```
    docker-compose build
    docker-compose up
    ```
    CLIに表示されるアドレスへHTTPリクエストを送ってください。
## Tutorials

```
docker-compose build
docker-compose up
```

Request to "`http://0.0.0.0:3000`".

For example "curl `http://0.0.0.0:3000`".

## Sample Projects

## API Reference
- ColorPick

    画像に使用されている色相の割合、彩度の割合、明度の割合を返します。

    - Request

        - production

            ```
            POST https://your_app.com/color
            ```

        - development
             ```
            POST http://0.0.0.0:3000/color
            ```

        |  Parameter name  |  Value  |  Description  |
        | ----| ---- | ---- |
        |  form  |  string  |  Base64 image  |

    - Response

        If successful, method returns a json in the response body. 

        ```
        {
            'hue': {
                'red': number,
                'red-yellow': number,
                'yellow': number,
                'yellow-green': number,
                'green': number,
                'green-cyan': number,
                'cyan': number,
                'cyan-blue': number,
                'blue': number,
                'blue-purple': number,
                'purple': number,
                'purple-red': number
            },
            'saturation': {
                's0': number,
                's1': number,
                's2': number,
                's3': number,
                's4': number,
                's5': number,
                's6': number,
                's7': number,
                's8': number,
                's9': number,
                's10': number,
                's10': number,
            },
            'value': {
                'v0': number,
                'v1': number,
                'v2': number,
                'v3': number,
                'v4': number,
                'v5': number,
                'v6': number,
                'v7': number,
                'v8': number,
                'v9': number,
                'v10': number,
                'v11': number
            },
            'entropy': {
                'hue': number,
                'saturation': number,
                'value': number
            }
        }
        ```

- Hello color picker !!

    ただ 挨拶を返してくれるだけ。とくに意味はない。

    - Request
        - production

            ```
            GET https://your_app.com
            ```

        - development
             ```
            GET http://0.0.0.0:3000
            ```

        |  Parameter name  |  Value  |  Description  |
        | ----| ---- | ---- |

    - Response

        If successful, method returns a json in the response body. 

        ```
        Hello Color Picker !!
        ```

## Architecture Documentation