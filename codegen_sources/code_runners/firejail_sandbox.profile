# Firejail profile for default
# This file is overwritten after every install/update
# Persistent local customizations
include default.local
# Persistent global definitions
include globals.local

# generic gui profile
# depending on your usage, you can enable some of the commands below:

include disable-common.inc
# include disable-devel.inc
# include disable-exec.inc
# include disable-interpreters.inc
include disable-passwdmgr.inc
include disable-programs.inc
# include disable-xdg.inc

# apparmor
caps.drop all
# ipc-namespace
# machine-id
# net none
netfilter
# no3d
# nodbus
# nodvd
# nogroups
nonewprivs
noroot
# nosound
# notv
# nou2f
# novideo
protocol unix,inet,inet6
seccomp
# shell none
# tracelog

# disable-mnt
# private
# private-bin program
# private-cache
# private-dev
# private-etc alternatives
# private-lib
# private-tmp

# memory-deny-write-execute
read-only ${HOME}
read-only /home/circleci
read-only /home
read-only /tmp
read-only /usr
read-only /bin
read-only /boot
read-only /checkpoint
read-only /lib
read-only /sys
read-only /media
read-only /etc
read-only ./
