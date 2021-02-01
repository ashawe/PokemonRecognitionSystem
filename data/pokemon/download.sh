for entry in "url"/*
do
    echo "Downloading images for pokemon: $entry"
    cat $entry | while read y
    do
        # echo "Line contents are : $y "
        ent="${entry:4}"
        ent=${entry%.txt}
        wget -P "/$ent" $y
    done
done