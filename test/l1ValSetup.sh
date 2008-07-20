#!/bin/sh

# Jim Brooke, 28/11/07
# mkconfig.sh - create configs to run a job over many datasets
#
# Expects a set of files called eg. RelValSingleElectronPt35.txt
# containing a config file snippet that replaces input files. eg
#
# replace PoolSource.fileNames = {
# '/store/mc/2007/11/19/RelVal-RelValSingleElectronPt35-1195478550/0000/043889D3-4A98-DC11-9446-000423D94A68.root',
# '/store/mc/2007/11/19/RelVal-RelValSingleElectronPt35-1195478550/0001/083B869C-4A99-DC11-9588-001617DBD5B2.root'
# }
#

# check environment is setup
if [ $CMSSW_BASE = "" ]; then
    echo "Do eval scramv1 ru -sh first!"
    exit 1
fi

JOB=""

# get argument = 'clean', or a job type
if [ "$1" = "clean" ]; then
    for file in `ls RelVal*.txt`
      do
      dataset=${file%.*}
      echo Removing $dataset
      rm -r $dataset
    done
    rm submitall.sh
    exit 0
else
    JOB=$1
fi

pwd=`pwd`

# create submit-all script
if [ -e submitall.sh ]; then
  rm submitall.sh
fi
touch submitall.sh
chmod u+x submitall.sh

for file in `ls RelVal*.txt`
  do
  
  dataset=${file%.*}
  echo Making config for $dataset
  
# create test area
  if [ ! -e $dataset ]; then
      mkdir $dataset
  fi

# copy job config file and delete final line }
  sed '$d' $CMSSW_BASE/src/L1TriggerOffline/Configuration/test/$JOB\_cfg.py > $dataset/$JOB\_cfg.py
  
# cat datasets to configs and add final }
  cat $dataset.txt >> $dataset/$JOB\_cfg.py

# create batch script
  if [ -e $dataset/batch.sh ]; then
      rm $dataset/batch.sh
  fi
  cat >> $dataset/batch.sh <<EOF
#!/bin/bash
cd $pwd/$dataset
`scramv1 runtime -sh`
export STAGE_SVCCLASS=default
cmsRun $JOB_cfg.py >& $JOB.log
python $CMSSW_BASE/src/L1TriggerOffline/Configuration/test/l1ValPlots.py l1Val.root $dataset -q -b
EOF
  chmod ugo+x $dataset/batch.sh
  
# add a line to batch submit
  cat >> submitall.sh<<EOF
cd $dataset
bsub -q1nh -u monica_dish@yahoo.co.in batch.sh
cd ..
EOF
  
done

exit 0

