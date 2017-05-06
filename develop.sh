# get the local directory to convert relative paths to absolute ones
LOCAL_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# make sure we use the latest build
docker-compose -f $LOCAL_DIR/deployment/develop.yaml build

# run the development container
docker-compose -f $LOCAL_DIR/deployment/develop.yaml up
