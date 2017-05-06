# get the local directory to convert relative paths to absolute ones
LOCAL_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
#
# # make sure we use the latest build
# docker-compose -f $LOCAL_DIR/deployment/develop.yaml build
#
# # run the development container
# docker-compose -f $LOCAL_DIR/deployment/develop.yaml up
docker build . -f deployment/app/Dockerfile -t todorus/news_analysis-hunter_gatherer:production
docker run -it -v $LOCAL_DIR/app:/app todorus/news_analysis-hunter_gatherer:production /bin/bash
