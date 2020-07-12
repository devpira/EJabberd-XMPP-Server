FROM debian:stretch-slim


ARG EJABBERD_UID=999
ARG EJABBERD_GID=999

ENV EJABBERD_BRANCH=18.12 \
    EJABBERD_USER=ejabberd \
    EJABBERD_HTTPS=true \
    EJABBERD_STARTTLS=true \
    EJABBERD_S2S_SSL=true \
    EJABBERD_HOME=/home/ejabberd \
    EJABBERD_DEBUG_MODE=false \
    HOME=$EJABBERD_HOME \
    PATH=$EJABBERD_HOME/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/sbin \
    DEBIAN_FRONTEND=noninteractive \
    XMPP_DOMAIN=192.168.99.100 \
    LC_ALL=C.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    GOSU_VERSION=1.10

# Add ejabberd user and group
RUN groupadd --gid $EJABBERD_GID $EJABBERD_USER \
    && useradd -m \
       -g $EJABBERD_USER \
       -d $EJABBERD_HOME \
       --uid $EJABBERD_UID \
       $EJABBERD_USER

# Install packages and perform cleanup
RUN set -x \
    && buildDeps=' \
        automake \
        build-essential \
        dirmngr \
        erlang-src erlang-dev \
        git-core \
        gpg \
        libexpat-dev \
        libgd-dev \
        libssl-dev \
        libsqlite3-dev \
        libwebp-dev \
        libyaml-dev \
        wget \
        zlib1g-dev \
    ' \
    && requiredAptPackages=' \
        ca-certificates \
        erlang-base-hipe erlang-snmp erlang-ssl erlang-ssh \
        erlang-tools erlang-xmerl erlang-corba erlang-diameter erlang-eldap \
        erlang-eunit erlang-ic erlang-odbc erlang-os-mon \
        erlang-parsetools erlang-percept erlang-typer \
        gsfonts \
        imagemagick \
        inotify-tools \
        libgd3 \
        libwebp6 \
        libyaml-0-2 \
        locales \
        ldnsutils \
        openssl \
        python2.7 \
        python-jinja2 \
        python-mysqldb \
    ' \
    && apt-get update \
    && apt-get install -y $buildDeps $requiredAptPackages --no-install-recommends \
    && dpkg-reconfigure locales && \
        locale-gen C.UTF-8 \
    && /usr/sbin/update-locale LANG=C.UTF-8 \
    && echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen \
    && locale-gen \
    && cd /tmp \
    && git clone https://github.com/processone/ejabberd.git \
        --branch $EJABBERD_BRANCH --single-branch --depth=1 \
    && cd ejabberd \
    # && chmod +x ./autogen.sh \
    && ./autogen.sh \
    && ./configure --enable-user=$EJABBERD_USER \
         --prefix=$EJABBERD_HOME \
         --enable-all \
         --disable-tools \
         --disable-pam \
    && make \
    && make install 

COPY external_auth_script.py /home/ejabberd/etc/ejabberd/external_auth_script.py
RUN chown $EJABBERD_USER:$EJABBERD_USER /home/ejabberd/etc/ejabberd/external_auth_script.py

COPY ejabberd.yml /home/ejabberd/etc/ejabberd/ejabberd.yml
RUN chown root:ejabberd /home/ejabberd/etc/ejabberd/ejabberd.yml
RUN chmod 640 /home/ejabberd/etc/ejabberd/ejabberd.yml

RUN chown -R $EJABBERD_USER: $EJABBERD_HOME 

#RUN apt-get install -y vim

USER ejabberd

ENTRYPOINT ["/home/ejabberd/sbin/ejabberdctl"]
CMD ["foreground"]