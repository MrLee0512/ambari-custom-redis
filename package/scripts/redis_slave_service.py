import sys, os, pwd, signal, time
from resource_management import *
from subprocess import call
from redis import redis

class redis_service(Script):
  def install(self, env):
    print '!!!! redis_slave install start !!!!'
    # Install packages listed in metainfo.xml
    self.install_packages(env)
    self.configure(env)
    #if any other install steps were needed they can be added here
    print '!!!! redis_slave install end !!!!'
  
  def configure(self, env):
    print '!!!! redis_slave configure start !!!!'
    import params
    params.redis_slave=True
    env.set_params(params)
    redis()
    print '!!!! redis_slave configure end !!!!'

  #To stop the service, use the linux service stop command and pipe output to log file
  def stop(self, env):
    import params
    env.set_params(params)
    stop_cmd = format("systemctl stop redis")
    Execute(stop_cmd)

  #To start the service, use the linux service start command and pipe output to log file
  def start(self, env):
    print '!!!! redis_slave start start !!!!'
    import params
    env.set_params(params)
    start_cmd = format("systemctl start redis")
    Execute(start_cmd)
    print '!!!! redis_slave configure end !!!!'

  #To get status of the, use the linux service status command
  def status(self, env):
    print '!!!! redis_slave status start !!!!'
    import status_params
    env.set_params(status_params)
    check_process_status(status_params.redis_pid_file)
    print '!!!! redis_slave status end !!!!'
    
if __name__ == "__main__":
    redis_service().execute()