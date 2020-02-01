import-module "C:\Program Files (x86)\Microsoft Office 2013\LyncSDK\Assemblies\Desktop\Microsoft.Lync.Model.dll"
$client = [Microsoft.Lync.Model.LyncClient]::GetClient()

try {
	$client = [Microsoft.Lync.Model.LyncClient]::GetClient()
	
	if ($client -eq $null) {
		Throw "Unable to obtain client interface"
	}
} catch [Microsoft.Lync.Model.ClientNotFoundException] {
	Throw "Lync client is not running! Please launch your Lync client."
}

If ($client.InSuppressedMode -eq $false) {
	try {
		$auto = [Microsoft.Lync.Model.LyncClient]::GetAutomation()
		
		if ($Auto -eq $null) {
			Throw "Unable to obtain Lync Automation interface"
		}
	} catch {
		Throw "Automation Session is unavaiable"
	}
	
	$self = $client.Self
} else {
	Throw "UI Supression Mode is Active Suppressing UI Client Automation API's"
}

# set initial value
$LastAvailability = "n.a."

while (1) {

    $contact = $client.ContactManager.GetContactByUri($self.contact.Uri)
    $availabilityId = $contact.GetContactInformation("Availability")

    switch ($availabilityId)
    {
        3500 { 
            $Availability = "Available" 
            $Color = "G"
        }
        5000 { 
            $Availability = "Free (Idle)" 
            $Color = "G"        
        }
        6500 { 
            $Availability = "Busy" 
            $Color = "R"
        }
        7500 { 
            $Availability = "Busy (Idle)" 
            $Color = "R" }
        9500 {  
            $Availability = "Do Not Disturb" 
            $Color = "R" }
        12500 {  
            $Availability = "Temporarily Away" 
            $Color = "Y" }
        15500 {  
            $Availability = "Away" 
            $Color = "Y" }
        18500 {  
            $Availability = "Offline" 
            $Color = "R" }
    }

    if (!($LastAvailability -eq $Availability)) {
        $date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        $out = -join($date, " -- status change: ", $LastAvailability, " --> ", $Availability)
        Write-Output $out

        $LastAvailability = $Availability

        $date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        $out = -join($date, " -- setting new status color ", $Color)
        Write-Output $out

        # set the IP of your dnd device
        $Uri = -join("http://172.17.15.127/?color=", $Color)
        
        try {
            $response = Invoke-WebRequest -URI $Uri | Out-Null

            $date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            $out = -join($date, " -- indicator light request has been sent ")
            Write-Output $out
        } catch {
            $date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            $out = -join($date, " -- sending indicator light request failed")
            Write-Output $out       
        }
    }
        
    Start-Sleep -s 2
}
