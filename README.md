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
        /usr/sbin/nginx -c /etc/nginx/nginx.conf
        ```
    - nginx代理服务器的重启
        ```sh
        /usr/sbin/nginx -s reload
        ```
        