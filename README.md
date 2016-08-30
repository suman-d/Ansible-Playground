# Ansible-Playground

This playbook can be used to calculate VM Boot Up time(in secs),

To get started:

- Copy all the files in this repo in your server from where you manage your infrastructure via Ansible
- Edit the playbook, with appropriate "host" name
- Run the ansible playbook 
    ansible-playbook vmboot-time.yml
- Once its over, you will find "n" of files under /root/ (where "n" = number of hosts you have mentioned in the ansible playbook)
  with prefix "bootuptime-<vm_name>" 
- Each file would contain the respective boot up time


