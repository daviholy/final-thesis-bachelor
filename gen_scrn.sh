#!/bin/bash
#script for generating visualized screenshots of data 

BASE=$(pwd)

remove_empty_folders () {
for len in ./*/
do
  #iterate over simulations with same block
  for block in ${len}*/
  do
    #iterate over every simulation etap
    for n in ${block}*/
    do
      if  [[ ! -f "${n}CORREL" ]]
      then
        rm -r ${n}
      fi
    done
    #remove empty folder
    [ "$(ls -A ${block})" ] && continue || rm -r ${block}
  done
  [ "$(ls -A ${len})" ] && continue || rm -r ${len}
done
}

generate_xml () {
#iterate over every simulations with same lengths
for len in ./*/
do
  #iterate over simulations with same block
  for block in ${len}*/
  do
    #iterate over every simulation etap
    for n in ${block}*/
    do
      if  [[ ! -f "${n}export.xml" ]]
      then
        cd ${n}
        ../../../xmlExport
        cd ${BASE}
      fi
    done
  done
done
}

generate_image () {
for len in ./*/
do
  #iterate over simulations with same block
  for block in ${len}*/
  do
    #iterate over every simulation etap
    for n in ${block}*/
    do
      if  [[ ! -f "${n}render.jpg" ]]
      then
        echo "render: ${n}"
        cd ${n}
        python3 "../../../renderImage.py"
        cd ${BASE}
      fi
    done
  done
done
}

remove_empty_folders
generate_xml
generate_image
