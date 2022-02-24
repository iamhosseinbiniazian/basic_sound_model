path="/home/apasai/PycharmProjects/PyTest/data/ESC-50/"
for index in `ls $path`;do
	if   [ -d "${index}" ]
		then echo "${index} is a directory";
	elif [ -f "${index}" ]
		then echo "${index} is a file";
	else echo "${index} is not valid";
     exit 1
	fi
done
