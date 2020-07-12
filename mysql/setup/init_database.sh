#!/bin/bash

MYSQL="mysql -uroot -p${MYSQL_ROOT_PASSWORD}"

# Create initial user
USER=`${MYSQL} -se "SELECT User FROM mysql.user WHERE User='${USERNAME}'"`

if [[ -z $USER ]]
then
    ${MYSQL} -se "GRANT ALL PRIVILEGES ON *.* TO '${USERNAME}'@'%' IDENTIFIED BY '${PASSWORD}'"
    ${MYSQL} -se "FLUSH PRIVILEGES"
fi

# Create Tables:
${MYSQL} -s < /setup/sql/user_table.sql
