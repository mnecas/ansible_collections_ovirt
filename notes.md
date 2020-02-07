- update LICENCE
- all roles cant use - but _ or .
- repository is required
- change importing to ansible_collections.'namespace'.'name'.plugins.module_utils 
- filtery - var | 'namespace'.'name'.filtername 
- modules dones not need to add prefix
- example
```
---
- name: oVirt infra
  hosts: localhost
  connection: local
  tasks:
    - name: Login
      ovirt_auth:
          url: "{{ engine_url | default(omit) | default(lookup('env','host')) }}"
          password: "{{ engine_password | default(omit) | default(lookup('env','password')) }}"
          username: "{{ engine_user | default(omit) | default(lookup('env','username')) }}"

    - name: Creating VM
      ovirt_vm:
        auth: "{{ ovirt_auth }}"
        state: present
        cluster: Default
        name: Centos
        storage_domain: storage
      register: test
    - debug:
        msg: "{{ test | mnecas.ovirt.ovirtvmipv6 }}"
  collections:
    - mnecas.ovirt
```
