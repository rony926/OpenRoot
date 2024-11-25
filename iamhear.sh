chmod +x localhost.sh
chmod +x geturl.sh
chmod +x mod.sh
gnome-terminal -- bash -c "./localhost.sh; exec bash"
gnome-terminal -- bash -c "./geturl.sh; exec bash"
sleep 5
gnome-terminal -- bash -c "./mod.sh; exec bash"

gcc -o OpenR00t OpenR00t.c -lcrypto
./OpenR00t