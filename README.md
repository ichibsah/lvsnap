# lvsnap
A LVM snapshot helper script written in Bash.

* Rollback system upgrades
* Test alpha versions and revert to your stable system
* Completely remove a manually installed package

You need to have some free diskspace in your volume group or use thin provisioning.

**Only tested on Fedora!**

## Usage
Creating a snapshot of your system is as simple as:

    # lvsnap create

Reverting to the snapshot:

    # lvsnap restore

Or if you like the changes done to your system

    # lvsnap drop

## Installation
As a root user:

    # tar xzvf lvsnap*.tar.gz
    # cp lvsnap/lvsnap /usr/local/bin
    # chmod 755 /usr/local/bin/lvsnap
    # gzip lvsnap/lvsnap.1
    # cp lvsnap/lvsnap.1.gz /usr/local/share/man/man1/
    # cp lvsnap/99-hide-lvsnap-snapshots.rules /etc/udev/rules.d/99-hide-lvsnap-snapshots.rules
    
or you could use the included spec-file to build an RPM.
