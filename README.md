# Ansible-Playground

This playbook can be used to calculate VM Boot Up time(in secs),

To get started:

- Copy all the files in this repo in your server from where you manage your infrastructure via Ansible
- Edit the playbook, with appropriate "host" name
- run the ansible playbook 
    ansible-playbook vmboot-time.yml
- Once its over, you will find "n" of files under /root/ (where "n" = number of hosts you have mentioned in the ansible playbook)
  with prefix "bootuptime-<vm_name>" Each file would contain the respective boot up time



root@master:~# ansible-playbook vmboot-time.yml

PLAY [ubuntu] ******************************************************************

TASK [Copying the VM boot-time capturing script to all the VMs] ****************
ok: [vm03] => (item=vmboot-time.py)
ok: [vm04] => (item=vmboot-time.py)
ok: [vm02] => (item=vmboot-time.py)
ok: [vm01] => (item=vmboot-time.py)
changed: [vm02] => (item=vmboot-time-now.py)
changed: [vm01] => (item=vmboot-time-now.py)
changed: [vm03] => (item=vmboot-time-now.py)
changed: [vm04] => (item=vmboot-time-now.py)

TASK [Capturing the present time, before reboot] *******************************
changed: [vm03]
changed: [vm04]
changed: [vm02]
changed: [vm01]

TASK [Rebooting the VMs] *******************************************************
ok: [vm01]
ok: [vm02]
ok: [vm03]
ok: [vm04]

TASK [Waiting for the VMs to boot up] ******************************************
ok: [vm02 -> localhost]
ok: [vm04 -> localhost]
ok: [vm03 -> localhost]
ok: [vm01 -> localhost]

TASK [Calculating the VM Boot time] ********************************************
changed: [vm02]
changed: [vm04]
changed: [vm01]
changed: [vm03]

TASK [Fetching VM Boot time from all VMs] **************************************
changed: [vm02]
changed: [vm01]
changed: [vm03]
changed: [vm04]

PLAY RECAP *********************************************************************
vm01                       : ok=6    changed=4    unreachable=0    failed=0
vm02                       : ok=6    changed=4    unreachable=0    failed=0
vm03                       : ok=6    changed=4    unreachable=0    failed=0
vm04                       : ok=6    changed=4    unreachable=0    failed=0

root@master:~#
root@master:~#
root@master:~#
root@master:~# ls -ltr bootuptime-*
-rw-r--r-- 1 root root 14 Aug 30 07:30 bootuptime-vm02
-rw-r--r-- 1 root root 14 Aug 30 07:30 bootuptime-vm01
-rw-r--r-- 1 root root 14 Aug 30 07:30 bootuptime-vm03
-rw-r--r-- 1 root root 14 Aug 30 07:30 bootuptime-vm04
root@master:~#
root@master:~#
root@master:~#
root@master:~# cat bootuptime-vm0*
99.5287899971
99.1349101067
110.843479872
99.2294399738
root@master:~#
root@master:~#

