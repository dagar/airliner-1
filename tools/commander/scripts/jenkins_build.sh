
#!/bin/bash
#export YAMCS_WORKSPACE=~/git/airliner/config/shared/commander_workspace/
#sudo pip install service_identity

#cd /opt/yamcs
#bin/yamcs-server.sh &
#cd ~/git/airliner/build/softsim/default/target/exe/
#./core-bin &
#cd ~/git/airliner



#cd tools/commander/scripts/
#./Launch_YAMCS_airliner.sh &
#sleep 60
./Launch_Commander.sh 1 &

sleep 5
cd ../
cd groundcontrol/
cd test-reports
touch *.xml
cd ../
#npm install
#./node_modules/.bin/mocha test --reporter mocha-junit-reporter --reporter-options mochaFile=./test-reports/client-results.xml
py.test --junitxml ./test-reports/server-results.xml ./test/consumer_integration_test.py
#py.test --junitxml ./test-reports/gui-results.xml ./test/uitests.py

sleep 20
echo '###################INTENTIONAL WATING####################'
../scripts/killswitch.sh
cd ../
cd scripts/


#./kill_YAMCS_airliner.sh


