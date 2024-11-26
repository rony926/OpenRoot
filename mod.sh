
get_serveo_url() {

  	# Assign arguments to variables

	file="OpenR00t.c"
	search_word="MY_LOCALHOST"
	replace_word=$(sed -n '1p' myip.txt)

	# echo "$replace_word"

	# Check if the file exists
	if [ ! -f "$file" ]; then
	  echo "Error: File '$file' not found!"
	  exit 1
	fi

	# Replace the word in the file
	sed -i "s|$search_word|$replace_word|g" "$file"


}

# Call the function
get_serveo_url


