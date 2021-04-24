virtualenv chat_env
git clone git@github.com:django/channels.git
cd channels || exit
source ../chat_env/bin/activate
cd ..
python3 -m pip install channels_redis
