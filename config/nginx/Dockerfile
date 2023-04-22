FROM nginx:1.24
LABEL MAINTAINER="Reza Naeemi | https://radazin.com"

COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]