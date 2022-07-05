# debian linux
----------------------------------------------
## users, groups, permissions
### users
#### create new user
sudo adduser user_name

#### add user to sudoer group
sudo usermod -aG sudo user_name

#### switch user in shell (with su access)
su - user_name

## permissions
#### chmod
* three permissions for three groups
* read, write, execute
* owner, group, others

#### show permissions in directory; d directory, l symbolic link, - regular file
ls -lha

## set permissions, these two examples are effectively identical
chmod u=rwx,g=rx,o= file_path
chmod 750 file_path

## Octal Notation
Binary	Octal	Permission
000	    0   	—
001	    1   	–x
010	    2   	-w-
011	    3   	-wx
100	    4   	r–
101	    5   	r-x
110	    6   	rw-
111	    7   	rwx

### groups
#### create a new group
groupadd group_name

#### list all groups; group_name:password(encrypted):GID:user_list
cat /etc/group

#### list all groups alphabetically
getent group | cut -d: -f1 | sort

#### count of all groups
cat /etc/group | grep -c ""

#### groups for current user or with numeric id
groups
id
groups another_users_name

#### add a user to group/s
usermod -a -G group_name exampleusername
usermod -a -G group1,group2,group3 exampleusername

### processes

#### list of processes
ps -ef
ps -ef | grep proc_name # only processes containing proc_name

#### kill process by pid
kill -9 pid

#### get the full path of a file
readlink -f file.txt

#### decompress a .tar.gz file
	tar -zxvf archive.tgz
	-z : Uncompress the resulting archive with gzip command.
	-x : Extract to disk from the archive.
	-v : Produce verbose output i.e. show progress and file names while extracting files.
	-f data.tar.gz : Read the archive from the specified file called data.tar.gz

## installing ignition headless
this may be old, from when you could apt-get Ignition
##### ensure fontconfig
sudo apt-get install fontconfig