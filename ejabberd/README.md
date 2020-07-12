## Ejabberd - XMPP Server Config

Docker Image Used: https://hub.docker.com/r/ejabberd/ecs/

To start server:

`docker run --name ejabberd -d -p 5222:5222 -p 5280:5280 -p 5269:5269 -p 5443:5443 -p 1883:1883 -v $(pwd)/ejabberd.yml:/home/ejabberd/conf/ejabberd.yml ejabberd/ecs`

Create admin:
``docker exec -it ejabberd bin/ejabberdctl register admin 192.168.99.100 password``



docker run -d \
    --name "ejabberd" \
    -p 5222:5222 \
    -p 5269:5269 \
    -p 5280:5280 \
    -h '192.168.99.100' \
    -e "XMPP_DOMAIN=192.168.99.100" \
    -e "EJABBERD_ADMINS=admin@192.168.99.100 admin2@192.168.99.100" \
    -e "EJABBERD_USERS=admin@192.168.99.100:password admin2@192.168.99.100" \
    -e "TZ=Europe/Berlin" \
    rroemhild/ejabberd