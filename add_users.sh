#!/bin/bash

if [[ $# -eq 0 ]] ; then
    echo 'Error: must supply user file'
    exit 1
fi

# Ensure the working directory is at the script
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
pushd $SCRIPTPATH

echo $(set -o)

echo "Adding users from config file: $1"
exec < $1
read header
while IFS="," read -r user password user_type;
do
    echo "Adding user $user..."
    if [ "$user_type" = "manager" ]; then
        method="create_superuser"
    elif [ "$user_type" = "customer" ]; then
        method="create_user"
    else
        echo "Error: $user_type is not valid"
        exit 1
    fi
    command="from django.contrib.auth.models import User; User.objects.$method('$user', password='$password')"
    docker compose exec -T web python django_project/manage.py shell -c "$command" < /dev/null
    echo "User $user added to storefront"
done

# Return to original working directory
popd

exit 0
