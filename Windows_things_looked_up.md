#  Windows
----------------------------------------------
## powershell
---------------------------------------------

### test if venv is active
	Test-Path -Path Env:VIRTUAL_ENV

## Outlook
---------------------------------------------

### searching for things (e-mail etc.)
#### advanced search:
	control + shift + F 
#### guide that may actually be correct for this
https://www.howto-outlook.com/howto/searchcommands.htm

## Excel
----------------------------------------------
### array of constants in a formula, using search as an example, place them in {}, cannot be cell references
	=SEARCH({"llc","corp","ltd","limited","strata"},K2)

### convert true/false to 1/0
	--TRUE  # 1
	--FALSE  # 0
	--{TRUE,TRUE,FALSE,TRUE}  # {1,1,0,1}

## cmd, run, start
---------------------------------------------

### open a command windows as SYSTEM using psutils
	psexec -i -s cmd.exe

### get the timestamp when the system was started
	systeminfo|find "Time:"
	systeminfo | find /i "Boot Time"
	wmic os get lastbootuptime  # not epoch timestamp, YYYYMMDDHHMMSS.%-240  (240 being 4 hours in minutes for timezone)

### get the system name, command line
	hostname

## task scheduler
### creating a custom event filter, xml file:
	<QueryList>
	  <Query Id="0" Path="System">
		<Select Path="System">*[System[(EventID=105)]] and *[System[Provider[@Name="Microsoft-Windows-Kernel-Power"]]] and *[EventData[Data[@Name="AcOnline"] and (Data='true')]]</Select>
	  </Query>
	</QueryList>

## developing on Windows
### C:/Program Files vs appdata
"""users expect it to be in program files
pf requires admin rights
appdata can be installed without admin rights (such as school accounts)
for network accounts, app data will follow the user between computers
appdata correlates with the user software directory on linux"""