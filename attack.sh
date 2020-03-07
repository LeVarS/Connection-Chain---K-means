#
# Creation script for Connection Chain project
#
# The purpose of this script is to automate commands to increase the speed at
# which our group will be able to test the various connection chain length.
# At this moment this script does not simulate the commands an attacker will
# enter.
#
# Author: LeVar Small, Darian Thomas, Aaron Broom
# Created: Feb 27, 2020
#

echo "Attacking ..."

while [ true ]
do
  cd ~
  pwd
  ls -l
  echo "\n"
  sleep .75
  cd ..
  pwd
  ls -l
  echo "\n"
  sleep .75
  cd ..
  pwd
  ls -l
  echo "\n"
  sleep .75
  cd ~
  pwd
  ls -l
  echo "\n"
  sleep .75
  echo "\nCreating a file named info.txt with vital information\n"
  sleep .75
  echo "FAKE VITAL SYSTEM INFORMATION" > info.txt
  sleep .75
  cat info.txt
  sleep .75
  echo "\nDeleting info.txt\n"
  sleep .75
  rm info.txt
done
