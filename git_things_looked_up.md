# git - things looked up
---------------------------------------------

### change the default branch
	git config --global init.defaultBranch

### error: --mirror can't be combined with refspecs
#### the config option remote.origin.mirror is set
	git config --unset remote.remote_name.mirror

### delete directory recursively on windows command lines
#### git bash delete directory and contents recursively
	rm -f -r path_here

#### powershell delete directory and contents recursively
	rd -r

### started a rebase and decide to go back
#### error: you need to resolve your current index first
	git reset --merge
	git rebase --abort

### 'undo'ing a commit
	git reset hard [hash or "HEAD^" for the just made commit] 
### loses changes made, renamed files duplicates now with both names
        return {'results_dict': result_dict, 'default_column_order': DefectModel.__table__.columns.keys()}, 200

### git commands give the error: "fatal: git this operation must be run in a work tree"

### remove a file from tracking retroactively
#### !! this will change all revision numbers with that file !!
#### use git-filter-repo 3rd party tool, on windows use scoop to install it
#### create a new clone of the repo 
	git clone "//url/folder" --no-local  ### need no-local if from local/network path
	git filter-repo --path pdf_table_extraction/thickness_specifications.py --invert-paths
	git log -S something_that_is_unique_in_that_file --source --all

### see what commits have not been pushed/don't exist in remote
	git log remote_name/branch_name..HEAD

### see the diff with remote
	git diff remote_name/branch_name..HEAD