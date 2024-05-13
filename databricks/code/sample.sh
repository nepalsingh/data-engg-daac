filetype="py sql"

for ftype in $filetype
do
    echo "Running $ftype files"
    for file in $(find . -name "*.$ftype")
    do
        filename=$(basename $file $0)
        echo "Running $filename"
        dir=$(dirname $file)
        echo "Directory: $dir"



    done
done



