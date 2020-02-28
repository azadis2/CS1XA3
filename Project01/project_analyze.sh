#!/bin/bash

PS3='Please choose what you want to do: '
options=("FIXME Log" "File Size List" "Checkout Latest Merge" "File Type Count" "Quit")
select opt in "${options[@]}"
do
        case "$opt" in
                "FIXME Log")
			:> fixme.log
			find -type f -print0 | while IFS= read -d '' file
			do
				tail -1 "$file" | grep -q "FIXME"
				if [ "$?" -eq 0 ]; then
					echo "$(filename $file)" >> fixme.log
				fi
			done
                        ;;
                "File Size List")
			# Lists all files in your repo with their sizes
                        ls -laSh ./*
                        ;;
		"Checkout Latest Merge")
			x=git log | grep -i "merge" | head -n 1 | cut -d " " -f1
			git checkout "$x"
			;;
                "File Type Count")
			# Count the number of files the user gives you
                        read -p "Give me a file extension to look for: " ext
			ls -lR ./*."$ext" | wc -l
                        ;;
                "Quit")
                        break
                        ;;
                *) echo "invalid choice $REPLY";;
        esac
done
