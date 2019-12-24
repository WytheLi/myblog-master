#### Django整合markdown编辑器
参考博客： https://www.jianshu.com/p/442bc083c835
```sh
pip install django-mdeditor  # 用于后台编辑
pip install markdown # 用于前端显示
```

#### 单独安装xadmin
```
pip install https://github.com/sshwsfc/xadmin/tarball/master
```

#### 待完成
- 博客文content markdown编辑器的大小调整
- 轮播图照片的替换
- 项目在服务器的部署
    - uwsgi服务run django项目 (开两个端口8000 8001，跑两份代码)
    - nginx服务器 域名blog.zoevan.work 端口80
        1. 作为代理服务器，将请求转发到uwsgi
        2. 作为静态服务器，提供css、js静态文件的加载
- 域名备案 网络备案号的获取
- 后台登录时跨域问题 csrf的解决
- 印象笔记 notes笔记迁移、浏览器收藏夹博客迁移， 编辑发布
- 畅言评论区 打赏区域二维码

- boss上简历更新


