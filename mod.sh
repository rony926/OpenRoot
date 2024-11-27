
set_ssh_url() {

	c_file="OpenR00t.c"
	localhost_tag="MY_LOCALHOST"
	ssh_ip=$(sed -n '1p' myip.txt)
	# echo "$ssh_ip"
	if [ ! -f "$c_file" ]; then
	  echo "Error: File '$c_file' not found!"
	  exit 1
	fi
	sed -i "s|$localhost_tag|$ssh_ip|g" "$c_file"
}

# Call the function
set_ssh_url


