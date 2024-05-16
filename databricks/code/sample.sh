filetype="py sql"

for ftype in $filetype
do

    echo "Running $ftype files"

    for file in $(find . -name "*.$ftype" | sed 's|^\./||')
    do
        filename=$(basename $file .py)
        echo "Running $filename"
        dir=$(dirname $file)
        echo "Directory: $dir"

    done
done



