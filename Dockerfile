# syntax=docker/dockerfile:1
# Image: CopartBR static mirror + Nginx
FROM nginx:1.27-alpine

# Workdir for site assets
WORKDIR /usr/share/nginx/html

# Expect that the build context already contains the scraper output folder "copart_clone/"
# with subfolders "static/copart" and "templates/copart"
# Copy site content into the image
#   - Static assets -> /usr/share/nginx/html/static
#   - HTML pages    -> /usr/share/nginx/html/templates/copart
COPY copart_clone/static/ /usr/share/nginx/html/static/
COPY copart_clone/templates/ /usr/share/nginx/html/templates/

# Nginx config
RUN rm -f /etc/nginx/conf.d/default.conf
COPY copartbr.conf /etc/nginx/conf.d/copartbr.conf

# MIME for JSON is present by default, but ensure gzip and sendfile are on via nginx defaults.
EXPOSE 80
STOPSIGNAL SIGTERM
CMD ["nginx", "-g", "daemon off;"]
