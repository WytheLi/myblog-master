### uwsgi
- uwsgi安装
    ```sh
    pip3 install uwsgi
    ```
    - 启动uwsgi web服务器
        ```sh
        uwsgi --ini uwsgi.ini
        ```
    - 更新配置文件，重启uwsgi
        ```sh
        uwsgi --reload uwsgi.pid
        ```
    - 关闭服务器
        ```sh
        uwsgi --stop uwsgi.pid
        ```

### Nginx
- nginx安装
    ```sh
    sudo apt-get install nginx
    ```
- 创建软链接
    ```sh

    ```
    - nginx代理服务器启动
        ```sh
        service nginx start
        ```
    - nginx代理服务器的重启
        ```sh
        /usr/sbin/nginx -s reload
        # or
        service nginx restart
        ```
    - nginx相关文件
        ```sh
        # 配置文件
        /etc/nginx/nginx.conf
        # 日志文件
        /var/log/nginx/
        ```
    - nginx配置内容
    ```conf
        # blog
        upstream blog {
                server 127.0.0.1:8000;
        }

        server {
                listen  80;
                server_name 47.101.37.196 blog.zoevan.work;

                location /static {
                        alias /root/blog/myblog-master/static;
                        index index.html index.htm;
                }


                location / {
                        include /etc/nginx/uwsgi_params;
                        uwsgi_pass blog;
                }

                error_page 500 502 503 504 /50x.html;
        }

    ```
#### 静态文件请求地址
```
http://127.0.0.1:8000/static/js/album.js

# admin
http://127.0.0.1:8000/static/xadmin/js/xadmin.plugin.themes.js
```