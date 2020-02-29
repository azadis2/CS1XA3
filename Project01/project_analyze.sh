#!/bin/bash
# A menu for the user to select from
PS3='Please choose what you want to do: '
options=("FIXME Log" "File Size List" "File Type Count" "Checkout Latest Merge" "Find Tag" "Backup and Delete / Restore" "Custom Feature 2" "Quit")
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
                        ls -laSh ..
                        ;;
                "File Type Count")
                        # Count the number of files the user gives you
                        read -p "Give me a file extension to look for: " ext
                        ls -lR .. ".$ext" | wc -l
                        ;;
				"Checkout Latest Merge")
						x=$(gitlog -1 --oneline | grep -i "merge")
						echo $x
						;;
				"Find Tag")
						:> tag.log
						read -p "Give me a tag prompt: " tag
						find .. -type f -name "*.py" -print0 | while IFS= read -d '' file
						do
							egrep "^#.*${tag}.*" $file
						done
						;;
				"Backup and Delete / Restore")
					# Ask the user to backup or restore
					read -p "Choose to either Backup or Restore: " input
					H=$(find .. -name "*.tmp")
					# The user selects Backup
					if [ $input == "Backup" ]; then
						if [ -d backup ] ; then
							rm -r backup;mkdir backup
						else
							mkdir backup
						fi
						find .. -name "*.tmp" | xargs -I cp "./backup"
						find .. -name "*.tmp" | xargs rm -r
						if [ -f ./backup/restore.log ]; then
							rm ./backup/restore.log ; touch ./backup/restore.log
						else
							touch restore.log
							mv restore.log ./backup
						fi
						echo "$H" >> ./backup/restore.log
					fi
					if [ $input == "Restore" ] ; then
						if [ -f ./backup/restore.log ] ; then
							echo "restore.log exists."
						else
							echo "Error! restore.log does not exist."
						fi
					fi
					;;
				"Custom Feature 2")
					read -p "Give me a movie name: " movie
					mkdir tmp
					touch moviedata.log
					temp="/tmp/moviedata.log"
					imdburl="https://www.imdb.com/search/title/"
					titleurl="https://imdb.com/title?"

					summarize()
					{

					grep "^<title>" $temp | sed 's/<[^>]*>//g;s/(more)//'
					grep '<b class="ch">Plot Outline:</b>' $temp | \
						sed 's/<[^>]*>//g;s/(more)//;s/(view trailer)//' |fmt|sed 's/^/  /'
					exit 0
					}

					trap "rm -f $temp" 0 1 15

					if [ $# -eq 0 ] ; then
					echo "Usage: $movie " >&2 
					exit 1
					fi

					fixedname="$(echo $@ | tr ' ' '+')"	

					if [ $# -eq 1 ] ; then
					nodigits="$(echo $1 | sed 's/[[:digit:]]*//g')"
					if [ -z "$nodigits" ] ; then
						lynx -source "$titleurl$fixedname" > $temp
						summarize_film
					fi
					fi
					url="$imdburl$fixedname"

					if [ ! -z "$(grep "IMDb title search" $temp)" ] ; then
						grep 'HREF="/Title?' $temp | \
						sed 's/<OL><LI><A HREF="//;s/<\/A><\/LI>//;s/<LI><A HREF="//' | \
						sed 's/">/ -- /;s/<.*//;s/\/Title?//' | \
						sort -u | \
						more
					else
					summarize
					fi

					exit 0
					;;
                "Quit")
                        break
                        ;;
                *) echo "invalid choice $REPLY";;
        esac
done

