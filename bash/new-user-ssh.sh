#!/bin/bash
# chmod +x new-user-ssh.sh

USER_NAME=$1
PUB_KEY=$2
if [ -z "$1" ] && [ -z "$2" ]
then
    echo 'No arguments supplied - 1st username 2nd "pub ssh key"'
    echo 'As root run ./new-user-ssh.sh username "pub ssh key"'
else
    useradd -s /bin/bash -m ${USER_NAME}
    usermod -aG sudo ${USER_NAME}
    mkdir -p /home/${USER_NAME}/.ssh
    touch /home/${USER_NAME}/.ssh/authorized_keys
    chown ${USER_NAME}:${USER_NAME} /home/${USER_NAME}/.ssh
    chown ${USER_NAME}:${USER_NAME} /home/${USER_NAME}/.ssh/authorized_keys
    chmod 700 /home/${USER_NAME}/.ssh
    chmod 600 /home/${USER_NAME}/.ssh/authorized_keys
    echo ${PUB_KEY} >> /home/${USER_NAME}/.ssh/authorized_keys
    echo "Choose user password"
    passwd ${USER_NAME}
fi