param (
    [Alias("p")][string]
    $port,
    [Alias("b")][string]
    $board = $(Read-Host "Enter the board name"),
    [Alias("s")][string]
    $sketch = $(Read-Host "Enter the sketch name")
)

if ([string]::IsNullOrEmpty($port)) {
    Write-Output $port
    Write-Output "`nAvailable Ports:"
    $availablePorts = (Get-WmiObject -query "SELECT * FROM Win32_PnPEntity" | Where {$_.Name -Match "COM\d+"}).name
    foreach($availablePort in $availablePorts){
        Write-Output "  $availablePort"
    }
    Write-Output ""
    $port = $(Read-Host "Enter the port")
}

$board = $board.ToLower()

if ($port.ToUpper().Contains("COM")){
    $port = $port.ToUpper()
}

Write-Output "Board: $board, Port: $port, Sketch: $sketch"

switch ($board)
{
    "leonardo" {
        arduino-cli compile --fqbn arduino:avr:leonardo $sketch
        arduino-cli upload -p $port --fqbn arduino:avr:leonardo .\$sketch
    }
    "micro" {
	arduino-cli compile --fqbn arduino:avr:micro $sketch
        arduino-cli upload -p $port --fqbn arduino:avr:micro .\$sketch
    }
}

