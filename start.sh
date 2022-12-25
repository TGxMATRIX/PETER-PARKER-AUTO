if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/HansakaAnuhas/FiltersBot.git /FiltersBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /FiltersBot
fi
cd /FiltersBot
pip3 install -U -r requirements.txt
echo "Starting Bot..."
python3 bot.py
