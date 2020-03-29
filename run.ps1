param (
    [Alias("p")][string]
    $port = $(Read-Host "Enter the port"),
    [Alias("b")][string]
    $board = $(Read-Host "Enter the board name"),
    [Alias("s")][string]
    $sketch = $(Read-Host "Enter the sketch name")
)

Write-Output "Board: $board, Port: $port, Sketch: $sketch"

switch ($board)
{
    "leonardo" {
        arduino-cli compile --fqbn arduino:avr:leonardo $sketch
        arduino-cli upload -p $port --fqbn arduino:avr:leonardo .\$sketch
    }
    "micro" {

    }
}

