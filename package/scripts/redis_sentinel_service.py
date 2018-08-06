import sys, os, pwd, signal, time
from resource_management import *
from subprocess import call
from redis_sentinel import redis_sentinel

class redis_sentinel_service(Script):
  def install(self, env):
    print '!!!! redis_sentinel install start !!!!'
    # Install packages listed in metainfo.xml
    self.install_packages(env)
    self.configure(env)
    #if any other install steps were needed they can be added here
    print '!!!! redis_sentinel install end !!!!'
    
  def configure(self, env):
    print '!!!! redis_sentinel configure start !!!!'
    import params
    env.set_params(params)
    redis_sentinel()
    print '!!!! redis_sentinel configure end !!!!'

  #To stop the service, use the linux service stop command and pipe output to log file
  def stop(self, env):
    import params
    env.set_params(params)
    Execute('systemctl stop redis-sentinel')

  #To start the service, use the linux service start command and pipe output to log file
  def start(self, env):
    print '!!!! redis_sentinel start start !!!!'
    import params
    env.set_params(params)
    Execute('systemctl start redis-sentinel')
    print '!!!! redis_sentinel start end !!!!'

  #To get status of the, use the linux service status command
  def status(self, env):
    print '!!!! redis_sentinel status start !!!!'
    import status_params
    env.set_params(status_params)
    check_process_status(status_params.sentinel_pid_file)
    print '!!!! redis_sentinel status end !!!!'

if __name__ == "__main__":
    redis_sentinel_service().execute()
