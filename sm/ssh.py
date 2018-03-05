#coding:utf-8
#!/usr/bin/env python
import paramiko

class MySSH(object):
        def __init__(self):
                self.ssh=""
                pass
        def login(self,ip="",username="",password="",port="",key="",key_password="",login_method="password"):
                if len(ip)==0:
                        raise NameError("您必须传入一个IP：")
                elif len(username)==0:
                        raise NameError("您必须输入用户名！")
                elif not int(port):
                        raise NameError("您传入的端口不是一个数字")
                if login_method=="password":
                        pass
                elif login_method=="key":
                        if len(key)==0:
                                raise NameError("您指定的是秘钥登录方式，但没有指定秘钥文件的位置!")


                #开始登录服务器
                ssh=paramiko.SSHClient()      #类的实例化
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())    #确认是否是已知的主机

                if login_method=="password":
                        ssh.connect(ip,22,username,password)
                else:
                        raise NameError("对不起，暂时不支持除了密码外的其他登录方式")
                self.ssh=ssh
                print "很好，已经登录完成"

        def execute_command(self,command=""):
                status=False
                info={"status":status,"content":""}
                if len(command)==0:
                        raise NameError("您尚未制定命令")
                #开始执行命令
                stdin,stdout,stderr=self.ssh.exec_command(command)
                #整合命令的标准输出结果
                my_stdout="".join(stdout)         #拼接字符串
                my_stderr="".join(stderr)

                #判断一下，命令执行的成功或是失败
                if len(my_stdout)==0:
                        status=False
                        info["content"] = my_stderr
                        info["status"] = status
                else:
                        status=True
                        info["content"] = my_stdout
                        info["status"] = status
                return info