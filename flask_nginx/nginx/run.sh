docker run -it --rm --name nginx_test_proxy -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro -p 4999:80 nginx
