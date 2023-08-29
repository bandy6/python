#! /bin/bash

function check_postfix
{
   if [ `echo $1 |grep '\.h$' |wc -l` -gt 0\
 -o `ls $1 |grep '\.c$' |wc -l` -gt 0\
 -o `ls $1 |grep '\.cpp$' |wc -l` -gt 0\
 -o `ls $1 |grep '\.inc$' |wc -l` -gt 0 ]
  then
    return 1
  fi
  return 0
}

path_ignore_file=.pre-commit.gitignore
is_ignore=0
#过滤忽略的文件
function filter_path()
{
  local abs_path=$1
	for ignore_path in $(cat $path_ignore_file); do
	#echo ignore_path: $ignore_path
	#echo abs_path: $abs_path
	#为了解决在windows系统当中换行符号不兼容问题
	ignore_path=$(echo $ignore_path)
    if [[ $abs_path =~ $ignore_path ]];then
    	#is_ignore=1
		#echo SAME
		return 1
    fi
  done
  #echo NOT_SAME
  return 0
}

function format_file
{
  #replace tab with space
  #sed -i "s/\t/    /g" $1
  #echo format_file: $1
  
  filter_path ${1%/*}
  if [[ $? == 0 ]]; then
    echo format $1
    #format code
    ./clang-format -i $1
  fi
  #indent -npro -kr -i4 -ts8 -sob -l120 -ss -bl -nce -bli 4 $1
}

function format_path
{
  is_ignore=0
  local root=$1
  shift
  local file_in
  local path
  for file_in in $* 
  do
    path=${root}/${file_in}
	#echo $path
    if [ -d $path ] ;then 
      format_path $path `ls $path`
    else
      check_postfix $path
      if [ $? -gt 0 ] ;then
      format_file $path
      fi
    fi    
  done
}

if [ $# -lt 1 ] ;then
  echo "please enter a valid path for format!"
  echo "$0 <path/dir>"
else
echo start: `date`:
  if [ -d $1 ] ;then
    format_path ${1%/*} `ls $1`
  else
    format_file $1
  fi
echo finish:  `date`:
fi
