# get the local directory to convert relative paths to absolute ones
LOCAL_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# make sure we use the latest builds
docker-compose -f $LOCAL_DIR/deployment/test.yaml build

# run the tests
docker-compose -f $LOCAL_DIR/deployment/test.yaml up --abort-on-container-exit --force-recreate
