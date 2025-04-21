#!/bin/bash

#########################
#!!!!!!!!!!!! Need to run from analysis server account!!!
## Input ##
search_dir=/SNS/VENUS/IPTS-34969/images/raw_tpx3
save_dir_h5=/SNS/users/uff/VENUS_TPX3/TOT_per_cluster_distribution/Events_h5
save_dir_Fig=/SNS/users/uff/VENUS_TPX3/TOT_per_cluster_distribution/Fig
Run_number=7430
## Input ##



for eachfile in "$search_dir"/*
do
  filename=$(basename "$eachfile")
  # echo "> Sophiread work on ${filename}"
    filename="${filename%.*}"
  if [[ $filename == *$Run_number* ]]
  then
  echo "Found matching run number: $Run_number in $filename"
  working_file_name=$filename
  fi
done

echo "Working file name: $working_file_name"

/SNS/users/uff/VENUS_TPX3/mcpevent2hist/sophiread/build/Sophiread -i "$search_dir"/$working_file_name".tpx3" -E "$save_dir_h5"/$working_file_name".h5" -u ./example_config.json 

python Save_TOT_distribution.py "$save_dir_h5"/$working_file_name".h5" $save_dir_Fig $Run_number 


